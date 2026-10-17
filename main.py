from mesa_partes import MesaPartes
from validador import validar_texto, validar_folios, validar_opcion

def mostrar_lista(lista):
    if len(lista) == 0:
        print("No hay solicitudes registradas.")
    for t in lista:
        t.mostrar()

def registrar_solicitud(mesa):
    remitente = input("Remitente (nombres y apellidos): ")
    while not validar_texto(remitente):
        remitente = input("Dato inválido. Intenta de nuevo: ")

    print("Tipos de trámite:")
    for numero in mesa.Tipos:
        print(numero, "-", mesa.Tipos[numero])
    tipo = input("Elige el tipo: ")
    while not validar_opcion(tipo, len(mesa.Tipos)):
        tipo = input("Opción inválida. Elige de nuevo: ")

    asunto = input("Asunto: ")
    while not validar_texto(asunto, 5):
        asunto = input("Asunto muy corto. Intenta de nuevo: ")

    folios = input("Número de folios: ")
    while not validar_folios(folios):
        folios = input("Debe ser un entero mayor o igual a 1: ")

    remitente = remitente.strip().title()
    asunto = asunto.strip()
    asunto = asunto[0].upper() + asunto[1:]
    nuevo = mesa.registrar(remitente, int(tipo), asunto, int(folios))
    print("\n=== COMPROBANTE DE REGISTRO ===")
    nuevo.mostrar()
    print("Guarda tu código:", nuevo.codigo)


def menu():
    print("\n=== MESA DE PARTES DIGITAL - I.E. 3091 HUACA DE ORO ===")
    print("1. Registrar solicitud")
    print("2. Consultar por código")
    print("3. Listar ordenado por folios (menor a mayor)")
    print("4. Listar ordenado por folios (mayor a menor)")
    print("5. Salir")


def main():
    mesa = MesaPartes()
    salir = False
    while not salir:
        menu()
        opcion = input("Elige una opción: ")
        if opcion == "1":
            registrar_solicitud(mesa)
        elif opcion == "2":
            t = mesa.buscar_por_codigo(input("Código: ").upper())
            if t is None:
                print("No se encontró el expediente.")
            else:
                t.mostrar()
        elif opcion == "3":
            mostrar_lista(mesa.ordenar_por_folios())
        elif opcion == "4":
            mostrar_lista(mesa.ordenar_por_folios(descendente=True))
        elif opcion == "5":
            salir = True
            print("Hasta pronto.")
        else:
            print("Opción inválida.")


main()