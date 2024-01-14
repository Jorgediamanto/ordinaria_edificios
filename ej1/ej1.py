from copy import deepcopy

# Clases base para los tipos de edificios
class Edificio:
    def __init__(self, tipo, estilo):
        self.tipo = tipo
        self.estilo = estilo

    def duplica(self):
        return deepcopy(self)

    def mostrar_informacion(self):
        print(f"Tipo de edificio: {self.tipo}")
        print(f"Estilo arquitectónico: {self.estilo}")

class Residencial(Edificio):
    pass

class Comercial(Edificio):
    pass

class Industrial(Edificio):
    pass

# Clases base para los estilos arquitectónicos
class Moderno(Edificio):
    pass

class Clasico(Edificio):
    pass

class Futurista(Edificio):
    pass

# Fábrica abstracta utilizando prototipos
class FabricaEdificios:
    def __init__(self):
        self.prototipos = {
            "residencial": {
                "moderno": Residencial("residencial", "moderno"),
                "clasico": Residencial("residencial", "clasico"),
                "futurista": Residencial("residencial", "futurista"),
            },
            "comercial": {
                "moderno": Comercial("comercial", "moderno"),
                "clasico": Comercial("comercial", "clasico"),
                "futurista": Comercial("comercial", "futurista"),
            },
            "industrial": {
                "moderno": Industrial("industrial", "moderno"),
                "clasico": Industrial("industrial", "clasico"),
                "futurista": Industrial("industrial", "futurista"),
            }
        }

    def crear_edificio(self, tipo, estilo):
        if tipo not in self.prototipos or estilo not in self.prototipos[tipo]:
            raise ValueError("Tipo de edificio o estilo arquitectónico no válido.")
        return self.prototipos[tipo][estilo].duplica()
