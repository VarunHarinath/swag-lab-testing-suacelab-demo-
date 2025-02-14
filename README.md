# 🏎️ Python Selenium Automation  

Welcome to the **Selenium Automation Testing** project! 🚀 This repository contains automated test cases designed to run on **Sauce Labs** using Selenium.  

---

## 📌 Prerequisites  

Before running the tests, ensure you have the following installed:  
- 🐍 **Python 3.13.0**  
- 📦 **pip (Python package manager) 24.2**  

---

## 📥 Installation  

### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/VarunHarinath/swag-lab-testing-suacelab-demo-
cd swag-lab-testing
```

### 2️⃣ Create & Activate a Virtual Environment  

#### 🔹 On **Mac/Linux**:  
```bash
python -m venv venv
source venv/bin/activate
```

#### 🔹 On **Windows**:  
```bash
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install Dependencies  
```bash
pip install -r requirements.txt
```

---

## 🚀 Running the Tests  

Once everything is set up, you can run the test cases with:  
```bash
python saucelabs_test_cases.py -v
```
The `-v` flag runs the test suite in verbose mode, so you can see detailed output.

---

## 🛠️ Project Structure  

```
📂 swag-lab-testing
│-- 📂 __pycache__/               # Compiled Python files
│-- 📂 .pytest_cache/             # Pytest cache
│-- 📂 assets/                    # Contains CSS files for reports
│   │-- 📄 style.css
│-- 📂 pages/                     # Page Object Model (POM) files
│   │-- 📄 BasePage.py
│   │-- 📄 Login_page.py
│   │-- 📄 Product_Page.py
│-- 📂 utils/                     # Utility files for testing
│   │-- 📄 WaitUtil.py
│-- 📄 .gitignore                  # Git ignore file
│-- 📄 conftest.py                  # Pytest configuration file
│-- 📄 report.html                  # Test execution report
│-- 📄 requirements.txt             # Required dependencies
│-- 📄 saucelabs_test_cases.py      # Main test suite
```

---

## 📝 Notes  

- Ensure your **Selenium WebDriver** is compatible with your browser.  
- If you face **authentication issues**, check your Sauce Labs credentials.  
- Always activate the virtual environment before running the tests.  

---

## 🤝 Contributing  

Feel free to fork this repository, make improvements, and submit a **pull request**! 💡  

---

### 🏁 Happy Testing! 🚀🎯  
