import requests
from bs4 import BeautifulSoup
from fake_headers import Headers
import random 
from Anime import Anime

class Generate_Bot:
    def __init__(self):
        self.headers = Headers()

    def generate_headers(self):
        self.headers = Headers()
        platform = ["win", "mac", "lin"]
        browser = ['chrome', 'firefox', 'opera']
        self.headers.os = random.choice(platform)
        self.headers.browser = random.choice(browser)
        self.headers.headers = True
        h = self.headers.generate()
        return h

class Parser(Generate_Bot):
    def set_session(self):
        self.sess = requests.Session()
        return 0

    def get_cookies(self):
        return self.sess.cookies.get_dict()

    def get_html(self, url, param={}):
        html = self.sess.get(url, params=param, headers=self.generate_headers(), cookies=self.get_cookies())
        del param
        return html

    def post_html(self, url, data):
        html = self.sess.get(url, data=data, headers=self.generate_headers(), cookies=self.get_cookies())
        return html

    def download_poster(self):
        pass

class AnimeParser(Parser):
    def __init__(self):
        self.set_session()

    def get_random_anime(self):
        html = self.get_html("https://animego.org/anime/random")
        soup = BeautifulSoup(html.text, 'lxml')
        anime_rnd = [soup.find_all("div", {"class": "anime-title"})[0].h1.text, html.url]
        return anime_rnd

    def get_information_anime(self, link):
        if isinstance(link, list):
            link = link[1]
        link = ''.join(link.split())
        html = self.get_html(link)
        soup = BeautifulSoup(html.text, 'lxml')
        find_poster = soup.find_all("div", {"class": "anime-poster position-relative cursor-pointer"})
        dt = list(filter(None, [' '.join(x.text.split()).lower() for x in soup.find_all('dt')]))
        dd = list(filter(None, [' '.join(x.text.split()).lower() for x in soup.find_all('dd')]))

        anime_description = list(zip(dt, dd))[:7]
        anime_description.insert(0, ("название", soup.h1.contents[0]))
        anime_description.append(("постер", find_poster[0].img["src"]))
        anime_description.append(("ссылка", link))

        if 'статус' not in dict(anime_description):
            anime_description.append(("статус", 0))

        return dict(anime_description)

    def search_anime(self, name):
        html = self.get_html("https://animego.org/search/anime", {"q": name})
        soup = BeautifulSoup(html.text, 'lxml')
        dict_anime = []
        find = soup.find_all("div", {"class": "h5 font-weight-normal mb-2 card-title text-truncate"})
        for i in range(len(find)):
            dict_anime.append({"name": find[i].a["title"], "link": find[i].a["href"]})

        if len(dict_anime) == 0:
            return 0
        return dict_anime

    def get_anime(self, name):
        anime_link = self.search_anime(name)
        count_anime_get = 5
        if len(anime_link) < 5:
            count_anime_get = len(anime_link)
        last_anime = []
        for i in range(count_anime_get):
            search_anime = self.get_information_anime(anime_link[i]["link"])
            ANIME = Anime(search_anime['название'], search_anime['тип'], search_anime['эпизоды'],
                          search_anime['статус'], search_anime['постер'], search_anime['ссылка'])
            last_anime.append(ANIME)

        return last_anime