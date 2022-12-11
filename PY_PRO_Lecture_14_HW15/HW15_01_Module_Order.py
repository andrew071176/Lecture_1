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