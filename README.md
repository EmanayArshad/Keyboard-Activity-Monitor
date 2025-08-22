# Keyboard Activity Monitor

A secure, encrypted keyboard activity monitoring tool written in Python with real-time keystroke logging, window tracking, and session management capabilities.

## ⚠️ **IMPORTANT DISCLAIMER**

This tool is designed for **educational purposes, authorized monitoring, and legitimate use cases only**. Users are responsible for ensuring compliance with local laws and regulations regarding privacy and monitoring. This tool should **NOT** be used for unauthorized surveillance or malicious purposes.

## 🚀 Features

- **Real-time Keystroke Monitoring**: Captures all keyboard input with timestamp tracking
- **Window Context Tracking**: Records which application window is active during typing
- **Session Management**: Automatically segments data into 30-minute sessions
- **Encrypted Storage**: All data is encrypted using Fernet encryption (AES-128)
- **Special Key Support**: Handles function keys, modifiers, and control combinations
- **Cross-platform**: Works on Windows (with additional Linux/macOS support possible)
- **Executable Build**: Includes pre-compiled .exe for easy deployment

## 📁 Project Structure

```
Keyboard_Activity_Monitor/
├── keylogger_listener.py    # Main monitoring script
├── Decrypter.py             # Decryption utility
├── keylogger_listener.exe   # Pre-compiled executable
├── keystrokes.enc          # Encrypted log file (generated)
├── dec.txt                 # Decrypted output (generated)
├── build/                  # Build artifacts
├── dist/                   # Distribution files
└── keylogger_listener.spec # PyInstaller specification
```

## 🛠️ Installation

### Prerequisites

- Python 3.7 or higher
- Windows OS (primary support)
- Administrator privileges (for keyboard hook access)

### Dependencies

```bash
pip install pynput cryptography pywin32
```

### Quick Start

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/Keyboard_Activity_Monitor.git
   cd Keyboard_Activity_Monitor
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the monitor:**
   ```bash
   python keylogger_listener.py
   ```

## 🔐 Usage

### Starting the Monitor

```bash
# Using Python script
python keylogger_listener.py

# Using executable (Windows)
keylogger_listener.exe
```

The monitor will:
- Start capturing keystrokes immediately
- Create encrypted log files in the project directory
- Track active windows and session changes
- Buffer data for 30-minute intervals

### Decrypting Logs

Use the included decrypter to view captured data:

```bash
python Decrypter.py
```

**Default Password**: `secret123`

**Note**: Change the default password in both files for production use.

### Configuration

Key settings can be modified in `keylogger_listener.py`:

- **Base Path**: Change `base_path` variable for different storage location
- **Session Duration**: Modify `timedelta(minutes=30)` for different intervals
- **Password**: Update `password` variable for custom encryption key

## 🔒 Security Features

- **Fernet Encryption**: Uses AES-128 encryption with SHA-256 key derivation
- **Password Protection**: Encrypted logs require correct password for decryption
- **Secure Storage**: All sensitive data is encrypted before writing to disk
- **Session Isolation**: Data is segmented to prevent unauthorized access

## 📊 Data Format

### Encrypted Log Structure

```
===============NEW SESSION===========
--- Window: Application Name | 2024-01-15 14:30:00 ---
User typed text here with [Ctrl+C] and [Ctrl+V] shortcuts
--- Window: Another App | 2024-01-15 15:00:00 ---
More keystroke data...
```

### Special Key Mappings

- **Modifiers**: `[Ctrl]`, `[Shift]`, `[Alt]`
- **Function Keys**: `[F1]`, `[F2]`, etc.
- **Navigation**: `[UP]`, `[DOWN]`, `[LEFT]`, `[RIGHT]`
- **Control**: `[Ctrl+C]`, `[Ctrl+V]`, `[Ctrl+X]`, etc.

## 🚨 Legal and Ethical Considerations

### Permitted Uses
- **Educational purposes** and learning about system monitoring
- **Authorized workplace monitoring** with proper consent
- **Personal computer monitoring** on your own devices
- **Security research** and penetration testing (with permission)

### Prohibited Uses
- **Unauthorized surveillance** of others
- **Corporate espionage** or data theft
- **Stalking** or harassment
- **Violation of privacy laws** or regulations

### Compliance
- Ensure compliance with local laws (GDPR, CCPA, etc.)
- Obtain proper consent before monitoring
- Respect privacy rights and data protection regulations
- Use only for legitimate, authorized purposes

## 🔧 Building from Source

### Creating Executable

```bash
# Install PyInstaller
pip install pyinstaller

# Build executable
pyinstaller --onefile keylogger_listener.py
```

### Custom Build Options

```bash
# Build with console hidden (Windows)
pyinstaller --onefile --windowed keylogger_listener.py

# Build with custom icon
pyinstaller --onefile --icon=icon.ico keylogger_listener.py
```

## 🐛 Troubleshooting

### Common Issues

1. **Permission Denied**: Run as Administrator
2. **Import Errors**: Ensure all dependencies are installed
3. **Keyboard Hook Failures**: Check antivirus software interference
4. **Encryption Errors**: Verify password consistency between files

### Debug Mode

Add debug prints to troubleshoot:

```python
# Add to keylogger_listener.py
print(f"Captured: {key}")
```

## 📝 License

This project is provided for educational purposes. Users are responsible for compliance with applicable laws and regulations.

## 🤝 Contributing

Contributions are welcome! Please ensure:

1. Code follows Python PEP 8 standards
2. All changes include appropriate documentation
3. Security considerations are addressed
4. Legal compliance is maintained

## 📞 Support

For questions or issues:

1. Check the troubleshooting section
2. Review legal compliance requirements
3. Ensure proper authorization for use
4. Contact maintainers for technical support

## ⚡ Performance Notes

- **Memory Usage**: Minimal memory footprint (~10-20MB)
- **CPU Usage**: Low CPU utilization during normal operation
- **Storage**: Encrypted logs grow based on typing activity
- **Network**: No network communication (local operation only)

## 🔄 Updates and Maintenance

- Regularly update dependencies for security patches
- Monitor for new privacy regulations
- Review and update encryption methods as needed
- Test compatibility with new OS versions

---

**Remember**: This tool is a powerful monitoring solution. Use it responsibly, legally, and ethically. Always respect privacy rights and obtain proper authorization before monitoring any system or user.
