from elem import Elem, Text
from elements import Html, Head, Body, Title, Meta, Img, Table, Th, Tr, Td, Ul, Ol, Li, H1, H2, P, Div, Span, Hr, Br


class Page:
    """
    Class representing an HTML document with structure validation.
    """

    def __init__(self, root: Elem):
        """
        Constructor that takes an HTML element as the root.
        :param root: Instance of Elem representing the root element.
        """
        if not isinstance(root, Elem):
            raise TypeError("Root must be an instance of Elem.")
        self.root = root

    def is_valid(self) -> bool:
        """
        Validates whether the HTML tree structure follows the defined rules.
        """
        if not isinstance(self.root, Html):
            return False  # El elemento raíz debe ser <html>
        return self._validate_tree(self.root)

    def _validate_tree(self, elem: Elem) -> bool:
        """
        Recursively validates the HTML tree starting from an element.
        """
        rules = {
            "html": lambda e: (
                        self._check_children(e, [Head, Body], exact=True)
                        and len([child for child in e.content if isinstance(child, Head)]) == 1
                        and len([child for child in e.content if isinstance(child, Body)]) == 1),
            "head": lambda e: (
                        self._check_children(e, [Title, Meta], exact=False)
                        and len([child for child in e.content if isinstance(child, Title)]) == 1),
            "body": lambda e: self._check_children(e, [H1, H2, Div, Table, Ul, Ol, Span, P, Text, Hr, Br, Img], exact=False),
            "div": lambda e: self._check_children(e, [H1, H2, Div, Table, Ul, Ol, Span, P, Text], exact=False),
            "title": lambda e: self._check_children(e, [Text], exact=True),
            "h1": lambda e: self._check_children(e, [Text], exact=True),
            "h2": lambda e: self._check_children(e, [Text], exact=True),
            "li": lambda e: self._check_children(e, [Text], exact=True),
            "th": lambda e: self._check_children(e, [Text], exact=True),
            "td": lambda e: self._check_children(e, [Text], exact=True),
            "p": lambda e: self._check_children(e, [Text], exact=True),
            "span": lambda e: self._check_children(e, [Text, P], exact=False),
            "ul": lambda e: self._check_children(e, [Li, Ol, Ul], exact=False, minimum=1),
            "ol": lambda e: self._check_children(e, [Li, Ol, Ul], exact=False, minimum=1),
            "tr": lambda e: self._check_children(e, [Th, Td], exact=False, exclusive=True),
            "table": lambda e: self._check_children(e, [Tr], exact=False),
            "hr": lambda e: len(e.content) == 0,
            "br": lambda e: len(e.content) == 0,
            "img": lambda e: len(e.content) == 0
        }

        if isinstance(elem, Meta):
            # return not elem.content
            return len(elem.content) == 0

        if elem.tag not in rules:
            return False

        if not rules[elem.tag](elem):
            return False

        for child in elem.content:
            if isinstance(child, Elem) and not self._validate_tree(child):
                return False

        return True

    def _check_children(self, elem, allowed, exact=False, exclusive=False, minimum=0):
        """
        Validates the children of an HTML element based on predefined rules.

        :param elem: The element whose children need validation.
        :param allowed: A list of allowed child element types.
        :param exact: If True, the element must contain only the allowed types.
        :param exclusive: If True, all children must be of the same type.
        :param minimum: The minimum number of children required.
        :return: True if the element's children comply with the rules, False otherwise.
        """
        if len(elem.content) < minimum:
            return False
        if exclusive:
            tags = [type(child) for child in elem.content if isinstance(child, Elem)]
            if len(set(tags)) > 1:
                return False
        for child in elem.content:
            if isinstance(child, Elem) and type(child) not in allowed:
                return False
            if isinstance(child, Text) and not str(child).strip():
                continue  # Ignorar textos vacíos
        print(f"Validating {elem.tag} → Allowed: {[a.__name__ for a in allowed]} → Current: {[type(c).__name__ for c in elem.content]}")

        return True

    def __str__(self) -> str:
        """
        Returns the HTML as a string, including <!DOCTYPE html> if necessary.
        """
        if isinstance(self.root, Html):
            return f"<!DOCTYPE html>\n{self.root}"
        return str(self.root)

    def write_to_file(self, filename: str):
        """
        Writes the HTML to a file.
        :param filename: Name of the file.
        """
        with open(filename, "w") as file:
            file.write(str(self))


def test():
    """
    Runs a minimal but complete set of tests to validate the Page class.
    """
    print("\n" + "=" * 30)
    print("=== TESTING PAGE CLASS ===")
    print("=" * 30)

    # Caso 1: Página válida con estructura correcta
    print("\n" + "-" * 30)
    print("[TEST 1] Valid HTML Page (Basic Structure)")
    print("-" * 30)
    valid_page = Page(Html([
        Head([Title(Text("Hello World")), Meta({'charset': 'UTF-8'})]),
        Body([
            H1(Text("Welcome")),
            P(Text("This is a valid HTML document.")),
            Hr(),
            Img({'src': 'image.jpg'}),
            Br()
        ])
    ]))
    assert valid_page.is_valid(), "Test failed: Valid page should be valid."
    print("Passed: Basic structure is valid.")

    # Caso 2: Página inválida con errores de estructura
    print("\n" + "-" * 30)
    print("[TEST 2] Invalid Page (Structural Errors)")
    print("-" * 30)
    invalid_page = Page(Html([
        Head([Title(Text("Title 1")), Title(Text("Title 2"))]),  # Duplicated <title>
        Body([Meta({'charset': 'UTF-8'})])  # <meta> inside <body>
    ]))
    assert not invalid_page.is_valid(), "Test failed: Page with invalid structure should be rejected."
    print("Passed: Structural errors detected correctly.")

    # Caso 3: Página inválida con errores de jerarquía
    print("\n" + "-" * 30)
    print("[TEST 3] Invalid Page (Hierarchy Errors)")
    print("-" * 30)
    invalid_page = Page(Html([
        Head([Title(Text("Hierarchy Test"))]),
        Body([
            P([H1(Text("Wrong usage"))]),  # <h1> inside <p>
            Table([Tr([Th(Text("Header")), Td(Text("Data"))])]),  # Mixing <th> and <td>
            Ul([])  # Empty <ul> (should have at least one <li>)
        ])
    ]))
    assert not invalid_page.is_valid(), "Test failed: Page with invalid hierarchy should be rejected."
    print("Passed: Hierarchy errors detected correctly.")

    # Generación de archivos HTML (válido e inválido)
    print("\n" + "-" * 30)
    print("[GENERATING HTML FILES]")
    print("-" * 30)
    valid_page.write_to_file("valid_page.html")
    invalid_page.write_to_file("invalid_page.html")
    print("HTML files generated successfully.")

    print("\n" + "=" * 30)
    print("=== ALL TESTS PASSED SUCCESSFULLY ===")
    print("=" * 30)


if __name__ == "__main__":
    test()
