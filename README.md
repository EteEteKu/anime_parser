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

## Использование

Вот примеры кода, которые показывают функциональность этого парсера:

## Пример использования

Пример использования парсера для поиска аниме по названию:

```python
anime_parser = AnimeParser()
search_results = anime_parser.search_anime("название_аниме")
if search_results:
    for result in search_results:
        print(f"Название: {result['name']}")
        print(f"Ссылка: {result['link']}")
else:
    print("Аниме не найдено.")
```
