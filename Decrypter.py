from cryptography.fernet import Fernet
import base64
import hashlib
import getpass

import os
import sys

base_path = r"D:\Keyboard_Activity_Monitor"
os.makedirs(base_path, exist_ok=True)
log_file = os.path.join(base_path, "keystrokes.enc")
output_file = os.path.join(base_path, "dec.txt")



def get_encryption_key(password):
    digest = hashlib.sha256(password.encode()).digest()
    return base64.urlsafe_b64encode(digest)


def decrypt_file(file_path, password):
    try:
        key = get_encryption_key(password)
        fernet = Fernet(key)
        with open(file_path, "rb") as f:
            lines = f.readlines()

        decrypted_data = ""
        for line in lines:
            if line.strip():
                decrypted_data += fernet.decrypt(line.strip()).decode("utf-8")

        with open(output_file, "w", encoding="utf-8") as out:
            out.write(decrypted_data)

        print(f"[✓] Successfully decrypted to '{output_file}'.")

    except Exception as e:
        print("[✗] Decryption failed: Incorrect password or corrupted file.")


if __name__ == "__main__":
    pwd = getpass.getpass("Enter decryption password: ")
    if pwd == "secret123":
        decrypt_file(log_file, pwd)
    else:
        print("[✗] Wrong password.")

