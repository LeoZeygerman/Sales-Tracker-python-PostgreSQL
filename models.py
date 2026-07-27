class Product:
    def __init__(self, id, name, amount, count):
        self.id = id
        self.name = name
        self.amount = amount
        self.count = count
        
    def add_product_models(self):
        print(f'=====================================\nТовар добавлен!\nНазвание: {self.name}\nЦена: {self.amount}\nКоличество: {self.count}\n=====================================')
      
    def find_product_models(self):
        print(f'===========================\nID: {self.id}\nНазвание: {self.name}\nЦена: {self.amount}\nКоличество: {self.count}\n===========================')
    
class Track:
    def __init__(self, id, type, count):
        self.id = id
        self.type = type
        self.count = count
    
    def show_changes(self):
        print(f'========================\nID: {self.id}\nТип: {self.type}\nКоличество: {self.count}\n========================')