import tkinter as tk
from ui import GestorTareasUI
from database import conectar

if __name__ == "__main__":
    conectar()
    root = tk.Tk()
    app = GestorTareasUI(root)
    root.mainloop()

    