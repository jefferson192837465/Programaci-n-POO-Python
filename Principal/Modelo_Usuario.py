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

usuario = Usuario("Jean", "Carlos", "carlosp123", "La Pastora", "Yan_carlos", "no_se_que_poner")
usuario.enviar_sugerencia()
usuario.leer()
usuario.comprar()
usuario.vender()
usuario.realizar_reclamacion()