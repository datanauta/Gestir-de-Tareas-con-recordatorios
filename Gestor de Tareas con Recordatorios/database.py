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

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS subtareas(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        tarea_id INTEGER,
        titulo TEXT,
        completada BOOLEAN DEFAULT 0,
        FOREIGN KEY (tarea_id) REFERENCES tareas(id)
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

conexion = sqlite3.connect("tareas.db")
cursor = conexion.cursor()

def agregar_subtarea(tarea_id,titulo):
    cursor.execute("INSERT INTO sutareas (tarea_id,titulo) VALUES(?,?)",(tarea_id,titulo))
    conexion.commit()

def obtener_subtareas(tarea_id):
    cursor.execute("SELECT * FROM subtareas WHERE tarea_id = ?",(tarea_id,))
    return cursor.fetchall()

def completar_subtarea(subtarea_id, estado):
    cursor.execute("UPDATE subtareas SET completada = ? WHERE id = ?",(estado,subtarea_id))
    conexion.commit()

   