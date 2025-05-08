# 🛡️ KeyLogger (Educational Use Only)

⚠️ **WARNING**: This repository is strictly for **educational purposes only** in a **controlled, sandboxed environment**. Unauthorized use of this code to capture data without **explicit consent** is **ILLEGAL** and **UNETHICAL**. Always obtain permission before executing it on any system.

This project demonstrates a Python-based keylogger for understanding keylogger mechanics and improving defensive cybersecurity skills. It captures keystrokes, mouse events, screenshots, audio, and system information, and sends them via email. Intended for research and ethical cybersecurity training only.

---

## 🎯 Purpose

- Understand how keyloggers function to build better detection and prevention tools.
- Learn secure coding practices and ethical boundaries in cybersecurity.
- Practice analyzing malicious software behavior in a safe environment.

---

## ✨ Features

- ✅ Capture keystrokes, mouse clicks, movements, and scrolls (`pynput`)
- 📸 Take screenshots (`pyscreenshot`)
- 🎙️ Record audio via the microphone (`sounddevice`)
- 🖥️ Collect system information (hostname, IP address, OS, etc.)
- 📧 Send email reports via SMTP with attached logs, screenshots, and audio
- 📝 Runtime logs stored in `keylogger.log` for analysis

---


## ⚙️ Prerequisites

- **Sandbox Environment**: Virtual machine (e.g., VirtualBox, VMware) without network access (unless testing email functionality).
- **Python**: Version 3.7+ (for Pillow compatibility).
- **OS**: Tested on Windows and Linux.
- **SMTP**: Access to a test SMTP server (e.g., [Mailtrap](https://mailtrap.io)).

---

## 🚀 Installation

### 1. Set Up a Safe Sandbox Environment

- Install Python 3.7+ in a virtual machine.
- Disable networking unless testing email sending.
- Create VM snapshots to restore after testing.

### 2. Clone the Repository

```bash
git clone https://github.com/Rishabh001pawar/KeyLogger.git
cd KeyLogger
```

##  Install Dependencies

# Optional: Create a virtual environment
python -m venv venv
# Activate it
source venv/bin/activate <br>     # On Linux/macOS<br> 
venv\Scripts\activate  <br>          # On Windows<br> 

# Install required libraries
pip install -r requirements.txt

-Contents of requirements.txt:
pynput==1.7.3<br> 
pyscreenshot==0.5.1<br> 
sounddevice==0.4.3<br> 
Pillow==9.3.0<br> 
numpy<br> 


## 🧪 Usage

1. Prepare Environment
- Ensure no internet access (except for SMTP testing).
-Ensure the keylogger_data/ directory is writable (auto-created if missing).

2. Run the Keylogger
```bash
python keylogger.py
```

<h3>This will:</h3>

- Log keystrokes and mouse events
- Capture screenshots and audio clip
- Collect system info
- Send a report every 60 seconds (customizable)


3. Stop the Keylogger
- Press Ctrl + C to manually stop
-- Or terminate process:
- pkill python (Linux)
- taskkill /IM python.exe /F (Windows)


## 📧 Test Email Delivery (Optional)

- Temporarily re-enable networking
- Use a test SMTP service like Mailtrap
- Confirm delivery with attachments

## 🔐 Simulate Detection

- Monitor running processes:
   <br>-Linux: ps aux | grep python
   <br>-Windows: tasklist | findstr python
- Monitor file changes in keylogger_data/
- Use Wireshark to detect outbound SMTP traffic

## 🧹 Cleanup
- Restore VM snapshot to revert changes
- Delete keylogger_data/ and keylogger.log manually if needed

# ⚖️ Ethical and Legal Considerations
- 🔒 NEVER use this on a real or third-party system without explicit consent.
- Violating privacy laws (e.g., GDPR, CCPA) may lead to legal consequences.
-- Use only for:
  <br>- Research and education
  <br>- Secure coding and reverse engineering training

## 🛡️ Defensive Applications
- Create scripts to detect pynput or sounddevice activity
- Use OS-level controls like AppLocker (Windows) or AppArmor (Linux)
- Monitor outbound SMTP or unusual log writes

## 🛠️ Troubleshooting
- ModuleNotFoundError: Check pip list to verify packages
- SMTP Errors: Check your credentials and Mailtrap settings
- Screenshot or Audio Fails: Ensure the VM supports those features and directory is writable
- Line 173 or img.save() Errors: Use the latest script version with img.save(screenshot_path)

## 🤝 Contributing
- We welcome educational contributions! You can help by:
- Improving documentation
- Adding new detection or analysis tools
- Enhancing error handling and logging

STEPS:
```
git checkout -b feature/your-feature
git commit -m "Add your feature"
git push origin feature/your-feature
# Then open a pull request
```

##📬 Contact
For questions, open an issue or contact the repository maintainer.<br>
✨ Stay ethical. Prioritize privacy. Study safely. ✨<br>


