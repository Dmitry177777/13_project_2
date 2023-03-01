
class Shanell ():
    """"Класс канала"""
    all =[]
    pay_rate = 1

    def __init__(self, categories, price, quantity):
        self.categories = categories  #категория
        self.price = price #цена
        self.quantity = quantity # кол-во
        Item.all.append(Item)


    def print_info (self):
        """Метод вывода данных о канале"""

        total_price =self.price*self.quantity

        return total_price



