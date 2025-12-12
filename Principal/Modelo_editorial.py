class Editorial:
    def __init__(self, nombre, direccion, telefono):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        print("\n")

    def vender(self):
        print("La editorial ha realizado la venta de uno de sus productos.")

editorial1 = Editorial("Editorial random", "Av. 7 Cll 51", "173427498728")
editorial1.vender()