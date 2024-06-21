from tkinter import *
from tkinter import ttk
from tkinter.font import Font

from tkinter import scrolledtext as st
from tkinter import filedialog as fd
from tkinter import messagebox as mb




class Lex:
    def __init__(self):
        print ("Lexico")
        
        self.listaMinusculas=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        self.listaMayusculas=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.listaNumeros=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.listaOperadores=['+','-','*','/']
        self.listaplabrasreservadas=["&int","&float","&chr","&str","&bool","Start{\n","}End\n","print(","read"]
        
        self.archivo = open("axu.txt","r")
        self.lis = []
        for i in self.archivo:
            self.lis.append(i)
        self.archivo.close()
        print (self.lis)
        self.contador = int(len(self.lis))#contador de lineas
        
        self.Palabas_reservadas()
        
        print(self.contador)
        
        #self.operador()
        
        primtra = self.Patron_Inicio()
        print(primtra)
        ultima = self.Patron_Final()
        print(ultima)
    
    def Patron_Inicio(self):
        inicio=self.list[0]
        """if self.lis[0] == "Start{\n":
            return True
        else:
            print ("Error en el patron de inicio")
            return False"""
        
    def Patron_Final(self):
        if self.lis[-1] == "}End\n":
            return True
        else:
            return False
    def Palabas_reservadas(self):
        for i in range(1,self.contador-1):
            #print(self.lis[i],"vo")
            axu = self.lis[i]
            if  axu[0:1] == "&":
                #print(axu[0:1],axu)#"&Int\n","&float\n","&chr\n","&str\n","&bool\n","Start{\n","}End\n","print(\n","read"
                if axu[1:4] == "int" or axu[1:4] == "chr" or axu[1:4] == "str":
                    print(axu[0:4])
                elif axu[1:6] == "float":
                    print(axu[0:6])
                elif axu[1:5] == "bool":
                    print(axu[0:5])
                else:
                    print("error no se encuentra",axu[0:3])
                    
                    
                
            elif axu[0:1] == "$":
                print(axu[0:1])
                
            elif axu[0:6] == "print(" :
                print(axu[0:6])
                #self.caracter_pri()
            elif axu[0:4] == "read":
                print(axu[0:4])
            elif axu[0:1] == "#":
                print(axu[0:1])
                
                
            else:
                print("error",axu[0:6])
                
            
        

    def operador(self):
        pass
                
    def identificador(self):
        pass
    
    def caracter_pri(self):
        pass
    def numeros(self):
        pass
    def operacion(sef):
        #creacion de operadires
        pass
    
    
    
    
    
    
