class Text(str):
    """Converts a text string into HTML by replacing each character with its HTML equivalent"""
    def __str__(self):
        text = super().__str__()
        text = text.replace('&', '&amp;')
        text = text.replace('<', '&lt;')
        text = text.replace('>', '&gt;')
        text = text.replace('"', '&quot;')
        text = text.replace('\n', '\n<br />\n')
        return text

class Elem:
    """
    HTML elements representation.
    """
    class ValidationError(Exception):
        def __init__(self) -> None:
            super().__init__("Incorrect behaviour")

    def __init__(self, tag='div', attr={}, content=None, tag_type='double'):
        """
        Initializes the element with tag name, attributes, content and tag type.
        """
        self.tag = tag
        self.attr = attr
        self.content = []
        if not (self.check_type(content) or content is None):
            raise self.ValidationError
        if type(content) == list:
            self.add_content(content)
        elif content is not None:
            self.add_content(content)
        if (tag_type != 'double' and tag_type != 'simple'):
            raise self.ValidationError
        self.tag_type = tag_type

    def __str__(self):
        """
        The __str__() method returns HTML representation

        Make sure it renders everything (tag, attributes, embedded
        elements...).
        """
        attr = self.__make_attr()
        result = "<{tag}{attr}".format(tag=self.tag, attr=attr)
        if self.tag_type == 'double':
            result += ">{content}</{tag}>".format(
                content=self.__make_content(), tag=self.tag)
        elif self.tag_type == 'simple':
            result += " />"
        return result

    def __make_attr(self):
        """
        Here is a function to render our elements attributes.
        """
        result = ''
        for pair in sorted(self.attr.items()):
            result += ' ' + str(pair[0]) + '="' + str(pair[1]) + '"'
        return result

    def __make_content(self):
        """
        Here is a method to render the content, including embedded elements.
        """
        if len(self.content) == 0:
            return ""
        result = "\n"
        for elem in self.content:
            # Convert content to string and replace &quot; back to "
            if isinstance(elem, Text):
                if elem:  # Check if Text is not empty
                    result += "{elem}\n".format(elem=str(elem).replace('&quot;', '"'))
            else:
                result += "{elem}\n".format(elem=elem)
        result = "  ".join(line for line in result.splitlines(True))
        if len(result.strip()) == 0:
            return ''
        return result

    def add_content(self, content):
        if not Elem.check_type(content):
            raise Elem.ValidationError
        if type(content) == list:
            self.content += [elem for elem in content if isinstance(elem, Elem) or (isinstance(elem, Text) and elem)]
        elif isinstance(content, Elem) or (isinstance(content, Text) and content):
            self.content.append(content)

    @staticmethod
    def check_type(content):
        return (isinstance(content, Elem) or isinstance(content, Text) or
                (type(content) == list and all([isinstance(elem, Text) or
                                                isinstance(elem, Elem)
                                                for elem in content])))


# Prueba para generar el HTML solicitado
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
