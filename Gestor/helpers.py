import os
import platform
import re


def limpiar_pantalla():
    """
    Esta función limpia la pantalla de la consola.

    Utiliza los módulos 'os' y 'platform' para determinar el sistema operativo actual
    y ejecuta el comando adecuado para limpiar la pantalla de la consola.
    Si el sistema operativo es Windows, emplea el comando 'cls' para limpiar la pantalla.
    De lo contrario, usa el comando 'clear'.

    Argumentos:
    Ninguno.

    Retorna:
    Ninguno.
    """
    os.system('cls') if platform.system() == "Windows" else os.system('clear')


def leer_texto(longitud_min=0, longitud_max=100, mensaje=None):
    """
    Esta función lee una cadena de texto ingresada por el usuario desde la entrada estándar (consola). La función
    válida que la longitud del texto esté dentro del rango longitud_min y longitud_max. Si el texto ingresado es
    demasiado corto o demasiado largo, se le solicita al usuario que ingrese una cadena de texto válida. También se
    puede proporcionar un mensaje opcional para ser mostrado al usuario antes de la entrada.

    Argumentos:

    longitud_min (int, opcional): Longitud mínima permitida para el texto ingresado. Por defecto, es 0.
    longitud_max (int, opcional): Longitud máxima permitida para el texto ingresado. Por defecto, es 100.
    mensaje (str, opcional): Mensaje a mostrar al usuario antes de que ingrese el texto. Por defecto, es None.

    Retorna:

    Una cadena de texto con la entrada del usuario.
    """
    while True:
        texto = input(mensaje)
        if len(texto) < longitud_min:
            print(f"El texto debe tener al menos {longitud_min} caracteres.")
        elif len(texto) > longitud_max:
            print(f"El texto debe tener como máximo {longitud_max} caracteres.")
        else:
            return texto


def curp_valido(curp, lista):
    """
    Esta función toma una cadena de texto que representa una CURP y valida si cumple con las reglas de formato de
    una CURP en México. Si la CURP es válida, la función devuelve un mensaje indicando que la CURP es correcta.
    Si la CURP es inválida, la función devuelve un mensaje indicando el problema con la CURP.

    Argumentos:

    curp (str): La cadena de texto que representa la CURP a validar.

    Retorna:

    Un mensaje indicando si la CURP es válida o no. Si la CURP es válida, el mensaje es "CURP correcta". Si la CURP
    es inválida, el mensaje describe el problema con la CURP.
    """
    for cliente in lista:
        if cliente.curp == curp:
            return False, "La CURP ingresada ya ha sido utilizada por otro cliente."
    if len(curp) != 15:
        return False, "El CURP debe tener 15 caracteres."
    if not curp[0].isupper():
        return False, "La primera letra del CURP debe ser mayúscula."
    if curp[1] not in ['A', 'E', 'I', 'O', 'U']:
        return False, "La segunda letra del CURP debe ser una vocal."
    if not curp[2:4].isupper():
        return False, "Las letras 3 y 4 de la CURP deben ser mayúsculas."
    if not curp[4:10].isdigit():
        return False, "Los siguientes 6 caracteres deben ser dígitos numéricos."
    if curp[10] not in ['H', 'M']:
        return False, "La CURP debe tener una letra H o M después de los primeros 6 dígitos numéricos."
    entidades_federativas = ['AS', 'BC', 'BS', 'CC', 'CL', 'CM', 'CS', 'DF', 'DG', 'GR', 'GT', 'HG', 'JC', 'MC', 'MN',
                             'MS', 'NE', 'NL', 'NT', 'OC', 'PL', 'QR', 'QT', 'SP', 'SL', 'SR', 'TC', 'TL', 'TS', 'VZ',
                             'YN', 'ZS']
    if curp[11:13] not in entidades_federativas:
        return False, "Las letras 12 y 13 de la CURP no corresponden a una entidad federativa válida."
    if not curp[12:16].isalnum():
        return False, "Los dos últimos caracteres de la CURP deben ser letras mayúsculas o dígitos numéricos."
    return True, "Registro de CURP correcto"  # Validación exitosa


def curp_valido_api(curp, lista):
    """
      Esta función toma una cadena de texto que representa una CURP y valida si cumple con las reglas de formato de
      una CURP en México. Si la CURP es válida, la función devuelve un mensaje indicando que la CURP es correcta.
      Si la CURP es inválida, la función devuelve un mensaje indicando el problema con la CURP. Esta función se utiliza
      para la comprobación de la api

      Argumentos:

      curp (str): La cadena de texto que representa la CURP a validar.

      Retorna:

      Un mensaje indicando si la CURP es válida o no. Si la CURP es válida, el mensaje es "CURP correcta". Si la CURP
      es inválida, el mensaje describe el problema con la CURP.
      """
    for cliente in lista:
        if cliente.curp == curp:
            return "La CURP ingresada ya ha sido utilizada por otro cliente."
    if len(curp) != 15:
        return "El CURP debe tener 15 caracteres."
    if not curp[0].isupper():
        return "La primera letra del CURP debe ser mayúscula."
    if curp[1] not in ['A', 'E', 'I', 'O', 'U']:
        return "La segunda letra del CURP debe ser una vocal."
    if not curp[2:4].isupper():
        return "Las letras 3 y 4 de la CURP deben ser mayúsculas."
    if not curp[4:10].isdigit():
        return "Los siguientes 6 caracteres deben ser dígitos numéricos."
    if curp[10] not in ['H', 'M']:
        return "La CURP debe tener una letra H o M después de los primeros 6 dígitos numéricos."
    entidades_federativas = ['AS', 'BC', 'BS', 'CC', 'CL', 'CM', 'CS', 'DF', 'DG', 'GR', 'GT', 'HG', 'JC', 'MC', 'MN',
                             'MS', 'NE', 'NL', 'NT', 'OC', 'PL', 'QR', 'QT', 'SP', 'SL', 'SR', 'TC', 'TL', 'TS', 'VZ',
                             'YN', 'ZS']
    if curp[11:13] not in entidades_federativas:
        return "Las letras 12 y 13 de la CURP no corresponden a una entidad federativa válida."
    if not curp[12:16].isalnum():
        return "Los dos últimos caracteres de la CURP deben ser letras mayúsculas o dígitos numéricos."

    return None  # La CURP es válida