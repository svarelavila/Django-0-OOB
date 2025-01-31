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
            "html": lambda e: self._check_children(e, [Head, Body], exact=True),
            "head": lambda e: (
                        self._check_children(e, [Title, Meta], exact=False)
                        and len([child for child in e.content if isinstance(child, Title)]) == 1),
            "body": lambda e: self._check_children(e, [H1, H2, Div, Table, Ul, Ol, Span, P, Text], exact=False),
            "div": lambda e: self._check_children(e, [H1, H2, Div, Table, Ul, Ol, Span, P, Text], exact=False),
            "title": lambda e: self._check_children(e, [Text], exact=True),
            "h1": lambda e: self._check_children(e, [Text], exact=True),
            "h2": lambda e: self._check_children(e, [Text], exact=True),
            "li": lambda e: self._check_children(e, [Text], exact=True),
            "th": lambda e: self._check_children(e, [Text], exact=True),
            "td": lambda e: self._check_children(e, [Text], exact=True),
            "p": lambda e: self._check_children(e, [Text], exact=True),
            "span": lambda e: self._check_children(e, [Text, P], exact=False),
            "ul": lambda e: self._check_children(e, [Li], exact=False, minimum=1),
            "ol": lambda e: self._check_children(e, [Li], exact=False, minimum=1),
            "tr": lambda e: self._check_children(e, [Th, Td], exact=False, exclusive=True),
            "table": lambda e: self._check_children(e, [Tr], exact=False),
            "hr": lambda e: len(e.content) == 0,
            "br": lambda e: len(e.content) == 0,
        }
        if isinstance(elem, Meta):
            return len(elem.content) == 0  # Validar que <meta> no tenga contenido
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


# Pruebas exhaustivas
def test():
    """
    Performs a series of exhaustive tests to validate
    the functionality of the Page class and its validation rules.
    """

    # Caso 1: Página válida con estructura básica
    page = Page(Html([
        Head([Title(Text('"Hello ground!"')), Meta({'charset': 'UTF-8'})]),
        Body([])
    ]))
    if page.is_valid():
        print('\nValid page (example)')
        print(page)
        print("-------------")

    # Caso 2: Página inválida con una etiqueta no reconocida
    page = Page(Html([
        Head([Title(Text('"Hello ground!"')), Meta({'charset': 'UTF-8'}), Elem('tortilla de patata')]),
        Body()
    ]))
    if not page.is_valid():
        print('\nInvalid page (invalid tag)')
        print(page)
        print("------------")

    # Caso 3: Página inválida sin etiquetas <head> ni <body>
    page = Page(Html([]))
    if not page.is_valid():
        print('\nInvalid page (no head or body)')
        print(page)
        print("--------------")

    # Caso 4: Página inválida sin etiqueta <head>
    page = Page(Html([Body([])]))
    if not page.is_valid():
        print('\nInvalid page (no head)')
        print(page)
        print("-------------")

    # Caso 5: Página inválida con dos etiquetas <head>
    page = Page(Html([
        Head([Title(Text('"Hello ground!"')), Meta({'charset': 'UTF-8'})]),
        Head([Title(Text('"Bye ground!"')), Meta({'charset': 'UTF-8'})]),
        Body([])
    ]))
    if not page.is_valid():
        print('\nInvalid page (two <head> tags)')
        print(page)
        print("----------------")

    # Caso 6: Página inválida sin etiquetas <title> en <head>
    page = Page(Html([
        Head([]),
        Body([])
    ]))
    if not page.is_valid():
        print('\nInvalid page (no <title> tags in <head>)')
        print(page)
        print("---------------")

    # Caso 7: Página inválida con dos etiquetas <title> en <head>
    page = Page(Html([
        Head([Title(Text('"Hello ground!"')), Title(Text('"Another title!"')), Meta({'charset': 'UTF-8'})]),
        Body([])
    ]))
    if not page.is_valid():
        print('\nInvalid page (two <title> tags)')
        print(page)
        print("-------------")

    # Caso 8: Página inválida con etiqueta <meta> dentro de <body>
    page = Page(Html([
        Head([Title(Text('"Hello ground!"'))]),
        Body([Meta({'charset': 'UTF-8'})])
    ]))
    if not page.is_valid():
        print('\nInvalid page (meta in body)')
        print(page)
        print("-----------------")

    # Caso 9: Página inválida con múltiples textos en <title>
    page = Page(Html([
        Head([Title([Text('"Hello ground!"'), Text('"Extra text"')])]),
        Body([])
    ]))
    if not page.is_valid():
        print('\nInvalid page (multiple texts in <title>)')
        print(page)
        print("-----------------")

    # Caso 10: Página inválida con etiqueta <h1> dentro de <title>
    page = Page(Html([
        Head([Title(H1(Text('"Hello ground!"')))]),
        Body([])
    ]))
    if not page.is_valid():
        print('\nInvalid page (<h1> in <title>)')
        print(page)
        print("---------------")

    # Caso 11: Página inválida con etiqueta <p> directamente dentro de <body>
    page = Page(Html([
        Head([Title(Text('"Hello ground!"'))]),
        Body([P(Text('"Not allowed here!"'))])
    ]))
    if not page.is_valid():
        print('\nInvalid page (<p> directly in <body>)')
        print(page)
        print("----------------")

    # Caso 12: Página inválida con etiqueta <h1> dentro de <p>
    page = Page(Html([
        Head([Title(Text('"Hello ground!"'))]),
        Body([P(H1(Text('"Not allowed here!"')))])
    ]))
    if not page.is_valid():
        print('\nInvalid page (<h1> inside <p>)')
        print(page)
        print("-----------------")

    # Caso 13: Página inválida con etiqueta <h1> dentro de <span>
    page = Page(Html([
        Head([Title(Text('"Hello ground!"'))]),
        Body([Span(H1(Text('"Not allowed here!"')))])
    ]))
    if not page.is_valid():
        print('\nInvalid page (<h1> inside <span>)')
        print(page)
        print("-----------------")

    # Caso 14: Página inválida con etiqueta <h1> dentro de <ul>
    page = Page(Html([
        Head([Title(Text('"Hello ground!"'))]),
        Body([Ul(H1(Text('"Not allowed here!"')))])
    ]))
    if not page.is_valid():
        print('\nInvalid page (<h1> inside <ul>)')
        print(page)
        print("------------------")

    # Caso 15: Página inválida con mezcla de <th> y <td> en <tr>
    page = Page(Html([
        Head([Title(Text('"Hello ground!"'))]),
        Body([Table([Tr([Th(Text('"Header"')), Td(Text('"Data"'))])])])
    ]))
    if not page.is_valid():
        print('\nInvalid page (mix of <th> and <td> in <tr>)')
        print(page)
        print("===========================")

    # Caso 16: Página inválida con etiqueta <h1> dentro de <table>
    page = Page(Html([
        Head([Title(Text('"Hello ground!"'))]),
        Body([Table([H1(Text('"Not allowed here!"'))])])
    ]))
    if not page.is_valid():
        print('\nInvalid page (<h1> inside <table>)')
        print(page)
        print("===================")

    # Página de ejemplo válida
    page = Page(Html([
        Head([Title(Text('"Hello ground!"'))]),
        Body([
            H1(Text('"Oh no, not again!"')),
            Hr(),
            Img({'src': 'http://i.imgur.com/pfp3T.jpg'}),
            Br(),
        ])
    ]))
    if not page.is_valid():
        print('\nValid page (example)')
        print(page)


if __name__ == '__main__':
    test()
