#!/usr/bin/python3

class Text(str):
    """
    A Text class to represent a text you could use with your HTML elements.
    """

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
    Elem will permit us to represent our HTML elements.
    """

    class ValidationError(Exception):
        """
        Custom exception for invalid HTML element operations.
        """
        pass

    def __init__(self, tag='div', attr=None, content=None, tag_type='double'):
        if attr is None:
            attr = {}
        self.tag = tag
        self.attr = attr
        self.tag_type = tag_type

        if tag_type not in ['double', 'simple']:
            raise Elem.ValidationError(f"Invalid tag_type '{tag_type}'. Must be 'double' or 'simple'.")

        self.content = []
        if content:
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
        for pair in sorted(self.attr.items()):
            result += ' ' + str(pair[0]) + '="' + str(pair[1]) + '"'
        return result

    def __make_content(self):
        if not self.content:
            return ''
        result = []
        for elem in self.content:
            elem_str = str(elem).replace('\n', '\n  ')
            result.append(f"  {elem_str}")
        return '\n'.join(result)

    def add_content(self, content):
        """
        Add content to the element.
        """
        if not Elem.check_type(content):
            raise Elem.ValidationError("Invalid content type.")
        if isinstance(content, list):
            for item in content:
                if not Elem.check_type(item):
                    raise Elem.ValidationError("Invalid content in list.")
                if isinstance(item, str) and not item.strip():
                    raise Elem.ValidationError("Empty string is not allowed.")
                self.content.append(item)
        elif isinstance(content, str) and not content.strip():
            raise Elem.ValidationError("Empty string is not allowed.")
        else:
            self.content.append(content)

    @staticmethod
    def check_type(content):
        """
        Validate if the content is an instance of Elem, Text, or a valid list of these.
        """
        return (isinstance(content, Elem) or isinstance(content, Text) or
                (isinstance(content, list) and all(isinstance(elem, (Text, Elem)) for elem in content)))


if __name__ == '__main__':
    html = Elem(tag='html', content=[
        Elem(tag='head', content=Elem(tag='title', content=Text('"Hello ground!"'))),
        Elem(tag='body', content=[
            Elem(tag='h1', content=Text('"Oh no, not again!"')),
            Elem(tag='img', attr={'src': 'http://i.imgur.com/pfp3T.jpg'}, tag_type='simple')
        ])
    ])
    print(html)
