# ui.py
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from database import insertar_tarea, obtener_todas_las_tareas, eliminar_tarea_por_id,marcar_tarea_completada

class GestorTareasUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas")
        self.root.geometry("700x500")
        self.root.configure(bg="#f5f5f5")

        self.ids_tareas = []

       

        # --- Formulario de entrada ---
        frame_form = ttk.LabelFrame(root, text="Nueva Tarea", padding=10)
        frame_form.pack(fill="x", padx=20, pady=10)

        ttk.Label(frame_form, text="Título:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.entry_titulo = ttk.Entry(frame_form, width=40)
        self.entry_titulo.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(frame_form, text="Descripción:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.entry_descripcion = ttk.Entry(frame_form, width=40)
        self.entry_descripcion.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(frame_form, text="Fecha Límite (YYYY-MM-DD):").grid(row=2, column=0, sticky="w", padx=5, pady=5)
        self.entry_fecha = ttk.Entry(frame_form, width=40)
        self.entry_fecha.grid(row=2, column=1, padx=5, pady=5)

        ttk.Label(frame_form, text="Prioridad:").grid(row=3, column=0, sticky="w", padx=5, pady=5)
        self.combo_prioridad = ttk.Combobox(frame_form, values=["Alta", "Media", "Baja"], state="readonly")
        self.combo_prioridad.grid(row=3, column=1, padx=5, pady=5)
        self.combo_prioridad.current(1)

        self.btn_agregar = ttk.Button(frame_form, text="Agregar Tarea", command=self.agregar_tarea)
        self.btn_agregar.grid(row=4, column=0, columnspan=2, pady=10)

        # --- Lista de tareas ---
        frame_lista = ttk.LabelFrame(root, text="Tareas", padding=10)
        frame_lista.pack(fill="both", expand=True, padx=20, pady=10)

        self.lista_tareas = tk.Listbox(frame_lista, height=10, font=("Segoe UI", 10))
        self.lista_tareas.pack(side="left", fill="both", expand=True)

        scrollbar = ttk.Scrollbar(frame_lista, orient="vertical", command=self.lista_tareas.yview)
        scrollbar.pack(side="right", fill="y")
        self.lista_tareas.config(yscrollcommand=scrollbar.set)

        # --- Botón eliminar ---
        self.btn_eliminar = ttk.Button(root, text="Eliminar Tarea Seleccionada", command=self.eliminar_tarea)
        self.btn_eliminar.pack(pady=10)

        # --- Cargar tareas guardadas ---
        self.cargar_tareas()

        self.lista_tareas.bind("<Double-Button-1>",self.marcar_como_completada)

    def agregar_tarea(self):
        titulo = self.entry_titulo.get()
        descripcion = self.entry_descripcion.get()
        fecha = self.entry_fecha.get()
        prioridad = self.combo_prioridad.get()

        if titulo.strip() == "":
            messagebox.showerror("Error", "El título no puede estar vacío.")
            return

        insertar_tarea(titulo, descripcion, fecha, prioridad)
        self.limpiar_campos()
        self.cargar_tareas()

    def limpiar_campos(self):
        self.entry_titulo.delete(0, tk.END)
        self.entry_descripcion.delete(0, tk.END)
        self.entry_fecha.delete(0, tk.END)
        self.combo_prioridad.current(1) 

    def cargar_tareas(self):
        tareas = obtener_todas_las_tareas()
        self.lista_tareas.delete(0, tk.END)
        self.ids_tareas = []

        for tarea in tareas:
            id_, titulo, descripcion, fecha, prioridad, completada = tarea
            estado = "✔️" if completada else "⏳"
            self.lista_tareas.insert(tk.END, f"{estado} {titulo} - {prioridad} - {fecha}")
            self.ids_tareas.append(id_)

    def eliminar_tarea(self):
        seleccion = self.lista_tareas.curselection()
        if not seleccion:
            messagebox.showwarning("Aviso", "Selecciona una tarea para eliminar.")
            return

        indice = seleccion[0]
        if indice >= len(self.ids_tareas):
            messagebox.showerror("Error","La tarea seleccionada no es válida")
            return 

        tarea_id = self.ids_tareas[indice]
        eliminar_tarea_por_id(tarea_id) #error
        self.cargar_tareas()    


    def marcar_como_completada(self,event):
        try:
            seleccion = self.lista_tareas.curselection()
            if not seleccion:
                return
        
            indice = seleccion[0]
            if indice >= len(self.ids_tareas):
                return

            tarea_id = self.ids_tareas[indice]
            marcar_tarea_completada(tarea_id)
            self.cargar_tareas()
        except Exception as e:
            messagebox.showerror("Error",f"No se puede marcar como completada{str(e)}")                 

            