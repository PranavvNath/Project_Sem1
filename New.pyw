import json
import os
import tkinter as tk
from tkinter import messagebox

FILENAME = "expenses.json"

def load_expenses():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as f:
            return json.load(f)
    return []

def save_expenses(expenses):
    with open(FILENAME, "w") as f:
        json.dump(expenses, f, indent=4)

class ExpenseTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Personal Expense Tracker")
        self.root.geometry("420x480")
        self.root.config(bg="#f4f4f9")
        
        self.expenses = load_expenses()

        # Title Header
        title_label = tk.Label(root, text="Expense Tracker", font=("Arial", 16, "bold"), bg="#f4f4f9", fg="#333")
        title_label.pack(pady=15)

        # Input Frame
        input_frame = tk.Frame(root, bg="#f4f4f9")
        input_frame.pack(pady=5)

        tk.Label(input_frame, text="Category:", bg="#f4f4f9", font=("Arial", 11)).grid(row=0, column=0, sticky="w", padx=8, pady=8)
        self.category_entry = tk.Entry(input_frame, font=("Arial", 11), width=18)
        self.category_entry.grid(row=0, column=1, padx=8, pady=8)

        tk.Label(input_frame, text="Amount ($):", bg="#f4f4f9", font=("Arial", 11)).grid(row=1, column=0, sticky="w", padx=8, pady=8)
        self.amount_entry = tk.Entry(input_frame, font=("Arial", 11), width=18)
        self.amount_entry.grid(row=1, column=1, padx=8, pady=8)

        # Add Button with Styling
        add_btn = tk.Button(root, text="Add Expense", command=self.add_expense, bg="#4CAF50", fg="white", font=("Arial", 11, "bold"), width=16, relief="raised")
        add_btn.pack(pady=10)

        # Display Area (Text box acting like a list view)
        self.text_area = tk.Text(root, height=10, width=42, font=("Courier", 10), bg="#ffffff", fg="#333")
        self.text_area.pack(pady=10)

        # Total Label
        self.total_label = tk.Label(root, text="Total Spent: $0.00", font=("Arial", 12, "bold"), bg="#f4f4f9", fg="#222")
        self.total_label.pack(pady=10)

        self.update_display()

    def add_expense(self):
        category = self.category_entry.get().strip()
        amount_str = self.amount_entry.get().strip()

        if not category or not amount_str:
            messagebox.showerror("Error", "Please fill in all fields!")
            return

        try:
            amount = float(amount_str)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number for the amount!")
            return

        self.expenses.append({"category": category, "amount": amount})
        save_expenses(self.expenses)
        
        # Clear inputs
        self.category_entry.delete(0, tk.END)
        self.amount_entry.delete(0, tk.END)
        
        self.update_display()
        messagebox.showinfo("Success", "Expense added successfully!")

    def update_display(self):
        self.text_area.delete("1.0", tk.END)
        total = 0.0
        for item in self.expenses:
            self.text_area.insert(tk.END, f"{item['category']:<22} ${item['amount']:.2f}\n")
            total += item["amount"]
        self.total_label.config(text=f"Total Spent: ${total:.2f}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ExpenseTrackerApp(root)
    root.mainloop()