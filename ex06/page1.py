from elem import Elem, Text
from elements import Html, Head, Body, Title, Meta, Img, Table, Th, Tr, Td, Ul, Ol, Li, H1, H2, P, Div, Span, Hr, Br


class Page:
    """
    Class representing an HTML document with structure validation.
    """

    def __init__(self, root: Elem):
        if not isinstance(root, Elem):
            raise TypeError("Root must be an instance of Elem.")
        self.root = root

    def is_valid(self) -> bool:
        print("\n=== Running is_valid() ===")
        result = isinstance(self.root, Html) and self._validate_tree(self.root)
        print(f"Final Validation Result: {'✅ Valid' if result else '❌ Invalid'}")
        return result

    def _validate_tree(self, elem: Elem) -> bool:
        # print(f"\nValidating <{elem.tag}> with children {[child.tag for child in elem.content if isinstance(child, Elem)]}")

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
            # print(f"❌ Validation failed: Unknown tag <{elem.tag}>")
            return False

        if not rules[elem.tag](elem):
            # print(f"❌ Validation failed: Tag <{elem.tag}> did not meet its rules")
            return False

        for child in elem.content:
            if isinstance(child, Elem):
                # print(f"  ├── Validating child <{child.tag}> of <{elem.tag}>...")
                if not self._validate_tree(child):
                    # print(f"❌ Validation failed: Child <{child.tag}> of <{elem.tag}> is invalid")
                    return False
        # print(f"✅ <{elem.tag}> is valid.")
        return True

    def _check_children(self, elem, allowed, exact=False, exclusive=False, minimum=0):
        # print(f"Checking children of <{elem.tag}> → Allowed: {[t.__name__ for t in allowed]} → Current: {[child.tag for child in elem.content if isinstance(child, Elem)]}")
        if len(elem.content) < minimum:
            return False
        if exclusive and len(set(type(child) for child in elem.content if isinstance(child, Elem))) > 1:
            return False
        return all(
            isinstance(child, (Elem, Text)) and (not isinstance(child, Elem) or type(child) in allowed)
            for child in elem.content
        )

    def __str__(self) -> str:
        return f"<!DOCTYPE html>\n{self.root}" if isinstance(self.root, Html) else str(self.root)

    def write_to_file(self, filename: str):
        with open(filename, "w") as file:
            file.write(str(self))


def test():
    """
    Runs a minimal but complete set of tests to validate the Page class.
    """
    print("\n" + "=" * 50)
    print("=== TESTING PAGE CLASS ===")
    print("=" * 50)

    # Caso 1: Página válida con estructura correcta
    print("\n" + "-" * 50)
    print("[TEST 1] Valid HTML Page (Basic Structure)")
    print("-" * 50)
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
    print("\n" + "-" * 50)
    print("[TEST 2] Invalid Page (Structural Errors)")
    print("-" * 50)
    invalid_page = Page(Html([
        Head([Title(Text("Title 1")), Title(Text("Title 2"))]),  # Duplicated <title>
        Body([Meta({'charset': 'UTF-8'})])  # <meta> inside <body>
    ]))
    assert not invalid_page.is_valid(), "Test failed: Page with invalid structure should be rejected."
    print("Passed: Structural errors detected correctly.")

    # Caso 3: Página inválida con errores de jerarquía
    print("\n" + "-" * 50)
    print("[TEST 3] Invalid Page (Hierarchy Errors)")
    print("-" * 50)
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
    print("\n" + "-" * 50)
    print("[GENERATING HTML FILES]")
    print("-" * 50)
    valid_page.write_to_file("valid_page.html")
    invalid_page.write_to_file("invalid_page.html")
    print("HTML files generated successfully.")

    print("\n" + "=" * 50)
    print("========= ALL TESTS PASSED SUCCESSFULLY ==========")
    print("=" * 50)


if __name__ == "__main__":
    test()