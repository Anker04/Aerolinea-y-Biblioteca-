class Avion:
    def __init__(self, modelo, num_asientos):
        self.modelo = modelo
        self.num_asientos = num_asientos

class Vuelo:
    def __init__(self, num_vuelo, origen, destino, fecha_hora, avion):
        self.num_vuelo = num_vuelo
        self.origen = origen
        self.destino = destino
        self.fecha_hora = fecha_hora
        self.avion = avion
        self.reservaciones = []

    def agregar_reservacion(self, reservacion):
        if len(self.reservaciones) < self.avion.num_asientos:
            self.reservaciones.append(reservacion)
            return True
        else:
            return False

class Pasajero:
    def __init__(self, nombre, num_pasaporte):
        self.nombre = nombre
        self.num_pasaporte = num_pasaporte
        self.vuelos_reservados = []

class Reservacion:
    def __init__(self, num_reservacion, pasajero, vuelo):
        self.num_reservacion = num_reservacion
        self.pasajero = pasajero
        self.vuelo = vuelo
        self.estado = "reservado"
        pasajero.vuelos_reservados.append(vuelo)
        vuelo.agregar_reservacion(self)

    def cancelar(self):
        self.estado = "cancelado"


class Aerolinea:
    def __init__(self):
        self.vuelos_disponibles = []
        self.reservaciones = []
        self.pasajeros = []

    def crear_vuelo(self, num_vuelo, origen, destino, fecha_hora, avion):
        vuelo = Vuelo(num_vuelo, origen, destino, fecha_hora, avion)
        self.vuelos_disponibles.append(vuelo)
        return vuelo

    def reservar_vuelo(self, pasajero, vuelo):
        if pasajero in self.pasajeros:
            if vuelo.agregar_reservacion(Reservacion(len(self.reservaciones) + 1, pasajero, vuelo)):
                self.reservaciones.append(vuelo.reservaciones[-1])
                return True
        return False

    def cancelar_reservacion(self, reservacion):
        reservacion.cancelar()

    def mostrar_reservaciones_pasajero(self, pasajero):
        for vuelo in pasajero.vuelos_reservados:
            for reservacion in vuelo.reservaciones:
                if reservacion.pasajero == pasajero:
                    print(f"Vuelo: {vuelo.num_vuelo}, Estado: {reservacion.estado}")

    def mostrar_pasajeros_vuelo(self, vuelo):
        for reservacion in vuelo.reservaciones:
            print(f"Nombre: {reservacion.pasajero.nombre}, Estado: {reservacion.estado}")


def main():
    aerolinea = Aerolinea()

    avion1 = Avion("Boeing 737", 150)
    avion2 = Avion("Airbus A320", 180)
    avion3 = Avion("Boeing 737", 150)

    vuelo1 = aerolinea.crear_vuelo("BA123", "Santiago", "Buenos aires", "2023-09-01 12:00", avion1)
    vuelo2 = aerolinea.crear_vuelo("AA456", "Santiago", "Arica", "2023-09-02 15:30", avion2)
    vuelo3 = aerolinea.crear_vuelo("DD123", "Santiago", "CDMX", "2023-09-02 16:30", avion3)

    pasajero1 = Pasajero("Alice", "A123456")
    pasajero2 = Pasajero("Bob", "B789012")

    aerolinea.pasajeros.extend([pasajero1, pasajero2])

    while True:
        print("\n*** Menú ***")
        print("1. Consultar vuelos disponibles")
        print("2. Reservar un vuelo")
        print("3. Cancelar una reservación")
        print("4. Ver las reservaciones de un pasajero")
        print("5. Ver la lista de pasajeros en un vuelo")
        print("6. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            print("\nVuelos disponibles:")
            for vuelo in aerolinea.vuelos_disponibles:
                print(f"{vuelo.num_vuelo}: {vuelo.origen} -> {vuelo.destino} ({vuelo.fecha_hora})")
            else:
                input("Presiona Enter para continuar...")

        elif opcion == "2":
            pasaporte = input("Ingrese su número de pasaporte: ")
            nombre = input("Ingrese su nombre: ")

            pasajero = Pasajero(nombre, pasaporte)
            aerolinea.pasajeros.append(pasajero)

            print("Vuelos disponibles:")
            for vuelo in aerolinea.vuelos_disponibles:
                print(f"{vuelo.num_vuelo}: {vuelo.origen} -> {vuelo.destino} ({vuelo.fecha_hora})")

            num_vuelo = input("Ingrese el número de vuelo que desea reservar: ")
            vuelo_seleccionado = None
            for vuelo in aerolinea.vuelos_disponibles:
                if vuelo.num_vuelo == num_vuelo:
                    vuelo_seleccionado = vuelo
                    break

            if vuelo_seleccionado:
                if aerolinea.reservar_vuelo(pasajero, vuelo_seleccionado):
                    print("Reservación exitosa.")
                else:
                    print("No se pudo realizar la reservación.")
            input("Presiona Enter para continuar...")

        elif opcion == "3":
            pasaporte = input("Ingrese el número de pasaporte del pasajero: ")
            num_reservacion = int(input("Ingrese el número de reservación que desea cancelar: "))

            pasajero_encontrado = None
            for pasajero in aerolinea.pasajeros:
                if pasajero.num_pasaporte == pasaporte:
                    pasajero_encontrado = pasajero
                    input("Presiona Enter para continuar...")
                    break

            if pasajero_encontrado:
                reservacion_encontrada = None
                for vuelo in pasajero_encontrado.vuelos_reservados:
                    for reservacion in vuelo.reservaciones:
                        if reservacion.pasajero == pasajero_encontrado and reservacion.num_reservacion == num_reservacion:
                            reservacion_encontrada = reservacion
                            input("Presiona Enter para continuar...")
                            break

                if reservacion_encontrada:
                    aerolinea.cancelar_reservacion(reservacion_encontrada)
                    print("Reservación cancelada exitosamente.")
                else:
                    print("Reservación no encontrada.")
            else:
                print("Pasajero no encontrado.")
            pass

        elif opcion == "4":
            pasaporte = input("Ingrese el número de pasaporte del pasajero: ")
            pasajero_encontrado = None
            for pasajero in aerolinea.pasajeros:
                if pasajero.num_pasaporte == pasaporte:
                    pasajero_encontrado = pasajero
                    input("Presiona Enter para continuar...")
                    break

            if pasajero_encontrado:
                aerolinea.mostrar_reservaciones_pasajero(pasajero_encontrado)
            else:
                print("Pasajero no encontrado.")
                input("Presiona Enter para continuar...")

        elif opcion == "5":
            num_vuelo = input("Ingrese el número de vuelo: ")
            vuelo_encontrado = None
            for vuelo in aerolinea.vuelos_disponibles:
                if vuelo.num_vuelo == num_vuelo:
                    vuelo_encontrado = vuelo
                    input("Presiona Enter para continuar...")
                    break

            if vuelo_encontrado:
                aerolinea.mostrar_pasajeros_vuelo(vuelo_encontrado)
            else:
                print("Vuelo no encontrado.")

        elif opcion == "6":
            print("¡Hasta luego!")
            break

        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")


if __name__ == "__main__":
    main()
