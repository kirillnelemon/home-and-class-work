
from  tkinter import  *
from tkinter.ttk import Combobox
# def clicked():
#     res = f"привет, {txt.get()}"
#     lbl.configure(text=res)
#
# window = Tk()#создание окна
# window.title("добро пожаловать в мое приложение!")#титульник
# window.geometry('400x250')#задаем разрешение
# lbl = Label(window, text='Введи имя:', font=('Arial Bold', 50))#cоздание строки
# lbl.grid(column=0, row=0)#цвета строки
# btn = Button(window, text="клик", bg='black',fg='red',command= clicked)#создание кнопки и функция
# btn.grid(column= 1, row=0)
# txt = Entry(window, width=10)
# txt.grid(column = 1, row=5)
# combo = Combobox(window)
# combo['values'] = (1,2,3,4,5,6,7,8,9)
# combo.current(1)
# combo.grid(column=1,row=10)
# chk_state = BooleanVar()
# chk_state.set(True)
# chk = Checkbutton(window, text='Выбрать',var=chk_state)
# chk.grid(column=0,row=3)
#
#
# window.mainloop()#бесконечный цикл
def clicked():
    res = "lable"
    lbl.configure(text=res)

window = Tk()
window.title("tic_tac_toe")
window.geometry('1080x720')
lbl = Label(window, text='ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤпривет!', font=('Arial Bold', 20))
lbl.grid(column=1, row=1)
btn = Button(text='ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤPlayㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ', bg='Black', fg='white', font=('Arial bold', 20),command= clicked)
btn.grid(column= 1, row=3)
btn = [Button(), Button(1),Button(2),Button(3),Button(4),Button(5),Button(6),Button(7),Button(8),Button(9)]

window.mainloop()