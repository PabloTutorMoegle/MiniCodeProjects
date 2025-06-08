# “I like turtles”
# Escribe un programa que pida al usuario ingrese su animal favorito, 
# si coloca ‘Tortuga’, ‘tortuga’, ‘TORTUGA’ o cualquier otra variante 
# de la palabra entonces mostrar en pantalla “También me gustan las tortugas”. 
# En caso contrario mostrar el mensaje “Ese animal es genial, pero prefiero las tortugas”.

def animal():
    print("Ingresa tu animal favorito")
    animal = input()
    if (animal.lowerCase() == "tortuga"):
        print("También me gustan las tortugas")
    else:
        print("Ese animal es genial, pero prefiero las tortugas")