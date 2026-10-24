# Facebook Auto Reporter - The Giant

An automated Python-based tool built with Selenium to streamline and submit automated reports on Facebook profiles efficiently, featuring custom red animated branding and attribution by **The Giant**.

---

## Features

- **Automated Profile Reporting**: Automatically navigates, fills out, and submits reports on target Facebook profiles.
- **JavaScript Click Interception Handling**: Solves UI overlap issues (`ElementClickInterceptedException`) using reliable JavaScript click handling.
- **Persistent Session Storage**: Uses a local Google Chrome profile directory to keep you logged into Facebook without needing to re-login every run.
- **The Giant Aesthetic**: Custom red animated ASCII banner, watermark, and author attribution.

---

## Installation & Setup Guide

Follow these steps to set up the isolated environment and run the tool on Linux/macOS systems:

### 1. Clone the Repository
```bash
git clone https://github.com/thegiant21/facebook-auto-reporter.git
cd facebook-auto-reporter
```

### 2. Install Python Virtual Environment Package
If you are using Ubuntu/Debian and do not have `venv` installed, run:
```bash
sudo apt update && sudo apt install python3-venv python3-pip -y
```

### 3. Create a Virtual Environment
Create a clean and isolated Python environment:
```bash
python3 -m venv venv
```

### 4. Activate the Virtual Environment
Activate the isolated environment using the following command:
```bash
source venv/bin/activate
```

### 5. Install Dependencies
Install all required Python packages using `requirements.txt`:
```bash
pip install -r requirements.txt
```

---

## Requirements

Ensure your `requirements.txt` file contains the following dependencies:
```text
pystyle==2.0
selenium>=4.0.0
```

---

## Running the Tool

1. Make sure your virtual environment is active (`(venv)` should appear in your terminal prompt).
2. Execute the main reporter script:
```bash
python reporter.py
```
3. Enter the target Facebook profile URL when prompted.
4. Log into Facebook in the opened Chrome browser window (if not already logged in), then press **Enter** in your terminal to start the automated reporting process.

To deactivate the virtual environment when you are done:
```bash
deactivate
```

---

## Author & Attribution

- **Created by**: The Giant
- **GitHub**: [https://github.com/thegiant21](https://github.com/thegiant21)
