# 1. Модифікуйте Перше домашнє завдання так, щоб при спробі встановити від'ємну
# або нульову вартість товару викликалася виняткова ситуація
# (тип виняткової ситуації треба самостійно реалізувати).

# 1. Створіть клас для опису товару. У якості атрибутів товару можете використовувати значення ціни товару,
# опису товару, габарити товару. Створіть пару екземплярів вашого класу та протестуйте їхню роботу.
class PriceErrors(Exception):
    def __init__(self, price):
        self.price = price

    def __str__(self):
        if self.price < 0:
            return 'The price can`t be negative'
        elif self.price == 0:
            return 'The price can`t be zero'

class Product:
    def __init__(self, description, price, dimensions):
        if price <= 0:
            raise PriceErrors(price)

        self.description = description
        self.price = price
        self.dimensions = dimensions

    def __str__(self):
        return f'{self.description} {self.price} {self.dimensions}'

product_1 = Product('Potatoes', 1.00, 'mesh package')
product_2 = Product('Tomatoes', 2.00, 'package')
product_3 = Product('Banana', 3.00, 'brush')

# 2. Створіть клас "Покупець". У якості атрибутів можна використовувати прізвище, ім'я, по батькові,
# мобільний телефон тощо.
class Buyer:
    def __init__(self, name, surname, mobile_phone):
        self.name = name
        self.surname = surname
        self.mobile_phone = mobile_phone

    def __str__(self):
        return f'{self.name} {self.surname} {self.mobile_phone}'

buyer_1 = Buyer('Ivan', 'Ivanov', '+38-097-111-11-11')
byuer_2 = Buyer('Petr', 'Petrov', '+38-097-222-22-22')
buyer_3 = Buyer('Sergey', 'Sergeyev', '+38-097-333-33-33')

# 3. Створіть клас "Замовлення". Замовлення може містити декілька товарів певної кількості.
# Замовлення має містити дані про користувача, який його здійснив.
# Реалізуйте метод обчислення сумарної вартості замовлення.
# Визначте метод str() для коректного виведення інформації про це замовлення.
class Order:
    def __init__(self, title):
        self.title = title
        self.orders = []
        self.total_price = []

    def add_order(self, product):
        if product not in self.orders:
            self.orders.append(product)
            self.total_price.append(product.price)

    def __str__(self):
        return f"{self.title}\n{'-' * 30}\n" + '\n'.join(map(str, self.orders)) + '\n' +\
                'Total: USD ' + f'{sum(self.total_price):.2f}' + '\n'

buyer_1_order = Order('Buyer_1_Order')
buyer_1_order.add_order(product_1)
buyer_1_order.add_order(product_2)
print (buyer_1_order)

buyer_2_order = Order('Buyer_2_Order')
buyer_2_order.add_order(product_2)
buyer_2_order.add_order(product_3)
print (buyer_2_order)

buyer_3_order = Order('Buyer_3_Order')
buyer_3_order.add_order(product_1)
buyer_3_order.add_order(product_2)
buyer_3_order.add_order(product_3)
print (buyer_3_order)
