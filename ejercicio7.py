correo = input("Cual es tu correo electrónico? ")

nombre_usuario = correo.split('@')[0]
nuevo_correo = f"{nombre_usuario}@ceu.es"

print(nuevo_correo)
