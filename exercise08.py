class Laptop:

    def __init__(self, price):
        if not isinstance(price, (int, float)):
            raise TypeError('The price attribute must be an int or float type.')
        elif not price > 0:
            raise ValueError('The price attribute must be a positive int or float value.')
        else:
            self._price = price

    def get_price(self):
        return self._price

    def set_price(self, value):
        
        if not isinstance(value, (int, float)):
            raise TypeError('The price attribute must be an int or float type.')
        
        if not value > 0:
            raise ValueError('The price attribute must be a positive int or '
                'float value.')
        
        self._price = value

try:
    laptop = Laptop(-3499)
except (ValueError, TypeError) as error:
    print(error)

