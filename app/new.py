import requests
from bs4 import BeautifulSoup


class New:
    def __init__(self, href, title):
        self.href = href
        self.title = title

    def get_content(self):
        page = requests.get(self.href)
        soup = BeautifulSoup(page.text, "html.parser")
        return "\n".join(item.text.replace("\n", "") for item in soup.findAll("p"))
