import tkinter as tk
from tkinter import ttk, messagebox

# Static conversion rates (example values)
conversion_rates = {
    'USD': {'INR': 83.2, 'EUR': 0.93, 'GBP': 0.79, 'USD': 1},
    'INR': {'USD': 0.012, 'EUR': 0.011, 'GBP': 0.0095, 'INR': 1},
    'EUR': {'USD': 1.07, 'INR': 89.0, 'GBP': 0.85, 'EUR': 1},
    'GBP': {'USD': 1.26, 'INR': 104.5, 'EUR': 1.17, 'GBP': 1}
}

currencies = list(conversion_rates.keys())

def convert_currency():
    try:
        amount = int(entry_amount.get())
        from_curr = combo_from.get()
        to_curr = combo_to.get()
        rate = conversion_rates[from_curr][to_curr]
        result = amount * rate
        label_result.config(text=f"{amount:.2f} {from_curr} = {result:.2f} {to_curr}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")
    except KeyError:
        messagebox.showerror("Conversion Error", "Conversion rate not available.")

# Tkinter window setup
root = tk.Tk()
root.title("Currency Converter")
root.geometry("400x300")
root.config(padx=20, pady=20)

tk.Label(root, text="Amount:").pack(pady=5)
entry_amount = tk.Entry(root, width=20)
entry_amount.pack()

tk.Label(root, text="From Currency:").pack(pady=5)
combo_from = ttk.Combobox(root, values=currencies, state="readonly")
combo_from.current(0)
combo_from.pack()

tk.Label(root, text="To Currency:").pack(pady=5)
combo_to = ttk.Combobox(root, values=currencies, state="readonly")
combo_to.current(1)
combo_to.pack()

tk.Button(root, text="Convert", command=convert_currency).pack(pady=10)

label_result = tk.Label(root, text="Result will be shown here", font=("Arial", 12, "bold"))
label_result.pack(pady=10)

root.mainloop()
