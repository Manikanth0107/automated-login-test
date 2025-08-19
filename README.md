# 🔐 Automated Login Testing Script

An automation tool built with **Python** and **Selenium WebDriver** to test and validate login workflows for web applications.  
It can be adapted to multiple platforms and ensures authentication features work as expected under various scenarios.

---

## 🚀 Features
- **Automated Browser Actions** – Opens the target site and performs login steps
- **Credential Validation** – Tests with valid & invalid credentials
- **Configurable Settings** – Easily change credentials and URLs from `config.py`
- **Fast Feedback** – Pinpoints failures in authentication flow

---

## 🛠 Tech Stack
- **Python 3.11+**
- **Selenium WebDriver**
- **ChromeDriver / GeckoDriver**
- **PyTest** (optional, for test structuring)

---

## ⚙️ Installation & Setup

1. **Clone the Repository**
```bash
git clone https://github.com/Manikanth0107/automated-login-test.git
cd automated-login-test
```

2. **Install Dependencies**
```bash
pip install -r requirements.txt
```

3. **Update Configurations**
   - Edit config.py with:
```bash
URL = "https://example.com/login"
USERNAME = "your_username"
PASSWORD = "your_password"
```

4. **Run the Script**
   ```bash
   python login_test.py
   ```

 Example Test Flow
- Launch browser and go to login page
- Enter credentials (from config.py)
- Submit login form
- Verify authentication success/failure

 Future Improvements
- Integrate with pytest for assertions
- Add multi-browser support
- Enable CI/CD pipeline with GitHub Actions
- Capture screenshots on failure

Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.







