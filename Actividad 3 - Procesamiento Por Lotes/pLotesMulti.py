#Diego León Govea Ortiz
#Programación en Lotes y Multiprogramación
#Act 3
#SSP DE SISTEMAS OPERATIVOS

import threading
import time
import datetime
from tkinter import *
from tkinter import ttk

window = Tk()
window.title('MULTIPROCESO Y POR LOTES')
window.geometry("600x400")


def lotes(): #Aqui se ejecuta el programa cuando es por lotes
    valor = NoProcesos.get()
    num = int(valor)
    print(num)
    #En estos If verifica que numero de procesos se ingreso en la caja de texto.
    if num>=1:
        for x in range(50):
            if my_Proceso['value'] <= 98:
                my_Proceso['value'] += 4
                ProcesoP.config(text=my_Proceso['value'])
                window.update_idletasks()
                time.sleep(0.01) #tiempo que tardará en ejecutarse el proceso
    if num>=2:
        for x in range(50):
            if my_Proceso1['value'] <= 98:
                my_Proceso1['value'] += 4
                ProcesoP1.config(text=my_Proceso1['value'])
                window.update_idletasks()
                time.sleep(0.01)
    if num>=3:
        for x in range(50):
            if my_Proceso2['value'] <= 98:
                my_Proceso2['value'] += 4
                ProcesoP2.config(text=my_Proceso2['value'])
                window.update_idletasks()
                time.sleep(0.06)
    if num>=4:
        for x in range(50):
            if my_Proceso3['value'] <= 98:
                my_Proceso3['value'] += 4
                ProcesoP3.config(text=my_Proceso3['value'])
                window.update_idletasks()
                time.sleep(0.1)
    if num>=5:
        for x in range(50):
            if my_Proceso4['value'] <= 98:
                my_Proceso4['value'] += 4
                ProcesoP4.config(text=my_Proceso4['value'])
                window.update_idletasks()
                time.sleep(0.05)
    if num>=6:
        for x in range(50):
            if my_Proceso5['value'] <= 98:
                my_Proceso5['value'] += 4
                ProcesoP5.config(text=my_Proceso5['value'])
                window.update_idletasks()
                time.sleep(0.01)



def multi(): #Aqui se ejecutan los multiprocesos
    valor=NoProcesos.get()
    num=int(valor)
    print(num)
    #los if indican hasta donde se dejará de ejecutar dependiendo de los procesos seleccionados
    if num>=1:
        t1.start()
    if num>=2:
        t2.start()
    if num>=3:
        t3.start()
    if num>=4:
        t4.start()
    if num>=5:
        t5.start()
    if num>=6:
        t6.start()


#Aqui definimos los procesos como el por lotes, pero de forma individual
def proceso():
    for x in range(100):
        if my_Proceso['value'] <= 99:
            my_Proceso['value'] += x
            ProcesoP.config(text=my_Proceso['value'])
            window.update_idletasks()
            time.sleep(0.02)#tiempo que tardará en ejecutarse el proceso
    return
def proceso1():
    for x in range(100):
        if my_Proceso1['value'] <= 99:
            my_Proceso1['value'] += x
            ProcesoP1.config(text=my_Proceso1['value'])
            window.update_idletasks()
            time.sleep(0.02)#tiempo que tardará en ejecutarse el proceso
    return
def proceso2():
    for x in range(100):
        if my_Proceso2['value'] <= 99:
            my_Proceso2['value'] += x
            ProcesoP2.config(text=my_Proceso2['value'])
            window.update_idletasks()
            time.sleep(0.02)#tiempo que tardará en ejecutarse el proceso
    return
def proceso3():
    for x in range(100):
        if my_Proceso3['value'] <= 99:
            my_Proceso3['value'] += x
            ProcesoP3.config(text=my_Proceso3['value'])
            window.update_idletasks()
            time.sleep(0.2)#tiempo que tardará en ejecutarse el proceso
    return
def proceso4():
    for x in range(100):
        if my_Proceso4['value'] <= 99:
            my_Proceso4['value'] += x
            ProcesoP4.config(text=my_Proceso4['value'])
            window.update_idletasks()
            time.sleep(0.05)#tiempo que tardará en ejecutarse el proceso
    return
