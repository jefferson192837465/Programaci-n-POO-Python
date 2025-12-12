class Novedades:
    def __init__(self, clasificacion, tema):
        self.clasificacion = clasificacion
        self.tema = tema
        print("\n")

    def cambiar_clasificacion(self):
        print("La clasificación de la novedad ha sido modificada exitosamente.")

novedad1 = Novedades("Científico", "Avances Tecnológicos")
novedad1.cambiar_clasificacion()