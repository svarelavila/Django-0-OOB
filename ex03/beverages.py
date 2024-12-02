class HotBeverage:
    """
    Clase base para bebidas calientes.
    """

    def __init__(self, name="hot beverage", price=0.30):
        """
        Constructor de la clase HotBeverage.
        
        :param name: (str) Nombre de la bebida.
        :param price: (float) Precio de la bebida.
        """
        self.name = name
        self.price = price

    def description(self):
        """
        Devuelve una descripción genérica de la bebida.
        """
        return "Just some hot water in a cup."

    def __str__(self):
        """
        Devuelve una representación textual de la bebida.
        """
        TEMPLATE = ("name : {name}\n"
                    "price: {price:0.2f}\n"
                    "description: {description}")
        return TEMPLATE.format(name=self.name, price=self.price, description=self.description())


class Coffee(HotBeverage):
    """
    Clase que representa un café.
    """

    def __init__(self):
        super().__init__(name="coffee", price=0.40)

    def description(self):
        return "A coffee, to stay awake."


class Tea(HotBeverage):
    """
    Clase que representa un té.
    """

    def __init__(self):
        super().__init__(name="tea")


class Chocolate(HotBeverage):
    """
    Clase que representa un chocolate caliente.
    """

    def __init__(self):
        super().__init__(name="chocolate", price=0.50)

    def description(self):
        return "Chocolate, sweet chocolate..."


class Cappuccino(HotBeverage):
    """
    Clase que representa un cappuccino.
    """

    def __init__(self):
        super().__init__(name="cappuccino", price=0.45)

    def description(self):
        return "Un po' di Italia nella sua tazza!"


def test():
    """
    Función de prueba para demostrar el comportamiento de las clases.
    """
    beverages = [
        HotBeverage(),
        Coffee(),
        Tea(),
        Chocolate(),
        Cappuccino()
    ]

    for beverage in beverages:
        print(beverage)
        print()


if __name__ == '__main__':
    test()

