import tkinter as tk
from tkinter import *
import pygame
from pygame import mixer
from PIL import ImageTk, Image
import subprocess
import sys

"""Nota para de desarrollador:!!!!!!!!!!!!!!!
Esta archivo(Proyecto Parte grafica_ingles.py) junto con 'Proyecto Parte grafica2.py' son archivos hijos de 'Proyecto Parte grafica.py', (nótese la diferencia de nombres),
los tres archivos cuentan con el mismo código, la diferencia es que los dos primeros mencionados no tienen música de fondo, sin embargo, tiene el resto de las propiedades
que el archivo madre. Solamente fueron suprimidas las lineas de código que le otorgaban a los dos archivos música de fondo. Los sonidos que se reproducen cuando el cursor
entra en el área del botón se mantienen
La decisión numero 1 de este cambio es debido a que durante la implementación del idioma inglés, se encontró problemas con cambiar el idioma en una misma carpeta.
La decisión numero 2 es debido a que se encontró problemas para que se mantuviera solo una pista musical durante el direccionamiento de archivos, ya que se superponía una
canción sobre la otra, produciendo un efecto de eco, para eliminar esto, se decidió que solo el archivo madre contendrá la pista musica, ya que esta le proporciona
el soundtrack al resto del código

"""

window = tk.Tk()  # Creación ventana principal
window.attributes("-fullscreen", True)  # Pantalla completa

def esc(event):
    window.destroy()

window.bind('<Escape>', esc)
window.configure(cursor="star")

fondo = tk.PhotoImage(file="Image/fotor_2023-6-4_22_5_7.png")
w, h = fondo.width(), fondo.height()
window.geometry("%dx%d+0+0" % (w, h))
background_label = tk.Label(window, image=fondo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)


def salir():
    window.destroy()

def abrir_ventana():
    ventana_secundaria = tk.Toplevel()
    ventana_secundaria.title("Ventana Secundaria")
    ventana_secundaria.overrideredirect(True)

    screen_width = ventana_secundaria.winfo_screenwidth()
    screen_height = ventana_secundaria.winfo_screenheight()

    window_width = 400
    window_height = 300
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2

    ventana_secundaria.geometry(f"{window_width}x{window_height}+{x}+{y}")

    imagen_fondo = Image.open("Image/image (8) (1).png")
    imagen_fondo = imagen_fondo.resize((400, 300))
    fondo = ImageTk.PhotoImage(imagen_fondo)

    fondo_label = tk.Label(ventana_secundaria, image=fondo)
    fondo_label.place(x=0, y=0, relwidth=1, relheight=1)

    def salir1():
        ventana_secundaria.destroy()

    boton1 = tk.Button(ventana_secundaria, text="Persist Behind the Wheel", fg="gray1",
                       bg="green4",
                       relief="sunken",
                       font=("System 18 bold"),
                       cursor="exchange", command=salir1)
    boton1.pack(pady=10)

    def salir():
        # Función que se encarga del parámetro salir, mediante un botón usando el método "destroy"
        # Eentrada: Pulsar "boton1"presente dos líneas más abajo
        # Salida: Se deja de ejecutar el juego
        window.destroy()  # Metodo que se encarga de salir del juego
    boton2 = tk.Button(ventana_secundaria, text="Cease the control", fg="gray1",
                       bg="red3",
                       relief="sunken",
                       font=("System 18 bold"),
                       cursor="exchange", command=salir)
    boton2.pack(pady=10)

    # Ejecutar el bucle de la ventana principal
    ventana_secundaria.mainloop()

boton1=tk.Button(window, text="Cease the control", #Parámetros para configurar el botón de salir
                 command=abrir_ventana,
                 fg="gray1",
                 bg="DodgerBlue4",
                 relief="sunken",
             font=("System 18 bold"),
                 cursor="exchange")
boton1.pack()       #Se coloca el botón sobre el Canvas
boton1.place(x=1075,y=730, height=40, width=289) #Se ajusta el tamaño
def change_color_enter(event):
    boton1.configure(bg="white")
