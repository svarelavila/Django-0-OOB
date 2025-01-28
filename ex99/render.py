import sys
import os
import settings  # Importamos las variables del archivo settings.py


def render(template):
    try:
        # Leer el contenido del archivo .template
        with open(template, 'r') as file:
            content = file.read()  # Cargamos todo el contenido del template en una variable

        # Reemplazar las variables con los valores definidos en settings.py
        for key, value in vars(settings).items():  # Iterar sobre las variables del archivo settings.py
            if not key.startswith("__"):  # Ignorar variables internas de Python (como __name__)
                content = content.replace(f'{{{key}}}', str(value))  # Sustituir {key} por su valor

        # Crear el archivo de salida con extensión .html
        output_file = template.replace('.template', '.html')  # Cambiar la extensión a .html
        with open(output_file, 'w') as file:
            file.write(content)  # Guardar el contenido renderizado en el archivo de salida

        print(f"Archivo generado correctamente: {output_file}")

    except Exception as e:
        # Capturar y mostrar cualquier error inesperado
        print(f"Error procesando la plantilla: {e}")


def main():
    # Validar que el usuario pase el archivo de plantilla como argumento
    if len(sys.argv) != 2:
        print("Uso: python render.py <archivo.template>")
        sys.exit(1)

    template = sys.argv[1]  # Obtener el nombre del archivo pasado como argumento

    # Comprobar si el archivo existe
    if not os.path.isfile(template):
        print(f"Error: el archivo {template} no existe.")
        sys.exit(1)

    # Comprobar si el archivo tiene la extensión correcta
    if not template.endswith('.template'):
        print("Error: el archivo debe tener la extensión .template")
        sys.exit(1)

    # Procesar el archivo de plantilla
    render(template)


if __name__ == "__main__":
    main()
