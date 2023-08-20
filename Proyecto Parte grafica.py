import tkinter as tk
from tkinter import *
import pygame
from PIL import ImageTk, Image
import subprocess

window = tk.Tk()  # Creación ventana principal
window.attributes("-fullscreen", True)  # Pantalla completa

def esc(event): #Configurar salida rápida usando la tecla Esc
    window.destroy()
window.bind('<Escape>', esc)
window.configure(cursor="star") #Se configura la forma del cursor

fondo = tk.PhotoImage(file="Image/fotor_2023-6-4_22_5_7.png") #Se calrga el fondo de la imagen principal
w, h = fondo.width(), fondo.height() #Variable que obtiene el ancho y la largo de la imagen
window.geometry("%dx%d+0+0" % (w, h)) # Configura la geometría de la ventana utilizando el método geometry() para especificar el tamaño de la ventana en píxeles
background_label = tk.Label(window, image=fondo) #Se crea la etiqueta que muestra la imagen de fondo
background_label.place(x=0, y=0, relwidth=1, relheight=1) # Coloca la etiqueta background_label en la ventana de manera que establece los atributos relwidth y relheight en 1, ocupando toda la ventana.

# Establecer música de inicio importante la biblioteca Pygame
pygame.init() # Inicializa la librería Pygame
volumen = 0.5 #Vlolumen predeterminado inicial de 0.5( el valor va desde 0.0 hasta 1.0)

def cambiar_volumen():
    # Instituto tecnológico de Costa Rica
    # Ingeniería en Computadores
    # Autor:/ Bryan Monge Navarro - 2023026192 / Joaquín Ramirez Sequeira - 2023301855
    # Ultima fecha de modificación:/ 13/06/2023
    # Módulo:/ Función que comprueba si se ha pulsado la tecla 'Up' o 'Down' en la lista window.teclas_pulsadas(definida en la linea 32 y 36)
    #           Si se pulsa "up" y el volumen actual es < 1.0,  se incrementa el volumen en 0.01 y se actualiza el volumen de la música utilizando pygame.mixer.music.set_volume()
    #           Si se pulsa "down" y el volumen actual es > que 0.0, se decrementa el volumen en 0.01 y se actualiza el volumen de la música utilizando pygame.mixer.music.set_volume()
    #Entradas:/ NR
    #Salidas:/ NR
    global volumen #Valor que almacena el volumen actual de la ventana
    if 'Up' in window.teclas_pulsadas:
        if volumen < 1.0:
            volumen += 0.01
            pygame.mixer.music.set_volume(volumen)
    elif 'Down' in window.teclas_pulsadas:
        if volumen > 0.0:
            volumen -= 0.01
            pygame.mixer.music.set_volume(volumen)
    window.after(10, cambiar_volumen) # Despúes de 10 milisegundos, la función principal se programa para ejecutarse nuevamente utilizando window.after()

def tecla_pulsada(evento):
    window.teclas_pulsadas.add(evento.keysym)

def tecla_soltada(evento):
    window.teclas_pulsadas.remove(evento.keysym)

def iniciar(): # carga un archivo de música utilizando pygame.mixer.music.load() y lo asigna a la reproducción de música.
    pygame.mixer.music.load('Sound/musica_inicio.mp3')
    pygame.mixer.music.set_volume(volumen) # Configura el volumen de reproducción de música utilizando el valor de la variable global volumen
    pygame.mixer.music.play() #Inicia la reproducción de la música

    window.teclas_pulsadas = set()
    window.bind('<KeyPress>', tecla_pulsada) #Captura las teclas pulsadas y soltadas usando window.bind(), enlazando los eventos <KeyPress> y <KeyRelease> con las funciones tecla_pulsada() y tecla_soltada()
    window.bind('<KeyRelease>', tecla_soltada)
    window.after(10, cambiar_volumen) # Permite controlar el volumen mientras la música está reproduciéndose, programa la función para que se ejejute 10 ms después

iniciar() #Se activa el conjunto de acciones para comenzar la reproducción de la música y configurar el control de volumen del módulo "iniciar"

def salir(): #Función que se encarga de cerrar la ejecución de todo el programa usandondo el método destroy(la ventana principal se llama "window")
    window.destroy()

