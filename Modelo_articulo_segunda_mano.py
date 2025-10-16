class Articulo_segunda_mano:
    def __init__(self, clasificacion, tema, vendedor):
        self.clasificacion = clasificacion
        self.tema = tema
        self.vendedor = vendedor

if __name__ == "__main__":
    articulo_usado = Articulo_segunda_mano("Entretenimiento", "Cine", "nosequeponer")