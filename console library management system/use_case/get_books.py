from core.return_to_menu import return_to_menu
from core.file_handler import load_data, save_data
import json


def get_books():
    try:
        with open('dict.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
        if not data:
            print('Файл пуст')
        print('Список книг: ')
        for book in data:
            print(f"Название: {book['title']}, Автор: {book['author']}, Год: {book['year']}, "
                  f"Статус: {book['status']}")

    except FileNotFoundError:
        print('Файл не найден')

    except json.JSONDecodeError:
        print('Ошибка чтения файла')

    except Exception as e:
        print(f"Произошла ошибка {e}")

    return_to_menu()
