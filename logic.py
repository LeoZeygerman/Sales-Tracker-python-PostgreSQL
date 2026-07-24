from database import add_product_base
from models import Product
def add_product():
    name = input('Введите название продукта: ')
    amount = int(input('Введите цену продукта: '))
    count = int(input('Введите количество продукта: '))
    product = add_product_base(name, amount, count)
    product.add_product_models()