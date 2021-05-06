from tkinter import *
from tkinter import ttk
import cine_mydatabase

window = Tk()
frame_app = Frame(window, width=400, height=600, bg="red")
frame_app.pack()

cartelera=StringVar()
pelicula=StringVar()
hora=StringVar()
precio=StringVar()

def crear_sala():
    cartelera=entry_cartelera.get()
    pelicula=entry_pelicula.get()
    hora=entry_hora.get()
    fecha=entry_fecha.get()
    idioma=entry_idioma.get()

    bd_cine=cine_mydatabase.MyDatabase()
    bd_cine.insert_db(cartelera, pelicula, hora, fecha, idioma)

# Widgets dentro del contender APP
frame_navbar = Frame(frame_app, width=400, height=100)
frame_navbar.grid(row=0, column=0)
frame_title = Frame(frame_app, width=400, height=120)
frame_title.grid(row=1, column=0)
frame_options = Frame(frame_app, width=400, height=500)
frame_options.grid(row=2, column=0)

# Widgets dentro del contender NAVBAR
title = Label(frame_navbar, 
              text="CINE LOVE",
              font=("Century Gothic", "14"))
title.place(x=250, y=40)

# Widgets dentro del contender TITLE
title1 = Label(frame_title, 
              text="SALAS DE CINE", 
              font=("Century Gothic", "22", "bold"),
              justify=LEFT)
title1.place(x=25, y=10)
title2 = Label(frame_title, 
              text="Todos los campos son obligartorios.", 
              font=("Century Gothic", "14"),
              justify=LEFT)
title2.place(x=25, y=50)

# Widgets dentro del contender OPTIONS
frame_form = Frame(frame_options, width=350, height=450, bg="#d48df0")
frame_form.place(x=25, y=5)
label_cartelera = Label(frame_form, 
              text="CARTELERA:",
              font=("Century Gothic", "20", "bold"),
              fg="white",
              bg="#d48df0")
label_cartelera.place(x=30, y=30)
entry_cartelera = Entry(frame_form, justify=LEFT, width=25, 
             font=("Century Gothic", "14"))
entry_cartelera.place(x=30, y=70)

label_pelicula = Label(frame_form, 
              text="PELICULA:",
              font=("Century Gothic", "20", "bold"),
              fg="white",
              bg="#d48df0")
label_pelicula.place(x=30, y=100)
entry_pelicula = Entry(frame_form, justify=LEFT, width=25, 
                font=("Century Gothic", "14"))
entry_pelicula.place(x=30, y=140)

label_hora = Label(frame_form, 
              text="HORA:",
              font=("Century Gothic", "20", "bold"),
              fg="white",
              bg="#d48df0")
label_hora.place(x=30, y=170)
entry_hora = Entry(frame_form, justify=LEFT, width=25, 
                font=("Century Gothic", "14"))
entry_hora.place(x=30, y=210)

label_fecha = Label(frame_form, 
              text="FECHA:",
              font=("Century Gothic", "20", "bold"),
              fg="white",
              bg="#d48df0")
label_fecha.place(x=30, y=240)
entry_fecha = Entry(frame_form, justify=LEFT, width=25,
               font=("Century Gothic", "14"))
entry_fecha.place(x=30, y=280)

label_idioma = Label(frame_form, 
              text="IDIOMA:",
              font=("Century Gothic", "20", "bold"),
              fg="white",
              bg="#d48df0")
label_idioma.place(x=30, y=310)
entry_idioma = Entry(frame_form, justify=LEFT, width=25,
               font=("Century Gothic", "14"))
entry_idioma.place(x=30, y=350)


button_agregar = Button(frame_form, text="Crear sala", 
                        font=("Century Gothic", "14", "bold"),
                        command=crear_sala)
button_agregar.place(x=110, y=400)

window.mainloop()