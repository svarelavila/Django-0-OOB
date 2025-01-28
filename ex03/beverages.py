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
        if price < 0:
            raise ValueError("El precio no puede ser negativo.")  # Validación del precio
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
        TEMPLATE = ("Name : {name}\n"
                    "Price: {price:0.2f}\n"
                    "Description: {description}\n")
        return TEMPLATE.format(name=self.name, price=self.price, description=self.description())


class Coffee(HotBeverage):
    """
    Clase que representa un café.
    """

    def __init__(self):
        super().__init__(name="coffee", price=0.40)

    def description(self):
        """
        Devuelve una descripción específica para el café.
        """
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
        """
        Devuelve una descripción específica para el chocolate.
        """
        return "Chocolate, sweet chocolate..."


class Cappuccino(HotBeverage):
    """
    Clase que representa un cappuccino.
    """

    def __init__(self):
        super().__init__(name="cappuccino", price=0.45)

    def description(self):
        """
        Devuelve una descripción específica para el cappuccino.
        """
        return "Un po' di Italia nella sua tazza!"


def test():
    """
    Pruebas para demostrar el comportamiento de las clases de bebidas.
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
        print()  # Línea en blanco para separar las salidas


if __name__ == '__main__':
    test()
