import tkinter as tk
from tkinter import ttk
import time
import threading

class Proceso:
    def __init__(self, nombre, duracion):
        self.nombre = nombre
        self.duracion = duracion

class SimuladorFCFS:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Simulador FCFS")

        self.procesos = [
            Proceso("Proceso 1", 5),
            Proceso("Proceso 2", 3),
            Proceso("Proceso 3", 7),
            Proceso("Proceso 4", 2),
            Proceso("Proceso 5", 4),
        ]

        self.barras_progreso = []
        self.inicializar_interfaz()

    def inicializar_interfaz(self):
        self.boton_inicio = tk.Button(self.ventana, text="Iniciar", command=self.iniciar_simulacion)
        self.boton_inicio.pack(pady=10)

        for proceso in self.procesos:
            etiqueta = tk.Label(self.ventana, text=proceso.nombre)
            etiqueta.pack(pady=5)
            barra = ttk.Progressbar(self.ventana, length=200, maximum=proceso.duracion, mode='determinate')
            self.barras_progreso.append((etiqueta, barra))
            barra.pack(pady=5)

    def ejecutar_proceso(self, proceso, etiqueta, barra):
        for i in range(proceso.duracion):
            time.sleep(1)
            barra['value'] += 1
            self.ventana.update_idletasks()

    def iniciar_simulacion(self):
        self.boton_inicio.config(state=tk.DISABLED)

        for i in range(len(self.procesos)):
            proceso = self.procesos[i]
            etiqueta, barra = self.barras_progreso[i]

            thread = threading.Thread(target=self.ejecutar_proceso, args=(proceso, etiqueta, barra))
            thread.start()

if __name__ == "__main__":
    ventana = tk.Tk()
    simulador = SimuladorFCFS(ventana)
    ventana.mainloop()
