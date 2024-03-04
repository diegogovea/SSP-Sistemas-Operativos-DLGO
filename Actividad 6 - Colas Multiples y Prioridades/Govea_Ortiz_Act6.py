import tkinter as tk
from tkinter import ttk
import threading
import time


def proceso1():
    for i in range(101):
        time.sleep(0.1)
        progress1['value'] = i
        root.update_idletasks()


def proceso2():
    time.sleep(11)
    for i in range(101):
        time.sleep(0.1)
        progress2['value'] = i
        root.update_idletasks()


def proceso3():
    for i in range(101):
        time.sleep(0.1)
        progress3['value'] = i
        root.update_idletasks()


def proceso4():
    time.sleep(11)
    for i in range(101):
        time.sleep(0.2)
        progress4['value'] = i
        root.update_idletasks()


def iniciar_procesos1():
    thread1 = threading.Thread(target=proceso1)
    thread2 = threading.Thread(target=proceso2)

    thread1.start()
    thread2.start()


def iniciar_procesos2():
    thread3 = threading.Thread(target=proceso3)
    thread4 = threading.Thread(target=proceso4)

    thread3.start()
    thread4.start()


root = tk.Tk()
root.title("ACTIVIDAD 6")

# Sección para procesos 1 y 2
frame1 = ttk.Frame(root, padding=(10, 10))
frame1.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

label1 = ttk.Label(frame1, text="Proceso 1:", foreground="navy")
label1.grid(row=0, column=0, pady=5, sticky='w')

prioridad1_label = ttk.Label(frame1, text="Prioridad 1", foreground="navy")
prioridad1_label.grid(row=1, column=0, pady=5, sticky='w')

progress1 = ttk.Progressbar(frame1, length=200, mode='determinate', style="blue.Horizontal.TProgressbar")
progress1.grid(row=0, column=1, pady=5, sticky='w')

label2 = ttk.Label(frame1, text="Proceso 2:", foreground="navy")
label2.grid(row=2, column=0, pady=5, sticky='w')

prioridad2_label = ttk.Label(frame1, text="Prioridad 3", foreground="navy")
prioridad2_label.grid(row=3, column=0, pady=5, sticky='w')

progress2 = ttk.Progressbar(frame1, length=200, mode='determinate', style="blue.Horizontal.TProgressbar")
progress2.grid(row=2, column=1, pady=5, sticky='w')

button_frame1 = ttk.Frame(frame1)
button_frame1.grid(row=8, column=0, columnspan=2, pady=10)

button1 = ttk.Button(button_frame1, text="Iniciar Prioridades", command=iniciar_procesos1, style="blue.TButton")
button1.grid(row=0, column=0, padx=10)

# Sección para procesos 3 y 4
frame2 = ttk.Frame(root, padding=(10, 10))
frame2.grid(row=0, column=1, sticky=(tk.W, tk.E, tk.N, tk.S))

label3 = ttk.Label(frame2, text="Proceso 3:", foreground="forest green")
label3.grid(row=4, column=0, pady=5, sticky='w')

prioridad3_label = ttk.Label(frame2, text="Prioridad 1", foreground="forest green")
prioridad3_label.grid(row=5, column=0, pady=5, sticky='w')

progress3 = ttk.Progressbar(frame2, length=200, mode='determinate', style="green.Horizontal.TProgressbar")
progress3.grid(row=4, column=1, pady=5, sticky='w')

label4 = ttk.Label(frame2, text="Proceso 4:", foreground="forest green")
label4.grid(row=6, column=0, pady=5, sticky='w')

prioridad4_label = ttk.Label(frame2, text="Prioridad 1", foreground="forest green")
prioridad4_label.grid(row=7, column=0, pady=5, sticky='w')

progress4 = ttk.Progressbar(frame2, length=200, mode='determinate', style="green.Horizontal.TProgressbar")
progress4.grid(row=6, column=1, pady=5, sticky='w')

button_frame2 = ttk.Frame(frame2)
button_frame2.grid(row=8, column=0, columnspan=2, pady=10)

button2 = ttk.Button(button_frame2, text="Iniciar Multiples", command=iniciar_procesos2, style="green.TButton")
button2.grid(row=0, column=0, padx=10)

style = ttk.Style()
style.configure("blue.Horizontal.TProgressbar", troughcolor="lightblue", background="sky blue", thickness=20)
style.configure("green.Horizontal.TProgressbar", troughcolor="lightgreen", background="lime green", thickness=20)
style.configure("black.TButton", background="deep sky blue", foreground="white")
style.configure("black.TButton", background="lime green", foreground="white")

root.mainloop()
