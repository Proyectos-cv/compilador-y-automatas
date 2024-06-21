import os
from tkinter import *
from tkinter import ttk
from tkinter.font import Font

from tkinter import scrolledtext as st
from tkinter import filedialog as fd
from tkinter import messagebox as mb

from Lexico import Lex
#from sintatico import retroceso
from prueba import Sintactico
from Semantica import Semantico
from Generar_arbol import Arbol_semantico
import Tabla_Semantica as ts
from ventana_generacion import ventana

from ventana_de_optimizacion import ventana_optimizacion
class Ventana:
    def __init__(self):
        self.credenciales = [True, False, False, False, False, False]
        self.ventana = Tk()
        self.ventana.title("Compilador")
        self.ventana.geometry("1200x700")
        self.ventana.configure(background="wheat1", bd="10", relief="groove")
        self.caja = st.ScrolledText(self.ventana)
        self.caja.place(x=450, y=100)
        self.caja.config(height = 17, width = 50, font=("Verdana", 15))        
        
        #agregar boton para limpiar
        self.label = Label(self.ventana, text=" Compilador El Sobrante :(", font=("Arial", 25), background="coral1", relief="groove")
        self.label.place(x=480, y=10)
        
        self.boton_Lexico = Button(self.ventana, text=" Léxico ", font=("Arial", 15), background="lawn green",command=self.Lexic, width = 18)
        self.boton_Lexico.place(x=60, y=200)
        
        self.boton_Sintactico = Button(self.ventana, text=" Sintático ", font=("Arial", 15), background="lawn green",command=self.Sintatico, width = 18)
        self.boton_Sintactico.place(x=60, y=250)
        
        self.boton_Semantico = Button(self.ventana, text=" Semántico ", font=("Arial", 15), background="lawn green",command=self.Semantico, width = 18)
        self.boton_Semantico.place(x=60, y=300)
        
        self.boton_cod_intermedio = Button(self.ventana, text=" Código intermedio ", font=("Arial", 15), background="lawn green",command=self.Codigo_intermedio, width = 18)
        self.boton_cod_intermedio.place(x=60, y=350)
        
        self.boton_optimizacion = Button(self.ventana, text=" Optimización ", font=("Arial", 15), background="lawn green",command=self.Optimizacion, width = 18)
        self.boton_optimizacion.place(x=60, y=400)
        
        self.boton_cod_objeto = Button(self.ventana, text=" Código Objeto ", font=("Arial", 15), background="red",command=self.Codigo_Objeto, width = 18)
        self.boton_cod_objeto.place(x=60, y=450)
        
        self.Limpiar = Button(self.ventana ,text=" Limpiar ", font=("Arial", 15),command=self.limpiar, width = 10)
        self.Limpiar.place(x=300, y=210)
        
        self.Importar = Button(self.ventana ,text=" Importar\n Archivo ", font=("Arial", 15),command=self.recuperar, width = 10)
        self.Importar.place(x=300, y=300)
        
        self.Guarda = Button(self.ventana ,text=" Guardar ", font=("Arial", 15),command=self.guardar, width = 10)
        self.Guarda.place(x=300, y=400)
        
        self.lista = Listbox(self.ventana, font=("Arial", 15),width = 2,height=1)
        self.lista.place(x=450,y=550)
        self.bandera=0
        self.banderaSintactico=0
        self.banderaCodigo=0
        self.ventana.mainloop()
        
    def limpiar(self):
        self.conta=0
        self.caja.delete("1.0","end")
        self.credenciales = [True, False, False, False, False, False]

    def Lexic(self):
        if self.credenciales[0] == True:
            self.guardar_archivo()
            self.credenciales[1] = True

            self.a = Lex(self.lista)

            self.bandera,self.tokens,self.mostrarToken,mostrarTipo,mostrarDeclara,mostrarReferencia,tablaErrores = self.a.proces()
            self.a.ventanaTabla(self.mostrarToken,mostrarTipo,mostrarDeclara,mostrarReferencia,tablaErrores)

    def Sintatico(self):
        if self.credenciales[1] == True:

            self.guardar_archivo()
            self.credenciales[2] = True

            if self.bandera==1:
                cadena = Sintactico()

                letra = cadena.proces(self.tokens)
                ban2 = cadena.analisisSintacticoretorno()

                if ban2==1 and self.bandera==1:
                    self.banderaSintactico=1
                    self.banderaCodigo=0                
            else:
                mb.showerror("Error", "Existen errores sintácticos")
        else:
            mb.showerror("Error", "No se ha realizado el análisis léxico.")

    def Semantico(self):
        if self.credenciales[2] == True:
            self.guardar_archivo()
            self.credenciales[3] = True

            if self.banderaSintactico==1:            
                arbol = Semantico()
                variables,b = arbol.proces(self.tokens)
                if b == 0:
                    self.bandera=0
                    self.banderaSintactico=0
                else:
                    print("Todo bien")
                    tipoVariables, no_declarados, tipo_dato=arbol.identificarVariables(variables)
                    generacion_arbol = Arbol_semantico()
                    if len(tipoVariables)>0:
                        lista = Listbox(width = 200,height=5,font=Font(family="Sans Serif", size=10))        
                        lista.place(x=450,y=550)
                        lista.delete(0,END)
                        lista.insert(END,"errores tipo de dato: ")
                        for i in tipo_dato:
                            lista.insert(END,i)
                        lista.insert(END,"errores variables no declaradas: ")
                        for i in no_declarados:
                            lista.insert(END,i)
                        lista.insert(END,"errores de duplicación: ")
                        for i in tipoVariables:
                            lista.insert(END,i)
                    elif len(no_declarados)>0:
                        lista = Listbox(width = 200,height=5,font=Font(family="Sans Serif", size=10))        
                        lista.place(x=450,y=550)
                        lista.delete(0,END)
                        lista.insert(END,"errores tipo de dato: ")
                        for i in tipo_dato:
                            lista.insert(END,i)
                        lista.insert(END,"errores variables no declaradas: ")
                        for i in no_declarados:
                            lista.insert(END,i)
                        lista.insert(END,"errores de duplicación: ")
                        for i in tipoVariables:
                            lista.insert(END,i)
                    elif len(tipo_dato)>0:
                        lista = Listbox(width = 200,height=5,font=Font(family="Sans Serif", size=10))        
                        lista.place(x=450,y=550)
                        lista.delete(0,END)
                        lista.insert(END,"errores tipo de dato: ")

                        for i in tipo_dato:
                            lista.insert(END,i)
                        lista.insert(END,"errores variables no declaradas: ")

                        for i in no_declarados:
                            lista.insert(END,i)

                        lista.insert(END,"errores de duplicación: ")
                        for i in tipoVariables:
                            lista.insert(END,i)

                        #mb.showinfo("Información", "error en tipo de dato: ",tipo_dato[0]) 
                    else:
                        print("=================")
                        print(" SE LLAMÓ AL ÁRBOL ")
                        letra_2 = generacion_arbol.proces(self.tokens)
                        ban_2 = generacion_arbol.analisisSintacticoretorno()

                        try:
                            ts.correr()
                        except:
                            os.system('cls' if os.name == 'nt' else 'clear')
                            

                    print(tipoVariables, no_declarados, tipo_dato)
                    if len(tipoVariables)>0 or len(no_declarados)>0 or len(tipo_dato)>0:
                        self.bandera=0
                        self.banderaSintactico=0
                        self.banderaCodigo=0
                    else:
                        self.banderaCodigo=1
            else:
                mb.showinfo("Información", "No se ha realizado el análisis sintáctico o hay errores")
        else:
            mb.showerror("Error", "No se ha realizado el análisis semántico")

    def Codigo_intermedio(self):
        if self.credenciales[3] == True:
            self.guardar_archivo()
            self.credenciales[4] = True

            if self.banderaCodigo==1:
                generacion = ventana()
                determinar,ban = generacion.proces(self.tokens)
                if ban==1:
                    lista_ecuaciones = generacion.seccionar()
                    generacion.ventana_generacion(lista_ecuaciones)
                else:
                    self.bandera=0
                    self.banderaSintactico=0
                    self.banderaCodigo=0
            else:
                mb.showinfo("Información", "No se ha realizado el análisis semántico o hay errores")
        else:
            mb.showerror("Error", "No se ha realizado el análisis semántico")
        
    def Optimizacion(self):
        contenido = self.caja.get("1.0", "end")
        lista_de_codigo = contenido.split("\n")
        """ lista_depurada = []
        for i in range(len(lista_de_codigo)):
            if lista_de_codigo[i] != "":
                print (len(lista_de_codigo[i]))
                if lista_de_codigo[i][0] == "$" and len(lista_de_codigo[i]) > 9:
                    lista_depurada.append(lista_de_codigo[i])
        print(lista_depurada) """
        ventana_optimizacion.inicio(lista_de_codigo)
    def Codigo_Objeto(self):
        pass
    
    def guardar(self):
        nombrearch=fd.asksaveasfilename(initialdir = "/",title = "Guardar como",filetypes = (("txt files","*.txt"),("todos los archivos","*.*")))
        if nombrearch!='':
            archi1=open(nombrearch, "w", encoding="utf-8")
            archi1.write(self.caja.get("1.0", "end"))
            archi1.close()
            mb.showinfo("Información", "Los datos fueron guardados en el archivo.")

    def recuperar(self):
        nombrearch=fd.askopenfilename(initialdir = "/",title = "Seleccione archivo",filetypes = (("txt files","*.txt"),("todos los archivos","*.*")))
        if nombrearch!='':
            archi1=open(nombrearch, "r", encoding="utf-8")
            contenido=archi1.read()
            archi1.close()
            self.caja.delete("1.0", "end") 
            self.caja.insert("1.0", contenido)
    
    def leer_archivo(self):
        archivo = open("axu.txt", "r")
        contenido = archivo.read()
        archivo.close()

        if contenido != self.caja.get("1.0", "end"):
            self.credenciales = [True, False, False, False, False, False]
            mb.showinfo(
                "Información",
                "Se ha modificado el archivo, por favor vuelva a realizar el análisis completo.",
            )
    
    def guardar_archivo(self):
        archivo = open("axu.txt", "w")
        archivo.write(self.caja.get("1.0", "end"))
        archivo.close()

s = Ventana()