def change_color_leave(event):
    boton1.configure(bg="purple")
boton1.bind("<Enter>", change_color_enter)
boton1.bind("<Leave>", change_color_leave)
def play_sound(event):
    pygame.mixer.Channel(4).play(pygame.mixer.Sound("Sound/SD_NAVIGATE_53.mp3"))
def resume_music(event):
    pygame.mixer.music.unpause()  # Reanudar la música de fondo
boton1.bind("<Enter>", play_sound)
boton1.bind("<Leave>", resume_music)
pygame.mixer.init()



def acerca_de():
    # Crear nueva pestaña sobre los autores del proyecto
    # Entrada: Presionar botón 2, este se configura más abajo
    # Salida: Muestra al usuario información sobre los desarrolladores
    acerca_de = Toplevel()          #Se define el método con el que se va a trabajar: TopLevel
    acerca_de.attributes("-fullscreen", True) #Se ejecuta en pantalla completa
    imagen = Image.open("Image/acerca de_ingles.png")    # Cargar la imagen de fondo
    imagen = ImageTk.PhotoImage(imagen)
    fondo = Label(acerca_de, image=imagen)    # Superpone la imagen sobre la ventana de acerca de
    fondo.place(x=0, y=0, relwidth=1, relheight=1)
    acerca_de.configure(cursor = "star")    #Se confugura el cursor

    def salir():
        # Se utiliza la función construida anteriormente "salir" para volver a la pantalla principal
        # Entrada: Presinar "Volver" desde la pestaña "Acerca_de"
        # Salida: Devuelve al usuario a la ventana principal
        acerca_de.destroy()

    boton1 = tk.Button(acerca_de, text="Go back to start", # Se configura el botón "Volver" de "Acerca de"
                 command=salir,
                 fg="snow",
                 bg="SkyBlue3",
                 relief="sunken",
                 font=("System 30 bold"),
                 cursor="exchange")
    boton1.pack()       #Se posiciona el botón "Volver"
    boton1.place(x=5, y=8, height=50, width=350)
    def change_color_enter(event):
        boton1.configure(bg="SkyBlue1", fg="white")
    def change_color_leave(event):
        boton1.configure(bg="SkyBlue3", fg="white")
    boton1.bind("<Enter>", change_color_enter)
    boton1.bind("<Leave>", change_color_leave)

    acerca_de.mainloop()    # Mostrar ventana "acerca_de"
boton2=tk.Button(window, text="About",fg="snow",  #Se configura el botón "acerca_de" en la pantalla principal
                 bg="turquoise4",
                 relief="sunken",
                 font=("System 30 bold"),command=acerca_de,
                 cursor="exchange")
boton2.pack()         #Se posiciona el botón "Acerca_de"
boton2.place(x=1000,y=90, height=60, width=220)
def change_color_enter(event):
    boton2.configure(bg="sea green")
def change_color_leave(event):
    boton2.configure(bg="turquoise4")
boton2.bind("<Enter>", change_color_enter)
boton2.bind("<Leave>", change_color_leave)
def play_sound(event):
    pygame.mixer.Channel(1).play(pygame.mixer.Sound("Sound/misc308 (mp3cut.net) (1).mp3"))
def resume_music(event):
    pygame.mixer.music.unpause()  # Reanudar la música de fondo
boton2.bind("<Enter>", play_sound)
boton2.bind("<Leave>", resume_music)
pygame.mixer.init()



