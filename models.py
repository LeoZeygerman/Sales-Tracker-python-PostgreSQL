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
    
    def delete_product_models(self):
        print(f'Товар {self.name} успешно удален!')
class Track:
    def __init__(self, id, type, count):
        self.id = id
        self.type = type
        self.count = count
    
    def show_changes(self):
        print(f'========================\nID: {self.id}\nТип: {self.type}\nКоличество: {self.count}\n========================')
        
class Track_Product:
    def __init__(self,name, type, count, amount):
        self.name = name
        self.type = type
        self.count = count 
        self.amount = amount
        
    def show_history_models(self):
        print(f'========================\nТовар: {self.name}\nТип: {self.type}\nКоличество: {self.count}\nЦена: {self.amount}\n========================')