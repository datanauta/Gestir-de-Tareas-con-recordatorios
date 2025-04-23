import sqlite3

def conectar():
    conn = sqlite3.connect("tareas.db")
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS tareas(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        descripcion TEXT,
        fecha_limite TEXT,
        prioridad TEXT,
        completada INTEGER DEFAULT 0
        )
    """)
    conn.commit()
    conn.close()


def insertar_tarea(titulo,descripcion,fecha_limite, prioridad):
    conn = sqlite3.connect("tareas.db")
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO tareas(titulo,descripcion, fecha_limite,prioridad)
        VALUES(?,?,?,?)
        """,(titulo,descripcion,fecha_limite,prioridad))
    conn.commit()
    conn.close()

def obtener_todas_las_tareas():
    conn = sqlite3.connect("tareas.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, titulo, descripcion, fecha_limite,prioridad,completada FROM tareas")
    tareas = cursor.fetchall()
    conn.close()
    return tareas

def eliminar_tarea_por_id(tarea_id):
    conn = sqlite3.connect("tareas.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tareas WHERE id = ?",(tarea_id,)) #error
    conn.commit()
    conn.close()


def marcar_tarea_completada(tarea_id):
    conn = sqlite3.connect("tareas.db")
    cursor = conn.cursor()
    cursor.execute("UDATE tareas SET completada =  WHERE id = ?",(tarea_id,))
    conn.commit()
    conn.close()