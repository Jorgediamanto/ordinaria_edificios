from ej1 import FabricaEdificios

def main():
    fabrica = FabricaEdificios()
    edificios_creados = []

    while True:
        tipo_edificio = input("Selecciona el tipo de edificio (residencial, comercial, industrial): ")
        estilo_arquitectonico = input("Selecciona el estilo arquitectónico (moderno, clásico, futurista): ")

        try:
            edificio = fabrica.crear_edificio(tipo_edificio, estilo_arquitectonico)
            edificio.mostrar_informacion()

            while True:
                opcion_clonar = input("¿Deseas clonar el edificio? (s/n): ").lower()
                if opcion_clonar == 's':
                    edificio_clonado = edificio.duplica()
                    print("\nEdificio clonado:")
                    edificio_clonado.mostrar_informacion()
                    edificios_creados.extend([edificio, edificio_clonado])
                    break
                elif opcion_clonar == 'n':
                    edificios_creados.append(edificio)
                    break
                else:
                    print("Respuesta no válida. Por favor, ingresa 's' para sí o 'n' para no.")

            opcion_otro_edificio = input("¿Deseas crear otro edificio? (s/n): ").lower()
            if opcion_otro_edificio != 's':
                break

        except ValueError as e:
            print(f"Error: {e}")

    print("\nEdificios creados:")
    for i, edificio in enumerate(edificios_creados, start=1):
        print(f"\nEdificio {i}:")
        edificio.mostrar_informacion()

if __name__ == "__main__":
    main()
