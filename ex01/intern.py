class Intern:
    """
    Represents an intern in a company.
    """

    class Coffee:
        """
        Represents a cup of coffee prepared by the intern.
        """

        def __str__(self):
            """
            Returns a description of the coffee.
            """
            return "This is the worst coffee you ever tasted."

    def __init__(self, name="My name? I'm nobody, an intern, I have no name."):
        """
        Constructor for the Intern class.
        :param name: (str) Intern's name. Default value
        if not provided.
        """
        self.name = name

    def __str__(self):
        """
        Returns the intern's name.
        """
        return self.name

    def work(self):
        """
        Simulates a work action that the intern cannot perform.
        Raises an exception indicating that the intern cannot work.
        """
        raise Exception("I'm just an intern, I can't do that...")

    def make_coffee(self):
        """
        Simulates the intern preparing coffee.
        :return: (Coffee) An instance of the Coffee class.
        """
        return Intern.Coffee()


def test():
    """
    Tests to demonstrate the behavior of the
    Intern class and its nested Coffee class.
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
