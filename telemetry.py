from tkinter import *
import pygame  # Tk(), Label, Canvas, Photo
import tkinter as tk
from threading import Thread  # p.start()
import threading  #
import os  # ruta = os.path.join('')
import time  # time.sleep(x)
from tkinter import messagebox  # AskYesNo ()
import tkinter.scrolledtext as tkscrolled
##### Biblioteca para el Carro
from WiFiClient import NodeMCU


# Contiene lo que se va a mostrar en la pantalla
def inicio():
    # Configuración de la ventana
    root = tk.Tk()  # Se crea una ventana
    root.geometry("704x434")  # Se le especifica un tamaño
    root.resizable(False, False)  # Hace que no se pueda modificar el ancho y largo de la ventana
    root.title("Carro")  # Se le asigna un título (el nombre que aparece en la esquina superior izquierda)

    # Crea un Canvas (llamdo C_root) donde se colocaran las cosas
    C_root = tk.Canvas(root, width=700,
                       height=430)  # Este canvas será el primero en aparecer, contiene el botón de inicio y el logo
    C_root.place(x=0, y=0)  # Establece la ubicación del canvas C_root en la ventana
    C_root.config(bg="#161D2F")

    #           _____________________________________
    # __________/Creando el cliente para NodeMCU
    myCar = NodeMCU()
    myCar.start()

    pygame.init()
    pygame.display.set_mode((100, 100))
    pygame.mixer.music.load("Sound/musica_inicio.mp3")

    temp = []

    def send(command):
        """
        Ejemplo como enviar un mensaje sencillo sin importar la respuesta
        """
        if (len(command) > 0 and command[-1] == ";"):
            myCar.send(command)
        else:
            messagebox.showwarning("Error del mensaje", "Mensaje sin caracter de finalización (';')")

            # Comando usado en el botón BotonInicio


    bg = PhotoImage(file="Image/image (2).png")
    bgs = C_root.create_image(352, 217, image=bg)

    def labelDest(List):  # Esta función borra lo que está en el canvas de manera recursiva. Función de Arturo Acuña
        if List == []:  # Condición de finalización
            return []
        else:
            (List[0]).destroy()  # Destruye el primer elemmento
            return labelDest(List[1:])  # Hace slicing de la lista (quita el primer elemento)

    def sendShowID():
        """
        Ejemplo como capturar un ID de un mensaje específico.
        """
        mns = str(E_Command.get())
        if (len(mns) > 0 and mns[-1] == ";"):
            E_Command.delete(0, 'end')
            mnsID = myCar.send(mns)
            messagebox.showinfo("Mensaje pendiente", "Intentando enviar mensaje, ID obtenido: {0}\n\
    La respuesta definitiva se obtine en un máximo de {1}s".format(mnsID, myCar.timeoutLimit))

        else:
            messagebox.showwarning("Error del mensaje", "Mensaje sin caracter de finalización (';')")

    def read():
        """
        Ejemplo de como leer un mensaje enviado con un ID específico
        """
        mnsID = str(E_read.get())
        if (len(mnsID) > 0 and ":" in mnsID):
            mns = myCar.readById(mnsID)
            if (mns != ""):
                messagebox.showinfo("Resultado Obtenido",
                                    "El mensaje con ID:{0}, obtuvo de respuesta:\n{1}".format(mnsID, mns))
                E_read.delete(0, 'end')
            else:
                messagebox.showerror("Error de ID", "No se obtuvo respuesta\n\
    El mensaje no ha sido procesado o el ID es invalido\n\
    Asegurese que el ID: {0} sea correcto".format(mnsID))

        else:
            messagebox.showwarning("Error en formato", "Recuerde ingresar el separador (':')")

    root.bind('<Return>', send)  # Vinculando tecla Enter a la función send

    #           ____________________________
    # __________/Botones de ventana principal

    Izquier = Button(C_root, text='Avanzar', command=lambda: send("dir:0;"), width=23, height=2, background="white",cursor="hand2")
    Izquier.place(x=70, y=50)
    temp.append(Izquier)

    Atras = Button(C_root, text='Retroceder', command=lambda: send("pwm:1000;"), width=23, height=2,
                   background="white", cursor="hand2")
    Atras.place(x=70, y=140)
    temp.append(Atras)

    Btn = Button(C_root, text='Derecha', command=lambda: send("dir:1;"), width=23, height=2, background="white",cursor="hand2")
    Btn.place(x=70, y=230)
    temp.append(Btn)

    Derecha = Button(C_root, text='Izquierda', command=lambda: send("dir:-1;"), width=23, height=2,
                     background="white", cursor="hand2")
    Derecha.place(x=70, y=320)
    temp.append(Derecha)

    root.mainloop()


inicio()