import tkinter as tk
from tkinter import *


def calculate():
    try:
        # Считываем данные из текстовых полей
        ves = float(textfromves.get("1.0", END).strip())
        povtoreniya = float(textfromcolvo.get("1.0", END).strip())

        # Твоя формула: вес * (повторения / 30 + 1)
        result = ves * (povtoreniya / 30 + 1)

        # Выводим результат
        textfromresult.delete("1.0", END)
        textfromresult.insert("1.0", f"{round(result, 2)}")
    except ValueError:
        textfromresult.delete("1.0", END)
        textfromresult.insert("1.0", "Введите числа")


window = tk.Tk()
window.title("расчетчик силовых")
window.geometry("640x1350")

# Вес
lable = tk.Label(window, text="ves", fg="red", bg="gray")
lable.grid(row=0, column=0)
lable_enter_ves = Label(window, text="введите вес", fg="red")
lable_enter_ves.grid(row=1, column=0)
textfromves = Text(window, height=1, width=20)
textfromves.grid(row=2, column=0)

# Повторения
lable_enter_colvo = tk.Label(window, text="введите повторения")
lable_enter_colvo.grid(row=3, column=0)
textfromcolvo = Text(window, height=1, width=20)
textfromcolvo.grid(row=4, column=0)

# Кнопка (привязываем функцию calculate)
button = Button(text='расчитать', command=calculate)
button.grid(row=5, column=0)

# Результат
lable_result = Label(window, text="ваш максимум на 1")
lable_result.grid(row=6, column=0)
textfromresult = Text(window, height=1, width=20)
textfromresult.grid(row=7, column=0)

window.mainloop()