def abrir_ventana():
    """# Instituto Tecnológico de Costa Rica
    # Tecnológico de Costa Rica
    # Autor:/ Bryan Monge Navarro / Joaquín Ramirez Sequeira - 2023301855
    # Ultima fecha de modificación: 13/06/2023
    # Módulo:/ Función encargada de abrir una ventana secundaria sobre "window", mediante el método Toplevel(). Aquí se definirán dos botones, uno para cerrar el programa...
    #          confirmándo al usuario que desea salir del juego, y un botón de continuar, que mantiene al usuario en el programa sin cambio alguno.
    # Entradas:/ NR
    # Salidas:/ NR
    # Restricciones:/ NR"""
    ventana_secundaria = tk.Toplevel()
    ventana_secundaria.overrideredirect(True) #Configura la nueva ventana para que no tenga bordes ni barra de título, como los botones de minimizar, maximizar o cerrar.

    screen_width = ventana_secundaria.winfo_screenwidth() # Variable que obtiene el ancho de la pantalla en píxeles utilizando el método winfo_screenwidth() de la ventana ventana secundaria
    screen_height = ventana_secundaria.winfo_screenheight() # Variable que obtiene la altura de la pantalla en píxeles utilizando el método winfo_screenheight() de la ventana ventana secundaria

#   Se establece el ancho y largo deseado de la ventana
    window_width = 400
    window_height = 300
#   Calculan la posición "x" y "y" para centrar la ventana en la pantalla. Restan el ancho y la altura de la ventana al ancho y la altura de la pantalla, luego dividen el resultado entre 2.
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2

#   Configura la geometría de la ventana especificando el ancho y la altura de la ventana, seguido de un símbolo "+" y luego la posición "x" y "y" calculadas previamente
    ventana_secundaria.geometry(f"{window_width}x{window_height}+{x}+{y}")

    imagen_fondo = Image.open("Image/image (8) (1).png") # Variable que guarda el atributo "open()", este ejecuta una dirección de archivo, en este caso se le da el nombre de carpeta y nombre de la foto que se mostrará
    imagen_fondo = imagen_fondo.resize((400, 300)) #Redimensiona la imagen a un tamaño de 400 píxeles de ancho y 300 píxeles de alto antes de mostrarla en la ventana
    fondo = ImageTk.PhotoImage(imagen_fondo)

#   Utiliza la clase ImageTk.PhotoImage de la biblioteca Tkinter para crear un objeto(imagen), que permite que la imagen se utilice en widgets y elementos gráficos de la interfaz.
    fondo_label = tk.Label(ventana_secundaria, image=fondo)
    fondo_label.place(x=0, y=0, relwidth=1, relheight=1) #Posiciona y dimensiona el objeto Label "fondo_label", creando un fondo o imagen de fondo que ocupa todo el espacio visible.

    def salir1(): #Función que destruye la venta secundaria, enviando como parámentro el nombre de la ventana.método destroy()
        ventana_secundaria.destroy()

#   Crea, posiciona y dimensiona un botón en "ventana secundaria", haciendo confirmar al usuario que desea mantenerse dentro del programa
    boton1 = tk.Button(ventana_secundaria, text="Continuar conduciendo", fg="gray1",
                       bg="green4",
                       relief="sunken",
                       font=("System 18 bold"),
                       cursor="exchange", command=salir1) #envía como comando la función creada en la linea 101, cerrando la ventana secundaria sin algun cambio
    boton1.pack(pady=10)


    def salir():# Función que se encarga de cerrar el programa usando el método destroy, pasando como primer argumento "window", nombre de la venatan principal
        window.destroy()
#   Crea y posiciona un botón 2, que cierra todo el programa en caso de que el usuario así lo ejecute. Se pasa como primer arguemto el nombre de la ventana donde se encuentra el botón
    boton2 = tk.Button(ventana_secundaria, text="Abandonar la pista", fg="gray1",
                       bg="red3",
                       relief="sunken",
                       font=("System 18 bold"),
                       cursor="exchange", command=salir) #Se ejecuta el comando "salir" que cierra la ejecución del programa
    boton2.pack(pady=10)

    # Ejecutar en loop la venatan secundaria cuando se ejecuta
    ventana_secundaria.mainloop()

