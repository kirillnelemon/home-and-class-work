import tkinter as tk
from tkinter import messagebox

ENG_UPPER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ENG_LOWER = ENG_UPPER.lower()
RUS_UPPER = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
RUS_LOWER = RUS_UPPER.lower()

ALPHABETS = [ENG_UPPER, ENG_LOWER, RUS_UPPER, RUS_LOWER]


def char_info(ch):
    for alpha in ALPHABETS:
        if ch in alpha:
            return alpha, alpha.index(ch)
    return None, -1


def vigenere(text, key, decrypt=False):
    shifts = []
    for k in key:
        alpha, idx = char_info(k)
        if alpha:
            shifts.append(idx)
    if not shifts:
        return text

    res = []
    j = 0
    for ch in text:
        alpha, idx = char_info(ch)
        if alpha:
            shift = shifts[j % len(shifts)]
            if decrypt:
                shift = -shift
            res.append(alpha[(idx + shift) % len(alpha)])
            j += 1
        else:
            res.append(ch)
    return "".join(res)


def process(decrypt=False):
    text = text_input.get("1.0", tk.END).strip()
    key = key_input.get().strip()
    if not key:
        messagebox.showwarning("Внимание", "Пожалуйста, введите ключ!")
        return
    result = vigenere(text, key, decrypt=decrypt)
    text_output.delete("1.0", tk.END)
    text_output.insert(tk.END, result)


root = tk.Tk()
root.title("Шифр Виженера")
root.geometry("500x500")
root.resizable(False, False)

tk.Label(root, text="Исходный текст:").pack(pady=(10, 0), anchor="w", padx=20)
text_input = tk.Text(root, height=8, width=55)
text_input.pack(pady=5, padx=20)

tk.Label(root, text="Ключ:").pack(pady=(10, 0), anchor="w", padx=20)
key_input = tk.Entry(root, width=55)
key_input.pack(pady=5, padx=20)

btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Зашифровать",
          width=15, command=lambda: process(False)).grid(row=0, column=0, padx=10)
tk.Button(btn_frame, text="Расшифровать",
          width=15, command=lambda: process(True)).grid(row=0, column=1, padx=10)

tk.Label(root, text="Результат:").pack(pady=(10, 0), anchor="w", padx=20)
text_output = tk.Text(root, height=8, width=55)
text_output.pack(pady=5, padx=20)

root.mainloop()