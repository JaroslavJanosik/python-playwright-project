# Simple Automation Framework

This repository contains a lightweight test automation framework built using **Python**, **PyTest**, and **Playwright**. The instructions below will help you set up your development environment and run automated tests.

---

## 📋 Prerequisites

Before you begin, ensure the following components are installed on your system:

1. **Python 3.11.5**
   - Download: [Python 3.11.5 (64-bit)](https://www.python.org/downloads/release/python-3115/)

2. **Poetry** (for dependency management)
   - Install via pip:
```bash
  python -m pip install poetry
  ```

> ⚠️ **Note for Windows users**:  
After installing Python, update your installation to include environment variables:  
Go to **Control Panel → Programs and Features → Python Installation → Change → Modify → Add Python to environment variables**, then restart your PC.

---

## 🛠️ Project Setup

Follow these steps to clone the repository and set up your local environment:

1. **Clone the repository**:
```bash
  git clone https://github.com/JaroslavJanosik/PythonPlaywrightProject.git
  cd python-playwright-project
```

2. **Configure Poetry to create virtual environment inside the project**:
```bash
  poetry config virtualenvs.in-project true
```

3. **Install project dependencies**:
```bash
  poetry install
```

4. **Activate the virtual environment**:
```bash
  poetry shell
```

5. **Install Playwright browsers**:
```bash
  poetry run playwright install
```

---

## ▶️ Test Execution Instructions

You can run the automated tests using various configurations:

### ✅ Run All Tests
```bash
  poetry run pytest
```

### 🖥️ Run Tests in Headed Mode
```bash
  poetry run pytest --headed
```

### 🔖 Run Tests by Marker
```bash
  poetry run pytest -m "your_marker_name"
```

_Example:_
```bash
  poetry run pytest -m "Regress"
```

### 🐞 Run Tests in Debug Mode
Enables Playwright Inspector for debugging:
```bash
  PWDEBUG=1 poetry run pytest
```

---

## 🧰 Helpful Poetry Commands

- Show environment info:  
```bash
  poetry env info
```

- List available virtual environments:  
```bash
  poetry env list
```

- Add a new dependency:  
```bash
  poetry add <package-name>
```

- Remove a dependency:  
```bash
  poetry remove <package-name>
```

- Exit the virtual environment:  
```bash
  deactivate
```

---

## 📝 Sample Test Case (Gherkin Format)

```gherkin
Feature: Seznam Email - Send Email

  Scenario: Sending an email with an attachment
    Given the user is logged into the application
    When the user sends an email with an attachment
    Then the email should be sent successfully
    And the recipient should receive the email
```
