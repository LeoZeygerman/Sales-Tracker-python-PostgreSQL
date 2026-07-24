class Product:
    def __init__(self, id, name, amount, count):
        self.id = id
        self.name = name
        self.amount = amount
        self.count = count
        
    def add_product_models(self):
        print(f'=====================================\nТовар добавлен!\nНазвание: {self.name}\nЦена: {self.amount}\nКоличество: {self.count}\n=====================================')