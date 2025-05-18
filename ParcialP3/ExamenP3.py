from abc import ABC, abstractmethod


class IGestionAnimal(ABC):
    @abstractmethod
    def crear_animal(self, codigo, raza, edad):
        pass

    @abstractmethod
    def leer_animal(self, codigo):
        pass

    @abstractmethod
    def actualizar_animal(self, codigo, raza=None, edad=None):
        pass

    @abstractmethod
    def eliminar_animal(self, codigo):
        pass


class Animal:
    def __init__(self, codigo, raza, edad):
        self.codigo = codigo
        self.raza = raza
        self.edad = edad
        self.produccion_semanal = {}  # semana: huevos

    def registrar_produccion(self, semana, cantidad):
        self.produccion_semanal[semana] = cantidad

    def obtener_produccion_total(self):
        return sum(self.produccion_semanal.values())

    def obtener_produccion_por_semana(self, semana):
        return self.produccion_semanal.get(semana, 0)

    def __str__(self):
        return f"Código: {self.codigo}, Raza: {self.raza}, Edad: {self.edad} semanas"


class BaseDatos(IGestionAnimal):
    def __init__(self):
        self.animales = []

    def buscar_animal(self, codigo):
        for animal in self.animales:
            if animal.codigo == codigo:
                return animal
        return None

    def crear_animal(self, codigo, raza, edad):
        if self.buscar_animal(codigo):
            print("⚠️ Ya existe un animal con ese código.")
            return
        nuevo_animal = Animal(codigo, raza, edad)
        self.animales.append(nuevo_animal)
        print("✅ Animal creado exitosamente.")

    def leer_animal(self, codigo):
        animal = self.buscar_animal(codigo)
        if animal:
            print(animal)
            return animal
        else:
            print("⚠️ Animal no encontrado.")
            return None

    def actualizar_animal(self, codigo, raza=None, edad=None):
        animal = self.buscar_animal(codigo)
        if not animal:
            print("⚠️ Animal no encontrado.")
            return
        if raza:
            animal.raza = raza
        if edad:
            animal.edad = edad
        print("✅ Animal actualizado correctamente.")

    def eliminar_animal(self, codigo):
        animal = self.buscar_animal(codigo)
        if animal:
            self.animales.remove(animal)
            print("✅ Animal eliminado correctamente.")
        else:
            print("⚠️ Animal no encontrado.")

    def registrar_produccion(self, codigo, semana, cantidad):
        animal = self.buscar_animal(codigo)
        if animal:
            animal.registrar_produccion(semana, cantidad)
            print("✅ Producción registrada.")
        else:
            print("⚠️ Animal no encontrado.")

    def mostrar_produccion_total(self, codigo):
        animal = self.buscar_animal(codigo)
        if animal:
            total = animal.obtener_produccion_total()
            print(f"🐔 Producción total del animal {codigo}: {total} huevos.")
        else:
            print("⚠️ Animal no encontrado.")

    def mostrar_produccion_por_semana(self, codigo, semana):
        animal = self.buscar_animal(codigo)
        if animal:
            cantidad = animal.obtener_produccion_por_semana(semana)
            print(f"📅 Semana {semana}, producción: {cantidad} huevos.")
        else:
            print("⚠️ Animal no encontrado.")


def mostrar_menu():
    print("\n===== SISTEMA DE REGISTRO - GRANJA DE POLLOS =====")
    print("1. Agregar nuevo pollo")
    print("2. Ver información del pollo")
    print("3. Actualizar datos del pollo")
    print("4. Eliminar pollo")
    print("5. Registrar producción semanal")
    print("6. Ver producción total")
    print("7. Ver producción por semana")
    print("8. Salir")
    print("===================================================")

def main():
    bd = BaseDatos()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            codigo = input("Código del pollo: ")
            raza = input("Raza: ")
            edad = int(input("Edad (en semanas): "))
            bd.crear_animal(codigo, raza, edad)

        elif opcion == "2":
            codigo = input("Código del pollo a consultar: ")
            bd.leer_animal(codigo)

        elif opcion == "3":
            codigo = input("Código del pollo a actualizar: ")
            raza = input("Nueva raza (enter para no cambiar): ")
            edad_input = input("Nueva edad (enter para no cambiar): ")
            edad = int(edad_input) if edad_input else None
            bd.actualizar_animal(codigo, raza if raza else None, edad)

        elif opcion == "4":
            codigo = input("Código del pollo a eliminar: ")
            bd.eliminar_animal(codigo)

        elif opcion == "5":
            codigo = input("Código del pollo: ")
            semana = input("Semana (por ejemplo 'Semana1'): ")
            cantidad = int(input("Cantidad de huevos: "))
            bd.registrar_produccion(codigo, semana, cantidad)

        elif opcion == "6":
            codigo = input("Código del pollo: ")
            bd.mostrar_produccion_total(codigo)

        elif opcion == "7":
            codigo = input("Código del pollo: ")
            semana = input("Semana a consultar (por ejemplo 'Semana1'): ")
            bd.mostrar_produccion_por_semana(codigo, semana)

        elif opcion == "8":
            print("👋 Saliendo del sistema. ¡Hasta luego!")
            break

        else:
            print("❌ Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
