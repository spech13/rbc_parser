from bs4 import BeautifulSoup
import requests


class New:
    def __init__(self, href, title):
        self.href = href
        self.title = title

    def get_content(self):
        page = requests.get(self.href)
        soup = BeautifulSoup(page.text, "html.parser")
        return "\n".join(item.text.replace("\n", "") for item in soup.findAll("p"))


url = "https://rbc.ru"

page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")
news = [
    New(href.attrs["href"], href.findAll(class_="main__feed__title")[0].text)
    for href in soup.findAll(
        "a", class_="main__feed__link js-yandex-counter js-visited"
    )
]

for num, new in enumerate(news):
    print(f"{num}.{new.title}\n\n{new.get_content()}\n")
