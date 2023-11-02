# anime_parser

![GitHub](https://img.shields.io/github/license/EteEteKu/anime_parser)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/EteEteKu/anime_parser)
![GitHub last commit](https://img.shields.io/github/last-commit/EteEteKu/anime_parser)

## Описание

Простой аниме парсер, который берет данные с сайта animego.org.

## Возможности

С помощью этого парсера вы можете получить следующую информацию о аниме:
- Название
- Количество серий
- Постер
- Ссылку
- Статус аниме
- Тип аниме

Помимо этого, вы можете:
- Получить аниме с помощью поиска
- Получить случайное аниме с сайта


## Пример использования

Пример использования парсера для поиска аниме по названию:

```python
anime_parser = AnimeParser()
search_results = anime_parser.search_anime("ванпачмен")
if search_results:
    for result in search_results:
        print(f"Название: {result['name']}")
        print(f"Ссылка: {result['link']}")
else:
    print("Аниме не найдено.")
```
```python
anime = AnimeParser()
anime_search = anime.get_anime("реинкарнация безработного")[0]

print(anime_search.NAME) # Реинкарнация безработного: История о приключениях в другом мире
print(anime_search.EPISODE) # 11
print(anime_search.TYPE) # тв сериал
print(anime_search.STATUS) # вышел
print(anime_search.POSTER) # link poster
print(anime_search.LINK) # link animego

print(anime_search.get_all()) #all
```
Пример случайного аниме
```python
anime_parser = AnimeParser()
random_anime = anime_parser.get_random_anime()
if random_anime:
    print(f"Название: {random_anime[0]}")
    print(f"Ссылка: {random_anime[1]}")
else:
    print("Случайное аниме не найдено.")
```


