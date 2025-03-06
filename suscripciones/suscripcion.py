class SuscripcionesMant:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        suscripcionesMant = self.session.get("suscripcionesMant")
        if not suscripcionesMant:
            self.session["suscripcionesMant"] = {}
            self.suscripcionesMant = self.session["suscripcionesMant"]
        else:
            self.suscripcionesMant = suscripcionesMant
            
    def agregarr(self, tipoSuscripcion):
        id = str(tipoSuscripcion.id)
        if id not in self.suscripcionesMant.keys():
            self.suscripcionesMant[id]={
                "tiposuscripcion_id": tipoSuscripcion.id,
                "nombre": tipoSuscripcion.nombre,
                "preciofinal": tipoSuscripcion.precio,
            }
        else:
            print(self.suscripcionesMant)
            self.suscripcionesMant[id]["preciofinal"] += tipoSuscripcion.precio
        self.guardar_suscripcion()

    def guardar_suscripcion(self):
            self.session["suscripcionesMant"] = self.suscripcionesMant
            self.session.modified = True
            
    def eliminar(self, tipoSuscripcion):
        id = str(tipoSuscripcion.id)
        if id in self.suscripcionesMant:
            del self.suscripcionesMant[id]
            self.guardar_suscripcion()
      
    def limpiar(self):
            self.session["suscripcionesMant"] = {}
            self.session.modified = True