from logic import add_product, find_product, show_all, change_product, delete_product
from database import create_table
while True:
    try:
        create_table()
        print('===Sales-Tracker===')
        print('1. Добавление товара')
        print('2. Поиск товара по ID/имени')
        print('3. Список всех товаров')
        print('4. Изменение количества товара')
        print('5. Удаление товара')
        print('6. Просмотр истории продаж')
        print('7. Выйти')
        choice = int(input('Ваш выбор: '))
        
        if choice == 1:
            add_product()
        elif choice == 2:
            find_product()
        elif choice == 3:
            show_all()
        elif choice == 4:
            change_product()
        elif choice == 5:
            delete_product()
        elif choice == 7:
            print('Программа завершена!')
            exit()
    except ValueError:
        print('Ошибка при вводе!')