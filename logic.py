from database import add_product_base, find_by_id, find_by_name, show_all_base, change_product_base, update_count_add, update_count_delete
from models import Product, Track
def add_product():
    name = input('Введите название продукта: ')
    amount = int(input('Введите цену продукта: '))
    count = int(input('Введите количество продукта: '))
    product = add_product_base(name, amount, count)
    product.add_product_models()
    
def find_product():
    print('1. Найти товар по ID')
    print('2. Найти товар по имени')
    choice = int(input('Ваш выбор: '))
    
    if choice == 1:
        product_id = int(input('Введите ID продукта: '))
        product = find_by_id(product_id)
        product.find_product_models()
    
    elif choice == 2:
        product_name = input('Введите название продукта: ')
        products = find_by_name(product_name)
        products.find_product_models()
        
def show_all():
    product = show_all_base()
    for products in product:
        products.find_product_models()
        
def change_product():
    product_id = int(input('Введите ID товара: '))
    print(f'1.Добавить продажу товара\n2.Добавить пополнение товара')
    choice = int(input('Ваш выбор: '))
    if choice == 1:
        product_type = 'Продажа'
        count = int(input('Введите количество проданного товара: '))
        product = change_product_base(product_id, product_type, count)
        product.show_changes()
        update_count_delete(product_id, count)
    elif choice == 2:
        product_type = 'Пополнение'
        count = int(input('Введите количество пополненного товара: '))
        product = change_product_base(product_id, product_type, count)
        product.show_changes()
        update_count_add(product_id, count)