# Crea,posiciona y dimensiona un botón "Abandonar la pista", que hace confirmar al usuario si en verdad quiere salir del programa o continuar en él
boton1=tk.Button(window, text="Abandonar la pista", #Parámetros para configurar el botón de salir
                 command=abrir_ventana, # Si se pulsa, ejecuta la función con las propiedades definidas en la línea 68
                 fg="gray1",
                 bg="DodgerBlue4",
                 relief="sunken",
             font=("System 18 bold"),
                 cursor="exchange")
boton1.pack()       #Se coloca el botón sobre el Canvas
boton1.place(x=1075,y=727, height=40, width=289) #Se ajusta el tamaño

# Función que define la reproducción de un sonido cuando el cursor del mouse está en el área del botón "Abandonar la pista", usando el método .Channel para ejecutarlo en un canal diferente y no se superponga sobre otro sonido
def play_sound(event):
    pygame.mixer.Channel(4).play(pygame.mixer.Sound("Sound/SD_NAVIGATE_53.mp3")) #Se usa como parámetro .Sound() para abrir una dirección de archivo en la misma carpeta
# Función que se define para reanudar la reproducción de la música  de fondo cuando el cursor sale del área del botón "Abandonar la pista"
def resume_music(event):
    pygame.mixer.music.unpause()  # Reanudar la música de fondo
# Vincular los eventos de entrada y salida del mouse al "Abandonar la pista" con las funciones play_sound y resume_music
boton1.bind("<Enter>", play_sound)
boton1.bind("<Leave>", resume_music)
pygame.mixer.init() # Se utiliza para inicializar el módulo mixer de Pygame.
pygame.mixer.music.load("Sound/musica_inicio.mp3")  # Cargar música de fondo
pygame.mixer.music.play(-1) # Reproduce la musica de fondo en un bucle(para ello se usa "-1" como parámetro

"""Se crea una nueva ventana sobre "window" usando el método Toplevel, no cierra la ejecución de las propiedades de la ventana principal"""
"""Muestra información sobre los autores del proyecto"""
def acerca_de():

    acerca_de = Toplevel()          #Se define el método con el que se va a trabajar: TopLevel
    acerca_de.attributes("-fullscreen", True) #Se ejecuta en pantalla completa
    imagen = Image.open("Image/acerca de.png")    # Cargar la imagen de fondo
    imagen = ImageTk.PhotoImage(imagen)
    fondo = Label(acerca_de, image=imagen)    # Superpone la imagen sobre la ventana de acerca de
    fondo.place(x=0, y=0, relwidth=1, relheight=1)
    acerca_de.configure(cursor = "star")    #Se confugura el cursor

    """Comando que posee el método acerca_de(pantalla sobre los información de los autores). con el método Destroy, para cerrar la ejecucuión de la ventana Acerca de """
    def salir():
        acerca_de.destroy()
    """Se crea y posiciona el botón "Volver", que ejecuta el comando definido en la linea 164, devolviendo al usuario a la pantalla principal"""
    boton1 = tk.Button(acerca_de, text="Volver", # Se configura el botón "Volver" de "Acerca de"
                 command=salir,
                 fg="snow",
                 bg="SkyBlue3",
                 relief="sunken",
                 font=("System 30 bold"),
                 cursor="exchange")
    boton1.pack()       #Se posiciona el botón "Volver"
    boton1.place(x=5, y=8, height=50, width=150)
    """Cuando el cursor entra en el área del botón ("<Enter>") se ejecuta 'change_color_enter(event)', que cambia el color del (bg) a "SkyBlue1" y el color del (fg) a "white" del boton1 utilizando el método configure()"""
    """Cuando el cursor sale del área del botón ("<Leave>"), se ejecuta 'change_color_leave(event)', que restaura el color de fondo a "SkyBlue3" y el color de texto a "white" del objeto boton1."""
    def change_color_enter(event):
        boton1.configure(bg="SkyBlue1", fg="white")
    def change_color_leave(event):
        boton1.configure(bg="SkyBlue3", fg="white")
    boton1.bind("<Enter>", change_color_enter)
    boton1.bind("<Leave>", change_color_leave)

    acerca_de.mainloop()    # Mostrar ventana "acerca_de"
