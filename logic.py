from database import add_product_base, find_by_id, find_by_name
from models import Product
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