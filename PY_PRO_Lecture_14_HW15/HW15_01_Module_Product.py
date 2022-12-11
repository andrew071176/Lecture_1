class Product:
    def __init__(self, description, price, dimensions):
        self.description = description
        self.price = price
        self.dimensions = dimensions

        if self.price <= 0:
            raise ValueError ('The price can`t be zero or negative')

    def __str__(self):
        return f'{self.description} {self.price} {self.dimensions}'