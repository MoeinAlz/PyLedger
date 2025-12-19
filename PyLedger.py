"""
📊 PyLedger
A simple expense tracker that warns you if you overspend.
"""

import csv
import os
from datetime import datetime

EXPENSES_FILE = "expenses.csv"
BUDGET_FILE = "budget.txt"


def load_budget():
    """Load budget from file."""
    if os.path.exists(BUDGET_FILE):
        with open(BUDGET_FILE, 'r') as file:
            return float(file.read().strip())
    return None


def save_budget(amount):
    """Save budget to file."""
    with open(BUDGET_FILE, 'w') as file:
        file.write(str(amount))


def load_expenses():
    """Load expenses from CSV file."""
    expenses = []
    if os.path.exists(EXPENSES_FILE):
        with open(EXPENSES_FILE, 'r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                row['amount'] = float(row['amount'])
                expenses.append(row)
    return expenses


def save_expense(date, category, amount):
    """Save a new expense to CSV file."""
    file_exists = os.path.exists(EXPENSES_FILE)
    
    with open(EXPENSES_FILE, 'a', newline='') as file:
        fieldnames = ['date', 'category', 'amount']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        
        if not file_exists:
            writer.writeheader()
        
        writer.writerow({
            'date': date,
            'category': category,
            'amount': amount
        })


def get_total_spending(expenses):
    """Calculate total spending."""
    return sum(expense['amount'] for expense in expenses)


def check_budget_warning(budget, total):
    """Check if over budget and show warning."""
    if total > budget:
        over_by = total - budget
        print("\n" + "⚠️" * 20)
        print(f"🚨 WARNING: You are OVER BUDGET by ${over_by:.2f}!")
        print("⚠️" * 20)
    elif total >= budget * 0.9:
        remaining = budget - total
        print(f"\n⚠️  Caution: Only ${remaining:.2f} left in your budget!")
    else:
        remaining = budget - total
        print(f"\n✅ You have ${remaining:.2f} remaining in your budget.")


def set_budget():
    """Set or update the budget."""
    print("\n" + "-" * 40)
    print("💰 SET BUDGET")
    print("-" * 40)
    
    current_budget = load_budget()
    if current_budget:
        print(f"Current budget: ${current_budget:.2f}")
    
    try:
        amount = float(input("Enter your budget amount: $"))
        if amount <= 0:
            print("❌ Budget must be greater than 0!")
            return
        save_budget(amount)
        print(f"✅ Budget set to ${amount:.2f}")
    except ValueError:
        print("❌ Please enter a valid number!")


def add_expense():
    """Add a new expense."""
    print("\n" + "-" * 40)
    print("➕ ADD EXPENSE")
    print("-" * 40)
    
    # Date
    date_input = input("Enter date (YYYY-MM-DD) or press Enter for today: ").strip()
    if date_input == "":
        date = datetime.now().strftime("%Y-%m-%d")
    else:
        try:
            datetime.strptime(date_input, "%Y-%m-%d")
            date = date_input
        except ValueError:
            print("❌ Invalid date format! Using today's date.")
            date = datetime.now().strftime("%Y-%m-%d")
    
    # Category
    print("\nCategories: Food, Transport, Entertainment, Shopping, Bills, Other")
    category = input("Enter category: ").strip().capitalize()
    if category == "":
        category = "Other"
    
    # Amount
    try:
        amount = float(input("Enter amount: $"))
        if amount <= 0:
            print("❌ Amount must be greater than 0!")
            return
    except ValueError:
        print("❌ Please enter a valid number!")
        return
    
    save_expense(date, category, amount)
    print(f"\n✅ Expense added: {category} - ${amount:.2f} on {date}")
    
    # Check budget after adding
    budget = load_budget()
    if budget:
        expenses = load_expenses()
        total = get_total_spending(expenses)
        check_budget_warning(budget, total)


def view_expenses():
    """View all expenses."""
    print("\n" + "-" * 40)
    print("📋 ALL EXPENSES")
    print("-" * 40)
    
    expenses = load_expenses()
    
    if not expenses:
        print("No expenses recorded yet.")
        return
    
    print(f"{'Date':<12} {'Category':<15} {'Amount':>10}")
    print("-" * 40)
    
    for expense in expenses:
        print(f"{expense['date']:<12} {expense['category']:<15} ${expense['amount']:>8.2f}")
    
    print("-" * 40)
    total = get_total_spending(expenses)
    print(f"{'TOTAL':<12} {'':<15} ${total:>8.2f}")


def show_summary():
    """Show spending summary."""
    print("\n" + "-" * 40)
    print("📊 SPENDING SUMMARY")
    print("-" * 40)
    
    budget = load_budget()
    expenses = load_expenses()
    total = get_total_spending(expenses)
    
    if budget:
        print(f"Budget:     ${budget:.2f}")
    else:
        print("Budget:     Not set")
    
    print(f"Total Spent: ${total:.2f}")
    
    if budget:
        remaining = budget - total
        percentage = (total / budget) * 100
        print(f"Remaining:   ${remaining:.2f}")
        print(f"Used:        {percentage:.1f}%")
        check_budget_warning(budget, total)
    
    # Show spending by category
    if expenses:
        print("\n📁 By Category:")
        categories = {}
        for expense in expenses:
            cat = expense['category']
            categories[cat] = categories.get(cat, 0) + expense['amount']
        
        for cat, amount in sorted(categories.items(), key=lambda x: x[1], reverse=True):
            print(f"   {cat:<15} ${amount:.2f}")


def main():
    """Main function."""
    print("\n" + "=" * 40)
    print("   📊 PyLedger")
    print("   Track your expenses wisely!")
    print("=" * 40)
    
    # Check if budget is set
    budget = load_budget()
    if not budget:
        print("\n👋 Welcome! Let's set your budget first.")
        set_budget()
    
    while True:
        print("\n" + "=" * 40)
        print("MENU:")
        print("  1. ➕ Add Expense")
        print("  2. 📋 View Expenses")
        print("  3. 📊 Show Summary")
        print("  4. 💰 Set/Change Budget")
        print("  5. 🚪 Exit")
        print("=" * 40)
        
        choice = input("Choose an option (1-5): ").strip()
        
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            show_summary()
        elif choice == "4":
            set_budget()
        elif choice == "5":
            print("\n👋 Goodbye! Keep tracking your expenses!")
            break
        else:
            print("❌ Invalid choice. Please enter 1-5.")


if __name__ == "__main__":
    main()