# 1. Create a class that performs statistical processing of a text file - counting characters,
# words, sentences, etc. Determine the required attributes-data and attributes-methods in class
# for working with the text file.
class Process_text:
    def __init__(self, text_file: str):
        self.text_file = text_file

    def words_counter(self) -> int:
        import string
        with open(self.text_file, 'r') as f:
            words_counter = 0
            for line in f:
                for item in string.punctuation:
                    line = line.replace(item, ' ')
                words_counter += len(line.split())
            f.flush()
            f.close()
        return words_counter

    def sents_counter(self) -> int:
        with open(self.text_file, 'r') as f:
            sents_counter = 0
            for line in f:
                for item in '.!?':
                    if item in line:
                        sents_counter += 1
            f.flush()
            f.close()
        return sents_counter

    def lines_counter(self) -> int:
            with open(self.text_file, 'r') as f:
                lines_counter = 0
                for line in f:
                    lines_counter += 1
                f.flush()
                f.close()
            return lines_counter

    def letters_counter(self) -> int:
        with open(self.text_file, 'r') as f:
            letters_counter = 0
            for line in f:
                for letter in line:
                    if letter.isalpha():
                        letters_counter += 1
            f.flush()
            f.close()
        return letters_counter

    def __str__(self):
        return self.text_file

text_file_1 = Process_text ('corruption.txt')
print('Words quantity: ', text_file_1.words_counter())
print('Sentences quantity: ', text_file_1.sents_counter())
print('Lines quantity: ', text_file_1.lines_counter())
print('Letters quantity: ', text_file_1.letters_counter())

# 2. Pizzeria offers pizza-of-the-day for business lunch. The type of pizza-of-the-day depends
# on the day of week. Having a pizza-of-the-day simplifies ordering for customers. They don't have
# to be experts on specific types of pizza. Also, customers can add extra ingredients
# to the pizza-of-the-day. Write a program that will form orders from customers.
class Pizza:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def __str__(self):
        return f'{self.name}\tUSD {self.price:.2f}'

class Ingrs:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def __str__(self):
        return f'{self.name}\t\t\tUSD {self.price:.2f}'

class Order:
    def __init__ (self, order_name: str):
        self.order_name = order_name
        self.product_list = []
        self.product_quantity_list = []

    def add_product (self, product: object, quantity: float = 1) -> str:
        self.quantity = quantity
        if product not in self.product_list:
            self.product_list.append(product)
            self.product_quantity_list.append(self.quantity)
        else:
            self.product_quantity_list[self.product_list.index(product)] += self.quantity

    def total_price(self):
        return sum(item.price * self.product_quantity_list[index]
                   for index, item in enumerate(self.product_list))

    def __str__(self):
        result = '\n'.join(map(lambda item: f'{item[0]}\tx\t{item[1]}\t='
                                            f'\tUSD {item[0].price * item[1]:.2f}',
                            zip(self.product_list, self.product_quantity_list)))

        return f"{self.order_name}\n{50*'-'}\n" +\
               f"{result}\n{50*'-'}\n" \
               f"Total: USD {self.total_price():.2f}\n"

pizza_monday = Pizza('pizza_monday', 10)
pizza_tuesday = Pizza('pizza_tuesday', 20)
pizza_wednesday = Pizza('pizza_wednesday', 30)
pizza_thursday = Pizza('pizza_thursday', 40)
pizza_friday = Pizza('pizza_friday', 50)

ingr_1 = Ingrs('ingr_1', 1)
ingr_2 = Ingrs('ingr_2', 2)
ingr_3 = Ingrs('ingr_3', 3)
ingr_4 = Ingrs('ingr_4', 4)
ingr_5 = Ingrs('ingr_5', 5)

order_1 = Order('Order_1')
order_1.add_product(pizza_monday)
order_1.add_product(pizza_monday)
order_1.add_product(ingr_1)
order_1.add_product(ingr_1)
order_1.add_product(ingr_1)
order_1.add_product(ingr_5)
order_1.add_product(ingr_5)
print (order_1)

order_2 = Order('Order_2')
order_2.add_product(pizza_wednesday)
order_2.add_product(pizza_wednesday)
order_2.add_product(ingr_3, 5)
order_2.add_product(ingr_4)
print (order_2)

# 3. Write a program for selling tickets to IT-events. Each ticket has a unique number and a price.
# There are four types of tickets: regular ticket, advance ticket (purchased 60 or more days
# before the event), late ticket (purchased fewer than 10 days before the event) and student ticket.
# Additional information:
# -advance ticket - discount 40% of the regular ticket price;
# -student ticket - discount 50% of the regular ticket price;
# -late ticket - additional 10% to the regular ticket price.
# All tickets must have the following properties:
# -the ability to construct a ticket by number;
# -the ability to ask for a ticket’s price;
# -the ability to print a ticket as a String.
# Для останньої задачі реалізувати серіалізацію / десеріалізацію у форматі json проданих квитків.
import json
class Ticket:
    def __init__(self, number: int, type: str = 'regular', price: float = 100):
        self.number = number
        self.type = type
        if self.type == 'regular':
            self.price = price
        elif self.type == 'late':
            self.price = price * 0.9
        elif self.type == 'advance':
            self.price = price * 0.6
        elif self.type == 'student':
            self.price = price * 0.5
        else:
            raise '\nTicket type error'

    def __str__(self):
        return f"№ {self.number}\tType '{self.type}' \tUSD{self.price}"

