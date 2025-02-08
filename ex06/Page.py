from elem import Elem, Text
from elements import Html, Head, Body, Title, Meta, Img, Table, Th, Tr, Td, Ul, Ol, Li, H1, H2, P, Div, Span, Hr, Br


class Page:
    """
    Class representing an HTML document with structure validation.
    """

    def __init__(self, root: Elem):
        """
        Initializes the Page instance.
        :param root: The root HTML element.
        """
        if not isinstance(root, Elem):
            raise TypeError("Root must be an instance of Elem.")
        self.root = root

    def is_valid(self) -> bool:
        """
        Checks if the HTML document structure is valid.
        :return: True if valid, False otherwise.
        """
        result = isinstance(self.root, Html) and self._validate_tree(self.root)
        return result

    def _validate_tree(self, elem: Elem) -> bool:
        """
        Recursively validates the structure of the HTML tree.
        :param elem: The element to validate.
        :return: True if the element and its children are valid, False otherwise.
        """

        # Definición de funciones internas para validar cada tipo de etiquetas HTML
        def validate_html(e):
            if not self._check_children(e, [Head, Body], exact=True):
                return False
            head_count = sum(1 for child in e.content if isinstance(child, Head))
            body_count = sum(1 for child in e.content if isinstance(child, Body))
            return head_count == 1 and body_count == 1

        def validate_head(e):
            return self._check_children(e, [Title, Meta], exact=False) and sum(
                1 for child in e.content if isinstance(child, Title)) == 1

        def validate_body(e):
            return self._check_children(e, [H1, H2, Div, Table, Ul, Ol, Span, P, Text, Hr, Br, Img], exact=False)

        def validate_div(e):
            return self._check_children(e, [H1, H2, Div, Table, Ul, Ol, Span, P, Text], exact=False)

        def validate_text_only(e):
            return self._check_children(e, [Text], exact=True)

        def validate_span(e):
            return self._check_children(e, [Text, P], exact=False)

        def validate_list(e):
            return self._check_children(e, [Li], exact=False, minimum=1)

        def validate_tr(e):
            return self._check_children(e, [Th, Td], exact=False, exclusive=True)

        def validate_table(e):
            return self._check_children(e, [Tr], exact=False)

        def validate_img(e):
            return self._check_children(e, [], exact=True)

        def validate_empty(e):
            return len(e.content) == 0

        # Diccionario que asocia etiquetas con sus funciones de validación
        rules = {
            "html": validate_html,
            "head": validate_head,
            "body": validate_body,
            "div": validate_div,
            "title": validate_text_only,
            "h1": validate_text_only,
            "h2": validate_text_only,
            "li": validate_text_only,
            "th": validate_text_only,
            "td": validate_text_only,
            "p": validate_text_only,
            "span": validate_span,
            "ul": validate_list,
            "ol": validate_list,
            "tr": validate_tr,
            "table": validate_table,
            "hr": validate_empty,
            "br": validate_empty,
            "meta": validate_empty,
            "img": validate_img
        }

        if elem.tag not in rules:
            return False

        if not rules[elem.tag](elem):
            return False

        for child in elem.content:
            if isinstance(child, Elem):
                print(f"  ├── Validating child <{child.tag}> of <{elem.tag}>...")
                if not self._validate_tree(child):
                    print(f"Validation failed: Child <{child.tag}> of <{elem.tag}> is invalid")
                    return False
        return True

    def _check_children(self, elem, allowed, exact=False, exclusive=False, minimum=0):
        """
        Validates the children of an element based on allowed types and constraints.
        :param elem: The element whose children are being validated.
        :param allowed: List of allowed child element types.
        :param exact: If True, only allowed elements are permitted.
        :param exclusive: If True, all children must be of the same type.
        :param minimum: Minimum number of required children.
        :return: True if children are valid, False otherwise.
        """
        if len(elem.content) < minimum:
            return False
        if exclusive and len(set(type(child) for child in elem.content if isinstance(child, Elem))) > 1:
            return False
        return all(
            isinstance(child, (Elem, Text)) and (not isinstance(child, Elem) or type(child) in allowed)
            for child in elem.content
        )

    def __str__(self) -> str:
        """
        Returns the string representation of the HTML document.
        :return: String representation of the HTML page.
        """
        return f"<!DOCTYPE html>\n{self.root}" if isinstance(self.root, Html) else str(self.root)

    def write_to_file(self, filename: str):
        """
        Writes the HTML content to a file.
        :param filename: The name of the file to write to.
        """
        with open(filename, "w") as file:
            file.write(str(self))


def test():
    """
    Runs a minimal but complete set of tests to validate the Page class.
    """
    print("\n" + "=" * 50)
    print("TESTING PAGE CLASS")
    print("=" * 50)

    # Caso 1: Página válida con estructura correcta
    print("\n" + "-" * 50)
    print("[TEST 1] Valid HTML Page (Basic Structure)")
    print("-" * 50)
    valid_page = Page(Html([
        Head(Title(Text('"Hello ground!"'))),
        Body([
            H1(Text('"Oh no, not again!"')),
            Img({'src': 'http://i.imgur.com/pfp3T.jpg'})
        ])
    ]))
    assert valid_page.is_valid(), "Test failed: Valid page should be valid."
    print("Passed: Basic structure is valid.")
    print(valid_page)

    # Caso 2: Página inválida con errores de estructura
    print("\n" + "-" * 50)
    print("[TEST 2] Invalid Page (Structural Errors)")
    print("-" * 50)
    invalid_page = Page(Html([
        Head([Title(Text("Title 1")), Title(Text("Title 2"))]),  # Duplicado <title>
        Body([Meta({'charset': 'UTF-8'})])  # <meta> dentro <body>
    ]))
    assert not invalid_page.is_valid(), "Test failed: Page with invalid structure should be rejected."
    print("Passed: Structural errors detected correctly.")
    print(invalid_page)

    # Caso 3: Página inválida con errores de jerarquía
    print("\n" + "-" * 50)
    print("[TEST 3] Invalid Page (Hierarchy Errors)")
    print("-" * 50)
    invalid_page = Page(Html([
        Head([Title(Text("Hierarchy Test"))]),
        Body([
            P([H1(Text("Wrong usage"))]),  # <h1> dentro <p>
            Table([Tr([Th(Text("Header")), Td(Text("Data"))])]),  # Mezcla <th> and <td>
            Ul([])  # Vacio <ul> (debe tener al menos un <li>)
        ])
    ]))
    assert not invalid_page.is_valid(), "Test failed: Page with invalid hierarchy should be rejected."
    print("Passed: Hierarchy errors detected correctly.")
    print(invalid_page)

    # Generación de archivos HTML (válido e inválido)
    print("\n" + "-" * 50)
    print("[GENERATING HTML FILES]")
    print("-" * 50)
    valid_page.write_to_file("valid_page.html")
    invalid_page.write_to_file("invalid_page.html")
    print("HTML files generated successfully.")


if __name__ == "__main__":
    test()
