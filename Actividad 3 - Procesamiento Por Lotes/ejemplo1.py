import tkinter as tk
import time

class BatchProcessorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Batch Processor")
        self.master.geometry("400x150")

        self.canvas = tk.Canvas(master, width=400, height=50, bg="white")
        self.canvas.pack(pady=5)

        self.label = tk.Label(master, text="Proceso actual:")
        self.label.pack(pady=5)

        self.batch1 = ["proceso 1", "proceso 2", "proceso 3"]
        self.batch2 = ["proceso 4", "proceso 5", "proceso 6"]

        self.progress_bar = self.canvas.create_rectangle(0, 0, 0, 50, fill="green")

        self.start_button = tk.Button(master, text="Iniciar Procesos", command=self.start_processes)
        self.start_button.pack(pady=10)

    def execute_process(self, process):
        process_width = 400 / (len(self.batch1) + len(self.batch2))
        self.label.config(text="Proceso actual: " + process)
        self.canvas.coords(self.progress_bar, (self.canvas.coords(self.progress_bar)[2], 0, self.canvas.coords(self.progress_bar)[2] + process_width, 50))
        self.master.update()
        time.sleep(1)

    def start_processes(self):
        for process in self.batch1:
            self.execute_process(process)

        for process in self.batch2:
            self.execute_process(process)

        self.label.config(text="Proceso actual: ")
        self.canvas.coords(self.progress_bar, (0, 0, 0, 0))  # Reiniciar la barra de progreso
        self.master.update()

if __name__ == "__main__":
    root = tk.Tk()
    app = BatchProcessorApp(root)
    root.mainloop()
