import random
from beverages import Coffee, Tea, Chocolate, Cappuccino  # Importa las clases de bebidas

class CoffeeMachine:
    """
    Representa una máquina de café que puede servir bebidas calientes.
    """

    class BrokenMachineException(Exception):
        """
        Excepción personalizada para indicar que la máquina está rota.
        """
        def __init__(self, message="This coffee machine is broken."):
            super().__init__(message)

    def __init__(self):
        """
        Constructor de la máquina de café.
        """
        self.operation_count = 0
        self.operation_limit = 10  # Número máximo de operaciones antes de romperse

    def serve(self, beverage_class):
        """
        Sirve una bebida utilizando la clase de bebida especificada.
        
        :param beverage_class: Clase de bebida caliente que se quiere servir.
        :return: Instancia de la bebida si tiene éxito.
        :raises: BrokenMachineException si la máquina está rota o no puede servir.
        """
        if self.operation_count >= self.operation_limit:
            raise CoffeeMachine.BrokenMachineException()

        self.operation_count += 1

        # 50% de probabilidad de servir la bebida correctamente
        if random.choice([True, False]):
            return beverage_class()
        else:
            raise CoffeeMachine.BrokenMachineException("The machine failed to serve the beverage.")

    def repair(self):
        """
        Repara la máquina y restablece el contador de operaciones.
        """
        self.operation_count = 0
        print("The coffee machine has been repaired!")


# Pruebas
if __name__ == "__main__":
    machine = CoffeeMachine()

    # Intentar servir bebidas hasta que la máquina se rompa
    beverages = [Coffee, Tea, Chocolate, Cappuccino]
    for i in range(12):  # Intentar más de 10 operaciones
        try:
            beverage = machine.serve(random.choice(beverages))
            print(f"Served: {beverage}")
        except CoffeeMachine.BrokenMachineException as e:
            print(e)

    # Reparar la máquina
    machine.repair()

    # Intentar nuevamente
    for i in range(5):
        try:
            beverage = machine.serve(random.choice(beverages))
            print(f"Served: {beverage}")
        except CoffeeMachine.BrokenMachineException as e:
            print(e)
