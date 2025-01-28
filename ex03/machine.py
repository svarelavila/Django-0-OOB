import random
from beverages import HotBeverage, Coffee, Tea, Chocolate, Cappuccino


class CoffeeMachine:
    """
    Clase que representa una máquina de café.
    """

    class EmptyCup(HotBeverage):
        """
        Clase que representa una taza vacía.
        """

        def __init__(self):
            super().__init__(name="empty cup", price=0.90)

        def description(self):
            """
            Devuelve la descripción de la taza vacía.
            """
            return "An empty cup?! Gimme my money back!"

    class BrokenMachineException(Exception):
        """
        Excepción que se lanza cuando la máquina está rota.
        """

        def __init__(self):
            super().__init__("This coffee machine has to be repaired.")

    def __init__(self):
        """
        Constructor que inicializa el estado de la máquina.
        """
        self.served_count = 0  # Contador de bebidas servidas
        self.is_broken = False  # Estado de la máquina

    def serve(self, beverage_cls):
        """
        Sirve una bebida aleatoriamente o una taza vacía.

        :param beverage_cls: Clase de bebida derivada de HotBeverage.
        :return: Instancia de la bebida o de EmptyCup.
        :raises: BrokenMachineException si la máquina está rota.
        """
        if self.is_broken:
            raise CoffeeMachine.BrokenMachineException()

        # Incrementar el contador de bebidas servidas
        self.served_count += 1

        # Verificar si la máquina se rompe después de 10 bebidas
        if self.served_count > 10:
            self.is_broken = True
            raise CoffeeMachine.BrokenMachineException()

        # Aleatoriedad: usar random.randint(0, 1) para decidir entre bebida o taza vacía
        if random.randint(0, 1) == 0:  # 50% de probabilidad
            return CoffeeMachine.EmptyCup()

        return beverage_cls()  # Devuelve la bebida solicitada

    def repair(self):
        """
        Repara la máquina para que vuelva a servir bebidas.
        """
        self.is_broken = False
        self.served_count = 0  # Reinicia el contador
        print("The coffee machine has been repaired.")


def test():
    """
    Pruebas para la clase CoffeeMachine utilizando random.randint().
    """
    coffeeMachine = CoffeeMachine()
    beverages = [Coffee, Tea, Cappuccino, Chocolate, HotBeverage]

    for _ in range(24):  # Intentar servir hasta 24 bebidas
        try:
            # Seleccionar aleatoriamente una bebida con random.randint()
            random_index = random.randint(0, len(beverages) - 1)
            print(coffeeMachine.serve(beverages[random_index]))
        except CoffeeMachine.BrokenMachineException as e:
            # Manejar la excepción cuando la máquina se rompe
            print(e)
            coffeeMachine.repair()


if __name__ == '__main__':
    test()
