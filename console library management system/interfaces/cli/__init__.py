def display_menu():
    print("1. Добавить книгу")
    print("2. Удалить книгу")
    print("3. Просмотреть книги")
    print("4. Обновить статус книги")
    print("5. Поиск книги")
    print("0. Выход")


def get_user_input(prompt):
    return input(prompt).strip()
