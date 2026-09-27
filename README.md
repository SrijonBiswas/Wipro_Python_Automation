# 🧪 Automated Web Testing with Selenium

> **Group Project** | Institute of Engineering & Management (IEM), New Town  
> **Course:** Selenium Web Automation  
> **Language:** Python  
> **Framework:** Selenium WebDriver
> 
> **Group No:** 69

---

## 👥 Contributors

| **Student Name** | **University Roll** | **Enrollment ID** | **Stream** | **Section** |
|---|---:|---|---|:---:|
| **Sayan Sengupta** | 17 | `12023002001152` | CSE | B |
| **Srijon Biswas** | 64 | `12023002001176` | CSE | A |
| **Somes Sanyal** | 51 | `12023002029164` | CSE (IoT, CS, BT) | C |
| **Sourik Ghosh** | 32 | `12023002001384` | CSE | B |

---

## 🚀 Lab Assignments

### 🔹 Assignment 1: Using Selenium ID Locator

- **Summary:** Implemented Selenium's `By.ID` locator to identify and interact with input fields on the Test Automation Practice website. The program locates the Name, Email, Phone, and Address fields and enters sample data into each field.
- **Key Concepts:** `By.ID`, `find_element()`, `send_keys()`, browser automation
- **Website:** [Test Automation Practice](https://testautomationpractice.blogspot.com/)
- **Demo:** [🎥 Watch Recording](https://drive.google.com/file/d/15VMwi3EMhpZFzJKLZHZEH70S4q9pPTut/view?usp=sharing)

---

### 🔹 Assignment 2: Bulk Element Extraction

- **Summary:** Used Selenium's `find_elements()` method with `By.TAG_NAME` to locate all anchor (`<a>`) elements on the Rahul Shetty Academy website. The program iterates through the collected links and prints their visible text and corresponding URLs.
- **Key Concepts:** `find_elements()`, `By.TAG_NAME`, anchor elements, `get_attribute("href")`
- **Website:** [Rahul Shetty Academy](https://rahulshettyacademy.com/)
- **Demo:** [🎥 Watch Recording](https://drive.google.com/file/d/1AkIV_eKAFXS2BXAv7k0Sn7ikNgB2Dy6S/view?usp=sharing)

---

### 🔹 Assignment 3: CSS Attribute Selectors

- **Summary:** Demonstrated CSS attribute selectors for locating web elements using partial attribute values. The assignment implements the three CSS substring matching operators: `^=` for starts-with, `$=` for ends-with, and `*=` for contains.
- **Key Concepts:** CSS Selectors, `By.CSS_SELECTOR`, `^=`, `$=`, `*=`
- **Website:** [Test Automation Practice](https://testautomationpractice.blogspot.com/)
- **Demo:** [🎥 Watch Recording](https://drive.google.com/file/d/1eDB8IqkvsgKBJbeq4n6yk8ZQvOC4YsG2/view?usp=sharing)

#### CSS Selectors Demonstrated

| **Selector** | **Meaning** | **Example** |
|---|---|---|
| `^=` | Starts With | `input[placeholder^='Enter N']` |
| `$=` | Ends With | `input[placeholder$='EMail']` |
| `*=` | Contains | `input[placeholder*='Phone']` |

---

### 🔹 Assignment 4: DOM Traversal via CSS Child Selectors

- **Summary:** Used the CSS child selector `div > a` to locate a nested anchor element on the Rahul Shetty Academy website. The program retrieves the element's tag name, text, and URL, scrolls the element into view, and clicks it using JavaScript.
- **Key Concepts:** CSS Child Selector, `div > a`, `By.CSS_SELECTOR`, `get_attribute()`, JavaScript Executor, `scrollIntoView()`
- **Website:** [Rahul Shetty Academy](https://rahulshettyacademy.com/)
- **Demo:** [🎥 Watch Recording](https://drive.google.com/file/d/1bERE8LmqelO2CVzRgQjiWHa1Zoo_XqfI/view?usp=sharing)

---

## 🛠️ Technologies Used

- 🐍 Python
- 🌐 Selenium WebDriver
- 🧪 Automated Web Testing
- 🔎 CSS Selectors
- 🎯 Selenium Locators
- 📜 JavaScript Executor
- 🌍 Google Chrome
- 🌐 Microsoft Edge

---

## 📂 Project Structure

```text
selenium/
│
├── Assignment1.py
├── Assignment2.py
├── assignment3.py
├── assignment4.py
│
└── README.md
