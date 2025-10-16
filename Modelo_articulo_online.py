class Articulo_online:
    def __init__(self, tema):
        self.tema = tema
        print("\n")

    def publicar(self):
        print("El artículo en línea ha sido publicado correctamente.")

if __name__ == "__main__":
    articulo_online = Articulo_online("Historia Universal")
    articulo_online.publicar()