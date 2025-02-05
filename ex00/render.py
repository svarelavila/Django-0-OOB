import sys
import os
import settings


def render(template):
    """
    Processes a template file (.template), replacing variables
    defined in settings.py, and generates an HTML file with the
    final content.
    :param template: Name of the template file to process.
    """
    try:
        # Leer el contenido del archivo .template
        with open(template, 'r') as file:
            content = file.read()

        # Reemplazar las variables con los valores definidos en settings.py
        for key, value in vars(settings).items():
            if not key.startswith("__"):
                content = content.replace(f'{{{key}}}', str(value))

        # Crear el archivo de salida con extensión .html
        output_file = template.replace('.template', '.html')
        with open(output_file, 'w') as file:
            file.write(content)

        print(f"File successfully generated: {output_file}")

    except Exception as e:
        # Capturar y mostrar cualquier error inesperado
        print(f"Error processing the template: {e}")


def main():
    """
    Main script function.
    Ensures a template file is passed as an argument,
    validates its existence and extension, and calls the render() function.
    """
    # Validar que el usuario pase el archivo de plantilla como argumento
    if len(sys.argv) != 2:
        print("Usage: python render.py <template_file>")
        sys.exit(1)

    template = sys.argv[1]

    # Comprobar si el archivo existe
    if not os.path.isfile(template):
        print(f"Error: The file {template} does not exist.")
        sys.exit(1)

    # Comprobar si el archivo tiene la extensión correcta
    if not template.endswith('.template'):
        print("Error: The file must have a .template extension")
        sys.exit(1)

    # Procesar el archivo de plantilla
    render(template)


if __name__ == "__main__":
    main()
