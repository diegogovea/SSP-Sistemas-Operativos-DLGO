#Diego León Govea Ortiz
#Administrador de Procesos
#Act 4
#SSP DE SISTEMAS OPERATIVOS


import threading
import time
from tkinter import *
from tkinter import ttk

window = Tk()
window.title('INICIAR PROCESOS POR LOTES')
window.geometry("600x400")

# Variable compartida para indicar si se debe detener el hilo de video
stop_proceso = False
stop_proceso2 = False
stop_proceso3 = False


def Start():
    # Crear nuevos hilos cada vez que se hace clic en el botón
    t1 = threading.Thread(name="hilo_1", target=video)
    t2 = threading.Thread(name="hilo_2", target=song)
    t3 = threading.Thread(name="hilo_3", target=img)

    # Start los nuevos hilos
    t1.start()
    t2.start()
    t3.start()

    lbProceso.config(text="En progreso")
    lbProceso2.config(text="En progreso")
    lbProceso3.config(text="En progreso")

#Esta es la definicion de la función donde se detienen los procesos.
def stop():
    global stop_proceso
    stop_proceso = True
    lbProceso.config(text="Pausado")
    global stop_proceso2
    stop_proceso2 = True
    lbProceso3.config(text="Pausado")
    global stop_proceso3
    stop_proceso3 = True
    lbProceso2.config(text="Pausado")

#Esta es la definicion de la función donde se reanudan los procesos

def resume():
    global stop_proceso
    stop_proceso = False
    global stop_proceso2
    stop_proceso2 = False
    global stop_proceso3
    stop_proceso3 = False
    lbProceso.config(text="In progress")
    t1 = threading.Thread(name="hilo_1", target=video)
    t2 = threading.Thread(name="hilo_2", target=song)
    t3 = threading.Thread(name="hilo_3", target=img)
    t1.start()
    t2.start()
    t3.start()

#Esta es la definicion de la función donde se resetean los procesos.

def reset():
    my_prVideo.stop()
    my_prVideo['value'] = 0
    PorcentMP.config(text="")
    lbProceso.config(text="Reseteado")
    my_prIMG.stop()
    my_prIMG['value'] = 0
    PorcentIMG.config(text="")
    lbProceso3.config(text="Reseteado")
    my_prSong.stop()
    my_prSong['value'] = 0
    PorcentAudio.config(text="")
    lbProceso2.config(text="Reseteado")

#Aqui se establecen los procesos que vamos a utilizar

def video():
    global stop_proceso
    for x in range(100):
        if my_prVideo['value'] <= 99:
            if not stop_proceso:
                my_prVideo['value'] += x
                PorcentMP.config(text=my_prVideo['value'])
                window.update_idletasks()
                time.sleep(0.2)
            else:
                break
        else:
            lbProceso.config(text="Terminado")

#Aqui se establece el proceso 2

def song():
    for x in range(100):
        if my_prSong['value'] <= 99:
            if not stop_proceso3:
                my_prSong['value'] += x
                PorcentAudio.config(text=my_prSong['value'])
                window.update_idletasks()
            time.sleep(0.5)
        else:
            lbProceso2.config(text="Terminado")
    return

#Aqui se establece el proceso 3
def img():
    for x in range(100):
        if my_prIMG['value'] <= 99:
            if not stop_proceso2:
                my_prIMG['value'] += x
                PorcentIMG.config(text=my_prIMG['value'])
                window.update_idletasks()
            time.sleep(0.1)
        else:
            lbProceso3.config(text="Terminado")
    return


lbSpace = Label(window, text=" ")
lbSpace.pack(pady=20)

# PROCESO 1
lbProceso2 = Label(window, text="PROCESO 1")
lbProceso2.pack(pady=5)
my_prSong = ttk.Progressbar(window, orient=HORIZONTAL,length=300, mode='determinate')
my_prSong.pack()
PorcentAudio = Label(window, text=" ")
PorcentAudio.pack(pady=10)

# PROCESO 2
lbProceso = Label(window, text="PROCESO 2")
lbProceso.pack(pady=5)
my_prVideo = ttk.Progressbar(window, orient=HORIZONTAL,length=300, mode='determinate')
my_prVideo.pack()
PorcentMP = Label(window, text=" ")
PorcentMP.pack(pady=10)

# PROCESO 3
lbProceso3 = Label(window, text="PROCESO 3")
lbProceso3.pack(pady=5)
my_prIMG = ttk.Progressbar(window, orient=HORIZONTAL,length=300, mode='determinate')
my_prIMG.pack()
PorcentIMG = Label(window, text=" ")
PorcentIMG.pack(pady=10)

# Contenedor para los botones
button_frame = Frame(window)
button_frame.pack()

# DECLARACIÓN DE BOTONES
Startbtn = Button(button_frame, text="COMENZAR", command=Start)
Startbtn.pack(side=LEFT, padx=5)
stop_button = Button(button_frame, text="PARAR", command=stop)
stop_button.pack(side=LEFT, padx=5)
resume_button = Button(button_frame, text="REANUDAR", command=resume)
resume_button.pack(side=LEFT, padx=5)
reset_button = Button(button_frame, text="RESETEAR", command=reset)
reset_button.pack(side=LEFT, padx=5)

window.mainloop()
