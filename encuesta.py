class Encuesta:
  def __init__(self, nombre, preguntas=None):
    self.nombre = nombre
    self.preguntas = preguntas if preguntas else []
    self.listados_respuestas = []

  def mostrar_encuesta(self):
    print("Nombre de la encuesta:", self.nombre)
    for pregunta in self.preguntas:
      pregunta.mostrar_pregunta()

  def agregar_listado_respuestas(self, listado_respuestas):
    self.listados_respuestas.append(listado_respuestas)


class EncuestaLimitadaEdad(Encuesta):
  def __init__(self, nombre, edad_minima, edad_maxima, preguntas=None):
    super().__init__(nombre, preguntas)
    self.edad_minima = edad_minima
    self.edad_maxima = edad_maxima


class EncuestaLimitadaRegion(Encuesta):
  def __init__(self, nombre, regiones_permitidas, preguntas=None):
    super().__init__(nombre, preguntas)
    self.regiones_permitidas = regiones_permitidas