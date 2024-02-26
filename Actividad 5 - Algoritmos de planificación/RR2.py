import tkinter as tk
from tkinter import ttk
import threading
import time
import random

class RoundRobinSimulator:
    def __init__(self, root):
        self.root = root
        self.root.title("Round Robin Simulator")

        self.num_processes = 10  # Cambiar a 10 procesos
        self.processes = [{"id": i+1, "progress": 0, "quantum": random.randint(1, 5)} for i in range(self.num_processes)]
        # Asignar quantums aleatorios entre 1 y 5 segundos

        self.create_widgets()

    def create_widgets(self):
        self.progress_bars = []
        self.quantum_labels = []  # Lista para almacenar las etiquetas del quantum

        for i in range(self.num_processes):
            progress_label = tk.Label(self.root, text=f"Proceso {i+1}:")
            progress_label.grid(row=i, column=0, padx=10, pady=5, sticky=tk.W)

            progress_bar = ttk.Progressbar(self.root, length=200, mode="determinate")
            progress_bar.grid(row=i, column=1, padx=10, pady=5, sticky=tk.W)
            self.progress_bars.append(progress_bar)

            quantum_label = tk.Label(self.root, text=f"Quantum: {self.processes[i]['quantum']}s")
            quantum_label.grid(row=i, column=2, padx=10, pady=5, sticky=tk.W)
            self.quantum_labels.append(quantum_label)

        start_button = tk.Button(self.root, text="Start", command=self.start_simulation)
        start_button.grid(row=self.num_processes, column=0, columnspan=3, pady=10)

    def start_simulation(self):
        thread = threading.Thread(target=self.simulation_thread)
        thread.start()

    def simulation_thread(self):
        total_processes = len(self.processes)
        current_process = 0

        while any(process["progress"] < 100 for process in self.processes):
            current_process_data = self.processes[current_process]

            if current_process_data["progress"] < 100:
                current_process_data["progress"] += min(current_process_data["quantum"], 100 - current_process_data["progress"])
                self.update_progress_bars()

            current_process = (current_process + 1) % total_processes
            time.sleep(0.01)  # Simula un pequeño retraso entre actualizaciones

    def update_progress_bars(self):
        for i, progress_bar in enumerate(self.progress_bars):
            progress_bar["value"] = self.processes[i]["progress"]
            self.quantum_labels[i]["text"] = f"Quantum: {self.processes[i]['quantum']}s"  # Actualiza la etiqueta del quantum
            self.root.update()


if __name__ == "__main__":
    root = tk.Tk()
    app = RoundRobinSimulator(root)
    root.mainloop()
