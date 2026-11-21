
# 🏦 ATM Bank Simulator | Python Project

A command-line **ATM Banking Simulator** developed using Python. This project demonstrates basic banking operations, conditional statements, user input validation, and file handling.

The application allows users to check account balances, deposit money, withdraw cash, view transaction history, and access account details.

---

## ✨ Features

### 1. 💰 Check Account Balance
- Displays account holder information.
- Shows account number.
- Displays the available balance.
- Uses formatted currency output.

### 2. 💵 Deposit Money
- Accepts deposit amounts from users.
- Updates the balance during program execution.
- Saves deposit transactions in `transactions.txt`.
- Displays previous and updated balances.

### 3. 🏧 Withdraw Money
- Accepts withdrawal amounts.
- Validates numeric input.
- Prevents withdrawals exceeding the available balance.
- Prevents zero or negative withdrawals.
- Records successful transactions.

### 4. 📜 Transaction History
- Reads transaction records from a text file.
- Displays deposit and withdrawal details.
- Shows the balance after transactions.
- Displays the total number of recorded transactions.

### 5. 👤 Account Details
- Reads account information from `accounts.txt`.
- Displays the current account balance.
- Shows account status.

### 6. 🚪 Exit
- Displays a goodbye message.
- Informs the user that transaction history is saved.

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python 3 | Core programming language |
| Functions | Organizing program functionality |
| Conditional Statements | Handling ATM menu options |
| User Input | Collecting customer information |
| File Handling | Reading and writing transaction records |
| String Formatting | Displaying formatted currency |

**Dependencies:** No external Python libraries required.

---

## 📂 Project Structure

```text
ATM-Bank-Simulator/
│
├── main.py
├── accounts.txt
├── transactions.txt
└── README.md
```

| File | Description |
|---|---|
| `main.py` | Main ATM banking application |
| `accounts.txt` | Stores account information |
| `transactions.txt` | Stores transaction history |
| `README.md` | Project documentation |

---

## 🚀 Installation & Setup

### Step 1: Install Python

Download Python 3:

https://www.python.org/downloads/

Verify installation:

```bash
python --version
```

### Step 2: Clone Repository

```bash
git clone https://github.com/DevDass-py/ATM-Bank-Simulator.git
```

### Step 3: Open Project Folder

```bash
cd ATM-Bank-Simulator
```

### Step 4: Prepare Required Files

Create two text files in the project directory:

- `accounts.txt` — Add the account information you want displayed.
- `transactions.txt` — Create an empty file for transaction records.

### Step 5: Run the Application

```bash
python main.py
```

---

## 🖥️ Application Menu

```text
================================================
ATM BANKING SIMULATOR
================================================

WELCOME TO PYTHON BANK

================================================

1. Check Account Balance
2. Deposit Money
3. Withdraw Money
4. Transaction History
5. Account Details
6. Exit

Enter your choice:
```

Select an option from 1 to 6 to perform the corresponding operation.

---

## 📚 Concepts Practiced

Through this project, I practised:

- Python functions.
- Variables and data types.
- Conditional statements (`if`, `elif`, `else`).
- Taking user input.
- Type conversion.
- Input validation.
- Arithmetic operations.
- File handling (`open()`, read mode, append mode).
- `with` statements.
- String methods such as `.strip()` and `.isdigit()`.
- Formatted strings (f-strings).

---

## 🔮 Future Improvements

Planned enhancements:

- [ ] Add a repeating ATM menu.
- [ ] Implement PIN authentication.
- [ ] Support multiple bank accounts.
- [ ] Save account balances permanently.
- [ ] Add transaction date and time.
- [ ] Improve error handling.
- [ ] Prevent zero-value deposits.
- [ ] Integrate SQLite or MySQL database.
- [ ] Develop a graphical user interface.

---

## ⚠️ Project Limitations

This is an educational project and is not intended for real banking operations.

- The account balance resets to its initial value when the program restarts.
- The ATM menu currently performs one operation per execution.
- Account and transaction files must be created before accessing their respective features.
- Account information is not protected by authentication.
- The application does not connect to a real banking system.

**Security notice:** Do not enter real banking credentials or sensitive financial information.

---

## 👨‍💻 Author

**Dev Dass**

🐍 Python Programmer | Aspiring AI/ML Engineer

- GitHub: [@DevDass-py](https://github.com/DevDass-py)
- Project: [ATM Bank Simulator](https://github.com/DevDass-py/ATM-Bank-Simulator)

---

## ⭐ Support

If you find this project useful, consider giving the repository a star ⭐.

---

**Built with Python 🐍 by Dev Dass**
