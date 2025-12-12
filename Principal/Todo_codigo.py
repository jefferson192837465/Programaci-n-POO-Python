class Usuario:
    def __init__(self, nombre, apellido, cuenta, direccion, login, password):
        self.nombre = nombre
        self.apellido = apellido
        self.cuenta = cuenta
        self.direccion = direccion
        self.login = login
        self.password = password

    def enviar_sugerencia(self):
        print("Jean carlos ha enviado una sugerencia al sistema.")

    def leer(self):
        print("Jean carlos está leyendo un artículo o producto en la plataforma.")

    def comprar(self):
        print("Jean carlos ha realizado una compra exitosamente.")

    def vender(self):
        print("Jean carlos ha puesto un producto en venta.")

    def realizar_reclamacion(self):
        print("Jean carlos ha realizado una reclamación sobre un producto o servicio.")

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


class Procesador:
    def __init__(self):
        print("\n")

    def mandar_datos_de_venta(self):
        print("El procesador ha mandado los datos de la venta al recolector.")

    def mandar_articulo_online(self):
        print("El procesador ha mandado el artículo online al recolector.")

    def envia_sugerencia_administrador(self):
        print("El procesador ha enviado una sugerencia al administrador.")

    def modificar_stock(self):
        print("El procesador ha modificado el stock de un producto.")

    def realizar_cobro(self):
        print("El procesador ha realizado el cobro de una compra.")

    def realizar_pago(self):
        print("El procesador ha realizado el pago a un vendedor.")

    def actualiza_catalogo(self):
        print("El procesador ha actualizado el catálogo de productos.")

    def realiza_busqueda(self):
        print("El procesador ha realizado una búsqueda en el catálogo.")

class Recolector:
    def __init__(self):
        print("\n")

    def envia_novedades(self):
        print("El recolector ha enviado las novedades al procesador para su actualización.")

class Editorial:
    def __init__(self, nombre, direccion, telefono):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        print("\n")

    def vender(self):
        print("La editorial ha realizado la venta de uno de sus productos.")

class Hilo:
    def __init__(self):
        print("\n")

    def busca_novedades(self):
        print("El hilo está buscando novedades en el sistema.")

class Indexador:
    def __init__(self):
        print("\n")
        
    def envia_resultado_busqueda(self):
        print("El indexador ha enviado los resultados de la búsqueda al servidor.")

    def actualiza_almacen(self):
        print("El indexador ha actualizado la información del almacén.")

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

class Libro:
    def __init__(self, genero):
        self.genero = genero

class Revista:
    def __init__(self, categoria):
        self.categoria = categoria

class Articulo_segunda_mano:
    def __init__(self, clasificacion, tema, vendedor):
        self.clasificacion = clasificacion
        self.tema = tema
        self.vendedor = vendedor

class Novedades:
    def __init__(self, clasificacion, tema):
        self.clasificacion = clasificacion
        self.tema = tema
        print("\n")

    def cambiar_clasificacion(self):
        print("La clasificación de la novedad ha sido modificada exitosamente.")

class Articulo_online:
    def __init__(self, tema):
        self.tema = tema
        print("\n")

    def publicar(self):
        print(f"El artículo en línea {self.tema} ha sido publicado correctamente.")

# ----------------------------CODIGO PRINCIPAL----------------------------
    usuario = Usuario("Jean", "Carlos", "carlosp123", "La Pastora", "Jean_carlos", "no se que poner")
    usuario.enviar_sugerencia()
    usuario.leer()
    usuario.comprar()
    usuario.vender()
    usuario.realizar_reclamacion()

    servidor = Servidor()
    servidor.muestra_pagina()
    servidor.envia_sugerencia()
    servidor.envia_datos_de_compra()
    servidor.envia_datos_de_venta()

    procesador = Procesador()
    procesador.mandar_datos_de_venta()
    procesador.mandar_articulo_online()
    procesador.envia_sugerencia_administrador()
    procesador.modificar_stock()
    procesador.realizar_cobro()
    procesador.realizar_pago()
    procesador.actualiza_catalogo()
    procesador.realiza_busqueda()

    recolector = Recolector()
    recolector.envia_novedades()

    editorial1 = Editorial("No se", "Av. 7 Cll 51", "173427498728")
    editorial1.vender()

    hilo1 = Hilo()
    hilo1.busca_novedades()

    indexador1 = Indexador()
    indexador1.actualiza_almacen()
    indexador1.envia_resultado_busqueda()

    producto1 = Producto(25000, "El Viaje del Saber", "Ana Gómez", "Editorial Random", 2023, "Educativo")
    producto1.vender()
    producto1.comprar()
    producto1.ver_catalogo()

    libro_genero = Libro("IT")

    revista_categoria = Revista("Deportes extremos")

    articulo_usado = Articulo_segunda_mano("Entretenimiento", "Cine", "nosequeponer")

    novedad1 = Novedades("Científico", "Avances Tecnológicos")
    novedad1.cambiar_clasificacion()

articulo_online = Articulo_online("Historia Universal")
articulo_online.publicar()