def proceso5():
    for x in range(100):
        if my_Proceso5['value'] <= 99:
            my_Proceso5['value'] += x
            ProcesoP5.config(text=my_Proceso5['value'])
            window.update_idletasks()
            time.sleep(0.1)#tiempo que tardará en ejecutarse el proceso
    return



def stop():#Aqui se reinicia la barra de proceso de todos los procesos
    my_Proceso.stop()
    ProcesoP.config(text="")
    my_Proceso1.stop()
    ProcesoP1.config(text="")
    my_Proceso2.stop()
    ProcesoP2.config(text="")
    my_Proceso3.stop()
    ProcesoP3.config(text="")
    my_Proceso4.stop()
    ProcesoP4.config(text="")
    my_Proceso5.stop()
    ProcesoP5.config(text="")

lbSpace = Label(window, text=" ")
lbSpace.pack(pady=20)

#creacion de hilos
tiempo=datetime.datetime.now()
t1=threading.Thread(name="hilo_1", target=proceso)
t2=threading.Thread(name="hilo_2", target=proceso1)
t3=threading.Thread(name="hilo_3", target=proceso2)
t4=threading.Thread(name="hilo_4", target=proceso3)
t5=threading.Thread(name="hilo_5", target=proceso4)
t6=threading.Thread(name="hilo_6", target=proceso5)


# Contenedor para las barras de progreso
progress_frame = Frame(window)
progress_frame.pack()

#Ingresar procesos
NoProceso = Label(progress_frame, text="Ingresa el numero de Procesos")
NoProceso.pack(pady=5)
NoProcesos = Entry(progress_frame)
NoProcesos.pack(pady=5)

# Procesos
lbProceso = Label(progress_frame, text="Proceso")
lbProceso.pack(pady=5)
my_Proceso = ttk.Progressbar(progress_frame, orient=HORIZONTAL, length=300, mode='determinate')
my_Proceso.pack()
ProcesoP = Label(progress_frame, text=" ")
ProcesoP.pack(pady=10)

# Proceso1
lbProceso1 = Label(progress_frame, text="Proceso 2")
lbProceso1.pack(pady=5)
my_Proceso1 = ttk.Progressbar(progress_frame, orient=HORIZONTAL, length=300, mode='determinate')
my_Proceso1.pack()
ProcesoP1 = Label(progress_frame, text=" ")
ProcesoP1.pack(pady=10)

# Proceso2
lbProceso2 = Label(progress_frame, text="Proceso 3")
lbProceso2.pack(pady=5)
my_Proceso2 = ttk.Progressbar(progress_frame, orient=HORIZONTAL, length=300, mode='determinate')
my_Proceso2.pack()
ProcesoP2 = Label(progress_frame, text=" ")
ProcesoP2.pack(pady=10)

# Proceso3
lbProceso3 = Label(progress_frame, text="Proceso 4")
lbProceso3.pack(pady=5)
my_Proceso3 = ttk.Progressbar(progress_frame, orient=HORIZONTAL, length=300, mode='determinate')
my_Proceso3.pack()
ProcesoP3 = Label(progress_frame, text=" ")
ProcesoP3.pack(pady=10)

# Proceso4
lbProceso4 = Label(progress_frame, text="Proceso 5")
lbProceso4.pack(pady=5)
my_Proceso4 = ttk.Progressbar(progress_frame, orient=HORIZONTAL, length=300, mode='determinate')
my_Proceso4.pack()
ProcesoP4 = Label(progress_frame, text=" ")
ProcesoP4.pack(pady=10)

# Proceso5
lbProceso5 = Label(progress_frame, text="Proceso 6")
lbProceso5.pack(pady=5)
my_Proceso5 = ttk.Progressbar(progress_frame, orient=HORIZONTAL, length=300, mode='determinate')
my_Proceso5.pack()
ProcesoP5 = Label(progress_frame, text=" ")
ProcesoP5.pack(pady=10)

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
