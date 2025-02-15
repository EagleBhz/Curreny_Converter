import requests
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def get_exchange_rates():
    url = "https://api.exchangerate-api.com/v4/latest/USD"  # Güncel kur verilerini almak için API
    response = requests.get(url)
    data = response.json()
    return data["rates"]

def convert_currency():
    try:
        amount = float(entry_amount.get())
        from_currency = currency_mapping[combo_from.get()]
        to_currency = currency_mapping[combo_to.get()]
        rates = get_exchange_rates()
        if from_currency != "USD":
            amount = amount / rates[from_currency]
        converted_amount = amount * rates[to_currency]
        label_result.config(text=f"{converted_amount:.2f} {to_currency}", fg="#28A745")
    except ValueError:
        messagebox.showerror("Hata", "Lütfen geçerli bir sayı girin.")

currency_mapping = {
    "Turkish Lira": "TRY",
    "United States Dollar": "USD",
    "Pound Sterling": "GBP",
    "Euro": "EUR",
    "Azerbaijani Manat": "AZN",
    "Japanese Yen": "JPY",
    "Australian Dollar": "AUD",
    "Canadian Dollar": "CAD",
    "Swiss Franc": "CHF",
    "South Korean Won": "KRW",
    "Indian Rupee": "INR",
    "Russian Ruble": "RUB"
}

currencies = list(currency_mapping.keys())

root = tk.Tk()
root.title("Döviz Çevirici")
root.geometry("500x400")
root.config(bg="#2C3E50")

frame = tk.Frame(root, bg="#ECF0F1", padx=20, pady=20, relief="ridge", bd=5)
frame.pack(pady=20)

tk.Label(frame, text="Döviz Çevirici", font=("Arial", 18, "bold"), bg="#ECF0F1", fg="#2C3E50").pack(pady=10)

tk.Label(frame, text="Miktar:", font=("Arial", 12), bg="#ECF0F1").pack(pady=5)
entry_amount = tk.Entry(frame, font=("Arial", 12), width=20, relief="solid", bd=2)
entry_amount.pack(pady=5)

combo_from = ttk.Combobox(frame, values=currencies, font=("Arial", 12), state="readonly")
combo_from.pack(pady=5)
combo_from.set("United States Dollar")

tk.Label(frame, text="➡", font=("Arial", 14, "bold"), bg="#ECF0F1").pack()

combo_to = ttk.Combobox(frame, values=currencies, font=("Arial", 12), state="readonly")
combo_to.pack(pady=5)
combo_to.set("Turkish Lira")

convert_button = tk.Button(frame, text="Çevir", font=("Arial", 12, "bold"), bg="#3498DB", fg="white", padx=10, pady=5, relief="raised", command=convert_currency)
convert_button.pack(pady=10)

label_result = tk.Label(frame, text="", font=("Arial", 14, "bold"), bg="#ECF0F1", fg="#C0392B")
label_result.pack(pady=5)

root.mainloop()
