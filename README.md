# 🧪 Saucedemo Selenium Automation (Python + Pytest)

This project is a complete automation framework for testing Saucedemo.com  
It follows best practice standards such as Page Object Model (POM), Pytest, and clean test structuring.

---

## 🚀 Features

- ✅ Python + Selenium WebDriver
- ✅ Pytest fixtures and conftest
- ✅ Page Object Model (POM)
- ✅ Test data from YAML/JSON
- ✅ Reusable driver setup
- ✅ Allure/HTML test reports
- ✅ Cross-browser capability (Chrome/Firefox)
- ✅ Easy to extend for more test cases
---



## Install dependencies:

pip install -r requirements.txt


## ▶️ How to Run Tests and generate reports

pytest -v
pytest --alluredir=reports/allure-results
allure serve reports/allure-results



## The HTML report will be saved inside:

reports/report.html



## Technologies Used

Python

Selenium

Pytest

allure

Page Object Model (POM)