"""Se crea, posiciona y dimensiona un botón en la pantalla "window", encargado de direccionar al usuario la ventana acerca_de, con las propiedades definidas en la línea de código 153"""
boton2=tk.Button(window, text="Acerca de",fg="snow",  #Se configura el botón "acerca_de" en la pantalla principal
                 bg="turquoise4",
                 relief="sunken",
                 font=("System 30 bold"),command=acerca_de,
                 cursor="exchange")
boton2.pack()         #Se posiciona el botón "Acerca_de"
boton2.place(x=1000,y=90, height=60, width=220)
def play_sound(event):
    pygame.mixer.Channel(1).play(pygame.mixer.Sound("Sound/misc308 (mp3cut.net) (1).mp3"))
def resume_music(event):
    pygame.mixer.music.unpause()  # Reanudar la música de fondo
boton2.bind("<Enter>", play_sound)
boton2.bind("<Leave>", resume_music)
pygame.mixer.init()
pygame.mixer.music.load("Sound/musica_inicio.mp3")  # Cargar música de fondo
pygame.mixer.music.play(-1)


def como_jugar():
    """Instituto tecnológico de Costa Rica
            Ingeniería en Computadores
    Autor:/ Bryan Monge Navarro / Joaquín Ramirez Sequeira - 2023301855
    Ultima modificación:/  13/06/2023
    Entradas:/ NR
    Salidas:/ Muestra una ventana emergente de pantalla completa con el método Toplevel con una imagen de fondo yn botón de volver a la ventana principal
    Restricciones:/ Existen las imagenes y recursos requeridos, instalados por el usuario en la mismca carpeta que la dirección del archivo .py presente
    """
    como_jugar = Toplevel()         # Se define el método
    como_jugar.attributes("-fullscreen", True)          # Se configura a pantalla completa
    imagen = Image.open("Image/como jugar.png")    # Cargar la imagen de fondo
    imagen = ImageTk.PhotoImage(imagen)
    fondo = Label(como_jugar, image=imagen)    # Superpone la imagen sobre la ventana "Cómo jugar"
    fondo.place(x=0, y=0, relwidth=1, relheight=1)
    como_jugar.configure(cursor = "star")

    def salir():
        # Se utiliza el método destroy para eliminar la pantalla emergente "Cómo jugar" con todos sus widgets
        # Entrada: Presinar "Volver" desde la pestaña "Cómo jugar"
        # Salida: Devuelve al usuario a la ventana principal
        como_jugar.destroy()

    # Se crea, posiciona y dimensiona un botón que permite regresar al usuario volver a la ventana principal cuando presiona "Volver" desde la ventana principal
    boton1 = tk.Button(como_jugar, text="Volver", # Se configura el botón "Volver" de "Cómo jugar"
                 command=salir, #Recibe como comando la función definida en la línea 222, eliminando la pantalla emergente y restaurando la principal
                 fg="snow",
                 bg="SkyBlue3",
                 relief="sunken",
                 font=("System 30 bold"),
                 cursor="exchange")
    boton1.pack() #Se posiciona el botón "Volver"
    boton1.place(x=1150, y=20, height=50, width=150)
    def change_color_enter(event):
        boton1.configure(bg="SkyBlue1", fg="white")
    def change_color_leave(event):
        boton1.configure(bg="SkyBlue3", fg="white")
    boton1.bind("<Enter>", change_color_enter)
    boton1.bind("<Leave>", change_color_leave)

    como_jugar.mainloop()  #Muestra ventana "como_jugar" a modo de loop cuando es ejecutada
boton3=tk.Button(window, text="Cómo jugar",fg="snow", #Se configura el botón "Como jugar"
                 bg="turquoise4",
                 relief="sunken",
                 font=("System 30 bold"), command=como_jugar,
                 cursor="exchange")
boton3.pack
boton3.place(x=1100,y=180, height=60, width=250)

def play_sound(event):
    pygame.mixer.Channel(2).play(pygame.mixer.Sound("Sound/misc308 (mp3cut.net) (1).mp3"))
def resume_music(event):
    pygame.mixer.music.unpause()  # Reanudar la música de fondo
