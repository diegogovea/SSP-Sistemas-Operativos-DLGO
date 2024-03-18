import tkinter as tk
from tkinter import ttk
import threading
import random
import time


class ProductorConsumidor(tk.Tk):
    def __init__(self):
        super().__init__()

        # creacion de la ventana en buen tamaño pa ver bien
        self.title("Govea Ortiz Diego León")
        self.geometry("800x500")
        self.configure(bg='light grey')

        # creo los procesos con letras para entenderle mejor junto con los botones y estados
        self.procesos = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        self.barras = {}
        self.estados = {}
        self.botones = {}
        self.pausado = {}
        self.cola = tk.StringVar()
        self.ejecutando = tk.StringVar()
        self.terminado = tk.StringVar()

        tk.Label(self, text="Procesos", font=("Times New Roman", 14), bg='light grey').pack()

        # le asigno a cada proceso su boton y texto
        for proceso in self.procesos:
            frame = tk.Frame(self, bg='light grey')
            frame.pack(padx=20, pady=5)

            label = tk.Label(frame, text=f"Proceso {proceso}", bg='light grey')
            label.grid(row=0, column=0)

            barra = ttk.Progressbar(frame, orient="horizontal", length=200, mode="determinate")
            barra.grid(row=0, column=1)

            estado_label = tk.Label(frame, text="En cola", bg='light grey')
            estado_label.grid(row=0, column=2)

            boton = tk.Button(frame, text="Pausar/Reanudar",
                              command=lambda proceso=proceso: self.pausar_reanudar(proceso), bg='sky blue')
            boton.grid(row=0, column=3)

            self.barras[proceso] = barra
            self.estados[proceso] = estado_label
            self.botones[proceso] = boton
            self.pausado[proceso] = False

        # estados de los botones
        tk.Label(self, text="Estados", font=("Times New Roman", 14), bg='light grey').pack()

        self.cola_label = tk.Label(self, textvariable=self.cola, bg='light grey')
        self.cola_label.pack()
        self.ejecutando_label = tk.Label(self, textvariable=self.ejecutando, bg='light grey')
        self.ejecutando_label.pack()
        self.terminado_label = tk.Label(self, textvariable=self.terminado, bg='light grey')
        self.terminado_label.pack()

    # funcion para iniciar los procesos (hilos)
    def iniciar_procesos(self):
        self.actualizar_estados()
        for proceso in self.procesos:
            hilo = threading.Thread(target=self.ejecutar_proceso, args=(proceso,))
            hilo.start()

    def ejecutar_proceso(self, proceso):
        barra = self.barras[proceso]

        # Simulando la producción (carga de la barra)
        for _ in range(10):
            while self.pausado[proceso]:
                time.sleep(0.1)
            carga_actualizada = barra['value'] + 10
            barra['value'] = carga_actualizada

            self.update_idletasks()
            time.sleep(random.uniform(0.1, 1))  # aqui juegan carreritas los procesos (cargan de manera random jajas xd)

        self.estados[proceso].config(text="Ejecutándose")
        self.actualizar_estados()

        # Simulando el consumo (descarga de la barra) del consumidor
        for _ in range(10):
            while self.pausado[proceso]:
                time.sleep(0.1)
            carga_actualizada -= 10
            barra['value'] = carga_actualizada

            self.update_idletasks()
            time.sleep(random.uniform(0.1, 1))

        self.estados[proceso].config(text="Terminado")
        self.actualizar_estados()

    # de aqui pa abajo ya solo son los estados, facilito :D
    def pausar_reanudar(self, proceso):
        self.pausado[proceso] = not self.pausado[proceso]
        self.actualizar_estados()

    def actualizar_estados(self):
        en_cola = [proceso for proceso in self.procesos if self.estados[proceso].cget("text") == "En cola"]
        ejecutando = [proceso for proceso in self.procesos if self.estados[proceso].cget("text") == "Ejecutándose"]
        terminado = [proceso for proceso in self.procesos if self.estados[proceso].cget("text") == "Terminado"]

        self.cola.set(f"En cola: {en_cola}")
        self.ejecutando.set(f"Ejecutándose: {ejecutando}")
        self.terminado.set(f"Terminado: {terminado}")


if __name__ == "__main__":
    app = ProductorConsumidor()
    app.iniciar_procesos()
    app.mainloop()
