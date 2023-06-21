
from AnimeParser import *


if __name__ == '__main__':
    anime = AnimeParser()
    anime_search = anime.get_anime("реинкарнация безработного")[0]
    print(anime_search.NAME) # Реинкарнация безработного: История о приключениях в другом мире
    print(anime_search.EPISODE) # 11
    print(anime_search.TYPE) # тв сериал
    print(anime_search.STATUS) # вышел
    print(anime_search.POSTER) # link poster
    print(anime_search.LINK) # link animego

    print(anime_search.get_all()) #all
    
