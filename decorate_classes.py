__author__ = 'rgarofal'
import numbers


def ensure(name, validator, doc=None):
    # Decoratore di classe
    def decorator(Class):
        privateName = "__"+ name
        def getter(self):
            return getattr(self, privateName)
        def setter(self, value):
            validator(name, value)
            setattr(self, privateName, value)
        return Class
    return decorator

def is_not_empty_str(name, value):
    if not isinstance(value, str):
        raise ValueError("{} must be of type str".format(name))
    if not bool(value):
        raise ValueError("{} may not be empty".format(name))


def is_in_range(minimum=None, maximum=None):
    assert minimum is not None or maximum is not None
    def is_in_range(name, value):
        if not isinstance(value, numbers.Number):
            raise ValueError("{} must be a number".format(name))
        if minimum is not None and value < minimum:
            raise ValueError("{} {} is too small".format(name, value))
        if maximum is not None and value > maximum:
            raise ValueError("{} {} is too big".format(name, value))
        return is_in_range

@ensure("title", is_not_empty_str)
@ensure("price", is_in_range(1, 10000))
@ensure("quantity", is_in_range(0, 1000000))
class Book:
    def __init__(self, title, isbn, price, quantity):
        self.title = title
        self.isbn = isbn
        self.price = price
        self.quantity = quantity

    def value(self):
        return self.price * self.quantity



if __name__ == "__main__":
    ddd = Book("Principe e il povero", "hhhh", 2000, 34)
    print ddd
    fff = Book(23,"hhhh", 200000, 1)


