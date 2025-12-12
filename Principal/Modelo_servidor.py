class Servidor:
    def __init__(self):
        print("\n")

    def muestra_pagina(self):
        print("El servidor está mostrando la página principal al usuario.")

    def envia_sugerencia(self):
        print("El servidor ha enviado una sugerencia al procesador.")

    def envia_datos_de_compra(self):
        print("El servidor ha enviado los datos de una compra al procesador.")

    def envia_datos_de_venta(self):
        print("El servidor ha enviado los datos de una venta al procesador.")

servidor = Servidor()
servidor.muestra_pagina()
servidor.envia_sugerencia()
servidor.envia_datos_de_compra()
servidor.envia_datos_de_venta()