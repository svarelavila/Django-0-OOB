from elem import Elem, Text
from elements import Html, Head, Body, Title, Meta, Img, Table, Th, Tr, Td, Ul, Ol, Li, H1, H2, P, Div, Span, Hr, Br


class Page:
    """
    Clase que representa un documento HTML con validación de estructura.
    """

    def __init__(self, root: Elem):
        """
        Constructor que toma como raíz un elemento HTML.
        
        :param root: Instancia de Elem que representa el elemento raíz.
        """
        if not isinstance(root, Elem):
            raise TypeError("Root must be an instance of Elem.")
        self.root = root

    def is_valid(self) -> bool:
        """
        Valida si la estructura del árbol HTML cumple con las reglas definidas.
        """
        if not isinstance(self.root, Html):
            return False  # El elemento raíz debe ser <html>
        return self._validate_tree(self.root)

    def _validate_tree(self, elem: Elem) -> bool:
        """
        Valida recursivamente el árbol HTML a partir de un elemento.
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
        Devuelve el HTML como una cadena, incluyendo <!DOCTYPE html> si es necesario.
        """
        if isinstance(self.root, Html):
            return f"<!DOCTYPE html>\n{self.root}"
        return str(self.root)

    def write_to_file(self, filename: str):
        """
        Escribe el HTML en un archivo.
        
        :param filename: Nombre del archivo.
        """
        with open(filename, "w") as file:
            file.write(str(self))


# Pruebas exhaustivas
def test():
    """
    Realiza una serie de pruebas exhaustivas para validar la funcionalidad de la clase Page y sus reglas de validación.
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


def main():
    """
    Ejecuta las pruebas exhaustivas y muestra resultados adicionales.
    """
    test()

    # Página de ejemplo válida
    page = Page(Html([
        Head([Title(Text('"Hello ground!"'))]),
        Body([
            H1(Text('"Oh no, not again!"')),
            Img({'src': 'http://i.imgur.com/pfp3T.jpg'})
        ])
    ]))
    print(page)
    print("Is valid:", page.is_valid())
    page.write_to_file("output_valid.html")


if __name__ == '__main__':
    main()
