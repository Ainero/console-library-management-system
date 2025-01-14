# Импорты из core
from core.config import Config
from core.errors import ValidationError, NotFoundError, FileReadError
from core.verify import *
from core.Book import *
import json

# Импорты из use_case
from use_case.add_book import add_book
from use_case.delete_book import delete_book
from use_case.get_books import get_books
from use_case.search_books import search_books
from use_case.update_book import update_book

# Импорты из interfaces
from interfaces.cli import display_menu, get_user_input

# Импорты из entrypoint
from entrypoint.router import handle_route


def main():
    # Основной цикл программы
    while True:
        try:
            # Отображение главного меню
            display_menu()
            choice = get_user_input("Введите номер действия: ")

            # Маршрутизация действий
            handle_route(choice)

        except ValidationError as ve:
            print(f"Ошибка валидации: {ve.message}")
        except NotFoundError as ne:
            print(f"Ошибка: {ne.message}")
        except Exception as e:
            print(f"Произошла непредвиденная ошибка: {e}")




if __name__ == "__main__":
    main()