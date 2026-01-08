import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from tkcalendar import DateEntry
from datetime import datetime

# ---------------- DATABASE ----------------
conn = sqlite3.connect("expense_tracker.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    t_type TEXT,
    category TEXT,
    amount REAL,
    date TEXT,
    note TEXT
)
""")
conn.commit()

# ---------------- MAIN WINDOW ----------------
root = tk.Tk()
root.title("Expense Tracker")
root.geometry("900x550")
root.configure(bg="#1e1e1e")

# ---------------- STYLES ----------------
style = ttk.Style()
style.theme_use("clam")
style.configure("Treeview", background="#2b2b2b", foreground="white",
                rowheight=28, fieldbackground="#2b2b2b")
style.map("Treeview", background=[("selected", "#0078D7")])

# ---------------- VARIABLES ----------------
type_var = tk.StringVar(value="Expense")
cat_var = tk.StringVar()
amount_var = tk.StringVar()
note_var = tk.StringVar()

categories = ["Food", "Rent", "Travel", "Shopping", "Bills", "Salary", "Other"]

# ---------------- FUNCTIONS ----------------
def add_transaction():
    if not amount_var.get():
        messagebox.showerror("Error", "Amount required")
        return

    cur.execute(
        "INSERT INTO transactions VALUES (NULL,?,?,?,?,?)",
        (
            type_var.get(),
            cat_var.get(),
            float(amount_var.get()),
            date_entry.get_date().strftime("%Y-%m-%d"),
            note_var.get()
        )
    )
    conn.commit()
    clear_fields()
    load_data()

def clear_fields():
    amount_var.set("")
    note_var.set("")
    cat_var.set("")

def load_data(query="SELECT * FROM transactions"):
    for row in tree.get_children():
        tree.delete(row)

    cur.execute(query)
    for row in cur.fetchall():
        tree.insert("", tk.END, values=row)

    calculate_summary()

def calculate_summary():
    cur.execute("SELECT SUM(amount) FROM transactions WHERE t_type='Income'")
    income = cur.fetchone()[0] or 0

    cur.execute("SELECT SUM(amount) FROM transactions WHERE t_type='Expense'")
    expense = cur.fetchone()[0] or 0

    lbl_summary.config(
        text=f"Income: ₹{income:.2f}   Expense: ₹{expense:.2f}   Balance: ₹{income-expense:.2f}"
    )

def monthly_report():
    month = datetime.now().strftime("%Y-%m")
    load_data(f"SELECT * FROM transactions WHERE date LIKE '{month}%'")

def custom_report():
    start = from_date.get_date().strftime("%Y-%m-%d")
    end = to_date.get_date().strftime("%Y-%m-%d")
    load_data(
        f"SELECT * FROM transactions WHERE date BETWEEN '{start}' AND '{end}'"
    )

# ---------------- UI ----------------
frame_top = tk.Frame(root, bg="#1e1e1e")
frame_top.pack(fill="x", padx=10, pady=5)

ttk.Label(frame_top, text="Type").grid(row=0, column=0, padx=5)
ttk.Combobox(frame_top, textvariable=type_var,
             values=["Income", "Expense"], width=10).grid(row=0, column=1)

ttk.Label(frame_top, text="Category").grid(row=0, column=2)
ttk.Combobox(frame_top, textvariable=cat_var,
             values=categories, width=15).grid(row=0, column=3)

ttk.Label(frame_top, text="Amount").grid(row=0, column=4)
ttk.Entry(frame_top, textvariable=amount_var, width=12).grid(row=0, column=5)

ttk.Label(frame_top, text="Date").grid(row=0, column=6)
date_entry = DateEntry(frame_top, width=12)
date_entry.grid(row=0, column=7)

ttk.Entry(frame_top, textvariable=note_var, width=20).grid(row=0, column=8)
ttk.Button(frame_top, text="Add", command=add_transaction).grid(row=0, column=9, padx=5)

# ---------------- REPORT BUTTONS ----------------
frame_report = tk.Frame(root, bg="#1e1e1e")
frame_report.pack(fill="x", pady=5)

ttk.Button(frame_report, text="This Month", command=monthly_report).pack(side="left", padx=5)

from_date = DateEntry(frame_report)
from_date.pack(side="left")

to_date = DateEntry(frame_report)
to_date.pack(side="left", padx=5)

ttk.Button(frame_report, text="Custom Report", command=custom_report).pack(side="left")

# ---------------- TABLE ----------------
columns = ("ID", "Type", "Category", "Amount", "Date", "Note")
tree = ttk.Treeview(root, columns=columns, show="headings")

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, anchor="center")

tree.pack(expand=True, fill="both", padx=10, pady=10)

# ---------------- SUMMARY ----------------
lbl_summary = tk.Label(root, text="", font=("Segoe UI", 12),
                       bg="#1e1e1e", fg="white")
lbl_summary.pack(pady=5)

load_data()
root.mainloop()
