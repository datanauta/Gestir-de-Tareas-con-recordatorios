class Tarea:
    def __init__(self, id, titulo, descripcion, fecha_limite, prioridad, completada = False):
        self.id = id
        self.titulo = titulo
        self.descripcion = descripcion
        self.fecha_limite = fecha_limite
        self.prioridad = prioridad
        self.completada = completada
