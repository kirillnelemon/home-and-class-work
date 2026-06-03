import sqlite3
import shutil
from collections import Counter
from urllib.parse import unquote

# 1. Настраиваем пути к истории Chrome
source_path = r"C:\Users\kirag\AppData\Local\Google\Chrome\User Data\Default\History"
destination_path = "chrome_history.db"

# 2. Копируем файл истории, чтобы обойти блокировку открытого браузера
shutil.copy(source_path, destination_path)

# 3. Подключаемся к скопированной базе данных
conn = sqlite3.connect(destination_path)
cur = conn.cursor()

# 4. Вытаскиваем все посещенные адреса (URL)
cur.execute("SELECT url FROM urls")
urls = cur.fetchall()
conn.close()

# 5. Перебираем ссылки и достаем из них поисковые запросы Google
searches = []
for row in urls:
    url = row[0]  # Достаем чистый текст ссылки из кортежа

    # Ищем только поисковые запросы Гугла
    if "google." in url and "/search?q=" in url:
        parts = url.split("?q=")

        # Если после ?q= что-то есть, забираем этот текст
        if len(parts) > 1:
            query = parts[1].split("&")[0]  # Отрезаем лишние параметры ссылки

            # Заменяем плюсы на пробелы и расшифровываем русские буквы
            clean_query = unquote(query.replace("+", " "))

            # Добавляем в общий список, если запрос не пустой
            if clean_query.strip():
                searches.append(clean_query)

# 6. Считаем частоту и выводим ТОП-5 самых частых запросов
words_counts = Counter(searches)
jopa = words_counts.most_common(5)

print("\n--- ТВОЙ ТОП-5 ПОИСКОВЫХ ЗАПРОСОВ В GOOGLE ---")
for item in jopa:
    print(f"Запрос: '{item[0]}' — искал {item[1]} раз(а)")
