class ValidationError(Exception):
    """Ошибка валидации пользовательских данных"""
    def __init__(self, message):
        self.message = message
        super().__init__(message)


class NotFoundError(Exception):
    """Ошибка, если объект не найден."""
    def __init__(self, message):
        self.message = message
        super().__init__(message)


class FileReadError(Exception):
    """Ошибка чтения файла."""
    def __init__(self, filename):
        self.message = f"Не удалось прочитать файл: {filename}"
        super().__init__(self.message)


class FileNotFoundError(Exception):
    """Файл не найден"""
    def __init__(self, filename):
        self.message = f"Файл не найден: {filename}"
        super().__init__(self.message)
