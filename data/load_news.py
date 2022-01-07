from contextlib import closing

import requests
import urllib3
from bs4 import BeautifulSoup
from ui.styles import PROGRESS_BAR_STYLE, SCROLL_AREA_CSS

# as first, disable requests warnings
urllib3.disable_warnings()

HEADER = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.122 Safari/534.30"}

class News:
    def __init__(self, title, link):
        self.title= title
        self.link = link

    def __str__(self):
        return f"{self.title}"

def get_news():
    news = []
    try:
        with closing(requests.get("http://www.etecsa.cu/", verify=False, headers=HEADER, timeout=5)) as request:
            etecsa = request.text
            soup = BeautifulSoup(etecsa, "html.parser")
            raw_news = soup.find("ul", {"class": "list-group"})
            labels = raw_news.find_all("li")
            for li in labels:
                a = li.find("a")
                title = a.text.strip()
                link = a.get("href")
                if title:
                    news.append(News(title, link))
        for i in news:
            print(i.link)
    except Exception as e:
        print(e.args)
    return news
