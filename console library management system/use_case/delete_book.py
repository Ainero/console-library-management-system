from core.errors import NotFoundError
from core.file_handler import load_data, save_data
from core.return_to_menu import return_to_menu

def delete_book():
    """Удаление книги."""
    title = input("Введите название книги для удаления: ").strip()
    if not title:
        raise NotFoundError("Название книги не указано.")

    data = load_data()

    # Фильтруем книги, которые соответствуют введённому названию
    matches = [book for book in data if str(title).lower() in str(getattr(book, 'title', '')).lower()]

    if not matches:
        raise NotFoundError(f"Книга с названием '{title}' не найдена.")

    # Если книга найдена, удаляем её
    for book in matches:
        data.remove(book)

    # Сохраняем обновлённый список данных
    save_data(data)

    print(f"Книга '{title}' успешно удалена!")
