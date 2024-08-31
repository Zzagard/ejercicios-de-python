productos = input("Por favor, introduce los productos de tu cesta de la compra, separados por comas: ")

lista_productos = productos.split(',')

for producto in lista_productos:
    print(producto.strip())
