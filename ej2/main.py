from ej2 import FabricaEdificios


class ProyectoConstruccion:
    def __init__(self):
        self.fabrica_edificios = FabricaEdificios()
        self.edificios_creados = []

    def crear_edificio(self, tipo, estilo):
        try:
            edificio = self.fabrica_edificios.crear_edificio(tipo, estilo)
            self.edificios_creados.append(edificio)
            print("\nEdificio creado exitosamente:")
            edificio.mostrar_informacion()
        except ValueError as e:
            print(f"Error al crear el edificio: {e}")

    def fase_diseno_inicial(self, edificio):
        print(f"\nDiseño Inicial para el Edificio {self.edificios_creados.index(edificio) + 1}:")
        # Restricción de Altura
        if edificio.tipo == "residencial" and edificio.estilo == "moderno":
            print("Aplicar restricciones de altura para edificios residenciales modernos...")

        # Requisitos de Eficiencia Energética
        print("Considerar requisitos de eficiencia energética para cumplir con normativas locales...")

        # Otros aspectos del diseño inicial
        print("Definir planos y especificaciones...")
        print("Consultar con arquitectos e ingenieros...")

    def fase_construccion(self, edificio):
        print(f"\nConstrucción en Progreso para el Edificio {self.edificios_creados.index(edificio) + 1}:")
        # Aquí puedes agregar lógica específica para la fase de construcción
        print("Preparar el sitio de construcción...")
        print("Ejecutar las obras según el plan...")

    def fase_mantenimiento_posterior(self, edificio):
        print(f"\nMantenimiento Posterior a la Construcción para el Edificio {self.edificios_creados.index(edificio) + 1}:")
        # Aquí puedes agregar lógica específica para la fase de mantenimiento posterior
        print("Inspeccionar y corregir posibles problemas...")
        print("Implementar mejoras según sea necesario...")

    def gestionar_proceso_construccion(self):
        for edificio in self.edificios_creados:
            self.fase_diseno_inicial(edificio)
            self.fase_construccion(edificio)
            self.fase_mantenimiento_posterior(edificio)

if __name__ == "__main__":
    proyecto = ProyectoConstruccion()

    # Crear diferentes tipos de edificios con diferentes estilos
    proyecto.crear_edificio("residencial", "moderno")
    proyecto.crear_edificio("comercial", "clásico")
    proyecto.crear_edificio("industrial", "futurista")

    # Gestionar el proceso de construcción para los edificios creados
    proyecto.gestionar_proceso_construccion()
