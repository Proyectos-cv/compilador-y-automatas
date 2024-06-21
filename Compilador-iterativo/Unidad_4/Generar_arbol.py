from tkinter import *
from tkinter import ttk
from tkinter.font import Font

from tkinter import scrolledtext as st
from tkinter import filedialog as fd
from tkinter import messagebox as mb
from graphviz import Digraph
from copy import *
import time


import json 

class Arbol_semantico:
    def __init__(self) -> None:
        self.stack_semantico_producido = []
        self.productores_stack_semantico = []
        self.valores_terminales = []
        self.analizando_operacion = False
        self.operacion_finalizada = False
        self.primera = False
        self.iteraciones = 0

    def proces(self,tokens):
        self.variables = []
        self.variablesLexico = []
        self.pos_actual = 0

        #* Se abre el archivo para lectura
        self.archivo = open("axu.txt","r") 
        lineas = self.archivo.read() 
        count = 1

        #* Separar el codigo en lineas
        codigo_separado = lineas.split("\n") 
        listaNumeros = []
        listaLineas = []
        
        for k in codigo_separado:
            listaNumeros.append(count)
            listaLineas.append(k)
            token = k.split(" ")

            if count==len(codigo_separado)-1:
                print("Fin de archivo")
                break

            else:
                for j in token:                
                    self.variables.append(j)

        self.variables.append("%")
        self.variables.append("%")
        self.variables.append("%")

        #*Compara con lo que viene de lexico
        for k in tokens:
            token = k.split(" ")
            if count==len(tokens)-1:
                print("Fin de archivo")
                break

            else:
                for j in token:                
                    self.variablesLexico.append(j)

        self.variablesLexico.append("%")
        self.variablesLexico.append("%")
        self.variablesLexico.append("%")

        print (self.variables)
        print ( self.variablesLexico)

        if self.variables == self.variablesLexico:
            return self.variables         
        else:
            mb.showinfo("Información", "Se ah modificado el código, debe correr el análisis léxico nuevamente")

    def reglas(self,pila,analizado,siguiente):
        print (pila,analizado,siguiente)

        #* Regla de inicio del ánalisis
        if pila == "Programa" and analizado == "&Start":
            produccion = ["&Start",";", "Sentencias","&End"]
            return produccion

        #* Regla de finalización del análisis
        elif pila == analizado:
            if pila == "%" and analizado == "%":
                return "Cadena aceptada!!"
            else:
                return "reconoce"

        #* Opciones disponibles para la regla de sentencias
        elif pila == "Sentencias":
            if analizado == "&print":
                produccion = ["MensajePantalla","Sentencias"]
                return produccion
            
            elif analizado == "&read":
                produccion = ["Pedir","Sentencias"]
                return produccion
            
            elif analizado.startswith('#'):
                produccion = ["Comentario","Sentencias"]
                return produccion
            
            elif analizado == "&int" or analizado == "&float" or analizado == "&chr" or analizado == "&str" or analizado == "&bool":
                produccion = ["DeclaVar","Sentencias"]
                return produccion
            
            elif analizado.startswith('$'):
                produccion = ["Asignar","Sentencias"]
                return produccion

            elif analizado == "&End":
                produccion = "Cadena Vacia"
                return produccion
            else: 
                return "Cadena Rechazada"

        #* Opciones disponibles para la regla de declaración de variables con múltiples variables
        elif pila == "DeclaVar" and siguiente == ",": 
            if analizado == "&int" or analizado == "&float" or analizado == "&chr" or analizado == "&str" or analizado == "&bool":
                produccion = ["tipoDato","NomVar",",","NomVarMul",";"]
                return produccion
            else: 
                return "Cadena Rechazada"

        #* Opciones disponibles para la regla de declaración de variables con una sola variable
        elif pila == "DeclaVar" and siguiente == "hola":
            if analizado == "&int" or analizado == "&float" or analizado == "&chr" or analizado == "&str" or analizado == "&bool":
                produccion = ["tipoDato","NomVar",";"]
                return produccion

        #* Opciones disponibles para la regla de declaración de variables con múltiples variables (continuación)
        elif pila == "NomVarMul" and siguiente == ",":
            produccion = ["NomVar",",","NomVarMul"]
            return produccion
        
        elif pila == "NomVarMul" and analizado.startswith('$'):
            produccion = ["NomVar"]
            return produccion
        
        #* Opciones disponibles para la regla de identificadores de variables
        elif pila == "tipoDato":
            if analizado == "&int":
                produccion = ["&int"]
                return produccion
            
            elif analizado == "&float":
                produccion = ["&float"]
                return produccion
            
            elif analizado == "&chr":
                produccion = ["&chr"]
                return produccion
            
            elif analizado == "&str":
                produccion = ["&str"]
                return produccion
            
            elif analizado == "&bool":
                produccion = ["&bool"]
                return produccion

        #* Opciones disponibles para la regla de identificacion de variables 
        elif pila == "NomVar":
            if analizado.startswith('$'):
                produccion = "reconoce"
                if self.analizando_operacion == True and self.operacion_finalizada == False:
                    self.valores_terminales.append(analizado)

                elif self.analizando_operacion == True and self.operacion_finalizada == True:
                    self.valores_terminales.append(analizado)
                    self.analizando_operacion = False
                    self.operacion_finalizada = False
                    self.organizar_arbol()

                return produccion
            else:
                return "Cadena Rechazada"

        ##* SECCION DEL CÓDIGO ORIENTADA A LOS COMENTARIOS
        elif pila == "Comentario":
            if analizado.startswith('#'):
                produccion = "reconoce"
                return produccion

        ##* SECCION DEL CÓDIGO ORIENTADA A LA IMPRESIÓN DE MENSAJES
        elif pila == "MensajePantalla":
            produccion = ["&print","(", "Imprimir", ")",";"]
            return produccion

        elif pila == "Imprimir":
            if siguiente==",":
                produccion = ["imprime",",","Imprimir"]
                return produccion
            else:
                produccion = ["imprime"]
                return produccion

        #* Opciones disponibles para la regla de impresión de mensajes
        elif pila == "imprime":
            if analizado.startswith('"'):
                produccion = ["LoQueSea"]
                return produccion
            
            elif analizado.startswith('$'):
                produccion = ["NomVar"]
                return produccion   
            
            elif analizado.isdigit():
                produccion = ["Entero"]
                return produccion
            
            elif analizado.replace(".", "").isdigit():
                produccion = ["Decimal"]
                return produccion
            else :
                return "Cadena Rechazada"

        elif pila == "LoQueSea":
            if analizado.startswith('"'):
                produccion = "reconoce"
                return produccion
            
        elif pila == "Entero" and analizado.isdigit():
            produccion = "reconoce"
            if self.analizando_operacion == True and self.operacion_finalizada == False:
                self.valores_terminales.append(analizado)

            elif self.analizando_operacion == True and self.operacion_finalizada == True:
                self.valores_terminales.append(analizado)
                self.analizando_operacion = False
                self.operacion_finalizada = False
                self.organizar_arbol()
            return produccion
        
        elif pila == "Decimal" and analizado.replace(".", "").isdigit():
            produccion = "reconoce"
            if self.analizando_operacion == True and self.operacion_finalizada == False:
                self.valores_terminales.append(analizado)

            elif self.analizando_operacion == True and self.operacion_finalizada == True:
                self.valores_terminales.append(analizado)
                self.analizando_operacion = False
                self.operacion_finalizada = False
                self.organizar_arbol()
            return produccion     
        
        ##* SECCION DEL CÓDIGO ORIENTADA A LA PETICIÓN DE DATOS
        elif pila == "Pedir":
            produccion = ["&read","NomVar",";"]
            return produccion
        
        elif pila == "Asignar":
            

            if siguiente == "true" or siguiente == "false":
                produccion = ["NomVar","=","Bandera",";"]
                return produccion
            
            elif siguiente.startswith('"'):
                produccion = ["NomVar","=","LoQueSea",";"]
                return produccion
            
            elif siguiente.startswith('$') and not (analizado in ["+","-","*","/"]):
                produccion = ["NomVar","=","NomVar",";"]
                return produccion
            
            elif siguiente.isdigit() and not (analizado in ["+","-","*","/"]):
                produccion = ["NomVar","=","Entero",";"]
                return produccion
            
            elif siguiente.replace(".", "").isdigit() and not (analizado in ["+","-","*","/"]):
                produccion = ["NomVar","=","Decimal",";"]
                return produccion
            
            elif (siguiente.isdigit() or self.oeprando.startswith("$")) and (analizado in ["+","-","*","/"]):
                self.productores_stack_semantico.append("Asignar")
                self.analizando_operacion = True
                produccion = ["NomVar","=","Operacion",";"]
                self.stack_semantico_producido.append(produccion)
                return produccion
            
            elif (siguiente.replace(".", "").isdigit() or self.oeprando.startswith("$")) and (analizado in ["+","-","*","/"]):
                self.productores_stack_semantico.append("Asignar")
                self.analizando_operacion = True
                produccion = ["NomVar","=","Operacion",";"]
                self.stack_semantico_producido.append(produccion)

                return produccion
            else: 
                produccion = ["NomVar","=","LoQueSea",";"]
                return produccion
            
        elif pila == "Bandera":
            if analizado == "true":
                produccion = ["true"]
                return produccion
            
            elif analizado == "false":
                produccion = ["false"]
                return produccion
            else: 
                return "Cadena Rechazada"
        
        ##* SECCION DEL CÓDIGO ORIENTADA A LAS OPERACIONES  
        elif pila == "Operacion" and (analizado.isdigit() or analizado.replace(".", "").isdigit() or analizado.startswith("$")):
            self.productores_stack_semantico.append("Operacion")

            if siguiente in ["+","-","*","/"]:
                produccion = ["Operando", "Operador", "Operando", "Continuacion"]
                self.stack_semantico_producido.append(produccion)
                return produccion
            
            elif siguiente==";":
                produccion = ["Operando", "Operador", "Operando"]
                self.stack_semantico_producido.append(produccion)
                self.primera = True
                return produccion
            else :
                return "Cadena Rechazada"
            
        elif pila == "Operando":
            self.productores_stack_semantico.append("Operando")
            if self.primera == True:
                self.iteraciones = self.iteraciones + 1

                if self.iteraciones == 2:
                    self.operacion_finalizada = True

            if analizado.isdigit():
                produccion = ["Entero"]
                self.stack_semantico_producido.append(produccion)
                return produccion
            
            elif analizado.replace(".", "").isdigit():
                produccion = ["Decimal"]
                self.stack_semantico_producido.append(produccion)
                return produccion
            
            elif analizado.startswith("$"):
                produccion = ["NomVar"]
                self.stack_semantico_producido.append(produccion)
                return produccion
            else:
                return "Cadena Rechazada"
            
        elif pila == "Operador":
            self.productores_stack_semantico.append("Operador")
            if analizado == "+":
                produccion = ["+"]
                self.valores_terminales.append("+")
                return produccion
            
            elif analizado == "-":
                produccion = ["-"]
                self.valores_terminales.append("-")
                return produccion
            
            elif analizado == "*":
                produccion = ["*"]
                self.valores_terminales.append("*")
                return produccion
            
            elif analizado == "/":
                produccion = ["/"]
                self.valores_terminales.append("/")
                return produccion
            else:
                return "Cadena Rechazada"
            
        elif (pila == "+" and analizado == "+") or (pila == "-"and analizado == "-") or (pila == "*"and analizado == "*") or (pila == "/"and analizado == "/"):
            produccion = "reconoce"
            self.valores_terminales.append(pila)
            return produccion
        
        elif pila == "Continuacion":
            self.productores_stack_semantico.append("Continuacion")

            print (analizado,pila,siguiente)
            if siguiente in ["+","-","*","/"]:
                produccion = ["Operador", "Operando", "Continuacion"]    
                self.stack_semantico_producido.append(produccion)
                return produccion
            
            elif siguiente == ";":
                produccion = ["Operador", "Operando"]
                self.stack_semantico_producido.append(produccion)
                self.operacion_finalizada = True
                return produccion
            else:
                return "Cadena Rechazada"
        else:
            return "Cadena Rechazada"

    ##* SECCIÓN DEL CÓDIGO QUE SE ENCARGA DE LA ITERACIÓN POR LAS REGLAS DEL ANÁLISIS SINTÁCTICO
    def analisisSintactico(self):
        #* inicializa la pila y la cadena
        self.pila = ["%","Programa"]
        cadena = self.variables
        conta = 0

        #* eliminamos los espacios en blanco
        while "" in cadena:
            cadena.remove("")

        #* guardado de registro para tabla
        self.listaProduccion=[]
        self.listaPila=[]
        self.listaCadena=[]

        produccion = ""
        self.oeprando=""
 
        while produccion!="Cadena aceptada!!" and produccion!="Cadena Rechazada":            
            self.listaCadena.append(cadena)
            self.listaPila.append(self.pila)

            if (self.pila[-1] == "DeclaVar" and cadena[2] == ",") or (self.pila[-1] == "Continuacion" and cadena[2] in ["+","-","*","/",";"]): 
                produccion = self.reglas(self.pila[-1],cadena[0],cadena[2])

            elif (self.pila[-1] == "NomVarMul" and cadena[1] == ",") or (self.pila[-1] == "Imprimir" and cadena[1] == ","):
                produccion = self.reglas(self.pila[-1],cadena[0],cadena[1])

            elif (self.pila[-1] == "Asignar" and cadena[1] == "="):
                self.oeprando = cadena[0]
                produccion = self.reglas(self.pila[-1],cadena[3],cadena[2])

            elif (self.pila[-1] == "Operacion"):
                produccion = self.reglas(self.pila[-1],cadena[0],cadena[3])
            else:
                produccion = self.reglas(self.pila[-1],cadena[0],"hola")

            if produccion != None:
                if produccion == "reconoce":
                    self.pila.pop()
                    cadena.pop(0)
                elif produccion == "Cadena Vacia":
                    self.pila.pop()
                else:
                    self.pila.pop()
                    self.pila.extend(produccion[::-1])

            self.listaProduccion.append(produccion)
            conta+=1 
    
    def analisisSintacticoretorno(self):        
        #* inicializa la pila y la cadena
        self.pila = ["%","Programa"]
        cadena = self.variables
        conta = 0

        #* eliminamos los espacios en blanco
        while "" in cadena:
            cadena.remove("")

        #* guardado de registro para tabla
        self.listaProduccion = []
        self.listaPila = []
        self.listaCadena = []

        produccion = ""
        self.oeprando = ""

        while produccion != "Cadena aceptada!!" and produccion != "Cadena Rechazada":            
            self.listaCadena.append(cadena)
            self.listaPila.append(self.pila)

            if (self.pila[-1] == "DeclaVar" and cadena[2] == ",") or (self.pila[-1] == "Continuacion" and cadena[2] in ["+","-","*","/",";"]): 
                produccion = self.reglas(self.pila[-1],cadena[0],cadena[2])

            elif (self.pila[-1] == "NomVarMul" and cadena[1] == ",") or (self.pila[-1] == "Imprimir" and cadena[1] == ","):
                produccion = self.reglas(self.pila[-1],cadena[0],cadena[1])
                
            elif (self.pila[-1] == "Asignar" and cadena[1] == "="):
                self.oeprando = cadena[0]
                produccion = self.reglas(self.pila[-1],cadena[3],cadena[2])
                
            elif (self.pila[-1]=="Operacion"):
                produccion = self.reglas(self.pila[-1],cadena[0],cadena[3])
            else:
                produccion = self.reglas(self.pila[-1],cadena[0],"hola")

            if produccion != None:
                if produccion == "reconoce":
                    self.pila.pop()
                    cadena.pop(0)
                elif produccion == "Cadena Vacia":
                    self.pila.pop()
                else:
                    self.pila.pop()
                    self.pila.extend(produccion[::-1])
            self.listaProduccion.append(produccion)
            conta += 1 

        if produccion =="Cadena aceptada!!":
            return 1
        else: 
            return 0

    def organizar_arbol(self):
        nodos = []
        orden = []
        padre = []

        apariciones = [['Operando', 0], ['Operador', 0], ['Continuacion', 0],['NomVar', 0], ['Entero', 0], ['Decimal', 0], ['Operacion,', 0]]
        continuacion = self.productores_stack_semantico[0]
        finalizacion = False

        while not finalizacion:
            if continuacion == "Asignar":
                #*Se extrae la producción de stack_semantico_producido
                produccion = self.stack_semantico_producido[0]

                #* Se eliminan las producciones de las listas
                self.productores_stack_semantico.pop(0)
                self.stack_semantico_producido.pop(0)

                continuacion = produccion[0]

                #* Se crea el nodo padre
                padre = [1, "Asignar"]
                nodos.append([1, "Asignar"])

                for elemento in produccion:
                    item = nodos[-1][0] + 1
                    nodos.append([item, elemento])
                
                for nodo in nodos:
                    if nodo != padre:
                        raiz = padre[0]
                        hijo = nodo[0]
                        orden.append([raiz, hijo])

            if continuacion == "Operacion":
                #* Se extrae la producción de stack_semantico_producido
                produccion = self.stack_semantico_producido[0]

                #* Se eliminan las producciones de las listas
                self.stack_semantico_producido.pop(0)
                self.productores_stack_semantico.pop(0)

                continuacion = produccion[0]
                padre = []
                nodos_temporales = []
                #* Se localiza el nodo padre
                nodos_repetidos = 0
                for elemento in nodos:
                    item = elemento[0]
                    nombre = elemento[1]

                    if elemento[1] == 'Operacion' and  apariciones[6][1] == 0:
                        padre = [item, elemento[1]]
                        apariciones[6][1] += 1
                        break

                    elif elemento[1] == 'Operacion' and apariciones[6][1] <= nodos_repetidos:
                        padre = [item, elemento[1]]
                        apariciones[0][1] += 1
                        break

                    elif elemento[1] == 'Operacion' and apariciones[6][1] >= nodos_repetidos:
                        nodos_repetidos += 1
                
                for elemento in produccion:
                    item = nodos[-1][0] + 1
                    nodos.append([item, elemento])
                    nodos_temporales.append([item, elemento])
                
                #* Relaciona todos los nodos con el padre, excepto el mismo y almacena el orden de los nodos
                for nodo in nodos_temporales:
                    if nodo != padre:
                        raiz = padre[0]
                        hijo = nodo[0]
                        orden.append([raiz, hijo])

            if continuacion == "Operando":
                #* Se extraer la producción de stack_semantico_producido
                produccion = self.stack_semantico_producido[0]

                #* Se eliminan las producciones de las listas
                self.stack_semantico_producido.pop(0)
                self.productores_stack_semantico.pop(0)

                #* Se agrega el siguiente nodo a ser analizado
                continuacion = produccion[0]
                padre = []
                nodos_temporales = []

                #* Se localiza el nodo padre 
                nodos_repetidos = 0
                for elemento in nodos:
                    item = elemento[0]
                    nombre = elemento[1]

                    if elemento[1] == 'Operando' and  apariciones[0][1] == 0:
                        padre = [item, elemento[1]]
                        apariciones[0][1] += 1
                        break

                    elif elemento[1] == 'Operando' and apariciones[0][1] <= nodos_repetidos:
                        padre = [item, elemento[1]]
                        apariciones[0][1] += 1
                        break

                    elif elemento[1] == 'Operando' and apariciones[0][1] >= nodos_repetidos:
                        nodos_repetidos += 1
                
                for elemento in produccion:
                    item = nodos[-1][0] + 1
                    nodos.append([item, elemento])
                    nodos_temporales.append([item, elemento])
                
                #* Relaciona todos los nodos con el padre, excepto el mismo y almacena el orden de los nodos
                for nodo in nodos_temporales:
                    if nodo != padre:
                        raiz = padre[0]
                        hijo = nodo[0]
                        orden.append([raiz, hijo])

            if continuacion == "NomVar":
                #* Se extrae la produccion de valores terminales
                produccion = self.valores_terminales[0]

                #* Se elimina la produccion de la listas
                self.valores_terminales.pop(0)

                if len(self.valores_terminales) != 0:
                    continuacion = self.productores_stack_semantico[0]
                else:
                    continuacion = ";"

                padre = []
                nodos_repetidos = 0
                #* Se localiza el nodo padre
                for elemento in nodos:
                    item = elemento[0]
                    nombre = elemento[1]

                    if elemento[1] == 'NomVar' and  apariciones[3][1] == 0:
                        padre = [item, nombre]
                        apariciones[3][1] += 1
                        break

                    elif elemento[1] == 'NomVar' and apariciones[3][1] <= nodos_repetidos:
                        padre = [item, nombre]
                        apariciones[3][1] += 1
                        break
                    
                    elif elemento[1] == 'NomVar' and apariciones[3][1] >= nodos_repetidos:
                        nodos_repetidos += 1
                
                #* Se crea el nodo hijo
                item = nodos[-1][0] + 1
                nodos.append([item, produccion])

                #* Relaciona todos los nodos con el padre, excepto el mismo y almacena el orden de los nodos
                orden.append([padre[0], item])

            if continuacion == "Operador":
                #* Se extrae la produccion de valores terminales
                produccion = self.valores_terminales[0]

                #* Se elimina la produccion de la listas
                self.valores_terminales.pop(0)
                self.productores_stack_semantico.pop(0)

                #* Se agrega el siguiente nodo a ser analizado
                continuacion = self.productores_stack_semantico[0]

                padre = []
                nodos_repetidos = 0
                #* Se localiza el nodo padre
                for elemento in nodos:
                    item = elemento[0]
                    nombre = elemento[1]

                    if elemento[1] == 'Operador'and apariciones[1][1] == 0:
                        padre = [item, nombre]
                        apariciones[1][1] += 1
                        break

                    elif elemento[1] == 'Operador' and apariciones[1][1] <= nodos_repetidos:
                        padre = [item, nombre]
                        apariciones[1][1] += 1
                        break

                    elif elemento[1] == 'Operador' and apariciones[1][1] >= nodos_repetidos:
                        nodos_repetidos += 1
                
                #* Se crea el nodo hijo
                item = nodos[-1][0] + 1
                nodos.append([item, produccion])

                #* Relaciona todos los nodos con el padre, excepto el mismo y almacena el orden de los nodos
                orden.append([padre[0], item])

            if continuacion == "Continuacion":
                #* Se extrae la produccion de valores terminales
                produccion = self.stack_semantico_producido[0]

                #* Se elimina la produccion de la listas
                self.stack_semantico_producido.pop(0)
                self.productores_stack_semantico.pop(0)

                #* Se agrega el siguiente nodo a ser analizado
                continuacion = self.productores_stack_semantico[0]

                padre = []
                nodos_repetidos = 0
                #* Se localiza el nodo padre
                for elemento in nodos:
                    item = elemento[0]
                    nombre = elemento[1]

                    if elemento[1] == 'Continuacion' and apariciones[2][1] == 0:
                        padre = [item, nombre]
                        apariciones[2][1] += 1
                        break

                    elif elemento[1] == 'Continuacion' and apariciones[2][1] <= nodos_repetidos:
                        padre = [item, nombre]
                        apariciones[2][1] += 1
                        break

                    elif elemento[1] == 'Continuacion' and apariciones[2][1] >= nodos_repetidos:
                        nodos_repetidos += 1
                
                nodos_temporales = []

                #* Se crean los nodos hijos
                for elemento in produccion:
                    item = nodos[-1][0] + 1
                    nodos.append([item, elemento])
                    nodos_temporales.append([item, elemento])

                #* Relaciona todos los nodos con el padre, excepto el mismo y almacena el orden de los nodos
                for nodo in nodos_temporales:
                    if nodo != padre:
                        raiz = padre[0]
                        hijo = nodo[0]
                        orden.append([raiz, hijo])

            if continuacion == "Entero":
                #* Se extrae la produccion de valores terminales
                produccion = self.valores_terminales[0]

                #* Se elimina la produccion de la listas
                self.valores_terminales.pop(0)

                if len(self.valores_terminales) != 0:
                    continuacion = self.productores_stack_semantico[0]
                else:
                    continuacion = ";"

                padre = []
                nodos_repetidos = 0
                #* Se localiza el nodo padre
                for elemento in nodos:
                    item = elemento[0]
                    nombre = elemento[1]

                    if elemento[1] == 'Entero' and  apariciones[4][1] == 0:
                        padre = [item, nombre]
                        apariciones[4][1] += 1
                        break

                    elif elemento[1] == 'Entero' and apariciones[4][1] <= nodos_repetidos:
                        padre = [item, nombre]
                        apariciones[4][1] += 1
                        break
                    
                    elif elemento[1] == 'Entero' and apariciones[4][1] >= nodos_repetidos:
                        nodos_repetidos += 1
                
                #* Se crea el nodo hijo
                item = nodos[-1][0] + 1
                nodos.append([item, produccion])

                #* Relaciona todos los nodos con el padre, excepto el mismo y almacena el orden de los nodos
                orden.append([padre[0], item])

            if continuacion == "Decimal":
                #* Se extrae la produccion de valores terminales
                produccion = self.valores_terminales[0]

                #* Se elimina la produccion de la listas
                self.valores_terminales.pop(0)

                if len(self.valores_terminales) != 0:
                    continuacion = self.productores_stack_semantico[0]
                else:
                    continuacion = ";"

                padre = []
                nodos_repetidos = 0
                #* Se localiza el nodo padre
                for elemento in nodos:
                    item = elemento[0]
                    nombre = elemento[1]

                    if elemento[1] == 'Decimal' and  apariciones[5][1] == 0:
                        padre = [item, nombre]
                        apariciones[5][1] += 1
                        break

                    elif elemento[1] == 'Decimal' and apariciones[5][1] <= nodos_repetidos:
                        padre = [item, nombre]
                        apariciones[5][1] += 1
                        break
                    
                    elif elemento[1] == 'Decimal' and apariciones[5][1] >= nodos_repetidos:
                        nodos_repetidos += 1
                
                #* Se crea el nodo hijo
                item = nodos[-1][0] + 1
                nodos.append([item, produccion])

                #* Relaciona todos los nodos con el padre, excepto el mismo y almacena el orden de los nodos
                orden.append([padre[0], item])

            if continuacion == "=":
                continuacion = self.productores_stack_semantico

            if continuacion == ";":
                break

        #* Recorrer el árbol al revés para obtener sus valores
        orden_valores = orden[::-1]
        nodos_valores = nodos[::-1]

        valores_nodos = [[3, '='], [5, ';']]

        iteraciones = 0
        for elemento in orden_valores:
            nodo_inicial = elemento[1]
            nodo_destino = elemento[0]
            
            #* Buscamos cuantos nodos comparten el mismo valor para saber si es un productor o un terminal
            contador_nodos = 0

            for nodo in orden_valores:
                #* Verifica que el nodo que se está recoriendo no sea uno inferior al nodo inicial
                if nodo[0] == nodo_destino:
                    contador_nodos += 1
            
            #* Si el nodo es un productor terminal, se le asigna el valor de su primer hijo
            if contador_nodos == 1:
                valor = ""
                if len(valores_nodos) == 0:
                    for nodo in nodos:
                        if nodo[0] == nodo_inicial:
                            valor = nodo[1]
                            break
                else:
                    for nodo in valores_nodos:
                        if nodo[0] == nodo_inicial:
                            valor = nodo[1]
                            break

                    if valor == "":
                        for nodo in nodos:
                            if nodo[0] == nodo_inicial:
                                valor = nodo[1]
                                break

                valores_nodos.append([nodo_destino, valor])

            elif contador_nodos > 1:
                lista_nodos_relacionados = []
                lista_valores = []

                in_list = False
                #* Verificamos que el nodo no haya sido recorido antes
                for item in valores_nodos:
                    if item[0] == nodo_destino:
                        in_list = True

                if not in_list:
                    if nodo_destino == 1:
                        lista_nodos_relacionados = [2, 3, 4, 5]
                        lista_valores = []

                        for nodo in lista_nodos_relacionados:
                            for elemento_aux in valores_nodos:
                                if elemento_aux[0] == nodo:
                                    lista_valores.append(elemento_aux[1])
                                    lista_valores.append(" ")
                                    break
                        #* Se elimina el últmo espacio de la lista
                        lista_valores.pop(-1)
                        
                        #* Se concatenan las producciones
                        valor = ""
                        for cadena in lista_valores:
                            valor += cadena
                        
                        valores_nodos.append([nodo_destino, valor])  
                    else:  
                        for nodo in orden:
                            if nodo[0] == nodo_destino:
                                lista_nodos_relacionados.append(nodo[1])

                        #* Se extraen lis valores de los nodos relacionados
                        for elemento_aux in valores_nodos:
                            for nodo in lista_nodos_relacionados:
                                if elemento_aux[0] == nodo:
                                    lista_valores.append(elemento_aux[1])
                                    lista_valores.append(" ")
                                    break
                        #* Se elimina el últmo espacio de la lista
                        lista_valores.pop(-1)
                        
                        #* Se concatenan las producciones
                        valor = ""
                        lista_valores = lista_valores[::-1]
                        for cadena in lista_valores:
                            valor += cadena
                        
                        valores_nodos.append([nodo_destino, valor])


            iteraciones += 1
        
        #* Se eliminan los primeros dos elementos
        valores_nodos.pop(0)
        valores_nodos.pop(0)
        
        #* concatena los valores de los nodos con el mismo valor de tal manera que quede de la siguiente manera: [1, 'Asignacion, \n valor: $a = $a + 170 * 98.2 - $c0 ;']
        for elemento in valores_nodos:
            for nodo in nodos:
                if elemento[0] == nodo[0]:
                    nodo[1] = nodo[1] + " \n valor: " + elemento[1]
                    break
        
        #for nodo in nodos:
        #    print(nodo)

        #De los nodos, cambia el 1, 2, 3, etc por A, B, C, etc
        for nodo in nodos:
            if nodo[0] == 1:
                nodo[0] = 'A'
            elif nodo[0] == 2:
                nodo[0] = 'B'
            elif nodo[0] == 3:
                nodo[0] = 'C'
            elif nodo[0] == 4:
                nodo[0] = 'D'
            elif nodo[0] == 5:
                nodo[0] = 'E'
            elif nodo[0] == 6:
                nodo[0] = 'F'
            elif nodo[0] == 7:
                nodo[0] = 'G'
            elif nodo[0] == 8:
                nodo[0] = 'H'
            elif nodo[0] == 9:
                nodo[0] = 'I'
            elif nodo[0] == 10:
                nodo[0] = 'J'
            elif nodo[0] == 11:
                nodo[0] = 'K'
            elif nodo[0] == 12:
                nodo[0] = 'L'
            elif nodo[0] == 13:
                nodo[0] = 'M'
            elif nodo[0] == 14:
                nodo[0] = 'N'
            elif nodo[0] == 15:
                nodo[0] = 'O'
            elif nodo[0] == 16:
                nodo[0] = 'P'
            elif nodo[0] == 17:
                nodo[0] = 'Q'
            elif nodo[0] == 18:
                nodo[0] = 'R'
            elif nodo[0] == 19:
                nodo[0] = 'S'
            elif nodo[0] == 20:
                nodo[0] = 'T'
            elif nodo[0] == 21:
                nodo[0] = 'U'
            elif nodo[0] == 22:
                nodo[0] = 'V'
            elif nodo[0] == 23:
                nodo[0] = 'W'
            elif nodo[0] == 24:
                nodo[0] = 'X'
            elif nodo[0] == 25:
                nodo[0] = 'Y'
            elif nodo[0] == 26:
                nodo[0] = 'Z'
            elif nodo[0] == 27:
                nodo[0] = 'a'
            elif nodo[0] == 28:
                nodo[0] = 'b'
            elif nodo[0] == 29:
                nodo[0] = 'c'
            elif nodo[0] == 30:
                nodo[0] = 'd'
            elif nodo[0] == 31:
                nodo[0] = 'e'
            elif nodo[0] == 32:
                nodo[0] = 'f'
            elif nodo[0] == 33:
                nodo[0] = 'g'
            elif nodo[0] == 34:
                nodo[0] = 'h'
            elif nodo[0] == 35:
                nodo[0] = 'i'
            elif nodo[0] == 36:
                nodo[0] = 'j'
            elif nodo[0] == 37:
                nodo[0] = 'k'
            elif nodo[0] == 38:
                nodo[0] = 'l'
            elif nodo[0] == 39:
                nodo[0] = 'm'
            elif nodo[0] == 40:
                nodo[0] = 'n'
            elif nodo[0] == 41:
                nodo[0] = 'o'
            elif nodo[0] == 42:
                nodo[0] = 'p'
            elif nodo[0] == 43:
                nodo[0] = 'q'
            elif nodo[0] == 44:
                nodo[0] = 'r'
            elif nodo[0] == 45:
                nodo[0] = 's'
            elif nodo[0] == 46:
                nodo[0] = 't'
            elif nodo[0] == 47:
                nodo[0] = 'u'
            elif nodo[0] == 48:
                nodo[0] = 'v'
            elif nodo[0] == 49:
                nodo[0] = 'w'
            elif nodo[0] == 50:
                nodo[0] = 'x'
            elif nodo[0] == 51:
                nodo[0] = 'y'
            elif nodo[0] == 52:
                nodo[0] = 'y'
            elif nodo[0] == 53:
                nodo[0] = 'z'

        #Del orden , cambia el 1, 2, 3, etc por A, B, C, etc
        for elemento in orden:
            if elemento[0] == 1:
                elemento[0] = 'A'
            elif elemento[0] == 2:
                elemento[0] = 'B'
            elif elemento[0] == 3:
                elemento[0] = 'C'
            elif elemento[0] == 4:
                elemento[0] = 'D'
            elif elemento[0] == 5:
                elemento[0] = 'E'
            elif elemento[0] == 6:
                elemento[0] = 'F'
            elif elemento[0] == 7:
                elemento[0] = 'G'
            elif elemento[0] == 8:
                elemento[0] = 'H'
            elif elemento[0] == 9:
                elemento[0] = 'I'
            elif elemento[0] == 10:
                elemento[0] = 'J'
            elif elemento[0] == 11:
                elemento[0] = 'K'
            elif elemento[0] == 12:
                elemento[0] = 'L'
            elif elemento[0] == 13:
                elemento[0] = 'M'
            elif elemento[0] == 14:
                elemento[0] = 'N'
            elif elemento[0] == 15:
                elemento[0] = 'O'
            elif elemento[0] == 16:
                elemento[0] = 'P'
            elif elemento[0] == 17:
                elemento[0] = 'Q'
            elif elemento[0] == 18:
                elemento[0] = 'R'
            elif elemento[0] == 19:
                elemento[0] = 'S'
            elif elemento[0] == 20:
                elemento[0] = 'T'
            elif elemento[0] == 21:
                elemento[0] = 'U'
            elif elemento[0] == 22:
                elemento[0] = 'V'
            elif elemento[0] == 23:
                elemento[0] = 'W'
            elif elemento[0] == 24:
                elemento[0] = 'X'
            elif elemento[0] == 25:
                elemento[0] = 'Y'
            elif elemento[0] == 26:
                elemento[0] = 'Z'
            elif elemento[0] == 27:
                elemento[0] = 'a'
            elif elemento[0] == 28:
                elemento[0] = 'b'
            elif elemento[0] == 29:
                elemento[0] = 'c'
            elif elemento[0] == 30:
                elemento[0] = 'd'
            elif elemento[0] == 31:
                elemento[0] = 'e'
            elif elemento[0] == 32:
                elemento[0] = 'f'
            elif elemento[0] == 33:
                elemento[0] = 'g'
            elif elemento[0] == 34:
                elemento[0] = 'h'
            elif elemento[0] == 35:
                elemento[0] = 'i'
            elif elemento[0] == 36:
                elemento[0] = 'j'
            elif elemento[0] == 37:
                elemento[0] = 'k'
            elif elemento[0] == 38:
                elemento[0] = 'l'
            elif elemento[0] == 39:
                elemento[0] = 'm'
            elif elemento[0] == 40:
                elemento[0] = 'n'
            elif elemento[0] == 41:
                elemento[0] = 'o'
            elif elemento[0] == 42:
                elemento[0] = 'p'
            elif elemento[0] == 43:
                elemento[0] = 'q'
            elif elemento[0] == 44:
                elemento[0] = 'r'
            elif elemento[0] == 45:
                elemento[0] = 's'
            elif elemento[0] == 46:
                elemento[0] = 't'
            elif elemento[0] == 47:
                elemento[0] = 'u'
            elif elemento[0] == 48:
                elemento[0] = 'v'
            elif elemento[0] == 49:
                elemento[0] = 'w'
            elif elemento[0] == 50:
                elemento[0] = 'x'
            elif elemento[0] == 51:
                elemento[0] = 'y'
            elif elemento[0] == 52:
                elemento[0] = 'y'
            elif elemento[0] == 53:
                elemento[0] = 'z'

            if elemento[1] == 1:
                elemento[1] = 'A'
            elif elemento[1] == 2:
                elemento[1] = 'B'
            elif elemento[1] == 3:
                elemento[1] = 'C'
            elif elemento[1] == 4:
                elemento[1] = 'D'
            elif elemento[1] == 5:
                elemento[1] = 'E'
            elif elemento[1] == 6:
                elemento[1] = 'F'
            elif elemento[1] == 7:
                elemento[1] = 'G'
            elif elemento[1] == 8:
                elemento[1] = 'H'
            elif elemento[1] == 9:
                elemento[1] = 'I'
            elif elemento[1] == 10:
                elemento[1] = 'J'
            elif elemento[1] == 11:
                elemento[1] = 'K'
            elif elemento[1] == 12:
                elemento[1] = 'L'
            elif elemento[1] == 13:
                elemento[1] = 'M'
            elif elemento[1] == 14:
                elemento[1] = 'N'
            elif elemento[1] == 15:
                elemento[1] = 'O'
            elif elemento[1] == 16:
                elemento[1] = 'P'
            elif elemento[1] == 17:
                elemento[1] = 'Q'
            elif elemento[1] == 18:
                elemento[1] = 'R'
            elif elemento[1] == 19:
                elemento[1] = 'S'
            elif elemento[1] == 20:
                elemento[1] = 'T'
            elif elemento[1] == 21:
                elemento[1] = 'U'
            elif elemento[1] == 22:
                elemento[1] = 'V'
            elif elemento[1] == 23:
                elemento[1] = 'W'
            elif elemento[1] == 24:
                elemento[1] = 'X'
            elif elemento[1] == 25:
                elemento[1] = 'Y'
            elif elemento[1] == 26:
                elemento[1] = 'Z'
            elif elemento[1] == 27:
                elemento[1] = 'a'
            elif elemento[1] == 28:
                elemento[1] = 'b'
            elif elemento[1] == 29:
                elemento[1] = 'c'
            elif elemento[1] == 30:
                elemento[1] = 'd'
            elif elemento[1] == 31:
                elemento[1] = 'e'
            elif elemento[1] == 32:
                elemento[1] = 'f'
            elif elemento[1] == 33:
                elemento[1] = 'g'
            elif elemento[1] == 34:
                elemento[1] = 'h'
            elif elemento[1] == 35:
                elemento[1] = 'i'
            elif elemento[1] == 36:
                elemento[1] = 'j'
            elif elemento[1] == 37:
                elemento[1] = 'k'
            elif elemento[1] == 38:
                elemento[1] = 'l'
            elif elemento[1] == 39:
                elemento[1] = 'm'
            elif elemento[1] == 40:
                elemento[1] = 'n'
            elif elemento[1] == 41:
                elemento[1] = 'o'
            elif elemento[1] == 42:
                elemento[1] = 'p'
            elif elemento[1] == 43:
                elemento[1] = 'q'
            elif elemento[1] == 44:
                elemento[1] = 'r'
            elif elemento[1] == 45:
                elemento[1] = 's'
            elif elemento[1] == 46:
                elemento[1] = 't'
            elif elemento[1] == 47:
                elemento[1] = 'u'
            elif elemento[1] == 48:
                elemento[1] = 'v'
            elif elemento[1] == 49:
                elemento[1] = 'w'
            elif elemento[1] == 50:
                elemento[1] = 'x'
            elif elemento[1] == 51:
                elemento[1] = 'y'
            elif elemento[1] == 52:
                elemento[1] = 'y'
            elif elemento[1] == 53:
                elemento[1] = 'z'

        #* Se crea el arbol mediante graphviz
        dot = Digraph(comment='Arbol de derivación semántico')
        for nodo in nodos:
            dot.node(str(nodo[0]), str(nodo[1]))

        for elemento in orden:
            dot.edge(str(elemento[0]), str(elemento[1]))

        dot.render('Arbol de derivación semántico', view=True)
        #* Paraliza el proceso por medio segundo
        time.sleep(0.7)

        #* Reincia las variables
        self.productores_stack_semantico = []
        self.stack_semantico_producido = []
        self.valores_terminales = []
        self.variables = 0
        self.primera = False
        self.iteraciones = 0

        
if __name__ == "__main__":
    pass