import csv
from datetime import datetime
from tramite import Tramite


class MesaPartes:
    Tipos = { 
        1: "Certificado de notas",
        2: "Traslado de matrícula",
        3: "Constancia de vacantes",
        4: "Reclamo",
    }
    ARCHIVO = "registro_mesa_partes.csv"
    CAMPOS = ["codigo", "remitente", "tipo_tramite", "asunto", "folios", "fecha_registro"]

    def __init__(self):
        self.tramites = []
        self.contador = 0
        self.cargar_csv()

    def generar_codigo(self):
        self.contador += 1
        anio = datetime.now().year
        return "EXP-" + str(anio) + "-" + str(self.contador).zfill(4)

    def registrar(self, remitente, tipo, asunto, folios):
        codigo = self.generar_codigo()
        fecha = datetime.now().strftime("%d/%m/%Y %H:%M")
        nuevo = Tramite(codigo, remitente, self.Tipos[tipo], asunto, folios, fecha)
        self.tramites.append(nuevo)
        self.guardar_csv()
        return nuevo

    def buscar_por_codigo(self, codigo):
        for t in self.tramites:
            if t.codigo == codigo:
                return t
            return None
        
    def ordenar_por_folios(self, descendente=False):
        lista = self.tramites[:]
        n = len(lista)
        for i in range(n - 1):
            pos = i
            for j in range(i + 1, n):
                if descendente:
                    if lista[j].folios > lista[pos].folios:
                        pos = j
                else:
                    if lista[j].folios < lista[pos].folios:
                        pos = j
            lista[i], lista[pos] = lista[pos], lista[i]
        return lista
        
    def guardar_csv(self):
        with open(self.ARCHIVO, "w", newline="", encoding="utf-8") as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow(self.CAMPOS)
            for t in self.tramites:
                escritor.writerow([t.codigo, t.remitente, t.tipo_tramite,
                                   t.asunto, t.folios, t.fecha_registro])

    def cargar_csv(self):
        try:
            with open(self.ARCHIVO, "r", newline="", encoding="utf-8") as archivo:
                lector = csv.reader(archivo)
                next(lector)
                for fila in lector:
                    t = Tramite(fila[0], fila[1], fila[2], fila[3], int(fila[4]), fila[5])
                    self.tramites.append(t)
            self.contador = len(self.tramites)
        except FileNotFoundError:
            pass


