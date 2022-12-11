
# 1. Рознесіть класи, які використовували під час вирішення завдання про замовлення та
# групу студентів по модулям. Переконайтеся у працездатності проєктів.

# 1. Створіть клас для опису товару. У якості атрибутів товару можете використовувати значення ціни товару,
# опису товару, габарити товару. Створіть пару екземплярів вашого класу та протестуйте їхню роботу.

import HW_15_01_Module_Product
import HW_15_01_Module_Buyer
import HW_15_01_Module_Order

product_1 = HW_15_01_Module_Product.Product('Potatoes', 1.00, 'mesh package')
product_2 = HW_15_01_Module_Product.Product('Tomatoes', 2.00, 'package')
product_3 = HW_15_01_Module_Product.Product('Banana', 3.00, 'brush')

buyer_1 = HW_15_01_Module_Buyer.Buyer('Ivan', 'Ivanov', '+38-097-111-11-11')
byuer_2 = HW_15_01_Module_Buyer.Buyer('Petr', 'Petrov', '+38-097-222-22-22')
buyer_3 = HW_15_01_Module_Buyer.Buyer('Sergey', 'Sergeyev', '+38-097-333-33-33')

buyer_1_order = HW_15_01_Module_Order.Order('Buyer_1_Order')
buyer_1_order.add_order(product_1)
buyer_1_order.add_order(product_2)
print (buyer_1_order)

buyer_2_order = HW_15_01_Module_Order.Order('Buyer_2_Order')
buyer_2_order.add_order(product_2)
buyer_2_order.add_order(product_3)
print (buyer_2_order)

buyer_3_order = HW_15_01_Module_Order.Order('Buyer_3_Order')
buyer_3_order.add_order(product_1)
buyer_3_order.add_order(product_2)
buyer_3_order.add_order(product_3)
print (buyer_3_order)
