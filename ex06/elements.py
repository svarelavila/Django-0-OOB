from elem import Elem, Text


# Clases estructurales
class Html(Elem):
    """Class representing the <html> tag."""
    def __init__(self, content=None, attr=None):
        super().__init__(
            tag='html',
            attr=attr or {},
            content=content,
            tag_type='double'
        )


class Head(Elem):
    """Class representing the <head> tag."""
    def __init__(self, content=None, attr=None):
        super().__init__(
            tag='head',
            attr=attr or {},
            content=content,
            tag_type='double'
        )


class Body(Elem):
    """Class representing the <body> tag."""
    def __init__(self, content=None, attr=None):
        super().__init__(
            tag='body',
            attr=attr or {},
            content=content,
            tag_type='double'
        )


# Clases de cabecera y metaetiquetas
class Title(Elem):
    """Class representing the <title> tag."""
    def __init__(self, content=None, attr=None):
        super().__init__(
            tag='title',
            attr=attr or {},
            content=content,
            tag_type='double'
        )


class Meta(Elem):
    """Class representing the <meta> tag."""
    def __init__(self, attr=None):
        super().__init__(tag='meta', attr=attr or {}, tag_type='simple')


# Clases multimedia
class Img(Elem):
    """Class representing the <table> tag."""
    def __init__(self, attr=None):
        super().__init__(tag='img', attr=attr or {}, tag_type='simple')


# Clases para tablas
class Table(Elem):
    """Class representing the <table> tag."""
    def __init__(self, content=None, attr=None):
        super().__init__(
            tag='table',
            attr=attr or {},
            content=content,
            tag_type='double'
        )


class Th(Elem):
    """Class representing the <th> tag."""
    def __init__(self, content=None, attr=None):
        super().__init__(
            tag='th',
            attr=attr or {},
            content=content,
            tag_type='double'
        )


class Tr(Elem):
    """Class representing the <tr> tag."""
    def __init__(self, content=None, attr=None):
        super().__init__(
            tag='tr',
            attr=attr or {},
            content=content,
            tag_type='double'
        )


class Td(Elem):
    """Class representing the <td> tag."""
    def __init__(self, content=None, attr=None):
        super().__init__(
            tag='td',
            attr=attr or {},
            content=content,
            tag_type='double'
        )


# Clases de lista
class Ul(Elem):
    """Class representing the <ul> tag."""
    def __init__(self, content=None, attr=None):
        super().__init__(
            tag='ul',
            attr=attr or {},
            content=content,
            tag_type='double'
        )


class Ol(Elem):
    """Class representing the <ol> tag."""
    def __init__(self, content=None, attr=None):
        super().__init__(
            tag='ol',
            attr=attr or {},
            content=content,
            tag_type='double'
        )


class Li(Elem):
    """Class representing the <li> tag."""
    def __init__(self, content=None, attr=None):
        super().__init__(
            tag='li',
            attr=attr or {},
            content=content,
            tag_type='double'
        )


# Clases varias
class H1(Elem):
    """Class representing the <h1> tag."""
    def __init__(self, content=None, attr=None):
        super().__init__(
            tag='h1',
            attr=attr or {},
            content=content,
            tag_type='double'
        )


class H2(Elem):
    """Class representing the <h2> tag."""
    def __init__(self, content=None, attr=None):
        super().__init__(
            tag='h2',
            attr=attr or {},
            content=content,
            tag_type='double'
        )


class P(Elem):
    """Class representing the <p> tag."""
    def __init__(self, content=None, attr=None):
        super().__init__(
            tag='p',
            attr=attr or {},
            content=content,
            tag_type='double'
        )


class Div(Elem):
    """Class representing the <div> tag."""
    def __init__(self, content=None, attr=None):
        super().__init__(
            tag='div',
            attr=attr or {},
            content=content,
            tag_type='double'
        )


class Span(Elem):
    """Class representing the <span> tag."""
    def __init__(self, content=None, attr=None):
        super().__init__(
            tag='span',
            attr=attr or {},
            content=content,
            tag_type='double'
        )


class Hr(Elem):
    """Class representing the <hr> tag."""
    def __init__(self, attr=None):
        super().__init__(tag='hr', attr=attr or {}, tag_type='simple')


class Br(Elem):
    """Class representing the <br> tag."""
    def __init__(self, attr=None):
        super().__init__(tag='br', attr=attr or {}, tag_type='simple')


# Test
def test():
    """Demonstration of the exercise with the structure from the Subject."""
    # Ejemplo del enunciado
    simple_html = Html(content=[
        Head(),
        Body()
    ])
    print(simple_html)
    print("***************************************************************")
    # Ejemplo complejo replicando el ejercicio 04
    html = Elem('html', content=[
        Elem('head', content=Elem('title', content=Text('"Hello ground!"'))),
        Elem('body', content=[
            Elem('h1', content=Text('"Oh no, not again!"')),
            Elem('img', attr={'src': 'http://i.imgur.com/pfp3T.jpg'},
                 tag_type='simple')
        ])
    ])
    print(html)


if __name__ == '__main__':
    test()
