class Intern:
    """
    Representa a un interno en una empresa.
    """

    class Coffee:
        """
        Representa una taza de café preparado por el interno.
        """

        def __str__(self):
            """
            Devuelve una descripción del café.
            """
            return "This is the worst coffee you ever tasted."

    def __init__(self, name="My name? I'm nobody, an intern, I have no name."):
        """
        Constructor de la clase Intern.
        
        :param name: (str) Nombre del interno. Valor predeterminado si no se proporciona.
        """
        self.name = name

    def __str__(self):
        """
        Devuelve el nombre del interno.
        """
        return self.name

    def work(self):
        """
        Simula una acción de trabajo que el interno no puede realizar.
        Lanza una excepción indicando que no puede trabajar.
        """
        raise Exception("I'm just an intern, I can't do that...")

    def make_coffee(self):
        """
        Simula la preparación de café por el interno.

        :return: (Coffee) Una instancia de la clase Coffee.
        """
        return Intern.Coffee()


def test():
    """
    Pruebas para demostrar el comportamiento de la clase Intern y su clase anidada Coffee.
    """
    # Crear un interno sin nombre
    intern_no_name = Intern()
    print(intern_no_name)  # "My name? I'm nobody, an intern, I have no name."

    # Crear un interno con nombre
    intern_mark = Intern("Mark")
    print(intern_mark)  # "Mark"

    # Mark prepara café
    coffee = intern_mark.make_coffee()
    print(coffee)  # "This is the worst coffee you ever tasted."

    # Interno sin nombre intenta trabajar
    try:
        intern_no_name.work()
    except Exception as e:
        print(e)  # "I'm just an intern, I can't do that..."


if __name__ == "__main__":
    test()
