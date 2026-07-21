import string
import random

def mostrar_titulo():
    print("=== PASSWORD GENERATOR ===")


def opcion_caracteres():
    caracteres = string.ascii_lowercase
    caracteres += string.ascii_uppercase
    caracteres += string.digits
    caracteres += string.punctuation
    return caracteres

def generar_password(caracteres):
    
    return ''.join(random.choice(caracteres) for _ in range(12))

def main():
    opciones = opcion_caracteres()
    password = generar_password(opciones)
    print(f"Tu contraseña es: {password}")

mostrar_titulo()
main()
mostrar_titulo()


