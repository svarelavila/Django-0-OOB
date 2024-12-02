class Coffee:
    """
    Representa una taza de café preparada por un interno.
    """

    def __str__(self):
        """
        Devuelve una descripción del café cuando se imprime.
        """
        return "This is the worst coffe you ever tasted"

class Intern:
    """
    Representa a un interno con funcionalidades básicas.
    """

    def __init__(self, name="I'm nobody, I'm just an intern, I have no name"):
        """
        Constructor de la clase Intern.

        :param name: (str) Nombre del interno. Si no se proporcina, se usa un valor predeterminado.
        """
        self.name = name

    def __str__(self):
        """
        Devuelve el nombre del interno cuando se imprime.
        """
        return self.name

    def work(self):
        """
        Simula una acción de trabajo que el interno no puede realizar.
        Genera una excepción indicando que el interno no puede trabajar.
        """
        raise Exception("I'm just an intern, I can't do that...")
    
    def make_coffee(self):
        """
        Simula la preparación de cafe por el interno.

        :return: (Coffee) Una instancia de la clase Coffee.
        """
        return Coffee()


# Pruebas para demostrar el comportamiento de las clases.
if __name__ == "__main__":
    # Crear un interno sin nombre (se usará el valor predeterminado)
    intern_no_name = Intern()
    print(intern_no_name)  # Debería imprimir: "I'm nobody, I'm just an intern, I have no name"

    # Crear un interno con nombre
    intern_mark = Intern("Mark")
    print(intern_mark)  # Debería imprimir: "Mark"

    # Mark prepara café
    coffee = intern_mark.make_coffee()
    print(coffee)  # Debería imprimir: "This is the worst coffee you ever tasted."

    # Interno sin nombre intenta trabajar (esto genera una excepción)
    try:
        intern_no_name.work()
    except Exception as e:
        print(e)  # Debería imprimir: "I'm just an intern, I can't do that..."