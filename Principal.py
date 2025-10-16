from Modelo_editorial import Editorial
from Modelo_hilo import Hilo
from Modelo_indexador import Indexador
from Modelo_novedades import Novedades
from Modelo_procesador import Procesador
from Modelo_producto import Producto
from Modelo_recolector import Recolector
from Modelo_revista import Revista
from Modelo_servidor import Servidor
from Modelo_Usuario import Usuario
from Modelo_libro import Libro
from Modelo_articulo_segunda_mano import Articulo_segunda_mano
from Modelo_articulo_online import Articulo_online


if __name__ == "__main__":
    usuario = Usuario("Jean", "Carlos", "carlosp123", "La Pastora", "Jean_carlos", "no se que poner")
    usuario.enviar_sugerencia()
    usuario.leer()
    usuario.comprar()
    usuario.vender()
    usuario.realizar_reclamacion()

if __name__ == "__main__":
    servidor = Servidor()
    servidor.muestra_pagina()
    servidor.envia_sugerencia()
    servidor.envia_datos_de_compra()
    servidor.envia_datos_de_venta()

if __name__ == "__main__":
    procesador = Procesador()
    procesador.mandar_datos_de_venta()
    procesador.mandar_articulo_online()
    procesador.envia_sugerencia_administrador()
    procesador.modificar_stock()
    procesador.realizar_cobro()
    procesador.realizar_pago()
    procesador.actualiza_catalogo()
    procesador.realiza_busqueda()

if __name__ == "__main__":
    recolector = Recolector()
    recolector.envia_novedades()

if __name__ == "__main__":
    editorial1 = Editorial("No se", "Av. 7 Cll 51", "173427498728")
    editorial1.vender()

if __name__ == "__main__":
    hilo1 = Hilo()
    hilo1.busca_novedades()

if __name__ == "__main__":
    indexador1 = Indexador()
    indexador1.actualiza_almacen()
    indexador1.envia_resultado_busqueda()

if __name__ == "__main__":
    producto1 = Producto(25000, "El Viaje del Saber", "Ana Gómez", "Editorial Random", 2023, "Educativo")
    producto1.vender()
    producto1.comprar()
    producto1.ver_catalogo()

if __name__ == "__main__":
    libro_genero = Libro("IT")

if __name__ == "__main__":
    revista_categoria = Revista("Deportes extremos")

if __name__ == "__main__":
    articulo_usado = Articulo_segunda_mano("Entretenimiento", "Cine", "nosequeponer")

if __name__ == "__main__":
    novedad1 = Novedades("Científico", "Avances Tecnológicos")
    novedad1.cambiar_clasificacion()

if __name__ == "__main__":
    articulo_online = Articulo_online("Historia Universal")
    articulo_online.publicar()