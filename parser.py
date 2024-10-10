import requests
from bs4 import BeautifulSoup

# URL сайта, который нужно парсить
url = 'https://example.com'  # Заменить на нужный сайт

# Отправка GET-запроса
response = requests.get(url)

# Проверка успешности запроса
if response.status_code == 200:
    # Парсинг HTML-контента
    soup = BeautifulSoup(response.text, 'html.parser')

    # Находим все заголовки статей (например, в тегах <h2>)
    titles = soup.find_all('h2')

    # Вывод заголовков
    for title in titles:
        print(title.get_text())
else:
    print(f"Ошибка при запросе: {response.status_code}")

    