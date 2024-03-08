import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import matplotlib.pyplot as plt

def calculate_budget():
    # Calculate budget based on user input (you can modify this as needed)
    total_income = float(income_entry.get())
    total_expenses = float(expenses_entry.get())

    remaining_income = total_income - total_expenses
    remaining_label.config(text=f"Remaining Income: ${remaining_income:.2f}")

    # Pie chart for budget breakdown
    labels = ['Income', 'Expenses']
    sizes = [total_income, total_expenses]
    colors = ['#ff9999','#66b3ff']
    explode = (0.1, 0)  # explode 1st slice
    plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.title('Budget Breakdown')
    plt.show()

# Create main window
root = tk.Tk()
root.title("Budget Calculator")

# Income Input
income_label = ttk.Label(root, text="Total Income:")
income_label.grid(row=0, column=0, padx=5, pady=5)
income_entry = ttk.Entry(root)
income_entry.grid(row=0, column=1, padx=5, pady=5)

# Expenses Input
expenses_label = ttk.Label(root, text="Total Expenses:")
expenses_label.grid(row=1, column=0, padx=5, pady=5)
expenses_entry = ttk.Entry(root)
expenses_entry.grid(row=1, column=1, padx=5, pady=5)

# Calculate Button
calculate_button = ttk.Button(root, text="Calculate", command=calculate_budget)
calculate_button.grid(row=2, columnspan=2, padx=5, pady=5)

# Remaining Income Label
remaining_label = ttk.Label(root, text="")
remaining_label.grid(row=3, columnspan=2, padx=5, pady=5)

root.mainloop()
