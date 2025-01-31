class Text(str):
    """
    Class to handle text within HTML elements, ensuring proper escaping.
    """
    def __str__(self):
        # Reemplaza caracteres especiales con sus entidades HTML correspondientes
        text = super().__str__()
        text = text.replace('&', '&amp;')
        text = text.replace('<', '&lt;')
        text = text.replace('>', '&gt;')
        text = text.replace('"', '&quot;')
        text = text.replace('\n', '\n<br />\n')
        return text


class Elem:
    """
    Class to represent HTML elements.
    """

    class ValidationError(Exception):
        """
        Custom exception for validation errors in Elem.
        """
        pass

    def __init__(self, tag="div", attr=None, content=None, tag_type="double"):
        if attr is None:
            attr = {}
        self.tag = tag # Nombre de la etiqueta HTML
        self.attr = attr # Atribuos de la etiqueta HTML
        self.tag_type = tag_type # Tipo de etiqueta: doble o simple

        # Verifica que el tipo de etiqueta sea válido
        if tag_type not in ["double", "simple"]:
            raise Elem.ValidationError("Invalid tag type.")

        self.content = [] # Inicializa la lista de contenido
        if content is not None:
            self.add_content(content) # Agrega contenido si es proporcionado

    def __str__(self):
        """
        Generates the HTML representation of the element.
        """
        if self.tag_type == "double":
            # Si el elemento no tiene contenido, devueve una etiqueta vacía <tag></tag>
            if not self.content:
                return f"<{self.tag}{self.__make_attr()}></{self.tag}>"
            # Si tiene contenido, genera la etiquela con su contenido anidado
            return f"<{self.tag}{self.__make_attr()}>{self.__make_content()}</{self.tag}>"
        elif self.tag_type == "simple":
            # Si es un elemento de tipo "simple" (ej. <img />, <meta />), se cierra automáticamente
            return f"<{self.tag}{self.__make_attr()} />"

    def __make_attr(self):
        """
        Generates the attribute string for the HTML element.
        """
        result = "" # Inicializa una cadena vacía para almacenar los atributos
        
        # itera sobre los atributos ordenados por clave
        for key, value in sorted(self.attr.items()):
            # Agrega el atributo en formato key="value" a la cadena resultante
            result += f' {key}="{value}"'
        return result # Retorna la cadena con los atributos formateados

    def __make_content(self):
        """
        Generates the content of the element, including nested elements,
        ensuring proper indentation and formatting.
        """
        if not self.content:
            return ""
        result = []
        for elem in self.content:
            elem_str = str(elem).strip() # Convierte el contenido a string y elimina espacios en blanco.
            if elem_str: # Verifica que el contenido no esté vacío.
                # Agrega indentación y reemplaza &quot; por comillas dobles.
                indented_content = "  " + elem_str.replace("\n", "\n  ").replace("&quot;", '"')
                result.append(indented_content)
        
        # Retorna el contenido formateado con saltos de línea antes y después.
        return "\n" + "\n".join(result) + "\n"

    def add_content(self, content):
        """
        Adds content to the element, ensuring it follows validation rules.
        """
        # Verifica si el contenido es válido según la función estática check_type().
        if not Elem.check_type(content):
            raise Elem.ValidationError("Invalid content.")  # Lanza una excepción si el contenido no es válido.
        
        # Si el contenido es una lista, se procesa cada elemento individualmente.
        if isinstance(content, list):
            for item in content:
                if not Elem.check_type(item):
                    raise Elem.ValidationError("Invalid content in list.")
                if isinstance(item, Text) and not str(item).strip(): # Ignora cadenas vacías.
                    continue
                self.content.append(item)
        
        # Si el contenido es una instancia de Text y está vacío, se ignora.
        elif isinstance(content, Text) and not str(content).strip():
            return
        
        # Si el contenido no es una lista, ni un texto vacío, se agrega directamente.
        else:
            self.content.append(content) # Agrega el elemento válido a la lista de contenido.

    @staticmethod
    def check_type(content):
        """
        Validates that the content is an instance of Elem, Text,
        or a valid list of both.
        """
        return isinstance(content, (Elem, Text)) or (
            isinstance(content, list) and all(isinstance(item, (Elem, Text)) for item in content)
        )


# Function to generate an HTML structure for testing

def generate_html():
    """
    Generates a sample HTML document structure and prints it.
    """
    html = Elem("html", content=[
        Elem("head", content=[
            Elem("title", content=Text('"Hello ground!"')),
            ]),
        Elem("body", content=[
            Elem("h1", content=Text('"Oh no, not again!"')),
            Elem("img", attr={"src": "http://i.imgur.com/pfp3T.jpg"}, tag_type="simple")
        ])
    ])
    print(html)
    

if __name__ == "__main__":
    generate_html()
