# Importar módulos necesarios
import sys
from io import StringIO

# Función para compilar y ejecutar el código Python
def compile_and_execute(code):
    # Redirigir la salida estándar para capturarla en una cadena
    sys.stdout = StringIO()
    
    try:
        # Ejecutar el código Python
        exec(code)
        # Capturar la salida
        output = sys.stdout.getvalue()
    except Exception as e:
        # En caso de error, capturar el mensaje de error
        output = str(e)
    finally:
        # Restaurar la salida estándar
        sys.stdout = sys.__stdout__
    
    return output

# Ejemplo de uso:
if __name__ == "__main__":
    # Código de prueba
    code = """
    print("Hola, mundo!")
    x = 10
    y = 20
    suma = x + y
    print("La suma de x y y es:", suma)
    """
    
    # Compilar y ejecutar el código
    result = compile_and_execute(code)
    print(result)
