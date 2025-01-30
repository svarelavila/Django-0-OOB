class HotBeverage:
    """
    Base class for hot beverages.
    """

    def __init__(self, name="hot beverage", price=0.30):
        """
        Constructor for the HotBeverage class.
        :param name: (str) Name of the beverage.
        :param price: (float) Price of the beverage.
        """
        if price < 0:
            # Validación del precio
            raise ValueError("The price cannot be negative.")
        self.name = name
        self.price = price

    def description(self):
        """
        Returns a generic description of the beverage.
        """
        return "Just some hot water in a cup."

    def __str__(self):
        """
        Returns a textual representation of the beverage.
        """
        TEMPLATE = ("name : {name}\n"
                    "price: {price:0.2f}\n"
                    "description: {description}")
        return TEMPLATE.format(
            name=self.name,
            price=self.price,
            description=self.description()
        )


class Coffee(HotBeverage):
    """
    Class representing coffee.
    """

    def __init__(self):
        super().__init__(name="coffee", price=0.40)

    def description(self):
        """
        Returns a specific description for coffee.
        """
        return "A coffee, to stay awake."


class Tea(HotBeverage):
    """
    Class representing tea.
    """

    def __init__(self):
        super().__init__(name="tea")


class Chocolate(HotBeverage):
    """
    Class representing hot chocolate.
    """

    def __init__(self):
        super().__init__(name="chocolate", price=0.50)

    def description(self):
        """
        Returns a specific description for hot chocolate.
        """
        return "Chocolate, sweet chocolate..."


class Cappuccino(HotBeverage):
    """
    Class representing cappuccino.
    """

    def __init__(self):
        super().__init__(name="cappuccino", price=0.45)

    def description(self):
        """
        Returns a specific description for cappuccino.
        """
        return "Un po' di Italia nella sua tazza!"


def test():
    """
    Tests to demonstrate the behavior of the beverage classes.
    """
    # Crear una lista con instancias de las bebidas
    beverages = [
        HotBeverage(),  # Bebida genérica
        Coffee(),       # Café
        Tea(),          # Té
        Chocolate(),    # Chocolate caliente
        Cappuccino()    # Cappuccino
    ]

    # Imprimir los detalles de cada bebida
    for beverage in beverages:
        print(beverage)
        print()


if __name__ == '__main__':
    test()
