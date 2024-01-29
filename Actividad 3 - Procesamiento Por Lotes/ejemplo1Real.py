import threading
import time
import datetime
from tkinter import *
from tkinter import ttk

window = Tk()
window.title('Multiprocess and lote')
window.geometry("600x400")


def lotes():
    for x in range(50):
        if my_Proceso['value'] <= 98:
            my_Proceso['value'] += 4
            ProcesoP.config(text=my_Proceso['value'])
            window.update_idletasks()
            time.sleep(0.01)



def multi():
    t1.start()



def proceso():
    for x in range(100):
        if my_Proceso['value'] <= 99:
            my_Proceso['value'] += x
            ProcesoP.config(text=my_Proceso['value'])
            window.update_idletasks()
            time.sleep(0.02)
    return



def stop():
    my_Proceso.stop()
    ProcesoP.config(text="")

lbSpace = Label(window, text=" ")
lbSpace.pack(pady=20)

#creacion de hilos
tiempo=datetime.datetime.now()
t1=threading.Thread(name="hilo_1", target=proceso)


# Contenedor para las barras de progreso
progress_frame = Frame(window)
progress_frame.pack()

# Proceso
lbProceso = Label(progress_frame, text="Proceso")
lbProceso.pack(pady=5)
my_Proceso = ttk.Progressbar(progress_frame, orient=HORIZONTAL, length=300, mode='determinate')
my_Proceso.pack()
ProcesoP = Label(progress_frame, text=" ")
ProcesoP.pack(pady=10)

# Contenedor para los botones
button_frame = Frame(window)
button_frame.pack()

# BOTONES PARA EJECUTAR PROCESOS
my_button = Button(button_frame, text="RESETEO", command=stop)
my_button.pack(side=LEFT, padx=10)
multibtn = Button(button_frame, text="MULTIPROCESO", command=multi)
multibtn.pack(side=LEFT, padx=10)
lotesbtn = Button(button_frame, text="LOTES", command=lotes)
lotesbtn.pack(side=LEFT, padx=5)

window.mainloop()
