from core.errors import NotFoundError
from core.file_handler import load_data, save_data
from core.return_to_menu import return_to_menu

def update_book():
    """Обновление книги."""
    book_id = input("Введите ID книги для обновления: ").strip()
    new_status = input("Введите новый статус (в наличии/выдана): ").strip()

    if not book_id or not new_status:
        raise NotFoundError("Некорректный ввод данных для обновления.")

    data = load_data()

    book_found = False  # Флаг для отслеживания, найдена ли книга

    for book in data:
        if str(book.id).strip() == book_id:  # Проверка по ID
            book.status = new_status  # Обновление статуса через атрибут
            save_data(data)
            print(f"Статус книги с ID {book_id} обновлен на '{new_status}'.")
            book_found = True  # Книга найдена и статус обновлен
            break  # Прерываем цикл после обновления

    if not book_found:
        print(f"Книга с ID {book_id} не найдена.")  # Сообщение, если книга не найдена

    return_to_menu()
