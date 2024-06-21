import os
from tkinter import *
from tkinter import ttk
from tkinter.font import Font
from tkinter import scrolledtext as st
from tkinter import filedialog as fd
from tkinter import messagebox as mb
import tkinter as tk

from evaluacion_constantes import expresiones
from tkinter import scrolledtext

class ventana_optimizacion:
    def inicio(lista_codigo):
        print(lista_codigo)

        ventana = Tk()
        ancho_ventana = 475
        alto_ventana = 575
        x_ventana = ventana.winfo_screenwidth() // 2 - ancho_ventana // 2
        y_ventana = ventana.winfo_screenheight() // 2 - alto_ventana // 2 - 42
        posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
        ventana.geometry(posicion)
        ventana.title("optimizacion de codigo")
        ventana.configure(background="wheat1", bd="10", relief="groove")

        label = Label(ventana, text=" optimizacion de codigo ", font=("Arial", 25), background="coral1", relief="groove")
        label.grid(row=0, column=0, columnspan=2, sticky="nsew")

        label_constantes = Label(ventana, text="  Evaluacion constantes  ", font=("Arial", 15), background="coral1", relief="groove")
        label_constantes.grid(row=1, column=0, sticky="nsew")

        #----------------------------------------------------

        text_area = scrolledtext.ScrolledText(ventana, width=10, height=10, font=("Arial", 10), wrap=tk.NONE)
        text_area.grid(row=2, column=0, sticky="nsew")

        codigo_constantes = expresiones.inicio(lista_codigo)

        for k in range (len(codigo_constantes)-1,-1,-1):
            text_area.insert("1.0", codigo_constantes[k] + "\n")
        
        #----------------------------------------------------

        label_potencias = Label(ventana, text="  resuccion de potencias  ", font=("Arial", 15), background="coral1", relief="groove")
        label_potencias.grid(row=1, column=1, sticky="nsew")

        #----------------------------------------------------

        #LEO

        #----------------------------------------------------



        label_nulos = Label(ventana, text="  factores nulos  ", font=("Arial", 15), background="coral1", relief="groove")
        label_nulos.grid(row=3, column=0, sticky="nsew", )

        #-------------------------------------------------

        #LEO

        #----------------------------------------------------
        
        label_copias = Label(ventana, text="  extension de copias  ", font=("Arial", 15), background="coral1", relief="groove")
        label_copias.grid(row=3, column=1, sticky="nsew")

        #----------------------------------------------------

        #ALEJANDRO

        #----------------------------------------------------

        ventana.mainloop()



