# Wipro_Python_Automation
Wipro Course all materials
# 🚀 Selenium Automation Lab Assignments

A collection of hands-on Python scripts demonstrating core web automation and element location techniques using **Selenium WebDriver**. 

---

## 📋 Table of Contents
- [About the Labs](#-about-the-labs)
- [Technologies Used](#️-technologies-used)
- [Lab Assignments Overview](#-lab-assignments-overview)
- [Prerequisites & Setup](#-prerequisites--setup)

---

## 🛠️ Technologies Used
* **Language:** 🐍 Python
* **Automation Tool:** 🌐 Selenium WebDriver
* **Browser Engines:** 🌍 Google Chrome, 🌐 Microsoft Edge
* **Core Concepts:** Automated Web Testing, CSS Selectors, Selenium Locators, JavaScript Executor

---

## 🔬 Lab Assignments Overview

### 🔹 Assignment 1: Using Selenium ID Locator
* **Summary:** Implemented Selenium's `By.ID` locator to identify and interact with input fields on the Test Automation Practice website. The program locates the Name, Email, Phone, and Address fields and enters sample data into each field.
* **Key Concepts:** `By.ID`, `find_element()`, `send_keys()`, browser automation
* **Website:** Test Automation Practice
* **Demo:** [🎥 Watch Recording](#)

### 🔹 Assignment 2: Bulk Element Extraction
* **Summary:** Used Selenium's `find_elements()` method with `By.TAG_NAME` to locate all anchor (`<a>`) elements on the Rahul Shetty Academy website. The program iterates through the collected links and prints their visible text and corresponding URLs.
* **Key Concepts:** `find_elements()`, `By.TAG_NAME`, anchor elements, `get_attribute("href")`
* **Website:** Rahul Shetty Academy
* **Demo:** [🎥 Watch Recording](#)

### 🔹 Assignment 3: CSS Attribute Selectors
* **Summary:** Demonstrated CSS attribute selectors for locating web elements using partial attribute values. The assignment implements the three CSS substring matching operators: `^=` for starts-with, `$=` for ends-with, and `*=` for contains.
* **Key Concepts:** CSS Selectors, `By.CSS_SELECTOR`, `^=`, `$=`, `*=`
* **Website:** Test Automation Practice
* **Demo:** [🎥 Watch Recording](#)

#### CSS Selectors Demonstrated
| Selector | Meaning | Example |
| :--- | :--- | :--- |
| **`^=`** | Starts With | `input[placeholder^='Enter N']` |
| **`$=`** | Ends With | `input[placeholder$='EMail']` |
| **`*=`** | Contains | `input[placeholder*='Phone']` |

### 🔹 Assignment 4: DOM Traversal via CSS Child Selectors
* **Summary:** Used the CSS child selector `div > a` to locate a nested anchor element on the Rahul Shetty Academy website. The program retrieves the element's tag name, text, and URL, scrolls the element into view, and clicks it using JavaScript.
* **Key Concepts:** CSS Child Selector (`div > a`), `By.CSS_SELECTOR`, `get_attribute()`, JavaScript Executor (`scrollIntoView()`)
* **Website:** Rahul Shetty Academy
* **Demo:** [🎥 Watch Recording](#)

---

## ⚙️ Prerequisites & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
   cd your-repo-name
