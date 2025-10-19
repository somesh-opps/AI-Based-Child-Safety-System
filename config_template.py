# This is a template - copy to config.py and fill in your actual values
# The config.py file should NEVER be committed to Git!

import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# ===================================
# Arduino/RFID Settings
# ===================================
ARDUINO_SERIAL_PORT = os.getenv('ARDUINO_SERIAL_PORT', 'COM4')
ARDUINO_BAUD_RATE = int(os.getenv('ARDUINO_BAUD_RATE', '9600'))

# Parse RFID cards from comma-separated string
rfid_cards_str = os.getenv('RFID_AUTHORIZED_CARDS', 'E38ADA26,13326C28,93D6E113')
RFID_AUTHORIZED_CARDS = [card.strip().upper() for card in rfid_cards_str.split(',')]

# ===================================
# Directory and File Paths
# ===================================
STUDENTS_DIR = os.getenv('STUDENTS_DIR', r'D:/ScriptSanctuary/ProjectVault/AI-Based-Child-Safety-System/STUDENTS')
OUTPUT_FILE = os.getenv('OUTPUT_FILE', r'D:/ScriptSanctuary/ProjectVault/AI-Based-Child-Safety-System/attendance_log.txt')
SERVICE_ACCOUNT_KEY_PATH = os.getenv('SERVICE_ACCOUNT_KEY_PATH', r'D:/ScriptSanctuary/ProjectVault/AI-Based-Child-Safety-System/ai-based-child-safety-19c12c299c33.json')

# ===================================
# Google Sheets Settings
# ===================================
GOOGLE_SHEETS_NAME = os.getenv('GOOGLE_SHEETS_NAME', 'Attendance Records')
SCOPES = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]

# ===================================
# Camera Settings
# ===================================
CAM_INDEX = int(os.getenv('CAM_INDEX', '0'))

# ===================================
# Face Recognition Settings
# ===================================
DETECTION_MODEL = os.getenv('DETECTION_MODEL', 'hog')
TOLERANCE = float(os.getenv('TOLERANCE', '0.6'))
FRAME_SCALE = float(os.getenv('FRAME_SCALE', '0.5'))
PROCESS_EVERY_N = int(os.getenv('PROCESS_EVERY_N', '2'))

# ===================================
# WhatsApp Settings
# ===================================
WHATSAPP_WAIT_TIME = int(os.getenv('WHATSAPP_WAIT_TIME', '4'))
ENTER_DELAY_SEC = int(os.getenv('ENTER_DELAY_SEC', '8'))
WHATSAPP_TAB_CLOSE_DELAY = int(os.getenv('WHATSAPP_TAB_CLOSE_DELAY', '12'))

# Message templates
CHECKIN_MESSAGE_TEMPLATE = os.getenv('CHECKIN_MESSAGE_TEMPLATE', '{name} is present.\\nEntry date & time: {ts}')
CHECKOUT_MESSAGE_TEMPLATE = os.getenv('CHECKOUT_MESSAGE_TEMPLATE', '{student} checked out with Guardian: {guardian}\\nDate & Time: {ts}')

# ===================================
# Validation
# ===================================
def validate_config():
    """Validate that required configuration is present"""
    errors = []
    
    if not os.path.exists(SERVICE_ACCOUNT_KEY_PATH):
        errors.append(f"Service account key file not found: {SERVICE_ACCOUNT_KEY_PATH}")
    
    if not os.path.exists(STUDENTS_DIR):
        errors.append(f"Students directory not found: {STUDENTS_DIR}")
    
    if len(RFID_AUTHORIZED_CARDS) == 0:
        errors.append("No RFID authorized cards configured")
    
    if errors:
        print("[CONFIG ERROR] Configuration validation failed:")
        for error in errors:
            print(f"  - {error}")
        return False
    
    return True

if __name__ == "__main__":
    print("[CONFIG] Configuration loaded successfully!")
    print(f"  - Arduino Port: {ARDUINO_SERIAL_PORT}")
    print(f"  - Baud Rate: {ARDUINO_BAUD_RATE}")
    print(f"  - Authorized RFID Cards: {len(RFID_AUTHORIZED_CARDS)} cards")
    print(f"  - Students Directory: {STUDENTS_DIR}")
    print(f"  - Output File: {OUTPUT_FILE}")
    print(f"  - Service Account Key: {SERVICE_ACCOUNT_KEY_PATH}")
    print(f"  - Google Sheets: {GOOGLE_SHEETS_NAME}")
    print(f"\\n[CONFIG] Validating configuration...")
    if validate_config():
        print("[CONFIG] ✓ All configuration is valid!")
    else:
        print("[CONFIG] ✗ Configuration validation failed. Please check the errors above.")
