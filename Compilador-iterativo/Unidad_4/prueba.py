from tkinter import *
from tkinter import ttk
from tkinter.font import Font

from tkinter import scrolledtext as st
from tkinter import filedialog as fd
from tkinter import messagebox as mb
class Sintactico:

    def proces(self,tokens):
        self.variables=[]
        self.variablesLexico=[]
        self.pos_actual = 0
        self.archivo = open("axu.txt","r") #abro el archivo en lectura
        lineas=self.archivo.read() #leo el archivo
        count=1
        codigo_separado=lineas.split("\n") #separo el codigo en lineas
        listaNumeros=[]
        listaLineas=[]
        #print(len (codigo_separado))
        for k in codigo_separado:
            listaNumeros.append(count)
            listaLineas.append(k)
            token=k.split(" ")
            if count==len(codigo_separado)-1:
                    #print("Fin de archivo")
                    break
            else:
                for j in token:                
                    self.variables.append(j)
        #self.variables.pop()
        self.variables.append("%")
        self.variables.append("%")
        self.variables.append("%")
        #Comparacion con lo que viene de lexico
        for k in tokens:
            token=k.split(" ")
            if count==len(tokens)-1:
                    #print("Fin de archivo")
                    break
            else:
                for j in token:                
                    self.variablesLexico.append(j)
        #self.variables.pop()
        self.variablesLexico.append("%")
        self.variablesLexico.append("%")
        self.variablesLexico.append("%")
        #print (self.variables)
        #print ( self.variablesLexico)
        if self.variables== self.variablesLexico:
            return self.variables         
        else:
            mb.showinfo("Información", "Se ah modificado el código, debe correr el análisis léxico nuevamente")
    

    def reglas(self,pila,analizado,siguiente):
        #print (pila,analizado,siguiente)
        if pila == "Programa" and analizado == "&Start":
            produccion = ["&Start",";", "Sentencias","&End"]
            return produccion
        elif pila==analizado:
            if pila=="%" and analizado=="%":
                return "Cadena aceptada!!"
            else:
                return "reconoce"
        elif pila=="Sentencias":
            if analizado=="&print":
                produccion=["MensajePantalla","Sentencias"]
                return produccion
            elif analizado=="&read":
                produccion=["Pedir","Sentencias"]
                return produccion
            elif analizado.startswith('#'):
                produccion=["Comentario","Sentencias"]
                return produccion
            elif analizado=="&int" or analizado=="&float" or analizado=="&chr" or analizado=="&str" or analizado=="&bool":
                produccion=["DeclaVar","Sentencias"]
                return produccion
            elif analizado.startswith('$'):
                produccion=["Asignar","Sentencias"]
                return produccion

            elif analizado=="&End":
                produccion="Cadena Vacia"
                return produccion
            else: 
                return "Cadena Rechazada"
        elif pila=="DeclaVar" and siguiente==",": #Falta hacer lo de NomVarMul
            if analizado=="&int" or analizado=="&float" or analizado=="&chr" or analizado=="&str" or analizado=="&bool":
                produccion=["tipoDato","NomVar",",","NomVarMul",";"]
                return produccion
            else: 
                return "Cadena Rechazada"
        elif pila=="DeclaVar" and siguiente=="hola":
            if analizado=="&int" or analizado=="&float" or analizado=="&chr" or analizado=="&str" or analizado=="&bool":
                produccion=["tipoDato","NomVar",";"]
                return produccion
        
        elif pila=="NomVarMul" and siguiente==",":
            produccion=["NomVar",",","NomVarMul"]
            return produccion
        elif pila=="NomVarMul" and analizado.startswith('$'):
            produccion = ["NomVar"]
            return produccion
        
        elif pila=="tipoDato":
            if analizado=="&int":
                produccion=["&int"]
                return produccion
            elif analizado=="&float":
                produccion=["&float"]
                return produccion
            elif analizado=="&chr":
                produccion=["&chr"]
                return produccion
            elif analizado=="&str":
                produccion=["&str"]
                return produccion
            elif analizado=="&bool":
                produccion=["&bool"]
                return produccion
        elif pila=="NomVar":
            if analizado.startswith('$'):
                produccion="reconoce"
                return produccion
            else:
                return "Cadena Rechazada"
        #parte del codigo orientada a comentarios
        elif pila=="Comentario":
            if analizado.startswith('#'):
                produccion="reconoce"
                return produccion
        #parte del codigo orientada a imprimir
        elif pila=="MensajePantalla":
            produccion=["&print","(", "Imprimir", ")",";"]
            return produccion    
        elif pila=="Imprimir":
            if siguiente==",":
                produccion=["imprime",",","Imprimir"]
                return produccion
            else:
                produccion=["imprime"]
                return produccion
        elif pila=="imprime":
            if analizado.startswith('"'):
                produccion=["LoQueSea"]
                return produccion
            elif analizado.startswith('$'):
                produccion=["NomVar"]
                return produccion   
            elif analizado.isdigit():
                produccion=["Entero"]
                return produccion
            elif analizado.replace(".", "").isdigit():
                produccion=["Decimal"]
                return produccion
            else :
                return "Cadena Rechazada"
        elif pila=="LoQueSea":
            if analizado.startswith('"'):
                produccion="reconoce"
                return produccion
        elif pila=="Entero" and analizado.isdigit():
            produccion="reconoce"
            return produccion
        elif pila=="Decimal" and analizado.replace(".", "").isdigit() and analizado[-1] != ".":
            produccion="reconoce"
            return produccion     
        
        #parte del codigo orientada a leer
        elif pila=="Pedir":
            produccion=["&read","NomVar",";"]
            return produccion
        elif pila=="Asignar":
            if siguiente=="true" or siguiente=="false":
                produccion=["NomVar","=","Bandera",";"]
                return produccion
            elif siguiente.startswith('"'):
                produccion=["NomVar","=","LoQueSea",";"]
                return produccion
            elif siguiente.startswith('$') and not (analizado in ["+","-","*","/"]):
                produccion=["NomVar","=","NomVar",";"]
                return produccion
            elif siguiente.isdigit() and not (analizado in ["+","-","*","/"]):
                produccion=["NomVar","=","Entero",";"]
                return produccion
            elif siguiente.replace(".", "").isdigit() and not (analizado in ["+","-","*","/"]):
                produccion=["NomVar","=","Decimal",";"]
                return produccion
            elif (siguiente.isdigit() or self.oeprando.startswith("$")) and (analizado in ["+","-","*","/"]):
                produccion=["NomVar","=","Operacion",";"]
                return produccion
            elif (siguiente.replace(".", "").isdigit() or self.oeprando.startswith("$")) and (analizado in ["+","-","*","/"]):
                produccion=["NomVar","=","Operacion",";"]
                return produccion
            else: 
                produccion=["NomVar","=","LoQueSea",";"]
                return produccion
        elif pila=="Bandera":
            if analizado=="true":
                produccion=["true"]
                return produccion
            elif analizado=="false":
                produccion=["false"]
                return produccion
            else: 
                return "Cadena Rechazada"
        
        #codigo orientado a las operaciones
        elif pila=="Operacion" and (analizado.isdigit() or analizado.replace(".", "").isdigit() or analizado.startswith("$")):
            #print (analizado,pila,siguiente)
            if siguiente in ["+","-","*","/"]:
                produccion=["Operando", "Operador", "Operando", "Continuacion"]
                return produccion
            elif siguiente==";":
                produccion=["Operando", "Operador", "Operando"]
                return produccion
            else :
                return "Cadena Rechazada"
        elif pila=="Operando":
            if analizado.isdigit():
                produccion=["Entero"]
                return produccion
            
            elif analizado.replace(".", "").isdigit():
                produccion=["Decimal"]
                return produccion
            elif analizado.startswith("$"):
                produccion=["NomVar"]
                return produccion
            else:
                return "Cadena Rechazada"
        elif pila=="Operador":
            if analizado=="+":
                produccion=["+"]
                return produccion
            elif analizado=="-":
                produccion=["-"]
                return produccion
            elif analizado=="*":
                produccion=["*"]
                return produccion
            elif analizado=="/":
                produccion=["/"]
                return produccion
            else:
                return "Cadena Rechazada"
        elif (pila=="+" and analizado=="+") or( pila=="-"and analizado=="-") or (pila=="*"and analizado=="*") or (pila=="/"and analizado=="/"):
            produccion="reconoce"
            return produccion
        elif pila=="Continuacion":
            #print (analizado,pila,siguiente)
            if siguiente in ["+","-","*","/"]:
                produccion=["Operador", "Operando", "Continuacion"]                
                return produccion
            elif siguiente==";":
                produccion=["Operador", "Operando"]
                return produccion
            else:
                return "Cadena Rechazada"
        else:
            return "Cadena Rechazada"
        
    def analisisSintactico(self):
        #print("Analisis Sintactico")
        
        #inicializa la pila y la cadena
        self.pila = ["%","Programa"]
        cadena = self.variables
        conta=0
        #eliminamos los espacios en blanco
        while "" in cadena:
            cadena.remove("")
        #guardado de registro para tabla
        self.listaProduccion=[]
        self.listaPila=[]
        self.listaCadena=[]
        produccion=""
        self.oeprando=""
        ventanaTabla = Toplevel()
        ventanaTabla.title("Tabla de tokens")
        ventanaTabla.geometry("1900x400")
        ventanaTabla.configure(background="wheat1", bd="10", relief="groove")
        tablaMostrar=ttk.Treeview(ventanaTabla,columns=('Pila', 'Cadena', 'Produccion'), show='headings')
        tablaMostrar.heading("Pila",text="Pila")
        tablaMostrar.heading("Cadena",text="Cadena")
        tablaMostrar.heading("Produccion",text="Produccion")
        #tablaMostrar.insert("",0,text="1",values=(pila[0],cadena[0],produccion[0]))       
        tablaMostrar.insert("",0,text="1",values=(self.pila,cadena,produccion)) 
        while produccion!="Cadena aceptada!!" and produccion!="Cadena Rechazada":            
            self.listaCadena.append(cadena)
            self.listaPila.append(self.pila)#, $b
            if (self.pila[-1]=="DeclaVar" and cadena[2]==",") or (self.pila[-1]=="Continuacion" and cadena[2] in ["+","-","*","/",";"]): 
                produccion=self.reglas(self.pila[-1],cadena[0],cadena[2])
            elif (self.pila[-1]=="NomVarMul" and cadena[1]==",") or (self.pila[-1]=="Imprimir" and cadena[1]==","):
                produccion=self.reglas(self.pila[-1],cadena[0],cadena[1])
            elif (self.pila[-1]=="Asignar" and cadena[1]=="="):
                self.oeprando=cadena[0]
                produccion=self.reglas(self.pila[-1],cadena[3],cadena[2])
            elif (self.pila[-1]=="Operacion"):
                #print ("entro")
                produccion=self.reglas(self.pila[-1],cadena[0],cadena[3])
            else:
                produccion=self.reglas(self.pila[-1],cadena[0],"hola")
            #print (" ")
            #print(self.pila, "--",cadena,"--",produccion)
            tablaMostrar.insert("",0,text="1",values=(self.pila,cadena,produccion)) 
            if produccion!=None:
                if produccion=="reconoce":
                    self.pila.pop()
                    cadena.pop(0)
                elif produccion=="Cadena Vacia":
                    self.pila.pop()
                else:
                    self.pila.pop()
                    self.pila.extend(produccion[::-1])
            self.listaProduccion.append(produccion)
            conta+=1 
        tablaMostrar.column('Pila', width=300)
        tablaMostrar.column('Cadena', width=1200)
        tablaMostrar.column('Produccion', width=300)
        tablaMostrar.pack()
        ventanaTabla.mainloop()
    
    def analisisSintacticoretorno(self):
        #print("Analisis Sintactico")
        
        #inicializa la pila y la cadena
        self.pila = ["%","Programa"]
        cadena = self.variables
        conta=0
        #eliminamos los espacios en blanco
        while "" in cadena:
            cadena.remove("")
        #guardado de registro para tabla
        self.listaProduccion=[]
        self.listaPila=[]
        self.listaCadena=[]
        produccion=""
        self.oeprando=""
        ventanaTabla = Toplevel()
        ventanaTabla.title("Tabla de tokens")
        ventanaTabla.geometry("1900x400")
        ventanaTabla.configure(background="wheat1", bd="10", relief="groove")
        tablaMostrar=ttk.Treeview(ventanaTabla,columns=('Pila', 'Cadena', 'Produccion'), show='headings')
        tablaMostrar.heading("Pila",text="Pila")
        tablaMostrar.heading("Cadena",text="Cadena")
        tablaMostrar.heading("Produccion",text="Produccion")
        #tablaMostrar.insert("",0,text="1",values=(pila[0],cadena[0],produccion[0]))       
        tablaMostrar.insert("",0,text="1",values=(self.pila,cadena,produccion)) 
        while produccion!="Cadena aceptada!!" and produccion!="Cadena Rechazada":            
            self.listaCadena.append(cadena)
            self.listaPila.append(self.pila)#, $b
            if (self.pila[-1]=="DeclaVar" and cadena[2]==",") or (self.pila[-1]=="Continuacion" and cadena[2] in ["+","-","*","/",";"]): 
                produccion=self.reglas(self.pila[-1],cadena[0],cadena[2])
            elif (self.pila[-1]=="NomVarMul" and cadena[1]==",") or (self.pila[-1]=="Imprimir" and cadena[1]==","):
                produccion=self.reglas(self.pila[-1],cadena[0],cadena[1])
            elif (self.pila[-1]=="Asignar" and cadena[1]=="="):
                self.oeprando=cadena[0]
                produccion=self.reglas(self.pila[-1],cadena[3],cadena[2])
            elif (self.pila[-1]=="Operacion"):
                #print ("entro")
                produccion=self.reglas(self.pila[-1],cadena[0],cadena[3])
            else:
                produccion=self.reglas(self.pila[-1],cadena[0],"hola")
            #print (" ")
            #print(self.pila, "--",cadena,"--",produccion)
            tablaMostrar.insert("",0,text="1",values=(self.pila,cadena,produccion)) 
            if produccion!=None:
                if produccion=="reconoce":
                    self.pila.pop()
                    cadena.pop(0)
                elif produccion=="Cadena Vacia":
                    self.pila.pop()
                else:
                    self.pila.pop()
                    self.pila.extend(produccion[::-1])
            self.listaProduccion.append(produccion)
            conta+=1 
        tablaMostrar.column('Pila', width=300)
        tablaMostrar.column('Cadena', width=900)
        tablaMostrar.column('Produccion', width=300)
        tablaMostrar.pack()
        print (produccion)
        if produccion=="Cadena aceptada!!":
            return 1
        else: 
            return 0