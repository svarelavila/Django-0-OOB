import sys
import os
import re


def main():
    # Validar número correcto de argumentos
    if len(sys.argv) != 2:
        print("Uso: python3 render.py <archivo.template>")
        sys.exit(1)

    input_file = sys.argv[1]

    # Validar extensión del archivo
    if not input_file.endswith('.template'):
        print("Error: La extensión del archivo debe ser .template")
        sys.exit(1)

    # Validar existencia del archivo
    if not os.path.isfile(input_file):
        print(f"Error: El archivo '{input_file}' no existe.")
        sys.exit(1)

    # Importar configuraciones desde settings.py
    try:
        import settings
    except ImportError:
        print("Error: No se encontró el archivo settings.py.")
        sys.exit(1)

    # Leer el contenido del archivo .template
    try:
        with open(input_file, 'r') as file:
            template_content = file.read()
    except Exception as e:
        print(f"Error al leer el archivo '{input_file}': {e}")
        sys.exit(1)

    # Sustituir patrones con los valores de settings.py
    try:
        for key, value in settings.__dict__.items():
            if not key.startswith("__"):
                pattern = r"\{\{" + key + r"\}\}"
                template_content = re.sub(pattern, str(value), template_content)
    except Exception as e:
        print(f"Error al procesar el archivo: {e}")
        sys.exit(1)

    # Generar el archivo de salida con extensión .html
    output_file = input_file.replace('.template', '.html')
    try:
        with open(output_file, 'w') as file:
            file.write(template_content)
        print(f"Archivo procesado correctamente: {output_file}")
    except Exception as e:
        print(f"Error al escribir el archivo '{output_file}': {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
