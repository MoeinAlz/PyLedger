# 📊 PyLedger

A simple expense tracker that warns you if you overspend.

## 🎯 What Does PyLedger Do?

- **Set a budget** - Define how much you want to spend
- **Track expenses** - Add expenses with date, category, and amount
- **View expenses** - See all your spending in a table
- **Get warnings** - Alerts when you're close to or over budget
- **Auto-save** - All data saved to CSV file

## 🛠️ Prerequisites

### Install Python

**Windows:**
1. Download from [python.org](https://www.python.org/downloads/)
2. ✅ Check "Add Python to PATH" during installation
3. Click "Install Now"

**Mac/Linux:**
```bash
# Mac
brew install python3

# Linux
sudo apt install python3
```

### VS Code Extensions

| Extension | Publisher | Install Command |
|-----------|-----------|----------------|
| **Python** | Microsoft | `ms-python.python` |
| **Pylance** | Microsoft | `ms-python.vscode-pylance` |

## 🚀 How to Run

### Using VS Code:
1. Open folder containing `pyledger.py`
2. Click ▶️ Play button (top-right)
3. Follow the menu prompts

### Using Terminal:
```bash
python pyledger.py
# or
python3 pyledger.py
```

## 📖 How It Works

```
┌─────────────────────────────────────────┐
│  1. SET BUDGET                          │
│     Define your spending limit          │
├─────────────────────────────────────────┤
│  2. ADD EXPENSES                        │
│     Record date, category, amount       │
├─────────────────────────────────────────┤
│  3. VIEW & TRACK                        │
│     See all expenses and totals         │
├─────────────────────────────────────────┤
│  4. GET WARNINGS                        │
│     Alert if over or near budget        │
└─────────────────────────────────────────┘
```

## 📝 Example Usage

```
========================================
   📊 PyLedger
   Track your expenses wisely!
========================================

👋 Welcome! Let's set your budget first.

----------------------------------------
💰 SET BUDGET
----------------------------------------
Enter your budget amount: $500
✅ Budget set to $500.00

========================================
MENU:
  1. ➕ Add Expense
  2. 📋 View Expenses
  3. 📊 Show Summary
  4. 💰 Set/Change Budget
  5. 🚪 Exit
========================================
Choose an option (1-5): 1

----------------------------------------
➕ ADD EXPENSE
----------------------------------------
Enter date (YYYY-MM-DD) or press Enter for today: 
Categories: Food, Transport, Entertainment, Shopping, Bills, Other
Enter category: Food
Enter amount: $45.50

✅ Expense added: Food - $45.50 on 2025-08-01

✅ You have $454.50 remaining in your budget.
```

## 📁 Files Created

| File | Purpose |
|------|--------|
| `expenses.csv` | Stores all your expenses |
| `budget.txt` | Stores your budget amount |

## ⚠️ Budget Warnings

| Status | Message |
|--------|--------|
| ✅ Safe | "You have $X remaining" |
| ⚠️ Caution | "Only $X left" (when 90%+ used) |
| 🚨 Over | "You are OVER BUDGET by $X!" |

## 🔧 Troubleshooting

**"Python not recognized"**
→ Reinstall Python with "Add to PATH" checked

**Data not saving**
→ Make sure you have write permission in the folder

**Want to reset data?**
→ Delete `expenses.csv` and `budget.txt` files

## 📚 Python Concepts Used

| Concept | Usage |
|---------|-------|
| `csv` module | Read/write expense data |
| `os` module | Check if files exist |
| `datetime` | Handle dates |
| Functions | Organize code |
| Dictionaries | Store expense data |
| Loops | Menu system |

---

**The future belongs to those who believe in the beauty of their dreams. Go get them! 😎🔥🔥**