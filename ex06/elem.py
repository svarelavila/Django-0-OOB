class Text(str):
    """
    Clase para manejar texto dentro de elementos HTML.
    """

    def __str__(self):
        text = super().__str__()
        text = text.replace('&', '&amp;')
        text = text.replace('<', '&lt;')
        text = text.replace('>', '&gt;')
        #text = text.replace('"', '&quot;')
        text = text.replace('\n', '\n<br />\n')
        return text


class Elem:
    """
    Clase para representar elementos HTML.
    """

    class ValidationError(Exception):
        """
        Excepción personalizada para errores de validación en Elem.
        """
        def __init__(self, message="Contenido inválido."):
            super().__init__(message)

    def __init__(self, tag='div', attr=None, content=None, tag_type='double'):
        if attr is None:
            attr = {}
        self.tag = tag
        self.attr = attr
        self.tag_type = tag_type

        if tag_type not in ['double', 'simple']:
            raise Elem.ValidationError("Tipo de etiqueta inválido.")

        self.content = []
        if content is not None:
            self.add_content(content)

    def __str__(self):
        if self.tag_type == 'double':
            if not self.content:
                return f"<{self.tag}{self.__make_attr()}></{self.tag}>"
            return f"<{self.tag}{self.__make_attr()}>\n{self.__make_content()}\n</{self.tag}>"
        elif self.tag_type == 'simple':
            return f"<{self.tag}{self.__make_attr()} />"

    def __make_attr(self):
        result = ''
        for key, value in sorted(self.attr.items()):
            result += f' {key}="{value}"'
        return result

    def __make_content(self):
        """
        Genera el contenido del elemento, incluyendo elementos anidados con la indentación correcta.
        """
        if not self.content:
            return ''
        result = []
        for elem in self.content:
            elem_str = str(elem).strip()  # Convertimos el contenido a string y quitamos espacios
            if elem_str:  # Solo incluimos contenido no vacío
                # Añadimos indentación para cada nivel
                result.append("  " + elem_str.replace("\n", "\n  "))
        return '\n'.join(result)

    def add_content(self, content):
        if not Elem.check_type(content):
            raise Elem.ValidationError("Contenido inválido.")
        if isinstance(content, list):
            for item in content:
                if not Elem.check_type(item):
                    raise Elem.ValidationError("Contenido en lista inválido.")
                if isinstance(item, Text) and not str(item).strip():  # Ignorar textos vacíos
                    continue
                self.content.append(item)
        elif isinstance(content, Text) and not str(content).strip():  # Ignorar textos vacíos
            return
        else:
            self.content.append(content)

    @staticmethod
    def check_type(content):
        return isinstance(content, (Elem, Text)) or (
            isinstance(content, list) and all(isinstance(item, (Elem, Text)) for item in content)
        )


# Prueba para generar HTML
def generate_html():
    html = Elem('html', content=[
        Elem('head', content=Elem('title', content=Text('"Hello ground!"'))),
        Elem('body', content=[
            Elem('h1', content=Text('"Oh no, not again!"')),
            Elem('img', attr={'src': 'http://i.imgur.com/pfp3T.jpg'}, tag_type='simple')
        ])
    ])
    print(html)


if __name__ == '__main__':
    generate_html()
