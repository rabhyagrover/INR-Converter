
# Currency Converter (INR Base)

A robust command-line utility built in Python to perform multi-currency conversions from **Indian Rupees (INR)**. This project demonstrates foundational programming concepts such as data validation, constant management, and formatted output, making it an ideal starter project for 1st-year engineering students.

---

## 📖 Project Overview
Financial applications require precision and error-free logic. This script serves as a manual "Rate Calculator" where a base currency (INR) is converted into five international currencies based on predefined market values. It replaces the need for manual calculation by automating the math through a clean terminal interface.



---

## ✨ Key Features

* **One-to-Many Conversion:

* Enter the INR amount once and receive values for **USD, EUR, JPY, RUB,** and **ZAR** simultaneously.

*Data Integrity:** Implements `try-except` blocks to ensure the program doesn't crash if a user enters text instead of numbers.

*Visual Precision:** Uses Python f-string alignment to create a neat, table-like output in the console.

*Boundary Checking:** Includes logic to reject negative values, ensuring financial accuracy.

---

## 🛠️ Technical Implementation
* **Arithmetic Logic:** Uses the formula $Converted\,Value = Input \times Exchange\,Rate$.
* **Constants:** Utilizes static variables to represent exchange rates, adhering to the PEP 8 naming convention (e.g., `USD_RATE`).
* **Exception Handling:** Uses `ValueError` to catch invalid inputs gracefully.
* **Clean Output:** Employs precision specifiers (`.2f`) to round currency to the nearest cent/paise.

---

## 🚀 How to Run

1.  **Install Python:** Ensure you have Python 3.x installed on your system.

2.  **Save the Script:** Save the provided code as `currency_converter.py`.

3. **Execute:** Open your terminal or command prompt and run:
    ```bash
    python currency_converter.py
    ```
4.  **Input:** Enter the amount in INR when prompted to see the live conversion results.

---

## 📈 Static Conversion Table

| Currency | Code | Rate (1 INR =) |
| :--- | :--- | :--- |
| **US Dollar** | USD | 0.012 |
| **Euro** | EUR | 0.011 |
| **Japanese Yen** | JPY | 1.82 |
| **Russian Ruble** | RUB | 1.10 |
| **S. African Rand** | ZAR | 0.22 |

---

## 🎓 Learning Objectives

This project covers the following B.Tech First-Year syllabus components:
1.  **Basic Syntax:** Variables, data types, and operators.
2.  **Control Flow:** Using `if-else` for input validation.
3.  **Modular Programming:** Wrapping logic inside functions for reusability.
4.  **Formatting:** Master the use of escape characters and string padding.
