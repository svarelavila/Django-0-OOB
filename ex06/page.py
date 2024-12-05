from elem02 import Elem, Text
from elements import *

class Page:
    def __init__(self, root_element):
        if not isinstance(root_element, Elem):
            raise TypeError("The root element must be an instance of Elem or its derived classes.")
        self.root = root_element

    def is_valid(self):
        """
        Validate the HTML structure based on the rules provided in the exercise.
        """
        def validate_node(node):
            # Base case: Text node
            if isinstance(node, Text):
                return True

            # Valid tags
            valid_tags = {Html, Head, Body, Title, Meta, Img, Table, Th, Tr, Td,
                          Ul, Ol, Li, H1, H2, P, Div, Span, Hr, Br}

            if not isinstance(node, tuple(valid_tags)):
                return False

            # Specific rules for each tag
            if isinstance(node, Html):
                return (len(node.content) == 2 and
                        isinstance(node.content[0], Head) and
                        isinstance(node.content[1], Body))

            if isinstance(node, Head):
                return (len([child for child in node.content if isinstance(child, Title)]) == 1 and
                        all(isinstance(child, (Title, Meta)) for child in node.content))

            if isinstance(node, Body) or isinstance(node, Div):
                return all(isinstance(child, (H1, H2, Div, Table, Ul, Ol, Span, Text)) for child in node.content)

            if isinstance(node, Title) or isinstance(node, H1) or isinstance(node, H2) or isinstance(node, Li) or isinstance(node, Th) or isinstance(node, Td):
                return len(node.content) == 1 and isinstance(node.content[0], Text)

            if isinstance(node, P):
                return all(isinstance(child, Text) for child in node.content)

            if isinstance(node, Span):
                return all(isinstance(child, (Text, P)) for child in node.content)

            if isinstance(node, (Ul, Ol)):
                return len(node.content) > 0 and all(isinstance(child, Li) for child in node.content)

            if isinstance(node, Tr):
                th_count = sum(isinstance(child, Th) for child in node.content)
                td_count = sum(isinstance(child, Td) for child in node.content)
                return (th_count == 0 or td_count == 0) and th_count + td_count > 0

            if isinstance(node, Table):
                return all(isinstance(child, Tr) for child in node.content)

            return True

        # Validate the entire tree recursively
        def traverse(node):
            if not validate_node(node):
                return False
            if isinstance(node, Elem):
                return all(traverse(child) for child in node.content)
            return True

        return traverse(self.root)

    def __str__(self):
        """
        Return the HTML representation of the page.
        """
        doctype = "<!DOCTYPE html>\n" if isinstance(self.root, Html) else ""
        return f"{doctype}{self.root}"

    def write_to_file(self, filename):
        """
        Write the HTML to a file with an optional doctype.
        """
        with open(filename, 'w') as file:
            file.write(str(self))

if __name__ == '__main__':
    # Example of usage and validation
    html = Html(content=[
        Head(content=[
            Title(content=Text("Hello World")),
            Meta(attr={"charset": "UTF-8"})
        ]),
        Body(content=[
            H1(content=Text("Welcome to my page!")),
            P(content=Text("This is a paragraph.")),
            Div(content=[
                Span(content=Text("This is a span.")),
                P(content=Text("Another paragraph inside a div."))
            ]),
            Ul(content=[
                Li(content=Text("Item 1")),
                Li(content=Text("Item 2"))
            ]),
            Table(content=[
                Tr(content=[Th(content=Text("Header 1")), Th(content=Text("Header 2"))]),
                Tr(content=[Td(content=Text("Data 1")), Td(content=Text("Data 2"))])
            ])
        ])
    ])

    page = Page(html)
    print(page)
    print("Is valid:", page.is_valid())
    page.write_to_file("output.html")
