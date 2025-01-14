from use_case.add_book import add_book
from use_case.delete_book import delete_book
from use_case.get_books import get_books
from use_case.search_books import search_books
from use_case.update_book import update_book

def handle_route(choice):
    if choice == "1":
        add_book()
    elif choice == "2":
        delete_book()
    elif choice == "3":
        get_books()
    elif choice == "4":
        update_book()
    elif choice == "5":
        search_books()
    elif choice == "0":
        print("Выход из программы.")
        exit()
    else:
        print("Некорректный выбор. Попробуйте снова.")


