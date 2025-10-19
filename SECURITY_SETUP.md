# AI-Based Child Safety System - Security Setup Guide

## 🔒 Security Notice

This project has been configured to protect sensitive information from being committed to version control. **NEVER commit files containing:**
- Private keys or credentials
- RFID card IDs
- Personal information
- API keys or service account credentials

---

## 📋 Initial Setup Instructions

### Step 1: Install Required Python Package

This project requires `python-dotenv` to load environment variables:

```powershell
pip install python-dotenv
```

### Step 2: Create Your Environment File

1. Copy the example environment file:
   ```powershell
   Copy-Item .env.example -Destination .env
   ```

2. Open `.env` in a text editor and fill in your actual values:
   ```
   ARDUINO_SERIAL_PORT=COM4
   RFID_AUTHORIZED_CARDS=YOUR_CARD_1,YOUR_CARD_2,YOUR_CARD_3
   STUDENTS_DIR=D:/Your/Path/To/STUDENTS
   OUTPUT_FILE=D:/Your/Path/To/attendance_log.txt
   SERVICE_ACCOUNT_KEY_PATH=D:/Your/Path/To/your-service-account.json
   ```

3. **NEVER commit the `.env` file!** It's already in `.gitignore`.

### Step 3: Verify Your Configuration

Run the configuration validator:

```powershell
python config_template.py
```

This will check if all required files and settings are properly configured.

### Step 4: Protect Your Service Account Key

Your Google Cloud service account JSON file contains sensitive credentials:

1. **Keep it outside the project directory** (recommended) or ensure `.gitignore` is protecting it
2. **Update the path in your `.env` file** to point to its location
3. **Set proper file permissions** so only you can read it

---

## 🚫 What's Protected by .gitignore

The following files and directories will NOT be committed to Git:

- `*.json` - Service account keys and other JSON config files
- `.env` - Your environment variables file
- `config.py` - If you create a custom config file
- `STUDENTS/` - Student photos and personal data
- `*.log` - Log files with attendance records
- Various Python cache and IDE files

---

## 🔧 Configuration Files Explained

### `.env` (Create this yourself)
Contains your actual sensitive values. **Never commit this file!**

### `.env.example` (Committed to Git)
Template showing what variables are needed. Safe to commit.

### `config_template.py` (Committed to Git)
Loads environment variables from `.env` and provides them to the application.

---

## 🏃 Running the Application

After setup is complete, run the main application:

```powershell
python main_rfid_control.py
```

The application will:
1. Validate your configuration
2. Check that all required files exist
3. Start the RFID control system

---

## ⚠️ Security Best Practices

### For This Project:
- ✅ Keep `.env` file local only
- ✅ Store service account keys outside the project directory
- ✅ Use different RFID cards for production vs testing
- ✅ Regularly rotate your Google Cloud service account keys
- ✅ Review `.gitignore` before committing any new files

### Before Committing:
Always check what you're about to commit:

```powershell
git status
git diff
```

### If You Accidentally Committed Sensitive Data:
1. **Immediately revoke/rotate the exposed credentials**
2. Remove from Git history:
   ```powershell
   # For a specific file
   git filter-branch --force --index-filter "git rm --cached --ignore-unmatch path/to/sensitive/file" --prune-empty --tag-name-filter cat -- --all
   ```
3. Force push to remote (if already pushed):
   ```powershell
   git push origin --force --all
   ```

---

## 📁 Project Structure

```
AI-Based-Child-Safety-System/
├── .env                          # Your secrets (NOT committed)
├── .env.example                  # Template (committed)
├── .gitignore                    # Protects sensitive files
├── config_template.py            # Configuration loader (committed)
├── main_rfid_control.py          # Main application
├── checkin.py                    # Check-in module
├── checkout.py                   # Check-out module
├── ai-based-child-safety-*.json  # Service account (NOT committed)
├── STUDENTS/                     # Student data (NOT committed)
│   └── [student_name]/
│       ├── photo.jpg
│       ├── phone.txt
│       └── guardian/
│           └── guardian_name.jpg
└── attendance_log.txt            # Output logs (NOT committed)
```

---

## 🆘 Troubleshooting

### "Import dotenv could not be resolved"
```powershell
pip install python-dotenv
```

### "Configuration validation failed"
1. Check that your `.env` file exists
2. Verify all paths in `.env` point to existing files/directories
3. Run `python config_template.py` to see specific errors

### "Service account key file not found"
Update the `SERVICE_ACCOUNT_KEY_PATH` in your `.env` file with the correct path.

### "No RFID authorized cards configured"
Ensure `RFID_AUTHORIZED_CARDS` in `.env` has at least one card ID.

---

## 📞 Support

If you encounter issues:
1. Verify all paths in `.env` are correct
2. Check that required Python packages are installed
3. Run the configuration validator: `python config_template.py`
4. Review error messages carefully

---

## 🔐 Remember

**Security is everyone's responsibility!**
- Never share your `.env` file
- Never commit sensitive files
- Regularly review what's in your repository
- When in doubt, ask before committing

---

*Last Updated: October 19, 2025*
