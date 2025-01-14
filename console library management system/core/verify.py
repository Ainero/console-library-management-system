from string import ascii_letters

S_RUS = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
S_RUS_UPPER = S_RUS.upper()


def verify_title(title: str) -> None:
    if not title.strip():
        raise ValueError("Название книги не может быть пустым!")
    if len(title) > 200:
        raise ValueError("Название книги не должно превышать 200 символов!")


def verify_author(author: str) -> None:
    if not author.replace(' ', '').replace('.', '').isalpha():
        raise TypeError('Имя автора должно состоять из букв, пробелов и точек!')

    parts = author.split()
    if len(parts) < 2:
        raise TypeError('Имя автора должно содержать минимум два слова (имя и фамилию).')

    letters = ascii_letters + S_RUS + S_RUS_UPPER
    for part in parts:
        part_cleaned = part.strip(letters + '.')  # Убираем буквы и точки
        if len(part_cleaned) > 0:
            raise TypeError('Имя автора может содержать только буквы, пробелы, точки и дефисы!')


def verify_year(year: int) -> bool:
    if type(year) != int:
        raise TypeError('Год издания книги должен быть числом!')
    if year < 1000 or year > 9999:
        raise ValueError("Год издания должен быть в формате четырех цифр (например, 2024)!")
    return True


def verify_status(status: str) -> bool:
    valid_statuses = ["в наличии", "выдана"]
    if status.lower() not in valid_statuses:
        raise ValueError(f"Статус книги должен быть одним из следующих: {', '.join(valid_statuses)}")
    return True