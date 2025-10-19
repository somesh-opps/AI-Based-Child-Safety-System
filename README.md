# 🛡️ AI-Based Child Safety System

An intelligent RFID and facial recognition-based child safety and attendance system designed for schools and childcare facilities. The system uses Arduino RFID readers for authorization and facial recognition for automated check-in/check-out with guardian verification.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Active-success.svg)

---

## 📋 Table of Contents

- [Features](#-features)
- [System Architecture](#-system-architecture)
- [Prerequisites](#-prerequisites)
- [Installation](#-installation)
- [Configuration](#-configuration)
- [Usage](#-usage)
- [Project Structure](#-project-structure)
- [Security](#-security)
- [Troubleshooting](#-troubleshooting)
- [Contributing](#-contributing)
- [License](#-license)

---

## ✨ Features

### Core Functionality
- 🔐 **RFID Authorization** - Secure access control using authorized RFID cards
- 👤 **Facial Recognition** - Automated student identification using AI
- 👨‍👩‍👧 **Guardian Verification** - Check-out requires authorized guardian face match
- 📊 **Google Sheets Integration** - Real-time attendance logging to cloud spreadsheets
- 💬 **WhatsApp Notifications** - Automated parent notifications via WhatsApp Web
- 🖥️ **LCD Display** - Real-time status updates on Arduino-connected LCD

### Security Features
- 🔒 Environment-based configuration (no hardcoded credentials)
- 🚫 Protected sensitive files via `.gitignore`
- ✅ Configuration validation before startup
- 🔑 Support for multiple authorized RFID cards
- 👥 Support for multiple guardians per student

### User Experience
- ⚡ Real-time face detection and recognition
- 🔄 Sequential check-in/check-out workflow
- ❌ Duplicate prevention (no double check-ins)
- 📝 Detailed logging with timestamps
- 🎯 Cooldown periods to prevent accidental duplicate scans

---

## 🏗️ System Architecture

```
┌─────────────────┐
│  RFID Reader    │
│   (Arduino)     │
└────────┬────────┘
         │
         │ Serial USB
         │
┌────────▼────────────────────────────────────────┐
│                                                  │
│           Main Control System                   │
│         (main_rfid_control.py)                  │
│                                                  │
│  ┌──────────────┐        ┌──────────────┐     │
│  │   Check-in   │        │  Check-out   │     │
│  │    Module    │        │    Module    │     │
│  │ (checkin.py) │        │(checkout.py) │     │
│  └──────┬───────┘        └──────┬───────┘     │
│         │                        │              │
└─────────┼────────────────────────┼──────────────┘
          │                        │
    ┌─────▼────────┐        ┌─────▼────────┐
    │   Camera     │        │   Camera     │
    │ (Face Recog) │        │ (Guardian)   │
    └─────┬────────┘        └─────┬────────┘
          │                        │
          └────────┬───────────────┘
                   │
        ┌──────────▼──────────┐
        │                     │
        │  Output Services    │
        │                     │
        │  • Google Sheets    │
        │  • WhatsApp         │
        │  • Local Logs       │
        │  • LCD Display      │
        │                     │
        └─────────────────────┘
```

---

## 🔧 Prerequisites

### Hardware Requirements
- **Arduino** (Uno, Mega, or compatible)
- **MFRC522 RFID Reader** module
- **RFID Cards/Tags** for authorization
- **USB Webcam** (or laptop camera)
- **LCD Display** (16x2 or 20x4, I2C recommended)
- **Computer** running Windows/Linux/macOS

### Software Requirements
- **Python 3.8+**
- **Arduino IDE** (for uploading Arduino sketch)
- **Google Chrome** (for WhatsApp Web automation)
- **Google Cloud Account** (for Sheets API)

### Python Libraries
See `requirements.txt` for complete list. Key dependencies:
- `opencv-python` - Computer vision and camera access
- `face-recognition` - AI-based facial recognition
- `pyserial` - Arduino communication
- `gspread` - Google Sheets integration
- `pywhatkit` - WhatsApp automation
- `python-dotenv` - Environment variable management

---

## 📦 Installation

### 1. Clone the Repository
```bash
git clone https://github.com/somesh-opps/AI-Based-Child-Safety-System.git
cd AI-Based-Child-Safety-System
```

### 2. Install Python Dependencies
```bash
# Install in this order for best compatibility:
pip install cmake
pip install dlib
pip install face-recognition
pip install -r requirements.txt
```

### 3. Set Up Arduino
1. Upload the RFID reader sketch to your Arduino (sketch not included - use standard MFRC522 example)
2. Ensure Arduino sends RFID data in format: `RFID:CARD_ID`
3. Configure Arduino to receive LCD commands via serial

### 4. Configure Google Cloud
1. Create a project in [Google Cloud Console](https://console.cloud.google.com/)
2. Enable Google Sheets API and Google Drive API
3. Create a service account and download the JSON key file
4. Share your "Attendance Records" spreadsheet with the service account email

### 5. Set Up Student Database
Create a directory structure like this:
```
STUDENTS/
├── Student_Name_1/
│   ├── photo1.jpg
│   ├── photo2.jpg
│   ├── phone.txt          (Parent's WhatsApp number with country code)
│   └── guardian/
│       ├── mother.jpg
│       └── father.jpg
├── Student_Name_2/
│   └── ...
```

---

## ⚙️ Configuration

### Step 1: Create Environment File
```bash
# Copy the example file
copy .env.example .env    # Windows
# OR
cp .env.example .env      # Linux/Mac
```

### Step 2: Edit `.env` File
Open `.env` in a text editor and update all values:

```env
# Arduino Configuration
ARDUINO_SERIAL_PORT=COM4                    # Check Device Manager (Windows) or /dev/ttyUSB0 (Linux)
ARDUINO_BAUD_RATE=9600
RFID_AUTHORIZED_CARDS=CARD_ID_1,CARD_ID_2  # Your actual RFID card IDs (uppercase)

# Paths
STUDENTS_DIR=D:/Path/To/STUDENTS
OUTPUT_FILE=D:/Path/To/attendance_log.txt
SERVICE_ACCOUNT_KEY_PATH=D:/Path/To/your-service-account-key.json

# Google Sheets
GOOGLE_SHEETS_NAME=Attendance Records

# Camera
CAM_INDEX=0                                  # 0 for default camera, 1 for external

# Face Recognition Settings
DETECTION_MODEL=hog                          # 'hog' (faster, CPU) or 'cnn' (accurate, GPU)
TOLERANCE=0.6                                # Lower = stricter matching (0.0-1.0)
FRAME_SCALE=0.5                              # Scale frames for faster processing

# WhatsApp Settings
WHATSAPP_WAIT_TIME=4
ENTER_DELAY_SEC=8
WHATSAPP_TAB_CLOSE_DELAY=12
```

### Step 3: Validate Configuration
```bash
python config_template.py
```

This will check:
- ✅ All required files exist
- ✅ Paths are valid
- ✅ RFID cards are configured
- ✅ Service account key is accessible

---

## 🚀 Usage

### Starting the System
```bash
python main_rfid_control.py
```

### Workflow

#### Authorization
1. **Scan authorized RFID card** on the reader
2. System displays: "Card Scanned! Choose Mode: 1/2"
3. Choose option:
   - `1` - Start Check-in mode
   - `2` - Start Check-out mode

#### Check-in Mode
1. System activates camera
2. **Student shows face** to camera
3. System recognizes student automatically
4. Logs attendance to Google Sheets
5. Sends WhatsApp notification to parent
6. Returns to waiting for next student
7. **Scan RFID card again to stop check-in mode**

#### Check-out Mode
1. System activates camera
2. **Student shows face** to camera (recognized first)
3. System prompts: "Show Guardian Face"
4. **Guardian shows face** to camera
5. System verifies guardian is authorized
6. Logs check-out with guardian name
7. Sends WhatsApp notification
8. Returns to waiting for next student
9. **Scan RFID card again to stop check-out mode**

### Emergency Stop
- Press `Ctrl+C` in terminal to force stop
- Or scan authorized RFID card to gracefully stop current mode

---

## 📁 Project Structure

```
AI-Based-Child-Safety-System/
├── 📄 main_rfid_control.py      # Main control system
├── 📄 checkin.py                # Check-in module with face recognition
├── 📄 checkout.py               # Check-out module with guardian verification
├── 📄 config_template.py        # Configuration loader (loads from .env)
├── 📄 requirements.txt          # Python dependencies
├── 📄 README.md                 # This file
├── 📄 SECURITY_SETUP.md         # Detailed security documentation
├── 📄 IMPLEMENTATION_SUMMARY.md # Quick implementation guide
├── 📄 .env.example              # Environment variables template
├── 📄 .gitignore                # Git ignore rules (protects sensitive files)
│
├── 📁 STUDENTS/                 # Student database (not committed)
│   └── [Student_Name]/
│       ├── *.jpg                # Student photos
│       ├── phone.txt            # Parent WhatsApp number
│       └── guardian/
│           └── *.jpg            # Guardian photos
│
├── 🔒 .env                      # Your secrets (not committed)
├── 🔒 *-service-account.json    # Google credentials (not committed)
└── 📋 attendance_log.txt        # Output logs (not committed)
```

---

## 🔐 Security

This project implements security best practices:

### Protected Information
- ✅ Service account credentials (JSON files)
- ✅ RFID card IDs
- ✅ Student personal data
- ✅ File paths and system configuration
- ✅ API keys and tokens

### Security Measures
1. **Environment Variables** - All sensitive data in `.env` file
2. **`.gitignore`** - Prevents accidental commits of sensitive files
3. **Configuration Validation** - Checks setup before running
4. **No Hardcoded Secrets** - All credentials loaded at runtime

### Important Security Notes
- 🚫 **NEVER** commit `.env` file
- 🚫 **NEVER** commit service account JSON files
- 🚫 **NEVER** commit student photos or data
- ✅ **ALWAYS** review `git status` before committing
- ✅ **ALWAYS** keep service account keys secure
- ✅ **ALWAYS** use different credentials for testing vs production

**📖 Read `SECURITY_SETUP.md` for detailed security instructions!**

---

## 🐛 Troubleshooting

### Common Issues

#### "Import dotenv could not be resolved"
```bash
pip install python-dotenv
```

#### "Serial port not found" or "Access denied"
- **Windows**: Check Device Manager for correct COM port
- **Linux**: Add user to `dialout` group: `sudo usermod -a -G dialout $USER`
- Verify Arduino is connected and drivers are installed

#### "No face detected" or "Face not recognized"
- Ensure good lighting conditions
- Student should face camera directly
- Add more photos of the student from different angles
- Adjust `TOLERANCE` in `.env` (increase for more lenient matching)

#### "Google Sheets authentication failed"
- Verify service account JSON path in `.env`
- Ensure spreadsheet is shared with service account email
- Check that Sheets API and Drive API are enabled in Google Cloud

#### "WhatsApp message not sent"
- Ensure Google Chrome is installed
- WhatsApp Web must be logged in
- Check internet connection
- Verify phone number format: `+[country_code][number]` (e.g., `+919876543210`)

#### Camera not working
- Try different `CAM_INDEX` values (0, 1, 2...)
- Check camera permissions
- Close other apps using camera
- On Linux, check `/dev/video*` permissions

---

## 📊 Data Format

### Phone Numbers (`phone.txt`)
```
+919876543210
```
Format: `+[country_code][phone_number]` (no spaces or hyphens)

### Google Sheets Structure
The system automatically creates columns with format:
```
| Name      | 2025-10-19 (Check-in) | 2025-10-19 (Check-out) |
|-----------|------------------------|-------------------------|
| Student_1 | 08:30:15              | 15:45:20 (Guardian: Mom)|
| Student_2 | 08:35:42              | 16:00:10 (Guardian: Dad)|
```

---

## 🤝 Contributing

Contributions are welcome! Please follow these guidelines:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

**⚠️ Important:** Never include sensitive data in pull requests!

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Somesh**
- GitHub: [@somesh-opps](https://github.com/somesh-opps)
- Repository: [AI-Based-Child-Safety-System](https://github.com/somesh-opps/AI-Based-Child-Safety-System)

---

## 🙏 Acknowledgments

- **OpenCV** - Computer vision library
- **face_recognition** - Facial recognition built on dlib
- **Arduino** - Microcontroller platform
- **Google Cloud** - Sheets API and cloud services
- **pywhatkit** - WhatsApp automation

---

## 📞 Support

If you encounter issues:
1. Check the [Troubleshooting](#-troubleshooting) section
2. Review `SECURITY_SETUP.md` for configuration help
3. Run configuration validator: `python config_template.py`
4. Open an issue on GitHub with detailed error messages

---

## 🔄 Version History

- **v1.0.0** (2025-10-19)
  - Initial release
  - RFID authorization system
  - Facial recognition check-in/check-out
  - Guardian verification
  - Google Sheets integration
  - WhatsApp notifications
  - Security-first configuration system

---

## 🎯 Future Enhancements

- [ ] Web dashboard for real-time monitoring
- [ ] Mobile app for parents
- [ ] SMS notifications as fallback
- [ ] Multiple camera support
- [ ] Automated daily reports
- [ ] Face mask detection
- [ ] Temperature screening integration
- [ ] Multi-language support

---

## ⚖️ Disclaimer

This system is designed for educational and childcare facility use. Users are responsible for:
- Complying with local data protection laws (GDPR, COPPA, etc.)
- Obtaining proper consent for facial recognition
- Securing all biometric and personal data
- Regular security audits
- Proper hardware maintenance

---

<div align="center">

**Made with ❤️ for Child Safety**

⭐ Star this repo if you find it helpful!

</div>
