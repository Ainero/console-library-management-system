def return_to_menu():
    Yes = 'Да'
    No = 'Нет'
    while True:
        choice = input('Вернуться в меню? Да/Нет: ').strip().lower()
        if choice == Yes.strip().lower():
            return True
        elif choice == No.strip().lower():
            return False
        else:
            print('Некорректный ввод')