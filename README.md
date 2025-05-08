# KeyLogger

⚠️ WARNING: This repository is for EDUCATIONAL PURPOSES ONLY in a controlled, sandboxed environment. Unauthorized use of this code to capture data without explicit consent is ILLEGAL and UNETHICAL. Always obtain permission before running on any system.
This project provides a Python-based keylogger implementation for studying keylogger mechanics and developing defensive cybersecurity techniques (e.g., detection and prevention). It captures keystrokes, mouse events, screenshots, audio, and system information, then sends reports via email. The code is intended for academic research or cybersecurity training in a secure, isolated environment.<br>

# Purpose

Understand how keyloggers function to build better detection tools.<br>
Learn secure coding practices and the importance of user consent.<br>
Practice cybersecurity defense by analyzing malicious software behavior.<br>

# Features

Captures keystrokes, mouse movements, clicks, and scrolls using pynput.<br>
Takes screenshots with pyscreenshot.<br>
Records audio via sounddevice.<br>
Collects system information (hostname, IP, OS, etc.).<br>
Sends reports via SMTP with logs, screenshots, and audio attachments.<br>
Logs runtime details to a file for debugging and analysis.<br>

# Repository Structure

keylogger-educational/<br>
├── keylogger.py          # Main keylogger script<br>
├── keylogger_data/       # Directory for screenshots and audio (created at runtime)<br>
├── keylogger.log         # Runtime log file (created at runtime)<br>
├── README.md             # This file<br>
└── requirements.txt      # Dependency list<br>

# Prerequisites

Sandbox Environment: A virtual machine (e.g., VirtualBox, VMWare) with no network access unless testing SMTP.<br>
Python: Version 3.7+ (required for Pillow==9.3.0).<br>
Operating System: Tested on Windows and Linux.<br>
SMTP Server: Access to a test SMTP server (e.g., Mailtrap) for email testing.<br>

# Installation

Set Up a Sandbox:<br>

Create a virtual machine with Python 3.7+ installed.<br>
Disable network access unless testing SMTP functionality.<br>
Enable snapshots to revert changes after testing.<br>


# Clone the Repository:

git clone https://github.com/Rishabh001pawar/KeyLogger.git <br>
cd keyLogger<br>


Install Dependencies:Create a virtual environment (optional but recommended) and install dependencies:<br>
python -m venv venv<br>
source venv/bin/activate  # Linux/Mac<br>
venv\Scripts\activate     # Windows<br>
pip install -r requirements.txt<br>

The requirements.txt should contain:<br>
pynput==1.7.3<br>
pyscreenshot==0.5.1<br>
sounddevice==0.4.3<br>
Pillow==9.3.0<br>
numpy<br>


<h3>Configure SMTP (for email testing):Set environment variables to avoid hardcoding credentials:<h3>
export KEYLOGGER_EMAIL="your_smtp_username"<br>
export KEYLOGGER_PASSWORD="your_smtp_password"<br>
export SMTP_SERVER="smtp.mailtrap.io"<br>
export SMTP_PORT="2525"<br>

Alternatively, edit keylogger.py to replace YOUR_USERNAME and YOUR_PASSWORD with test credentials (not recommended).<br>


# Usage

<h3>repare the Environment:</h3>

Ensure the sandbox has no network access unless testing SMTP.<br>
Verify keylogger_data/ is writable (created automatically).<br>


<h3>Run the Keylogger:</h3>
python keylogger.py

The script will:<br>

Log keystrokes, mouse events, and system information.<br>
Save screenshots and audio to keylogger_data/.<br>
Send reports every 60 seconds (configurable via SEND_REPORT_EVERY) to the specified email.<br>
Log details to keylogger.log.<br>


<h3>Stop the Keylogger:</h3>

Press Ctrl+C to terminate.<br>
Alternatively, kill the Python process (pkill python on Linux, taskkill /IM python.exe /F on Windows).<br>


<h3>Inspect Output Files:</h3>

Check keylogger_data/ for:<br>
Screenshots (screenshot_*.png).<br>
Audio files (audio_*.wav).<br>


Verify content by opening files.<br>

<h3>Test Email Delivery (optional):</h3>

Configure a test SMTP server (e.g., Mailtrap).<br>
Enable network access temporarily.<br>
Run the script and verify emails contain logs, screenshots, and audio attachments.<br>
Disable network access after testing.<br>


<h3>Simulate Detection:</h3>

Monitor processes:ps aux | grep python  # Linux<br>
tasklist | findstr python  # Windows<br>

<br>
Check for file writes in keylogger_data/.<br>
Use tools like Wireshark to detect SMTP traffic (if network-enabled).<br>


<h3>Revert Changes:</h3>

Restore the VM snapshot to reset the environment.<br>
Delete keylogger_data/ and keylogger.log if no longer needed.<br>



# Ethical and Legal Considerations

Consent: Never run this code without explicit permission from the system owner. Unauthorized use violates privacy laws (e.g., GDPR, CCPA) and may lead to legal consequences.<br>
Educational Use: Use only in a sandbox for:<br>
Studying keylogger behavior.<br>
Developing detection tools (e.g., monitoring pynput or SMTP activity).<br>
Learning secure coding practices.<br>


<h3>Defensive Applications:</h3>
Write scripts to detect pynput or sounddevice processes.
Use AppLocker (Windows) or AppArmor (Linux) to restrict script execution.
Monitor network traffic for unauthorized SMTP connections.



# Troubleshooting

ModuleNotFoundError: Verify dependencies in requirements.txt are installed (pip list).<br>
SMTP Errors: Check SMTP credentials and server settings. Test with Mailtrap for safety.<br>
Screenshot/Audio Issues: Ensure keylogger_data/ is writable. Check keylogger.log for errors.<br>
Line 173 Error: If using an older version, ensure img.save(screenshot_path) in the screenshot method (fixed in the latest code).<br>

# Contributing
Contributions are welcome for educational enhancements, such as:<br>

Improved documentation for cybersecurity training.<br>
Detection scripts for keylogger activity.<br>
Better error handling or logging.To contribute:<br>


<h2>Fork the repository.</h2>
``
Create a branch (git checkout -b feature/your-feature).<br>
Commit changes (git commit -m "Add your feature").<br>
Push to the branch (git push origin feature/your-feature).<br>
Open a pull request with a clear description.<br>
``

# License
This project is licensed under the MIT License. It is provided "as is" for educational purposes. The author is not responsible for misuse or damages. Use ethically and legally.
<br>

# Contact
For questions or suggestions, open an issue or contact the repository maintainer. Do not use this code for malicious purposes.
Stay ethical, prioritize privacy, and study safely!
