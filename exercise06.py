class Laptop:

    def __init__(self, brand, model, price) -> None:
        self.brand = brand
        self.model = model
        if isinstance(price, int or float) and price > 0:
            self.price = price
        else:
            raise TypeError('The price attribute must be a positive int or float')


laptop = Laptop(brand='Acer', model='Predator', price=5490)

print(laptop.__dict__)



