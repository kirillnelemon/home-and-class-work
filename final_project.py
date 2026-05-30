import tkinter as tk
from tkinter import ttk


def perform_conversion():
    try:
        # Получаем данные из полей ввода
        amount = float(amount_entry.get())
        from_curr = from_currency_combo.get()
        to_curr = to_currency_combo.get()

        # Зашитые фиксированные курсы валют (базовая единица — Рубль)
        # Настройки можно легко менять вручную прямо в коде
        rates = {
            "USD": 92.5,
            "EUR": 100.0,
            "KZT": 0.20,
            "RUB": 1.0
        }

        # Алгоритм конвертации через базовую валюту
        amount_in_rub = amount * rates[from_curr]
        converted_amount = amount_in_rub / rates[to_curr]

        # Выводим красивый результат
        result_label.config(text=f"{amount:.2f} {from_curr} = {converted_amount:.2f} {to_curr}")

    except ValueError:
        result_label.config(text="Ошибка: введите корректное число")


# Создание главного графического окна
root = tk.Tk()
root.title("Умный конвертер валют")
root.geometry("350x260")
root.resizable(False, False)

# Список наших четырех валют
currency_list = ("USD", "EUR", "RUB", "KZT")

# Поле ввода числовой суммы
amount_label = ttk.Label(root, text="Введите сумму:")
amount_label.pack(pady=5, padx=10)
amount_entry = ttk.Entry(root, width=25)
amount_entry.pack(pady=5)

# Элемент выбора исходной валюты
from_label = ttk.Label(root, text="Из какой валюты:")
from_label.pack(pady=5)
from_currency_combo = ttk.Combobox(root, values=currency_list, state="readonly", width=22)
from_currency_combo.current(0)  # По умолчанию USD
from_currency_combo.pack(pady=5)

# Элемент выбора целевой валюты
to_label = ttk.Label(root, text="В какую валюту:")
to_label.pack(pady=5)
to_currency_combo = ttk.Combobox(root, values=currency_list, state="readonly", width=22)
to_currency_combo.current(2)  # По умолчанию RUB
to_currency_combo.pack(pady=5)

# Интерактивная кнопка запуска расчета
convert_button = ttk.Button(root, text="Конвертировать", command=perform_conversion)
convert_button.pack(pady=15)

# Текстовое поле вывода результатов
result_label = ttk.Label(root, text="Результат отобразится здесь", font=("Arial", 11, "bold"))
result_label.pack(pady=5)

# Запуск программы
root.mainloop()


