import tkinter as tk
from tkinter import ttk
import threading
import random
import time


class ProductorConsumidor(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Govea Ortiz Diego León")
        self.geometry("800x500")
        self.configure(bg='light grey')

        self.procesos = ['LECTOR A', 'LECTOR B', 'LECTOR C', 'LECTOR D', 'LECTOR E',
                         'ESCRITOR A', 'ESCRITOR B', 'ESCRITOR C', 'ESCRITOR D', 'ESCRITOR E']
        self.barras = {}
        self.estados = {}
        self.botones_pausar = {}
        self.botones_reanudar = {}
        self.pausado = {}
        self.cola = tk.StringVar()
        self.ejecutando = tk.StringVar()
        self.terminado = tk.StringVar()

        tk.Label(self, text="Procesos ", font=("Times New Roman", 14), bg='light grey').pack()

        for proceso in self.procesos:
            frame = tk.Frame(self, bg='light grey')
            frame.pack(padx=20, pady=5)

            label = tk.Label(frame, text=f"P: {proceso}", bg='light grey')
            label.grid(row=0, column=0)

            barra = ttk.Progressbar(frame, orient="horizontal", length=200, mode="determinate")
            barra.grid(row=0, column=1)

            estado_label = tk.Label(frame, text="En cola", bg='light grey')
            estado_label.grid(row=0, column=2)

            boton_pausar = tk.Button(frame, text="Pausar",
                                     command=lambda proceso=proceso: self.pausar(proceso), bg='sky blue')
            boton_pausar.grid(row=0, column=3)

            boton_reanudar = tk.Button(frame, text="Reanudar",
                                       command=lambda proceso=proceso: self.reanudar(proceso), bg='light green')
            boton_reanudar.grid(row=0, column=4)

            self.barras[proceso] = barra
            self.estados[proceso] = estado_label
            self.botones_pausar[proceso] = boton_pausar
            self.botones_reanudar[proceso] = boton_reanudar
            self.pausado[proceso] = False

        tk.Label(self, text="Estados", font=("Times New Roman", 14), bg='light grey').pack()

        self.cola_label = tk.Label(self, textvariable=self.cola, bg='light grey')
        self.cola_label.pack()
        self.ejecutando_label = tk.Label(self, textvariable=self.ejecutando, bg='light grey')
        self.ejecutando_label.pack()
        self.terminado_label = tk.Label(self, textvariable=self.terminado, bg='light grey')
        self.terminado_label.pack()

        self.sem_lectores = threading.Semaphore(1)  # Solo un lector puede acceder a la sección crítica a la vez
        self.sem_escritores = threading.Semaphore(0)  # Los escritores esperan a que los lectores terminen

        self.contador_lectores = len(self.procesos[:5])  # Contador para llevar la cuenta de los lectores

    def iniciar_procesos(self):
        self.actualizar_estados()
        for proceso in self.procesos[:5]:  # Los primeros 5 procesos son lectores
            hilo = threading.Thread(target=self.ejecutar_proceso, args=(proceso,))
            hilo.start()

    def ejecutar_proceso(self, proceso):
        barra = self.barras[proceso]

        if proceso in self.procesos[:5]:  # Si es un lector
            self.sem_lectores.acquire()  # Intenta adquirir el semáforo de lectores
            self.actualizar_estados()

        # Simulando la producción (carga de la barra)
        for _ in range(10):
            while self.pausado[proceso]:
                time.sleep(0.1)
            carga_actualizada = barra['value'] + 10
            barra['value'] = carga_actualizada

            self.update_idletasks()
            time.sleep(random.uniform(0.1, 1))

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

        if proceso in self.procesos[:5]:  # Si es un lector
            self.sem_lectores.release()  # Libera el semáforo de lectores
            self.contador_lectores -= 1  # Reduce el contador de lectores
            if self.contador_lectores == 0:  # Si todos los lectores han terminado
                self.iniciar_procesos_escritores()

    def iniciar_procesos_escritores(self):
        for proceso in self.procesos[5:]:  # Los siguientes 5 procesos son escritores
            hilo = threading.Thread(target=self.ejecutar_proceso, args=(proceso,))
            hilo.start()

    def pausar(self, proceso):
        self.pausado[proceso] = True
        self.actualizar_estados()

    def reanudar(self, proceso):
        self.pausado[proceso] = False
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
