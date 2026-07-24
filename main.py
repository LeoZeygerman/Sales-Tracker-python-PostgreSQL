from database import create_table
while True:
    try:
        print('===Sales-Tracker===')
        print('1. Поиск товара по ID/имени')
        print('2. Список всех товаров')
        print('3. Изменение товара')
        print('4. Удаление товара')
        print('5. Просмотр истории продаж')
        print('6. Выйти')
        choice = int(input('Ваш выбор: '))
        
        if choice == 6:
            print('Программа завершена!')
            exit()
    except ValueError:
        print('Ошибка при вводе!')