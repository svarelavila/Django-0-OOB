import random
from beverages import HotBeverage, Coffee, Tea, Chocolate, Cappuccino


class CoffeeMachine:
    """
    Class representing a coffee machine.
    """

    class EmptyCup(HotBeverage):
        """
        Class representing an empty cup.
        """

        def __init__(self):
            super().__init__(name="empty cup", price=0.90)

        def description(self):
            """
            Returns the description of the empty cup.
            """
            return "\nAn empty cup?! Gimme my money back!"

    class BrokenMachineException(Exception):
        """
        Exception raised when the machine is broken.
        """

        def __init__(self):
            super().__init__("\nThis coffee machine has to be repaired.")

    def __init__(self):
        """
        Constructor that initializes the machine's state.
        """
        self.served_count = 0  # Contador de bebidas servidas
        self.is_broken = False  # Estado de la máquina

    def serve(self, beverage):
        """
        Serves a randomly selected beverage or an empty cup.
        :param beverage_cls: Beverage class derived from HotBeverage.
        :return: Instance of the beverage or an EmptyCup.
        :raises: BrokenMachineException if the machine is broken.
        """
        if self.is_broken:
            raise CoffeeMachine.BrokenMachineException()

        # Incrementar el contador de bebidas servidas
        self.served_count += 1

        # Verificar si la máquina se rompe después de 10 bebidas
        if self.served_count > 10:
            self.is_broken = True
            raise CoffeeMachine.BrokenMachineException()

        # Usar random.randint(0, 1) para decidir entre bebida o taza vacía
        if random.randint(0, 1) == 0:  # 50% de probabilidad
            return CoffeeMachine.EmptyCup()

        return beverage()  # Devuelve la bebida solicitada

    def repair(self):
        """
        Repairs the machine so it can serve drinks again.
        """
        self.is_broken = False
        self.served_count = 0  # Reinicia el contador
        print("\nThe coffee machine has been repaired.")


def test():
    """
    Tests for the CoffeeMachine class using random.randint().
    """
    coffeeMachine = CoffeeMachine()
    beverages = [Coffee, Tea, Cappuccino, Chocolate, HotBeverage]

    for _ in range(24):  # Intentar servir hasta 24 bebidas
        try:
            # Seleccionar aleatoriamente una bebida con random.randint()
            random_index = random.randint(0, len(beverages) - 1)
            print(coffeeMachine.serve(beverages[random_index]))
            print()
        except CoffeeMachine.BrokenMachineException as e:
            # Manejar la excepción cuando la máquina se rompe
            print(e)
            coffeeMachine.repair()


if __name__ == '__main__':
    test()
