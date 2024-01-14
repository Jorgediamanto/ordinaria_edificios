from ej1 import FabricaEdificios

def test_fabrica_edificios():
    fabrica = FabricaEdificios()

    try:
        # Crear edificio residencial de estilo moderno
        edificio1 = fabrica.crear_edificio("residencial", "moderno")
        edificio1.mostrar_informacion()

        # Clonar edificio residencial de estilo clásico
        edificio2 = fabrica.crear_edificio("residencial", "clasico").duplica()
        print("\nEdificio clonado:")
        edificio2.mostrar_informacion()

        # Crear edificio comercial de estilo futurista
        edificio3 = fabrica.crear_edificio("comercial", "futurista")
        edificio3.mostrar_informacion()

        # Crear edificio industrial de estilo clásico
        edificio4 = fabrica.crear_edificio("industrial", "clasico")
        edificio4.mostrar_informacion()

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_fabrica_edificios()
