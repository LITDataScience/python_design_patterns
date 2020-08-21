# Open closed Principle

from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3


class Product:
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size


class ProductFilter:
    @staticmethod
    def filter_by_color(products, color):
        for p in products:
            if p.color == color:
                yield p

    @staticmethod
    def filter_by_size(products, size):
        for p in products:
            if p.size == size:
                yield p


class Specification:
    # Method is meant to be overridden so don't focus here.
    def is_satisfied(self, item):
        pass

    def __and__(self, other):
        # this is binary and operator i.e, `&`
        return AndSpecification(self, other)


class Filter:
    # Method is meant to be inherited.
    def filter(self, items, specs):
        pass


class ColorSpecification(Specification):
    def __init__(self, color):
        self.color = color

    def is_satisfied(self, item):
        return item.color == self.color


class SizeSpecification(Specification):
    def __init__(self, size):
        self.size = size

    def is_satisfied(self, item):
        return item.size == self.size


# Creating a Combinator class
class AndSpecification(Specification):
    def __init__(self, *args):
        self.args = args

    def is_satisfied(self, item):

        """ map() is used to go through every single element and apply some sort of lambda to it.
            And the lambda we're going to apply is to check whether the Specification is satisfied for a particular item

            all() checks whether all the items are boolean value `True` or not.
        """
        return all(map(
            # we go through every single item in self.args and check if the specks are satisfied.
            lambda spec: spec.is_satisfied(item), self.args
        ))


# Adding flexibility and following the OCP. That's why not doing this in the Base class.
class BetterFilter(Filter):
    def filter(self, items, spec):
        for item in items:
            if spec.is_satisfied(item):
                yield item


if __name__ == '__main__':
    apple = Product('Apple', Color.RED, Size.SMALL)
    tree = Product('Tree', Color.GREEN, Size.LARGE)
    house = Product('House', Color.BLUE, Size.LARGE)

    products = [apple, tree, house]

    pf = ProductFilter()
    print('Green Products (old approach): ')
    for p in pf.filter_by_color(products, Color.GREEN):
        print(f' - [{p.name}] is green')

    bf = BetterFilter()
    print('Green Products (new approach): ')
    green = ColorSpecification(Color.GREEN)
    for p in bf.filter(products, green):
        print(f' - [{p.name}] is green')

    print('Large Products (new approach): ')
    large = SizeSpecification(Size.LARGE)
    for p in bf.filter(products, large):
        print(f' - [{p.name}] is large')

    print('Large Blue Item: ')
    large_and_blue = AndSpecification(large, ColorSpecification(Color.BLUE))
    for p in bf.filter(products, large_and_blue):
        print(f' - [{p.name}] is large & blue')

    """ what if we want something like `this and that`. Looks pretty easy. But unfortunately,
        we cannot overload `and` operator in python. Although, we can overload the `&`.
    """
    large_and_green = large & ColorSpecification(Color.GREEN)
    for p in bf.filter(products, large_and_green):
        print(f' - [{p.name}] is large & green')