boton3.bind("<Enter>", play_sound)
boton3.bind("<Leave>", resume_music)
pygame.mixer.init()
pygame.mixer.music.load("Sound/musica_inicio.mp3")  # Cargar música de fondo
pygame.mixer.music.play(-1)

def detener(): # Función que detiene la ejecución actual de la venatana principal mediante el método destroy(), cerrando el juego en su totalidad con todas sus propiedades
    window.destroy()

def abrir_nueva_ventana():
    """
    Instituto Tecnológico de Costa Rica
      Ingeniería en Computadores
    Autor:/ Bryan Monge Navarro / Joaquín Ramirez Sequeira - 2023301855
    Módulo:/  Función encargada de ubicar en la misma carpeta donde se encuentra ubicado el proyecto, la carpeta .py:'Control remoto', que contiene el código el código
              que permite controlar el hardware del proyecto; se destruye además la API diseñada, sin embargo, el código de 'Control remoto' cuenta con un botón que permite
              retornar a la intefaz de navegación. Para realizar el direccionamiento, se ha importadola biblioteca 'subprocess', que ejecuta una ventana hija  desde la
              que se importa, sin embargo, se ejecuta detener(), definida en la linea 264, que cierra la carpeta de la iterfaz y mantiene solo abierto el contro, remoto
    Entradas:/ Dirección de archivo a abir cuando se ejecute el botón definido en la línea 285
    Salidas:/ Direccionamiento de archivos, cerrando la pestaña actual y abriendo los comandos para controlar el hardware
    Restricciones:/ Bibliotecas 'subprocess', 'sys' y archivo deseado importados correctamente, es decir, estám bien escritos además de que existen
    """
# Nota: se utiliza 'sys.executable' de la biblioteca ´sys' para devolver la ruta al ejecutable del intérprete de Python en uso. Puede ser útil para ejecutar otro script de Python desde el actual utilizando subprocess.Popen()
    detener()  # Detener la ventana actual
    subprocess.call(["python", "telemetry.py"])

# Se crea, posiciona y dimensiona el botón que direcciona al usuario a los comandos del hardware
boton_principal = tk.Button(window, text="ACELERA!!",
                            fg="white",
                            bg="steel blue",
                            relief="sunken",
                            font=("System 49 bold"),
                            command=abrir_nueva_ventana, #Se ejecuta la función definida en la linea 267 con todas sus propiedades
                            cursor="exchange")
boton_principal.pack()
boton_principal.place(x=950,y=320, height=80, width=380)
def change_color_enter(event):
    boton_principal.configure(bg="black", fg="red")
def change_color_leave(event):
    boton_principal.configure(bg="steel blue", fg= "white")
boton_principal.bind("<Enter>", change_color_enter)
boton_principal.bind("<Leave>", change_color_leave)


def abrir():
    """Instituto Tecnológico de Costa Rica
        ingeniería en Computadores
        Autor:/ Bryan Monge Navarro / Joaquín Ramirez Sequeira - 2023301855
        Modulo:/ Cierra la ventana actual aplicando el método .destroy(), y luego abrir un nuevo proceso que ejecuta otro script de Python llamado "Proyecto Parte grafica_ingles.py"

        Entradas:/ Dirección de Carpeta a abrir, nombre de la biblioteca utilizada: subprocess
        Salidas:/ Direccionamiento al usario a la carpeta deseada
        Restricciones:/ Nombre de la carpeta a direccionar escrito correctamente, así como el de la biblioteca

    """
    window.destroy()
    subprocess.call(["python", "Proyecto Parte grafica_ingles.py"])
def play_sound(event):
    pygame.mixer.Channel(3).play(pygame.mixer.Sound("Sound/SD_NAVIGATE_53.mp3"))
def resume_music(event):
    pygame.mixer.music.unpause()  # Reanudar la música de fondo

# Crea, posiciona y dimensiona el botón que permite al usario ver el programa en otr idioma, para ello, se cierra la ventana igual, y se abre una nueva con
#   las cosas escritas en inglés
boton_ingles = tk.Button(window, text="English",
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
pygame.mixer.music.load("Sound/musica_inicio.mp3")  # Cargar música de fondo
pygame.mixer.music.play(-1)


window.mainloop()
