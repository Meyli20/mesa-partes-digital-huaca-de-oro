class Tramite:

    def _init_(self, codigo, remitente, tipo_tramite, asunto, folios, fecha_registro):
        self.codigo = codigo
        self.remitente = remitente
        self.tipo_tramite = tipo_tramite
        self.asunto = asunto
        self.folios = folios              
        self.fecha_registro = fecha_registro  

    def mostrar(self):
        print("-" * 40)
        print("Código    :", self.codigo)
        print("Remitente :", self.remitente)
        print("Trámite   :", self.tipo_tramite)
        print("Asunto    :", self.asunto)
        print("Folios    :", self.folios)
        print("Fecha     :", self.fecha_registro)