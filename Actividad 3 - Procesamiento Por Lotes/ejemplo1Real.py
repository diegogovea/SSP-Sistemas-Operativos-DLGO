import threading
import time
import datetime
from tkinter import *
from tkinter import ttk

window=Tk()
window.title('Multiprocess and lote')
window.geometry("600x400")


def lotes():
    #print
    for x in range(50):
        if(my_prSong['value']<=98):
            my_prSong['value']+=4
            PorcentAudio.config( text=my_prSong['value'])
            window.update_idletasks()
            time.sleep(0.01)#pausas de 1ms

def multi():
    t3.start()
def song():
    for x in range(100):
        if(my_prSong['value']<=99):
                my_prSong['value']+=x
                PorcentAudio.config( text=my_prSong['value'])
                window.update_idletasks()
                time.sleep(0.02)
    return

def stop():
    my_prSong.stop()
    PorcentAudio.config( text="")

lbSpace= Label(window, text=" ")
lbSpace.pack(pady=20)

#creacion de hilos
tiempo=datetime.datetime.now()

t3=threading.Thread(name="hilo_3", target=song)

button_frame = Frame(window)
button_frame.pack()

#AUDIO

lbCancion= Label(window, text="Deleting song")
lbCancion.pack(pady=5)
my_prSong = ttk.Progressbar(window, orient=HORIZONTAL,length=300, mode='determinate')
my_prSong.pack()



PorcentAudio= Label(window, text=" ")
PorcentAudio.pack(pady=10)



#BOTONES PARA EJECUTAR PROCESOS
my_button=Button(button_frame, text="RESET", command=stop)
my_button.pack(side=LEFT, padx=20)
multibtn=Button(button_frame, text="MULTIPROCES", command=multi)
multibtn.pack(side=LEFT, padx=5)
lotesbtn=Button(button_frame, text="LOTES", command=lotes)
lotesbtn.pack(side=LEFT, padx=5)

window.mainloop()
