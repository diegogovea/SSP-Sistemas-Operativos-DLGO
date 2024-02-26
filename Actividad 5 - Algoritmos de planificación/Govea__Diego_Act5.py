import tkinter as tk
from tkinter import ttk
import threading
import time
import random

class RoundRobinSimulator:
    def __init__(self, root):
        self.root = root
        self.root.title("Round Robin Simulator")

        self.num_processes = 10
        self.processes = [{"id": i+1, "progress": 0, "quantum": random.randint(1, 5), "paused": False} for i in range(self.num_processes)]
        # Asignar quantums aleatorios entre 1 y 5 segundos
        self.processes.sort(key=lambda x: x["quantum"])  # Ordenar por tiempo de quantum

        self.create_widgets()

    def create_widgets(self):
        self.progress_bars = []
        self.quantum_labels = []
        self.pause_buttons = []
        self.resume_buttons = []
        self.cancel_buttons = []

        for i in range(self.num_processes):
            progress_label = tk.Label(self.root, text=f"Proceso {i+1}:")
            progress_label.grid(row=i, column=0, padx=10, pady=5, sticky=tk.W)

            progress_bar = ttk.Progressbar(self.root, length=200, mode="determinate")
            progress_bar.grid(row=i, column=1, padx=10, pady=5, sticky=tk.W)
            self.progress_bars.append(progress_bar)

            quantum_label = tk.Label(self.root, text=f"Quantum: {self.processes[i]['quantum']}s")
            quantum_label.grid(row=i, column=2, padx=10, pady=5, sticky=tk.W)
            self.quantum_labels.append(quantum_label)

            pause_button = tk.Button(self.root, text="Pausar", command=lambda i=i: self.pause_process(i))
            pause_button.grid(row=i, column=3, padx=10, pady=5, sticky=tk.W)
            self.pause_buttons.append(pause_button)

            resume_button = tk.Button(self.root, text="Reanudar", command=lambda i=i: self.resume_process(i))
            resume_button.grid(row=i, column=4, padx=10, pady=5, sticky=tk.W)
            self.resume_buttons.append(resume_button)

            cancel_button = tk.Button(self.root, text="Cancelar", command=lambda i=i: self.cancel_process(i))
            cancel_button.grid(row=i, column=5, padx=10, pady=5, sticky=tk.W)
            self.cancel_buttons.append(cancel_button)

        start_button = tk.Button(self.root, text="Start", command=self.start_simulation)
        start_button.grid(row=self.num_processes, column=0, columnspan=6, pady=10)

    def start_simulation(self):
        thread = threading.Thread(target=self.simulation_thread)
        thread.start()

    def simulation_thread(self):
        for current_process_data in self.processes:
            while current_process_data["progress"] < 100:
                if current_process_data["paused"]:
                    time.sleep(1)  # Esperar si el proceso está pausado
                else:
                    current_process_data["progress"] += min(current_process_data["quantum"], 100 - current_process_data["progress"])
                    self.update_progress_bars()
                    time.sleep(0.01)  # Simula un pequeño retraso entre actualizaciones

    def pause_process(self, process_index):
        self.processes[process_index]["paused"] = True
        print(f"Proceso {process_index + 1} pausado")

    def resume_process(self, process_index):
        self.processes[process_index]["paused"] = False
        print(f"Proceso {process_index + 1} reanudado")

    def cancel_process(self, process_index):
        # Puedes implementar la lógica de cancelar aquí
        print(f"Proceso {process_index + 1} cancelado")

    def update_progress_bars(self):
        for i, progress_bar in enumerate(self.progress_bars):
            progress_bar["value"] = self.processes[i]["progress"]
            self.quantum_labels[i]["text"] = f"Quantum: {self.processes[i]['quantum']}s"
            self.root.update()


if __name__ == "__main__":
    root = tk.Tk()
    app = RoundRobinSimulator(root)
    root.mainloop()
