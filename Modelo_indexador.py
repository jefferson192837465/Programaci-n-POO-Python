class Indexador:
    def __init__(self):
        print("\n")
        
    def envia_resultado_busqueda(self):
        print("El indexador ha enviado los resultados de la búsqueda al servidor.")

    def actualiza_almacen(self):
        print("El indexador ha actualizado la información del almacén.")

if __name__ == "__main__":
    indexador1 = Indexador()
    indexador1.actualiza_almacen()
    indexador1.envia_resultado_busqueda()