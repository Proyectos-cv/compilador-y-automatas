from tkinter import *
from tkinter import ttk
from tkinter.font import Font

from tkinter import scrolledtext as st
from tkinter import filedialog as fd
from tkinter import messagebox as mb


class retroceso:
    def __init__(self):
        print("hola")
        
        self.NoTerminales = ["Programa","Sentencias","DeclaraVar","nomVarMul","tipoDato","NomVar","letra","letnum","num","Comentario","LoQueSea","Mensaje","MendajePantalla","Imprimier","imprime","Pedir","Asignar","Bandera","Entero","Decimal","Operacion","Continuacion","Operando","Operador"]
        
        self.texto_a_pantalla = [["n"] , [1] , [" "] , ["Programa","#"]]#inicialisacion del programa
        #e = self.texto_a_pantalla[3]
        
        
        self.inicio()
        
        #print(e[0])
        #self.Ventana()
        
    def Ventana(self):
        self.ventana = Toplevel()
        self.ventana.geometry("1200x700+0+0")
        self.ventana.configure(background="wheat1", bd="10", relief="groove")
        self.lista = Listbox(self.ventana, width = 150,height=30,font=Font(family="Arial", size=10))        
        self.lista.place(x=20,y=25)
        self.lista.insert(END,self.texto_a_pantalla)
    def inicio(self):
        self.archivo = open("axu.txt","r") #abro el archivo en lectura
        lineas=self.archivo.read() #leo el archivo
        
        separar = lineas.split("\n")
        #print(separar)
        cadena = []
        for i in separar:
            axu = i.split(" ")
            for k in axu:
                cadena.append(k)#lo junta todo en una lista
            
        print(" ---.----")
        ###print(cadena)
        
        print(self.texto_a_pantalla)
        
        #del(self.texto_a_pantalla[3][0])
        
        #texto = ["Star","{","sentencia","}","#"]
        
        """print(self.texto_a_pantalla)
        texto  = self.texto_a_pantalla[3]
        del(texto[0])
        texto.insert(0,"End")
        texto.insert(0,"}")
        texto.insert(0,"Sentencias")
        texto.insert(0,"{")
        texto.insert(0,"Star")
        self.texto_a_pantalla[3] = texto
        
        #self.texto_a_pantalla.insert([3]"Star")
        
        print(self.texto_a_pantalla)"""
        
        
        self.programa(posicion=1)
    
    
    def Expancion_del_arbol(self,posicion,axu):
        if (axu == "Programa"):
            texto_cadena = ["End","}","Sentencias","{","Star"]
            self.inserta_a_la_cadena(texto_cadena)
            
        elif (axu == "Sentencias"):
            if (posicion == 1):
                texto_cadena = ["Sentencias","DeclaVar"]
                self.inserta_a_la_cadena(texto_cadena)
            elif(posicion == 2):
                texto_cadena = ["Sentencias","Comentario"]
                self.inserta_a_la_cadena(texto_cadena)
            elif(posicion == 3):
                texto_cadena = ["Sentencias","MensajePantalla"]
                self.inserta_a_la_cadena(texto_cadena)
            elif(posicion == 4):
                texto_cadena = ["Sentencias","Pedir"]
                self.inserta_a_la_cadena(texto_cadena)
            elif(posicion == 5):
                texto_cadena = ["Sentencias","Asignar"]
                self.inserta_a_la_cadena(texto_cadena)
            elif(posicion == 6):
                texto_cadena = ["DeclaVar"]
                self.inserta_a_la_cadena(texto_cadena)
            elif(posicion == 7):
                texto_cadena = ["Comentario"]
                self.inserta_a_la_cadena(texto_cadena)
            elif(posicion == 8):
                texto_cadena = ["MendajePantalla"]
                self.inserta_a_la_cadena(texto_cadena)
            elif(posicion == 9):
                texto_cadena = ["Pedir"]
                self.inserta_a_la_cadena(texto_cadena)
            elif(posicion == 10):
                texto_cadena = ["Asignar"]
                self.inserta_a_la_cadena(texto_cadena)
            
        elif (axu == "DeclaraVar"):
            if (posicion == 1):
                texto_cadena = [";","nomVar","tipoDato"]
                self.inserta_a_la_cadena(texto_cadena)
            elif(posicion == 2):
                texto_cadena = [";","nomVarMul","nomVar","tipoDato"]
                self.inserta_a_la_cadena(texto_cadena)
        
        elif (axu == "nomVarMul"):
            if (posicion == 1):
                texto_cadena = ["nomVar",","]
                self.inserta_a_la_cadena(texto_cadena)
            elif(posicion == 2):
                texto_cadena = ["nomVarMul",",","nomVar",","]
                self.inserta_a_la_cadena(texto_cadena)
        
        elif (axu == "tipoDato"):
            if (posicion == 1):
                texto_cadena = [""]
                self.inserta_a_la_cadena(texto_cadena)
            elif(posicion == 2):
                texto_cadena = [""]
                self.inserta_a_la_cadena(texto_cadena)
            elif(posicion == 3):
                texto_cadena = [""]
                self.inserta_a_la_cadena(texto_cadena)
            elif(posicion == 4):
                texto_cadena = [""]
                self.inserta_a_la_cadena(texto_cadena)
            elif(posicion == 5):
                texto_cadena = [""]
                self.inserta_a_la_cadena(texto_cadena)
        
        elif (axu == "NomVar"):
            if (posicion == 1):
                pass
            elif(posicion == 2):
                pass
        
        elif (axu == "letra"):
            if (posicion == 1):
                pass
        
        
        elif (axu == "letnum"):
            if (posicion == 1):
                pass
            elif(posicion == 2):
                pass
            elif(posicion == 3):
                pass
            elif(posicion == 4):
                pass
            elif(posicion == 5):
                pass
            elif(posicion == 6):
                pass
        elif (axu == "num"):
            if (posicion == 1):
                pass
        
        elif (axu == "Comentario"):
            if (posicion == 1):
                pass
        elif (axu == "LoQueSea"):
            if (posicion == 1):
                pass
        
        elif (axu == "Mensaje"):
            if (posicion == 1):
                pass
        
        elif (axu == "MensajePatalla"):
            if (posicion == 1):
                pass
        
        elif (axu == "Imprimir"):
            if (posicion == 1):
                pass
        
        elif (axu == "imprime"):
            if (posicion == 1):
                pass
        
        elif (axu == "Pedir"):
            if (posicion == 1):
                pass
        elif (axu == "Asignar"):
            if (posicion == 1):
                pass
            elif(posicion == 2):
                pass
            elif(posicion == 3):
                pass
            elif(posicion == 4):
                pass
            elif(posicion == 5):
                pass
        elif (axu == "Bandera"):
            if (posicion == 1):
                pass
            elif(posicion == 2):
                pass
        elif (axu == "Entero"):
            if (posicion == 1):
                pass
            elif(posicion == 2):
                pass
        elif (axu == "Decimal"):
            if (posicion == 1):
                pass
        elif (axu == "Operacion"):
            if (posicion == 1):
                pass
            elif(posicion == 2):
                pass
        
        elif (axu == "Continuacion"):
            if (posicion == 1):
                pass
            elif(posicion == 2):
                pass
        elif (axu == "Operando"):
            if (posicion == 1):
                pass
            elif(posicion == 2):
                pass
            elif(posicion == 3):
                pass
        elif (axu == "Operador"):
            if (posicion == 1):
                pass
            elif(posicion == 2):
                pass
            elif(posicion == 3):
                pass
            elif(posicion == 4):
                pass
        
        
    def inserta_a_la_cadena(self,axu):
        texto  = self.texto_a_pantalla[3]
        del(texto[0])
        for i in axu:
            texto.insert(0,i)
        self.texto_a_pantalla[3] = texto
        
    def programa(self,posicion):
        axu = self.texto_a_pantalla[3] 
        if axu[0] in self.NoTerminales:
            self.Expancion_del_arbol(posicion,axu)
            
        
        
        
        
s = retroceso()
    