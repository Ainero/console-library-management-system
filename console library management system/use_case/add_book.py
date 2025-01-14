from core.Book import Book
from core.errors import ValidationError
from core.file_handler import load_data, save_data
from core.verify import verify_title, verify_author, verify_year, verify_status
from core.return_to_menu import return_to_menu
import uuid


def add_book():
    """Добавляет новую книгу с проверкой данных на этапе ввода."""
    while True:
        try:
            title = input("Введите название книги: ").strip()
            verify_title(title)  # Верификация названия
            break
        except ValueError as e:
            print(f"Ошибка: {e}")

    while True:
        try:
            author = input("Введите имя автора (имя и фамилия): ").strip()
            verify_author(author)  # Верификация автора
            break
        except TypeError as e:
            print(f"Ошибка: {e}")

    while True:
        try:
            year = input("Введите год издания книги: ").strip()
            if year:
                year = int(year)
                verify_year(year)  # Верификация года
            break  # Если поле пустое или верификация прошла успешно
        except ValueError as e:
            print(f"Ошибка: {e}")
        except TypeError as e:
            print(f"Ошибка: {e}")

    # Статус устанавливается по умолчанию
    status = "в наличии"

    # Создание объекта книги после успешной верификации всех данных
    try:
        new_book = Book(
            book_id=str(uuid.uuid4()),
            title=title,
            author=author,
            year=year,
            status=status
        )
    except (TypeError, ValueError) as e:
        print(f"Ошибка при создании книги: {e}")
        return

    # Загрузка существующих данных и добавление новой книги
    data = load_data()
    data.append(new_book.to_dict())  # Сохранение объекта в виде словаря
    save_data(data)

    print(f"Книга '{title}' автора {author} успешно добавлена!")

    return_to_menu()
