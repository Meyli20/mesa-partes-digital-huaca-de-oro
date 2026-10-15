
def validar_texto(texto,minimo=3):
    return len(texto.strip()) >= minimo

def validar_folios(valor):
    return valor.isdigit() and int(valor) >= 1

def validar_opcion(opcion, cantidad):
    if not opcion.isdigit():
        return False
    return 1 <= int(opcion) <= cantidad

print(validar_texto("Ana"))
print(validar_texto("  "))
print(validar_folios("5"))
print(validar_folios("0"))
print(validar_folios("abc"))
print(validar_opcion("2", 4))
print(validar_opcion("9", 4))