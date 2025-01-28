import sys
import os
import settings


def render(template):
    """
    Procesa el archivo .template y genera un archivo .html.
    :param template: Nombre del archivo .template a procesar.
    """
    try:
        # Leer el contenido del archivo .template
        with open(template, 'r') as f:
            content = f.read()

        # Reemplazar los patrones {key} con los valores de settings.py
        for key, value in vars(settings).items():
            if not key.startswith("__"):  # Ignorar variables internas
                content = content.replace(f'{{{key}}}', str(value))

        # Escribir el contenido procesado en el archivo .html
        output_file = template.replace('.template', '.html')
        with open(output_file, 'w') as output:
            output.write(content)
        print(f"Archivo procesado correctamente: {output_file}")
    except Exception as e:
        print(f"Error al procesar la plantilla: {e}")


def valid_file(file):
    """
    Verifica si el archivo existe y tiene la extensión correcta.
    :param file: Nombre del archivo a validar.
    :return: True si es válido, False si no lo es.
    """
    if not file.endswith('.template'):
        print(f"Error: {file} no tiene la extensión .template")
        return False
    if not os.path.isfile(file):
        print(f"Error: El archivo {file} no existe")
        return False
    return True


def valid_imput():
    """
    Valida los argumentos de entrada.
    :return: True si los argumentos son válidos, False si no lo son.
    """
    if len(sys.argv) != 2:
        print("Error: Número inválido de argumentos.")
        print("Uso: python render.py <archivo>.template")
        return False

    file = sys.argv[1]
    return valid_file(file)


def main():
    """
    Punto de entrada del programa.
    """
    if not valid_imput():
        sys.exit(1)

    try:
        render(sys.argv[1])
    except Exception as e:
        print(f"Error inesperado: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
