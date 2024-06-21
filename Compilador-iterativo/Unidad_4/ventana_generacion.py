import os
from tkinter import *
from tkinter import ttk
from tkinter.font import Font
from tkinter import scrolledtext as st
from tkinter import filedialog as fd
from tkinter import messagebox as mb

from cuadruplos import Cuadruplos
from triplos import triplo
from polaca import expresiones

class ventana:
    def __init__(self):
        self.first = ['*', '/']
        self.second = ['+', '-']

    def proces(self,tokens):
        os.system('cls' if os.name == 'nt' else 'clear')
        self.variables = []
        self.variablesSemanticas = []
        self.pos_actual = 0
        self.archivo = open("axu.txt","r") #abro el archivo en lectura
        lineas = self.archivo.read() #leo el archivo
        count = 1
        codigo_separado = lineas.split("\n") #separo el codigo en lineas
        listaNumeros = []
        listaLineas = []
        #print(len (codigo_separado))
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
        #self.variables.pop()
        self.variables.append("%")
        self.variables.append("%")
        self.variables.append("%")
        #Comparacion con lo que viene de lexico
        for k in tokens:
            token = k.split(" ")
            if count==len(tokens)-1:
                    print("Fin de archivo")
                    break
            else:
                for j in token:                
                    self.variablesSemanticas.append(j)
        #self.variables.pop()
        self.variablesSemanticas.append("%")
        self.variablesSemanticas.append("%")
        self.variablesSemanticas.append("%")
        #print (self.variables)
        #print ( self.variablesSemanticas)
        if self.variables== self.variablesSemanticas:
            return self.variables,1         
        else:
            mb.showinfo("Información", "Se ah modificado el código, debe correr el análisis léxico nuevamente")
            return self.variables,0
        
    def seccionar(self):
        lista_lineas = []
        self.archivo = open("axu.txt","r") #abro el archivo en lectura
        lineas = self.archivo.read() #leo el archivo
        count = 1
        codigo_separado = lineas.split("\n")
        #print (codigo_separado)
        for i in codigo_separado:
            token = i.split(" ")
            if len(token)>1:
                if token[1].startswith("=") and len(token)>4:
                    lista_lineas.append(i)
        print (lista_lineas)
        return lista_lineas

    def ventana_generacion(self, operacion):
        self.ventana = Tk()
        ancho_ventana = 825
        alto_ventana = 575
        x_ventana = self.ventana.winfo_screenwidth() // 2 - ancho_ventana // 2
        y_ventana = self.ventana.winfo_screenheight() // 2 - alto_ventana // 2 - 42
        posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
        self.ventana.geometry(posicion)
        self.ventana.title("Generación de codigo intermedio")
        self.ventana.configure(background="wheat1", bd="10", relief="groove")

        self.label = Label(self.ventana, text=" Generación de codigo intermedio ", font=("Arial", 25), background="coral1", relief="groove")
        self.label.grid(row=0, column=0, columnspan=2, sticky="nsew")

        self.label_polaco = Label(self.ventana, text="Notación Polaca", font=("Arial", 15), background="coral1", relief="groove")
        self.label_polaco.grid(row=1, column=0, sticky="nsew")
        #----------------------------------------------------
        self.polaca = ttk.Treeview(self.ventana, columns=("pila1","pila2","cadena"), show="headings")
        self.polaca.heading("pila1", text="Pila1")
        self.polaca.heading("pila2", text="Pila2")
        self.polaca.heading("cadena", text="Cadena")
        self.polaca.column("pila1", width=100)
        self.polaca.column("pila2", width=100)
        self.polaca.column("cadena", width=200)
        self.polaca.grid(row=2, column=0, sticky="nsew")

        obj = expresiones()
        for e in range (0,len(operacion)):
            self.polaca.insert("", END, values=(str("---"),str("---"),str("---")))
            p1,p2,p3 = obj.inicio(operacion[e])
            cadena = ""
            for i in range(0,len(p1)):
                self.polaca.insert("", END, values=(str(p3[i]),str(p2[i]),str(p1[i])))
        """ polaco = obj.inicio(operacion) """
        
        """ cadena = ""
        for i in range(0,len(polaco)):
            cadena = cadena + str(polaco[i])
           
        self.polaca.insert("", END, values=(str(cadena))) """
        #----------------------------------------------------

        self.label_pcode = Label(self.ventana, text="P-Code", font=("Arial", 15), background="coral1", relief="groove")
        self.label_pcode.grid(row=1, column=1, sticky="nsew")

        self.label_triplos = Label(self.ventana, text="Triplos", font=("Arial", 15), background="coral1", relief="groove")
        self.label_triplos.grid(row=3, column=0, sticky="nsew", )

        #-------------------------------------------------

        self.tabla_triplos = ttk.Treeview(self.ventana, columns=("ruta","operador", "operando1", "operando2"), show="headings")
        self.tabla_triplos.heading("ruta", text="ruta")
        self.tabla_triplos.heading("operador", text="Operador")
        self.tabla_triplos.heading("operando1", text="Operando 1")
        self.tabla_triplos.heading("operando2", text="Operando 2")

        self.tabla_triplos.column("ruta", width=50)
        self.tabla_triplos.column("operador", width=60)
        self.tabla_triplos.column("operando1", width=60)
        self.tabla_triplos.column("operando2", width=50)

        self.tabla_triplos.grid(row=4, column=0, sticky="nsew")

        obj = triplo()
        for d in range(0,len(operacion)):
            self.tabla_triplos.insert("", END, values=("---", "---", "---", "---"))

            triplos = obj.inicio(operacion[d])
            # Llenar la tabla de Triplos
            for u in range(0,len(triplos)):
                posicion = triplos[u][0]
                operador = triplos[u][1]
                operando1 = triplos[u][2]
                operando2 = triplos[u][3]
                self.tabla_triplos.insert("", END, values=(posicion, operador, operando1, operando2))

        #Espacio del carlos

