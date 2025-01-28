from elem import Elem, Text


# Clases estructurales
class Html(Elem):
    """Clase que representa la etiqueta <html>."""
    def __init__(self, content=None, attr=None):
        super().__init__(tag='html', attr=attr or {}, content=content, tag_type='double')


class Head(Elem):
    """Clase que representa la etiqueta <head>."""
    def __init__(self, content=None, attr=None):
        super().__init__(tag='head', attr=attr or {}, content=content, tag_type='double')


class Body(Elem):
    """Clase que representa la etiqueta <body>."""
    def __init__(self, content=None, attr=None):
        super().__init__(tag='body', attr=attr or {}, content=content, tag_type='double')


# Clases de cabecera y metaetiquetas
class Title(Elem):
    """Clase que representa la etiqueta <title>."""
    def __init__(self, content=None, attr=None):
        super().__init__(tag='title', attr=attr or {}, content=content, tag_type='double')


class Meta(Elem):
    """Clase que representa la etiqueta <meta>."""
    def __init__(self, attr=None):
        super().__init__(tag='meta', attr=attr or {}, tag_type='simple')


# Clases multimedia
class Img(Elem):
    """Clase que representa la etiqueta <img>."""
    def __init__(self, attr=None):
        super().__init__(tag='img', attr=attr or {}, tag_type='simple')


# Clases para tablas
class Table(Elem):
    """Clase que representa la etiqueta <table>."""
    def __init__(self, content=None, attr=None):
        super().__init__(tag='table', attr=attr or {}, content=content, tag_type='double')


class Th(Elem):
    """Clase que representa la etiqueta <th>."""
    def __init__(self, content=None, attr=None):
        super().__init__(tag='th', attr=attr or {}, content=content, tag_type='double')


class Tr(Elem):
    """Clase que representa la etiqueta <tr>."""
    def __init__(self, content=None, attr=None):
        super().__init__(tag='tr', attr=attr or {}, content=content, tag_type='double')


class Td(Elem):
    """Clase que representa la etiqueta <td>."""
    def __init__(self, content=None, attr=None):
        super().__init__(tag='td', attr=attr or {}, content=content, tag_type='double')


# Clases de lista
class Ul(Elem):
    """Clase que representa la etiqueta <ul>."""
    def __init__(self, content=None, attr=None):
        super().__init__(tag='ul', attr=attr or {}, content=content, tag_type='double')


class Ol(Elem):
    """Clase que representa la etiqueta <ol>."""
    def __init__(self, content=None, attr=None):
        super().__init__(tag='ol', attr=attr or {}, content=content, tag_type='double')


class Li(Elem):
    """Clase que representa la etiqueta <li>."""
    def __init__(self, content=None, attr=None):
        super().__init__(tag='li', attr=attr or {}, content=content, tag_type='double')


# Clases varias
class H1(Elem):
    """Clase que representa la etiqueta <h1>."""
    def __init__(self, content=None, attr=None):
        super().__init__(tag='h1', attr=attr or {}, content=content, tag_type='double')


class H2(Elem):
    """Clase que representa la etiqueta <h2>."""
    def __init__(self, content=None, attr=None):
        super().__init__(tag='h2', attr=attr or {}, content=content, tag_type='double')


class P(Elem):
    """Clase que representa la etiqueta <p>."""
    def __init__(self, content=None, attr=None):
        super().__init__(tag='p', attr=attr or {}, content=content, tag_type='double')


class Div(Elem):
    """Clase que representa la etiqueta <div>."""
    def __init__(self, content=None, attr=None):
        super().__init__(tag='div', attr=attr or {}, content=content, tag_type='double')


class Span(Elem):
    """Clase que representa la etiqueta <span>."""
    def __init__(self, content=None, attr=None):
        super().__init__(tag='span', attr=attr or {}, content=content, tag_type='double')


class Hr(Elem):
    """Clase que representa la etiqueta <hr>."""
    def __init__(self, attr=None):
        super().__init__(tag='hr', attr=attr or {}, tag_type='simple')


class Br(Elem):
    """Clase que representa la etiqueta <br>."""
    def __init__(self, attr=None):
        super().__init__(tag='br', attr=attr or {}, tag_type='simple')


# Test
def test():
    """Demostración del ejercicio con la estructura del Subject."""
    # Ejemplo del enunciado
    simple_html = Html(content=[
        Head(),
        Body()
    ])
    print(simple_html)
    print("-------------------------------------------")
    # Ejemplo complejo replicando el ejercicio 04
    html = Elem('html', content=[
        Elem('head', content=Elem('title', content=Text('"Hello ground!"'))),
        Elem('body', content=[
            Elem('h1', content=Text('"Oh no, not again!"')),
            Elem('img', attr={'src': 'http://i.imgur.com/pfp3T.jpg'}, tag_type='simple')
        ])
    ])
    print(html)


if __name__ == '__main__':
    test()
