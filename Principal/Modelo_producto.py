class Producto:
    def __init__(self, precio, titulo, autor, editorial, anio_de_edicion, preferencias):
        self.precio = precio
        self.titulo = titulo
        self.autor = autor
        self.editorial = editorial
        self.anio_de_edicion = anio_de_edicion
        self.preferencias = preferencias
        print("\n")

    def vender(self):
        print(f"El producto '{self.titulo}' de {self.autor} ha sido vendido por la editorial '{self.editorial}'.")

    def comprar(self):
        print(f"Se ha comprado el producto '{self.titulo}' de {self.autor} por un valor de {self.precio}.")

    def ver_catalogo(self):
        print(f"Mostrando información del producto:\n"
              f"Título: '{self.titulo}'\n"
              f"Autor: {self.autor}\n"
              f"Editorial: {self.editorial}\n"
              f"Año de edición: {self.anio_de_edicion}\n"
              f"Preferencias: {self.preferencias}\n"
              f"Precio: {self.precio}")

producto1 = Producto(25000, "El Viaje del Saber", "Ana Gómez", "Editorial Random", 2023, "Educativo")
producto1.vender()
producto1.comprar()
producto1.ver_catalogo()