#-------------------------------------------------

        self.label_cuadruplos = Label(self.ventana, text="Cuadruplos", font=("Arial", 15), background="coral1", relief="groove")
        self.label_cuadruplos.grid(row=3, column=1, sticky="nsew")

        #Espacio de yo
        self.tabla_cuadruplos = ttk.Treeview(self.ventana, columns=("operador", "operando1", "operando2", "auxiliar"), show="headings")
        self.tabla_cuadruplos.heading("operador", text="Operador")
        self.tabla_cuadruplos.heading("operando1", text="Operando 1")
        self.tabla_cuadruplos.heading("operando2", text="Operando 2")
        self.tabla_cuadruplos.heading("auxiliar", text="Auxiliar")

        self.tabla_cuadruplos.column("operador", width=100)
        self.tabla_cuadruplos.column("operando1", width=100)
        self.tabla_cuadruplos.column("operando2", width=100)
        self.tabla_cuadruplos.column("auxiliar", width=100)

        self.tabla_cuadruplos.grid(row=4, column=1, sticky="nsew")

        obj = Cuadruplos()  
        resultados = []

        for operation in operacion:
            resultado = obj.procedimiento(operation)
            resultados.append(resultado)
        
        for jerarquias in resultados:
            for elemento in jerarquias:
                if elemento[0][1] != '=':
                    operador = elemento[0][1]
                    operando1 = elemento[0][0]
                    operando2 = elemento[0][2]
                    auxiliar = elemento[1]

                    self.tabla_cuadruplos.insert("", END, values=(operador, operando1, operando2, auxiliar))
                
                elif elemento[0][1] == '=':
                    operador = elemento[0][1]
                    operando1 = elemento[0][2]
                    operando2 = "--"
                    auxiliar = elemento[0][0]

                    self.tabla_cuadruplos.insert("", END, values=(operador, operando1, operando2, auxiliar))
                    self.tabla_cuadruplos.insert("", END, values=("---","---","---","---"))

        #espacio de leo
        lista_resultado=[]
        for l in operacion:
            operation_tokens = l.split(' ')
            jerarquías = []        
            lista_op=[]
            lista_nv=[]
            lista_resultado.append("lda "+operation_tokens[0]+ " ;")
            operation_tokens.pop(1)
            operation_tokens.pop(0)
            ban=False
            while ban==False:
                ban_string=False
                for i in range(len(operation_tokens)):
                    print (len(operation_tokens))
                    try:
                        float(operation_tokens[i])
                        ban_string=True
                    except ValueError:
                        ban_string=False
                    if len(operation_tokens)-1>i+1:
                        print (operation_tokens[i])
                        if ban_string==False and operation_tokens[i].startswith("$") and operation_tokens[i+1] not in self.first:
                            print ("entro 1")
                            lista_resultado.append("lod "+operation_tokens[i]+ " ;")
                            operation_tokens.pop(i)
                            if len(lista_op)>0:
                                if lista_op[0]=="+":
                                    lista_resultado.append("adi ;")
                                else:
                                    lista_resultado.append("sbi ;")
                                lista_op.pop(0)
                            break                            
                        elif ban_string and operation_tokens[i+1] not in self.first:
                            print ("entro 2")
                            lista_resultado.append("ldc "+operation_tokens[i]+ " ;")
                            operation_tokens.pop(i)
                            if len(lista_op)>0:
                                if lista_op[0]=="+":
                                    lista_resultado.append("adi ;")
                                else:
                                    lista_resultado.append("sbi ;")
                                lista_op.pop(0)
                            break
                        elif ban_string==True and operation_tokens[i+1] in self.first:
                            print ("entro 3")
                            lista_resultado.append("ldc "+operation_tokens[i]+ " ;")
                            if operation_tokens[i+2].startswith("$"):
                                lista_resultado.append("lod "+operation_tokens[i+2]+ " ;")
                            else:
                                lista_resultado.append("ldc "+operation_tokens[i+2]+ " ;")
                            if operation_tokens[i+1]=="*":
                                lista_resultado.append("mpi ;")
                            else:
                                lista_resultado.append("div ;")
                            operation_tokens.pop(i)
                            operation_tokens.pop(i)
                            operation_tokens.pop(i)
                            break  
                        elif ban_string==False and operation_tokens[i].startswith("$") and operation_tokens[i+1] in self.first:
                            print ("entro 4")
                            lista_resultado.append("lod "+operation_tokens[i]+ " ;")
                            if operation_tokens[i+2].startswith("$"):
                                lista_resultado.append("lod "+operation_tokens[i+2]+ " ;")
                            else:
                                lista_resultado.append("ldc "+operation_tokens[i+2]+ " ;")
                            if operation_tokens[i+1]=="*":
                                lista_resultado.append("mpi ;")
                            else:
                                lista_resultado.append("div ;")
                            operation_tokens.pop(i)
                            operation_tokens.pop(i)
                            operation_tokens.pop(i)
                            break                  
                                    
                        elif operation_tokens[i] in self.second and len(lista_op)==0:
                            print ("entro 5")
                            lista_op.append(operation_tokens[i])
                            operation_tokens.pop(i)                            
                            break
                        elif operation_tokens[i] in self.second and len(lista_op)>0:
                            print ("entro 6")
                            if lista_op[0]=="+":
                                lista_resultado.append("adi ;")
                            else:
                                lista_resultado.append("sbi ;")
                            lista_op.pop(0)
                            lista_op.append(operation_tokens[i])
                            operation_tokens.pop(i)                            
                            break
                        elif operation_tokens[i] in self.first:
                            print ("entro 7")                            
                            if operation_tokens[i+2].startswith("$"):
                                lista_resultado.append("lod "+operation_tokens[i+1]+ " ;")
                            else:
                                lista_resultado.append("ldc "+operation_tokens[i+1]+ " ;")
                            if operation_tokens[i]=="*":
                                lista_resultado.append("mpi ;")
                            else:
                                lista_resultado.append("div ;")                                
                            operation_tokens.pop(i)
                            operation_tokens.pop(i)
                            break
                    elif len(operation_tokens)==2 and len(lista_op)>0:
                        if operation_tokens[i].startswith("$"):
                            print ("entro 11")
                            lista_resultado.append("lod "+operation_tokens[i]+ " ;")
                            operation_tokens.pop(i)
                            if len(lista_op)>0:
                                if lista_op[0]=="+":
                                    lista_resultado.append("adi ;")
                                else:
                                    lista_resultado.append("sbi ;")
                                lista_op.pop(0)
                            break                            
                        else:
                            print ("entro 21")
                            lista_resultado.append("ldc "+operation_tokens[i]+ " ;")
                            operation_tokens.pop(i)
                            if len(lista_op)>0:
                                if lista_op[0]=="+":
                                    lista_resultado.append("adi ;")
                                else:
                                    lista_resultado.append("sbi ;")
                                lista_op.pop(0)
                            break
                    elif operation_tokens[0]==";" and len(lista_op)>0:
                        print ("entro 8")
                        if lista_op[0]=="+":
                            lista_resultado.append("adi ;")
                        else:
                            lista_resultado.append("sbi ;")
                        lista_op.pop(0)
                        ban=True
                    else:
                        ban=True          
                print (operation_tokens)
                print (lista_resultado)
            lista_resultado.append("sto ;")
            lista_resultado.append("________________")
            print (lista_nv)
            print (lista_op)
            print (operation_tokens)
            print (lista_resultado)
        self.tabla_pcode = ttk.Treeview(self.ventana, columns=("operador"), show="headings")
        self.tabla_pcode.heading("operador", text="P-Code")
        self.tabla_pcode.column("operador", width=50)
        self.tabla_pcode.grid(row=2, column=1, sticky="nsew")
        for dato in lista_resultado:
            self.tabla_pcode.insert('', 'end', values=(dato,))
        self.ventana.mainloop()

if __name__ == "__main__":
    ventana = ventana()
    lista = ["$x = 2 + 3 - 1 * 2"]
    ventana.ventana_generacion(lista)