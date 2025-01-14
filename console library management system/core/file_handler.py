import json
from core.config import Config
from core.Book import Book
from core.errors import FileNotFoundError

def load_data():
    """Загружает данные из файла dict.json и преобразует их в объекты Book."""
    try:
        with open(Config.DATABASE_PATH, "r", encoding="utf-8") as file:
            data = json.load(file)  # Пробуем загрузить данные
        # Если файл пустой, json.load() вызовет исключение JSONDecodeError
        if not data:  # Если данные пусты (например, файл пуст)
            return []
        return [Book.from_dict(book) for book in data]
    except FileNotFoundError:
        return []  # Если файл не найден, возвращаем пустой список
    except json.JSONDecodeError:  # Если не удается распарсить пустой файл
        return []  # Возвращаем пустой список при пустом или неправильном JSON


def save_data(data):
    """Сохраняет данные в файл dict.json."""
    try:
        with open(Config.DATABASE_PATH, "w", encoding="utf-8") as file:
            # Если данные еще не в формате словарей, преобразуем объекты Book в словари
            if isinstance(data[0], Book):  # Если данные содержат объекты Book
                json.dump([book.to_dict() for book in data], file, ensure_ascii=False, indent=4)
            else:
                json.dump(data, file, ensure_ascii=False, indent=4)  # Если уже в формате словаря
    except Exception as e:
        print(f"Ошибка при сохранении данных: {e}")



