import requests
from bs4 import BeautifulSoup
from new import New

url = "https://rbc.ru"

page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")
news = [
    New(href.attrs["href"], href.findAll(class_="main__feed__title")[0].text)
    for href in soup.findAll(
        "a", class_="main__feed__link js-yandex-counter js-visited"
    )
]

print(
    "".join(
        f"{num}.{new.title}\n\n{new.get_content()}\n\n" for num, new in enumerate(news)
    )
)