class Order:
    def __init__(self, order_name):
        self.order_name = order_name
        self.tickets_list = []
        self.ticket_quantity_list = []

    def add_ticket (self, ticket, quantity: float = 1) -> str:
        self.ticket = ticket
        self.quantity = quantity
        if len(self.tickets_list) == 0:
            self.tickets_list.append(ticket)
            self.ticket_quantity_list.append(self.quantity)
        else:
            for i in range (len(self.tickets_list)):
                if self.tickets_list[i].type == ticket.type:
                    self.ticket_quantity_list[i] += self.quantity
                    break
                elif i == len(self.tickets_list) - 1 and self.tickets_list[i].type != ticket.type:
                    self.tickets_list.append(ticket)
                    self.ticket_quantity_list.append(self.quantity)

    def total_price(self):
        return sum(item.price * self.ticket_quantity_list[index]
                   for index, item in enumerate(self.tickets_list))

    def __str__(self):
        result = '\n'.join(map(lambda item: f'{item[0]}\tx\t{item[1]}\t='
                                            f'\tUSD {item[0].price * item[1]:.2f}',
                            zip(self.tickets_list, self.ticket_quantity_list)))

        return f"{self.order_name}\n{50*'-'}\n" +\
               f"{result}\n{50*'-'}\n" \
               f"Total: USD {self.total_price():.2f}\n"

def main():
    dict_types = {1: 'regular',
                  2: 'late',
                  3: 'advance',
                  4: 'student'}
    regular_ticket_price = 100
    dict_prices = {'regular': regular_ticket_price, 'late': regular_ticket_price * 0.9,
                   'advance': regular_ticket_price * 0.6, 'student': regular_ticket_price * 0.5}
    dict_options = {1: 'Construct(order) the tickets',
                    2: 'Ask for ticket`s price',
                    3: 'Print a ticket as a string (data JSON serialization)',
                    4: 'Data JSON deserialization'}

    person_ID = 0
    choice_option = 0
    order = None
    dict_order = {}

    while person_ID == 0:

        try:
            person_ID = int(input('\nPlease, enter your_ID: '))
        except ValueError:
            print('\nYour`ve entered incorrect data')
        else:
            if not isinstance(person_ID, int):
                print('\nYour`ve entered choice out of options')

        marker = 'yes'
        while marker == 'yes':

            print('\nOptions:')
            for key, value in dict_options.items():
                print(key, ':', value)

            while choice_option not in dict_options:
                try:
                    choice_option = int(input('\nPlease, choose the option: '))
                except ValueError:
                    print('\nYour`ve entered incorrect data')
                else:
                    if not 1 <= choice_option <= 4:
                        print('\nYour`ve entered choice out of options')

            if choice_option == 1:
                order = Order(f'\nIT event tickets | Person_ID: {person_ID}')

                print('\nTicket types:')
                for key, value in dict_types.items():
                    print (key, ':', value)

                request_for_next_ticket = 'yes'

                while request_for_next_ticket.lower() == 'yes':
                    choice_type = 0

                    while choice_type not in dict_types:
                        try:
                            choice_type = int(input('\nPlease, choose the ticket type: '))
                        except ValueError:
                            print('\nYour`ve entered incorrect data')
                        else:
                            if not 1 <= choice_type <= 4:
                                print('\nYour`ve entered choice out of options')

                    ticket = Ticket(choice_type, dict_types[choice_type])
                    order.add_ticket(ticket)

                    if choice_type not in dict_order:
                        dict_order[choice_type] = [dict_types[choice_type], 1]
                    else:
                        dict_order[choice_type][1] += 1

                    request_for_next_ticket = (input('\nWould you like to buy one more ticket? Yes or No: ')).lower()

                print ('\nYou`ve chose the next tickets:', order, sep = '')

            if choice_option == 2:

                print('\nTicket types:')
                for key, value in dict_types.items():
                    print(key, ':', value)

                choice_type = 0
                while choice_type not in dict_types:
                    try:
                        choice_type = int(input('Please, choose the ticket type: '))
                    except ValueError:
                        print('Your`ve entered incorrect data')
                    else:
                        if not 1 <= choice_type <= 4:
                            print('Your`ve entered choice out of options')

                print (f"\nThe price of '{dict_types[choice_type]}' ticket is "
                       f"USD {dict_prices[dict_types[choice_type]]:.2f}")

            if choice_option == 3:
                if not isinstance(order, Order):
                    print('You must place the order first')
                    choice_option = 0
                else:
                    with open('tickets_order.json', 'w') as f:
                        str = json.dumps(dict_order)
                        f.write(str)
                        print ('Data JSON serialization is successfully finished')
                        f.flush()
                        f.close()

            if choice_option == 4:
                with open('tickets_order.json', 'r') as f:
                    data = json.load(f)
                    print('Data JSON deserialization is successfully finished:\n', data)
                    f.flush()
                    f.close()

            marker = (input('\nWould you like to make your choice one more time? Yes or No: ')).lower()
            choice_option = 0

main()
