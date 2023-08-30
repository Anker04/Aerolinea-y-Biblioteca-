class Libro:
    def __init__(self, codigo, titulo, autor, disponible=True):
        self.codigo = codigo
        self.titulo = titulo
        self.autor = autor
        self.disponible = disponible

class Usuario:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre
        self.libros_prestados = []

class Biblioteca:
    def __init__(self):
        self.catalogo = []
        self.usuarios = []
        self.prestamos = []

    def agregar_libro(self, libro):
        self.catalogo.append(libro)

    def eliminar_libro(self, codigo):
        for libro in self.catalogo:
            if libro.codigo == codigo:
                self.catalogo.remove(libro)
                break

    def registrar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def prestar_libro(self, usuario, libro):
        if libro.disponible:
            libro.disponible = False
            usuario.libros_prestados.append(libro)
            self.prestamos.append((usuario, libro))

    def devolver_libro(self, usuario, libro):
        if libro in usuario.libros_prestados:
            libro.disponible = True
            usuario.libros_prestados.remove(libro)
            self.prestamos.remove((usuario, libro))

    def consultar_libros_disponibles(self):
        return [libro for libro in self.catalogo if libro.disponible]

    def historial_prestamos_usuario(self, usuario):
        return [libro for u, libro in self.prestamos if u == usuario]


biblioteca = Biblioteca()

libro1 = Libro("ISBN123", "Libro 1", "Autor 1")
libro2 = Libro("ISBN456", "Libro 2", "Autor 2")
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)

usuario1 = Usuario("ID001", "Usuario 1")
biblioteca.registrar_usuario(usuario1)

biblioteca.prestar_libro(usuario1, libro1)
print(usuario1.libros_prestados[0].titulo)  # Debería mostrar "Libro 1"

biblioteca.devolver_libro(usuario1, libro1)

print(len(biblioteca.consultar_libros_disponibles()))  # Debería mostrar 2

def mostrar_menu():
    print("Bienvenido a la Biblioteca")
    print("1. Agregar libro")
    print("2. Eliminar libro")
    print("3. Registrar usuario")
    print("4. Prestar libro")
    print("5. Devolver libro")
    print("6. Consultar libros disponibles")
    print("7. Ver historial de préstamos de un usuario")
    print("8. Salir")

biblioteca = Biblioteca()

while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")
    mensaje_continuar = "Presione enter para continuar..."

    if opcion == "1":
        codigo = input("Ingrese el código del libro: ")
        titulo = input("Ingrese el título del libro: ")
        autor = input("Ingrese el autor del libro: ")
        libro = Libro(codigo, titulo, autor)
        biblioteca.agregar_libro(libro)
        print("Libro agregado con éxito.")
        input(mensaje_continuar)

    elif opcion == "2":
        codigo = input("Ingrese el código del libro a eliminar: ")
        biblioteca.eliminar_libro(codigo)
        print("Libro eliminado con éxito.")
        input(mensaje_continuar)

    elif opcion == "3":
        id = input("Ingrese el ID del usuario: ")
        nombre = input("Ingrese el nombre del usuario: ")
        usuario = Usuario(id, nombre)
        biblioteca.registrar_usuario(usuario)
        print("Usuario registrado con éxito.")
        input(mensaje_continuar)

    elif opcion == "4":
        id_usuario = input("Ingrese el ID del usuario: ")
        codigo_libro = input("Ingrese el código del libro a prestar: ")
        usuario = next((u for u in biblioteca.usuarios if u.id == id_usuario), None)
        libro = next((l for l in biblioteca.catalogo if l.codigo == codigo_libro), None)
        if usuario and libro:
            biblioteca.prestar_libro(usuario, libro)
            print("Libro prestado con éxito.")
            input(mensaje_continuar)
        else:
            print("Usuario o libro no encontrado.")
            input(mensaje_continuar)

    elif opcion == "5":
        id_usuario = input("Ingrese el ID del usuario: ")
        codigo_libro = input("Ingrese el código del libro a devolver: ")
        usuario = next((u for u in biblioteca.usuarios if u.id == id_usuario), None)
        libro = next((l for l in biblioteca.catalogo if l.codigo == codigo_libro), None)
        if usuario and libro:
            biblioteca.devolver_libro(usuario, libro)
            print("Libro devuelto con éxito.")
            input(mensaje_continuar)
        else:
            print("Usuario o libro no encontrado.")
            input(mensaje_continuar)

    elif opcion == "6":
        libros_disponibles = biblioteca.consultar_libros_disponibles()
        print("Libros disponibles:")
        for libro in libros_disponibles:
            print(f"- {libro.titulo} ({libro.codigo})")
        input(mensaje_continuar)

    elif opcion == "7":
        id_usuario = input("Ingrese el ID del usuario: ")
        usuario = next((u for u in biblioteca.usuarios if u.id == id_usuario), None)
        if usuario:
            historial = biblioteca.historial_prestamos_usuario(usuario)
            print("Historial de préstamos:")
            for libro in historial:
                print(f"- {libro.titulo} ({libro.codigo})")
            input(mensaje_continuar)
        else:
            print("Usuario no encontrado.")
            input(mensaje_continuar)

    elif opcion == "8":
        print("Gracias por usar la Biblioteca. ¡Hasta luego!")
        input(mensaje_continuar)
        break

    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
        input(mensaje_continuar)
