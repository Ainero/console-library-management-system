from core.config import Config
from core.errors import ValidationError, NotFoundError
from core.verify import verify_title, verify_author, verify_year
from core.file_handler import load_data
from core.return_to_menu import return_to_menu

def search_books() -> None:
    """Поиск книг по названию, автору или году."""
    try:
        # Запрашиваем критерий поиска
        print("Выберите критерий поиска: ")
        print("1. Название")
        print("2. Автор")
        print("3. Год")
        choice = input("Введите номер критерия: ").strip()

        if choice == "1":
            query = input("Введите название книги: ").strip()
            verify_title(query)
            key = "title"
        elif choice == "2":
            query = input("Введите имя автора: ").strip()
            verify_author(query)
            key = "author"
        elif choice == "3":
            query = input("Введите год издания книги: ").strip()
            if not query.isdigit():
                raise ValueError("Год должен быть числом!")
            query = int(query)
            verify_year(query)
            key = "year"
        else:
            print("Некорректный выбор!")
            return

        # Загружаем данные и фильтруем по критерию
        data = load_data()
        matches = [book for book in data if str(query).lower() in str(getattr(book, key, "")).lower()]

        if matches:
            print(f"Найдено {len(matches)} совпадений: ")
            for book in matches:
                print(f"Название: {book.title}, Автор: {book.author}, "
                        f"Год: {book.year}, Статус: {book.status}")
        else:
            print("Совпадений не найдено.")

    except ValueError as e:
        print(f"Ошибка: {e}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

    return_to_menu()
