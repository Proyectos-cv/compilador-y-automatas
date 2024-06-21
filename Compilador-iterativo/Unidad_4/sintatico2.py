from tkinter import *
from tkinter import ttk
from tkinter.font import Font

from tkinter import scrolledtext as st
from tkinter import filedialog as fd
from tkinter import messagebox as mb

from Gramatica import Regla1


class retroceso:
    def __init__(self):
        print("hola")
        
        self.NoTerminales = ["Programa","Sentencias","DeclaraVar","nomVarMul","tipoDato","NomVar","letra","letnum","num","Comentario","LoQueSea","Mensaje","MendajePantalla","Imprimier","imprime","Pedir","Asignar","Bandera","Entero","Decimal","Operacion","Continuacion","Operando","Operador"]
        
        self.texto_a_pantalla = [["n"] , [1] , [" "] ,[["Programa"],[" #"]]]#inicialisacion del programa
        #e = self.texto_a_pantalla[3]
        
        
        self.inicio()
        
    
    def inicio(self):
        self.archivo = open("axu.txt","r") #abro el archivo en lectura
        lineas=self.archivo.read() #leo el archivo
        
        separar = lineas.split("\n")
        #print(separar)
        self.cadena = []
        for i in separar:
            axu = i.split(" ")
            for k in axu:
                self.cadena.append(k)#lo junta todo en una lista
            
        print(" ---.----")
        
        self.cadena.append(" #")
        self.longitu = len(self.cadena)
        """print(self.texto_a_pantalla)
        print(self.longitu)
        print(self.cadena)"""
        print(self.cadena)
        print(self.texto_a_pantalla[3])
        
        self.ciclo()
        
    def ciclo(self):
        
        if (self.texto_a_pantalla[3] == self.cadena[0]):
            axu = self.texto_a_pantalla[2]
            axu.append([self.texto_a_pantalla[3], 1])
            
        elif self.texto_a_pantalla[3][0] in self.NoTerminales:
            texto = Regla1(self.texto_a_pantalla[3][0], posicion=1)
            print(texto)
    
        
s = retroceso()