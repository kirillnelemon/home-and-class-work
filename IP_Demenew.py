# Импортируем базовую библиотеку для создания графического интерфейса
import tkinter as tk
# Импортируем модуль всплывающих окон для уведомлений
from tkinter import messagebox
# Импортируем библиотеку для воспроизведения системных звуков Windows
import winsound


# Объявляем главный класс нашего приложения
class SmartDownApp:

    # Конструктор класса, инициализирующий главное окно
    def __init__(self, root):
        # Сохраняем ссылку на главное окно в переменную класса
        self.root = root
        # Устанавливаем заголовок окна приложения
        self.root.title("SmartDown — Таймер")
        # Задаем фиксированные размеры окна (ширина x высота)
        self.root.geometry("400x350")
        # Запрещаем пользователю изменять размеры окна
        self.root.resizable(False, False)
        # Окрашиваем фон главного окна в темно-синий цвет
        self.root.configure(bg="#2c3e50")

        # Инициализируем счетчик оставшегося времени в секундах
        self.total_seconds = 0
        # Флаг текущего состояния таймера (активен или на паузе)
        self.is_running = False
        # Переменная для хранения ID процесса метода after()
        self.timer_id = None

        # Вызываем метод для отрисовки всех элементов интерфейса
        self.create_widgets()

    # Метод для создания и размещения виджетов на экране
    def create_widgets(self):
        # Создаем текстовую метку для главного названия
        title_label = tk.Label(
            self.root,
            text="SmartDown",
            font=("Helvetica", 24, "bold"),
            fg="#ecf0f1",
            bg="#2c3e50"
        )
        # Выводим заголовок на экран с отступом сверху
        title_label.pack(pady=15)

        # Создаем невидимый контейнер для полей ввода
        input_frame = tk.Frame(self.root, bg="#2c3e50")
        # Выводим контейнер на экран с отступами
        input_frame.pack(pady=10)

        # Создаем словарь с общими настройками для подписей полей
        label_attr = {
            "font": ("Helvetica", 10),
            "fg": "#bdc3c7",
            "bg": "#2c3e50"
        }
        # Создаем словарь с общими настройками для окон ввода
        entry_attr = {
            "font": ("Helvetica", 18),
            "width": 3,
            "justify": "center",
            "bd": 2
        }

        # Создаем подпись "Чч" (Часы)
        tk.Label(input_frame, text="Чч", **label_attr).grid(row=0, column=0, padx=5)
        # Создаем поле ввода для часов
        self.hours_entry = tk.Entry(input_frame, **entry_attr)
        # Устанавливаем в поле часов значение по умолчанию "00"
        self.hours_entry.insert(0, "00")
        # Размещаем поле ввода в сетке (строка 1, колонка 0)
        self.hours_entry.grid(row=1, column=0, padx=5)

        # Создаем текстовый разделитель в виде двоеточия
        tk.Label(input_frame, text=":", font=("Helvetica", 18), fg="#ecf0f1", bg="#2c3e50").grid(row=1, column=1)

        # Создаем подпись "Мм" (Минуты)
        tk.Label(input_frame, text="Мм", **label_attr).grid(row=0, column=2, padx=5)
        # Создаем поле ввода для минут
        self.mins_entry = tk.Entry(input_frame, **entry_attr)
        # Устанавливаем в поле минут значение по умолчанию "00"
        self.mins_entry.insert(0, "00")
        # Размещаем поле ввода в сетке (строка 1, колонка 2)
        self.mins_entry.grid(row=1, column=2, padx=5)

        # Создаем второй текстовый разделитель двоеточие
        tk.Label(input_frame, text=":", font=("Helvetica", 18), fg="#ecf0f1", bg="#2c3e50").grid(row=1, column=3)

        # Создаем подпись "Сс" (Секунды)
        tk.Label(input_frame, text="Сс", **label_attr).grid(row=0, column=4, padx=5)
        # Создаем поле ввода для секунд
        self.secs_entry = tk.Entry(input_frame, **entry_attr)
        # Устанавливаем в поле секунд значение по умолчанию "00"
        self.secs_entry.insert(0, "00")
        # Размещаем поле ввода в сетке (строка 1, колонка 4)
        self.secs_entry.grid(row=1, column=4, padx=5)

        # Создаем главное цифровое табло таймера
        self.time_display = tk.Label(
            self.root,
            text="00:00:00",
            font=("Consolas", 36, "bold"),
            fg="#e74c3c",
            bg="#2c3e50"
        )
        # Выводим табло на экран с отступами
        self.time_display.pack(pady=20)

        # Создаем контейнер для нижних кнопок управления
        btn_frame = tk.Frame(self.root, bg="#2c3e50")
        # Выводим контейнер для кнопок на экран
        btn_frame.pack(pady=10)

        # Создаем словарь общих настроек для кнопок управления
        btn_attr = {
            "font": ("Helvetica", 11, "bold"),
            "width": 8,
            "cursor": "hand2"
        }

        # Создаем кнопку запуска
        self.start_btn = tk.Button(btn_frame, text="Старт", bg="#2ecc71", fg="white", command=self.start_timer, **btn_attr)
        # Размещаем кнопку старта в сетке (строка 0, колонка 0)
        self.start_btn.grid(row=0, column=0, padx=5)

        # Создаем кнопку паузы
        self.pause_btn = tk.Button(btn_frame, text="Пауза", bg="#f1c40f", fg="black", command=self.pause_timer, **btn_attr)
        # Размещаем кнопку паузы в сетке (строка 0, колонка 1)
        self.pause_btn.grid(row=0, column=1, padx=5)

        # Создаем кнопку сброса
        self.reset_btn = tk.Button(btn_frame, text="Сброс", bg="#95a5a6", fg="white", command=self.reset_timer, **btn_attr)
        # Размещаем кнопку сброса в сетке (строка 0, колонка 2)
        self.reset_btn.grid(row=0, column=2, padx=5)

    # Метод проверки введенных пользователем данных
    def validate_and_convert(self):
        # Открываем блок перехвата возможных ошибок
        try:
            # Считываем часы, преобразуем в int (если пусто, берем 0)
            h = int(self.hours_entry.get() or 0)
            # Считываем минуты, преобразуем в int (если пусто, берем 0)
            m = int(self.mins_entry.get() or 0)
            # Считываем секунды, преобразуем в int (если пусто, берем 0)
            s = int(self.secs_entry.get() or 0)

            # Проверяем, нет ли среди введенных чисел отрицательных
            if h < 0 or m < 0 or s < 0:
                # Если нашли минус, принудительно вызываем ошибку
                raise ValueError

            # Переводим всё время в секунды и возвращаем сумму
            return h * 3600 + m * 60 + s
        # Если пользователь ввел буквы, знаки или отрицательные числа
        except ValueError:
            # Показываем всплывающее критическое окно
            messagebox.showerror("Ошибка", "Введите корректные целые положительные числа!")
            # Возвращаем пустоту (сигнал о неудачной валидации)
            return None

    # Рекурсивный метод отсчета времени каждую секунду
    def update_countdown(self):
        # Если флаг работы выключен (нажали паузу или сброс)
        if not self.is_running:
            # Немедленно прерываем выполнение метода
            return

        # Если время на таймере еще осталось
        if self.total_seconds > 0:
            # Уменьшаем общее количество секунд на единицу
            self.total_seconds -= 1

            # Рассчитываем количество полных часов
            h = self.total_seconds // 3600
            # Рассчитываем количество полных минут
            m = (self.total_seconds % 3600) // 60
            # Рассчитываем количество оставшихся секунд
            s = self.total_seconds % 60

            # Форматируем текст в вид 00:00:00 и выводим на табло
            self.time_display.config(text=f"{h:02d}:{m:02d}:{s:02d}")

            # Планируем следующий запуск этого же метода через 1 секунду
            self.timer_id = self.root.after(1000, self.update_countdown)
        # Если секунд больше не осталось (таймер дошел до нуля)
        else:
            # Меняем флаг активности на выключенный статус
            self.is_running = False
            # Вызываем метод включения сигнализации
            self.trigger_alarm()

    # Метод, вызываемый при нажатии кнопки "Старт"
    def start_timer(self):
        # Если таймер уже запущен и считает
        if self.is_running:
            # Игнорируем повторное нажатие кнопки, выходим
            return

        # Если таймер запускается впервые или после сброса
        if self.total_seconds == 0:
            # Запускаем проверку корректности полей ввода
            seconds = self.validate_and_convert()
            # Если данные неверны или в полях кругом нули
            if seconds is None or seconds == 0:
                # Прерываем запуск таймера
                return
            # Записываем успешно проверенное время в секундах
            self.total_seconds = seconds

        # Возвращаем стандартный цвет фона
        self.update_bg_color("#2c3e50")

        # Ставим флаг активности таймера в True
        self.is_running = True
        # Делаем первый запуск функции отсчета
        self.update_countdown()

    # Метод, вызываемый при нажатии кнопки "Пауза"
    def pause_timer(self):
        # Если таймер в данный момент работает
        if self.is_running:
            # Переключаем статус флага на приостановку
            self.is_running = False
            # Если в системе есть активный запланированный таймаут
            if self.timer_id:
                # Отменяем будущий вызов авто-секунды
                self.root.after_cancel(self.timer_id)

    # Метод, вызываемый при нажатии кнопки "Сброс"
    def reset_timer(self):
        # Ставим таймер на паузу
        self.pause_timer()
        # Обнуляем внутренний счетчик секунд
        self.total_seconds = 0
        # Сбрасываем текст цифрового табло в нули
        self.time_display.config(text="00:00:00")
        # Возвращаем приложению стандартный цвет фона
    def update_bg_color(self, color):
        # Меняем цвет фона главного окна
        self.root.config(bg=color)
        # Запускаем цикл перебора всех элементов интерфейса
        for widget in self.root.winfo_children():
            # Проверяем, является ли элемент Текстом или Рамкой
            if isinstance(widget, (tk.Label, tk.Frame)):
                # Защищаем поля ввода (они должны остаться белыми)
                if widget not in [self.hours_entry, self.mins_entry, self.secs_entry]:
                    # Меняем фон подходящим виджетам на переданный цвет
                    widget.config(bg=color)

    # Метод включения оповещения при конце отсчета
    def trigger_alarm(self):
        # Окрашиваем приложение в тревожный красный цвет
        self.update_bg_color("#c0392b")

        # Открываем защищенный блок для проигрывания звука
        try:
            # Запускаем цикл, который повторится ровно три раза
            for _ in range(3):
                # Издаем писк на частоте 1000 Гц длительностью 400 мс
                winsound.Beep(1000, 400)
        # Перехватываем ошибки, если программа запущена не на Windows
        except Exception:
            # Игнорируем ошибку звука
            pass

        # Выводим на экран финальное информационное окно
        messagebox.showinfo("Время истекло!", "Обратный отсчёт успешно завершён!")


# Проверка: если файл запущен напрямую, а не импортирован
if __name__ == "__main__":
    # Создаем базовый корневой объект окна Tkinter
    root = tk.Tk()
    # Передаем окно в наш созданный класс и инициализируем приложение
    app = SmartDownApp(root)
    # Запускаем бесконечный цикл обработки событий интерфейса
    root.mainloop()
