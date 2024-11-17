import requests
from bs4 import BeautifulSoup
from fake_headers import Headers


KEYWORDS = ['дизайн', 'фото', 'web', 'python']
URL = "https://habr.com/ru/articles/"

response = requests.get(URL, headers=Headers(browser='chrome', os='windows').generate())
if response.status_code != 200:
    print("Ошибка загрузки страницы")

    # парсим HTML
soup = BeautifulSoup(response.text, 'html.parser')
articles = soup.find_all('article')
# if not articles:
#     print('Не найдено ни одной статьи')

for article in articles:
    title_tag = article.find('h2')
    title = title_tag.text.strip()

    #я не могу понять, как вытащить ссылку :c

    # link_tag = article.find('a', class_='tm-article-snippet__title-link')
    # if link_tag is None:
    #     continue
    # href_ = link_tag['href']
    # link = f"https://habr.com{href_}"
    # print(link_tag)

    preview = article.find('div', class_='article-formatted-body')
    preview_text = preview.text.strip()

    date_tag = article.find('time')
    date = date_tag['title'] if date_tag else "Дата неизвестна"

    if any(keyword.lower() in (title + preview_text).lower() for keyword in KEYWORDS):
        print(f"{date} - {title} ")