def como_jugar():
    # Se crea una nueva pestaña sobre cómo jugar
    # Entrada: Se presiona el botón "Cómo jugar"
    # Salida: muestra al usuario las instrucciones de juego
    como_jugar = Toplevel()         # Se define el método
    como_jugar.attributes("-fullscreen", True)          # Se configura a pantalla completa
    imagen = Image.open("Image/como jugar_ingles.png")    # Cargar la imagen de fondo
    imagen = ImageTk.PhotoImage(imagen)
    fondo = Label(como_jugar, image=imagen)    # Superpone la imagen sobre la ventana "Cómo jugar"
    fondo.place(x=0, y=0, relwidth=1, relheight=1)
    como_jugar.configure(cursor = "star")

    def salir():
        # Se utiliza la función construida anteriormente "salir" para volver a la pantalla principal
        # Entrada: Presinar "Volver" desde la pestaña "Cómo jugar"
        # Salida: Devuelve al usuario a la ventana principal
        como_jugar.destroy()

    boton1 = tk.Button(como_jugar, text="Go back to start", # Se configura el botón "Volver" de "Cómo jugar"
                 command=salir,
                 fg="snow",
                 bg="SkyBlue3",
                 relief="sunken",
                 font=("System 30 bold"),
                 cursor="exchange")
    boton1.pack() #Se posiciona el botón "Volver"
    boton1.place(x=990, y=15, height=50, width=350)
    def change_color_enter(event):
        boton1.configure(bg="SkyBlue1", fg="white")
    def change_color_leave(event):
        boton1.configure(bg="SkyBlue3", fg="white")
    boton1.bind("<Enter>", change_color_enter)
    boton1.bind("<Leave>", change_color_leave)

    como_jugar.mainloop()  #Muestra ventana "como_jugar"
boton3=tk.Button(window, text="How to Play?",fg="snow", #Se configura el botón "Como jugar"
                 bg="turquoise4",
                 relief="sunken",
                 font=("System 30 bold"), command=como_jugar,
                 cursor="exchange")
boton3.pack
boton3.place(x=1090,y=180, height=60, width=270)
def change_color_enter(event):
    boton3.configure(bg="sea green")
def change_color_leave(event):
    boton3.configure(bg="turquoise4")
boton3.bind("<Enter>", change_color_enter)
boton3.bind("<Leave>", change_color_leave)
def play_sound(event):
    pygame.mixer.Channel(2).play(pygame.mixer.Sound("Sound/misc308 (mp3cut.net) (1).mp3"))
def resume_music(event):
    pygame.mixer.music.unpause()  # Reanudar la música de fondo
boton3.bind("<Enter>", play_sound)
boton3.bind("<Leave>", resume_music)
pygame.mixer.init()


def detener():
    # Función para detener la ventana actual
    window.destroy()

def abrir_nueva_ventana():
    # Función para abrir una nueva ventana
    detener()  # Detener la ventana actual
    subprocess.call(["python", "telemetry.py"])

boton_principal = tk.Button(window, text="LET´S RACE!!",
                            fg="white",
                            bg="steel blue",
                            relief="sunken",
                            font=("System 49 bold"),
                            command=abrir_nueva_ventana,
                            cursor="exchange")
boton_principal.pack()
boton_principal.place(x=910,y=320, height=80, width=440)
def change_color_enter(event):
    boton_principal.configure(bg="black", fg="red")
def change_color_leave(event):
    boton_principal.configure(bg="steel blue", fg= "white")
boton_principal.bind("<Enter>", change_color_enter)
boton_principal.bind("<Leave>", change_color_leave)


def abrir():
    mixer.music.stop()
    # Cerrar ventana principal
    window.destroy()
    # Abrir el archivo "Proyecto Parte grafica_ingles.py" como una nueva ventana
    subprocess.call(["python", "Proyecto Parte grafica2.py"])



boton_ingles = tk.Button(window, text="Español",
                         fg="white",
                         bg="dark slate gray",
                         relief="sunken",
                         font=("System 20 bold"),
                         cursor="exchange",
                         command=abrir
                         )
boton_ingles.pack()
boton_ingles.place(x=1242,y=0, height=40, width=120)
def play_sound(event):
    pygame.mixer.Channel(3).play(pygame.mixer.Sound("Sound/SD_NAVIGATE_53.mp3"))
def resume_music(event):
    pygame.mixer.music.unpause()  # Reanudar la música de fondo
boton_ingles.bind("<Enter>", play_sound)
boton_ingles.bind("<Leave>", resume_music)
pygame.mixer.init()




window.mainloop()
