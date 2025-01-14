class Book:

    def __init__(self, book_id, title, author, year, status):
        self.id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def to_dict(self):
        """Преобразование объекта книги в словарь."""
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "status": self.status
        }


    @classmethod
    def from_dict(cls, data):
        """Создание объекта книги из словаря."""
        return cls(
            book_id=data["id"],
            title=data["title"],
            author=data["author"],
            year=data.get("year"),
            status=data.get("status", "в наличии")
        )



