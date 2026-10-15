
def validar_texto(texto,minimo=3):
    return len(texto.strip()) >= minimo

def validar_folios(valor):
    return valor.isdigit() and int(valor) >= 1

def validar_opcion(opcion, cantidad):
    if not opcion.isdigit():
        return False
    return 1 <= int(opcion) <= cantidad
