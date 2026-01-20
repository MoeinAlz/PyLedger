# PyLedger

A straightforward expense tracker that keeps you honest about your spending.

## Why I Made This

I kept wondering where my money went each month. Sound familiar? So I built something simple - set a budget, log what you spend, get a warning when you're close to going over. Nothing fancy, but it works.

## Getting Started

### Install Python

**Windows:**
1. Download from [python.org](https://www.python.org/downloads/)
2. Check "Add Python to PATH" during setup
3. Install

**Mac/Linux:**
```bash
python3 --version
```

### VS Code Extensions (If You Use It)

- **Python** by Microsoft
- **Pylance** by Microsoft

## How to Run

**VS Code:**
1. Open the folder with `pyledger.py`
2. Click the play button
3. Follow the prompts

**Terminal:**
```bash
python pyledger.py
# or
python3 pyledger.py
```

## What You Can Do

```
========================================
MENU:
  1. Add Expense
  2. View Expenses
  3. Show Summary
  4. Set/Change Budget
  5. Exit
========================================
```

## Quick Example

```
PyLedger
Track your expenses wisely!

Welcome! Let's set your budget first.

SET BUDGET
Enter your budget amount: $500
Budget set to $500.00

ADD EXPENSE
Enter date (or press Enter for today): 
Categories: Food, Transport, Entertainment, Shopping, Bills, Other
Enter category: Food
Enter amount: $45.50

Expense added: Food - $45.50

You have $454.50 remaining in your budget.
```

## The Warning System

This is the part that keeps you in check:

| Status | What It Means |
|--------|---------------|
| Safe | You're good, money left in the budget |
| Caution | You've used 90%+ of your budget |
| Over Budget | Time to stop spending |

## Where's My Data?

Everything saves to two files in the same folder:
- `expenses.csv` - All your expenses
- `budget.txt` - Your budget amount

Want to start fresh? Just delete these files.

## Troubleshooting

**"Python not recognized"**
Reinstall Python and check "Add to PATH"

**Data not saving?**
Make sure you have permission to write files in that folder

**Want to reset everything?**
Delete `expenses.csv` and `budget.txt`, then run the app again

## What's Under the Hood

If you're curious about the code:
- Uses Python's `csv` module for storing expenses
- `datetime` for handling dates
- Simple file I/O for the budget
- Basic input validation so it doesn't crash on weird inputs

---

Keep track of your money. Future you will thank you.