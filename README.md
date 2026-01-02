# 💸 Expense Tracker (Python)

A **menu-driven Expense Tracker application** built using **Python functions**.  
This project helps users **add expenses**, **view expense history**, and **calculate total spending**, while following **clean and modular coding practices**.

---

## ✨ Features

- ➕ Add a new expense (date, category, description, amount)
- 📋 View all expenses with numbering
- 🧮 View total amount spent
- 🔁 Continuous menu until user exits
- 🧩 Code organized using functions
- 📦 Uses a list of dictionaries for data storage

---

## 🧠 Concepts Used

- 🧾 Variables  
- 📚 Lists & Dictionaries  
- 🧠 User-defined Functions  
- 🔄 While Loop  
- 🔀 Conditional Statements (`if-elif-else`)  
- ⌨️ User Input Handling  
- 🧵 f-Strings for formatted output  

---

## ⚙️ How the Program Works

1. 📌 The program starts by displaying a **menu with 4 options**:
   - ➕ Add a New Expense  
   - 📋 View All Expenses  
   - 🧮 View Total Spending  
   - ❌ Exit  

2. 🧑‍💻 The user selects an option by entering a number **(1–4)**.

3. 🗂️ Each expense is stored as a **dictionary** with the following keys:
   - `date`
   - `category`
   - `description`
   - `amount`

4. 📚 All expense dictionaries are stored inside a **global list** called `expensesList`.

5. 🧩 Each menu operation is handled by a **separate function**:
   - `show_menu()` → Displays the menu  
   - `add_expense()` → Adds a new expense  
   - `view_expenses()` → Displays all expenses  
   - `view_total()` → Calculates total spending  
   - `main()` → Controls overall program flow  

6. 🔁 The program runs continuously until the user selects **Exit**.

---

## 📂 Project Structure

```text
Expense-tracker/
├── ExpenseTracker.py
└── README.md




