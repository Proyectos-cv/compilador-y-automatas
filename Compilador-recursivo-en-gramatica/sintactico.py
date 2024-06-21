import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
class sintactico():
    def analizar(self, tokens):
        cadena = []

        for sublista in tokens:
            cadena.extend(sublista[1])

        ventana = tk.Tk()
        ventana.geometry("1000x1000")
        text_area = tk.Text(ventana)

        self.tabla = ttk.Treeview(ventana)
        # Definir las columnas
        self.tabla["columns"] = ("columna1", "columna2", "columna3", "columna4","columna5","columna6")

        # Configurar las columnas

        self.tabla.column("columna1", width=0)
        self.tabla.column("columna2", width=150)
        self.tabla.column("columna3", width=150)
        self.tabla.column("columna4", width=150)
        self.tabla.column("columna5", width=150)
        self.tabla.column("columna6", width=150)
        # Definir los encabezados de las columnas
        self.tabla.heading("columna1", text="Columna 1")
        self.tabla.heading("columna2", text="Columna 2")
        self.tabla.heading("columna3", text="Columna 3")
        self.tabla.heading("columna4", text="Columna 4")
        self.tabla.heading("columna5", text="Columna 5")
        self.tabla.heading("columna6", text="")
        



        cadena.append("&")
        self.producciones = ["progama", "sentencia", "declaravar", "declaravar2", "tipodato", "complemento", "complemento2", "comentario"]

        self.produccion = ["programa","&"]
        self.arbol = []

        self.posicion = 0
        print (cadena)
        #print("extension del arbol: ", ['n',self.posicion+1,self.arbol,self.produccion])
        self.tabla.insert(parent="", index="end", iid=1, values=("n",self.posicion+1, self.arbol, self.produccion,"expansion del arbol"))
        if self.programa(cadena):
            print ("cadena aceptada")
            self.produccion.pop(0)
            print ("coincidencia de simbolo: ",['n',self.posicion+1,self.arbol,self.produccion])
            self.arbol.append(self.produccion[0])
            self.produccion.pop(0)
            """  text_area.insert(tk.END, [self.posicion,'t',self.posicion+1,self.arbol,"&"])
            text_area.insert(tk.END, "\n")
            text_area.insert(tk.END, "cadena aceptada")
            text_area.pack()
            text_area.grid(row=0, column=0) """
            
            self.tabla.insert(parent="", index="end", values=("t",self.posicion, self.arbol, self.produccion,"terminacion con exito"))
            self.tabla.insert(parent="", index="end", values=("OK","OK","OK", "OK", "OK"))
            messagebox.showinfo("Resultados", "Cadena aceptada")

            # Mostrar la tabla
            self.tabla.place(x=0,y=0)

            ventana.mainloop()
        else:
            
            print ("coincidencia de simbolo: ",['e',self.posicion+1,self.arbol,self.produccion])
            self.arbol.append(self.produccion[0])
            self.produccion.pop(0)
            """ text_area.insert(tk.END, ['e',self.posicion,self.arbol,self.produccion])
            text_area.insert(tk.END, "\n")
            text_area.insert(tk.END, "cadena no aceptada")
            text_area.pack()
            text_area.grid(row=0, column=0) """
            self.tabla.insert(parent="", index="end", values=("n",self.posicion, self.arbol, self.produccion, "no hay otra alternativa"))
            self.tabla.insert(parent="", index="end", values=("NO OK","NO OK", "NO OK","NO OK", "NO OK"))
            print ("cadena no aceptada")
            messagebox.showinfo("Resultados", "Cadena no aceptada")
            self.tabla.place(x=0,y=0)
            ventana.mainloop()
    def programa(self, cadena):
        self.arbol.append(self.produccion[0])
        self.produccion = [" ¿ ", "sentencia", " ?", "&"]
        #print("concordancia de simbolo: ", ['n',self.posicion+1,self.arbol,self.produccion])
        self.tabla.insert(parent="", index="end", values=("n",self.posicion+1, self.arbol, self.produccion,"concordancia de simbolo"))
        
        if cadena[self.posicion] == '¿':
            self.arbol.append(self.produccion[0])
            self.produccion.pop(0)
            #print("expansion del arbol: ", ['n',self.posicion+1,self.arbol,self.produccion])
            self.tabla.insert(parent="", index="end", values=("n",self.posicion+1, self.arbol, self.produccion,"expansion del arbol"))
            if self.sentencia(cadena):
                self.posicion += 1
                if self.posicion < len (cadena):
                    """  self.arbol.append(self.produccion[0])
                    self.produccion.pop(0)
                    print ("coincidencia de simbolo: ",['n',self.posicion+1,self.arbol,self.produccion]) """
                    if cadena[self.posicion] == '?' and cadena[self.posicion+1] == "&":
                        return True
                else:
                    return False
            else:
                return False
        else :
            return False 
    def sentencia(self, cadena):
        declara = self.declaravar(cadena)
        #print (declara)
        if declara == True or declara == None:
            return True
        comment = self.comentario(cadena)
        if comment == True or comment == None:
            return True
        message = self.mensaje(cadena)
        if message == True or message == None:
            return True
        ins = self.insertar(cadena)
        if ins == True or ins == None:
            return True
        con = self.concatena(cadena)
        if con ==True or con == None:
            return True
        asig = self.asignacion(cadena)
        if asig == True or asig == None:
            return True
        opera = self.operacion(cadena)
        if opera == True or opera == None:
            return True
        df = self.mjs(cadena)
        if df == True or df == None:
            return True
        else:
            #print ("entro aqui")
            return False
    def mjs(self, cadena):
        print (self.posicion)
        self.posicion += 1
    
        if cadena[self.posicion] == "SND":
            

            self.posicion += 1
            if cadena[self.posicion] == '"':

                    self.posicion += 1
                    
                    if cadena[self.posicion] == ',':
                        self.posicion += 1
                        
                        var = self.variable(cadena)
                        if var:
                            #print ("llego")
                            
                            if cadena[self.posicion] == ";":
                               
                                if self.posicion+1 < len(cadena):
                                    if cadena[self.posicion+1] == "?" and cadena[self.posicion+2] == "&":
                                        return True
                                    else:  
                                        self.sentencia(cadena)   
                                else:
                                    return False
                            else:
                                self.posicion -= 4
                                print (self.posicion)
                                return False
                        else :
                            self.posicion -= 3
                            print (self.posicion)
                            return False
                    else:
                        self.posicion -= 2
                        print (self.posicion)
                        return False
            else: 
                self.posicion -= 1
                print (self.posicion)
                return False
        else :
            self.posicion -= 1
            print (self.posicion)
            return False
    def operacion (self,cadena):
        self.arbol.append(self.produccion[0])
        self.produccion.pop(0)
        self.produccion.insert(0,"operacion") 
        #print ("ampliacion del arbol: ",['n',self.posicion+1,self.arbol,self.produccion])
        self.tabla.insert(parent="", index="end", values=("n",self.posicion+1, self.arbol, self.produccion,"ampliacion del arbol"))
        self.arbol.append(self.produccion[0])
        self.produccion.pop(0)
        self.produccion[0:0] = ["nomvar","=","ecuacion",";","sentencias"]
        #print ("ampliacion del arbol: ",['n',self.posicion+1,self.arbol,self.produccion])
        self.tabla.insert(parent="", index="end", values=("n",self.posicion+1, self.arbol, self.produccion,"ampliacion del arbol"))
        self.posicion += 1
        vari = self.variable(cadena)
        if vari:
            self.posicion -= 1
            self.arbol.append(self.produccion[0])
            self.produccion.pop(0) 
            #print ("pasamos produccion: ",['n',self.posicion+1,self.arbol,self.produccion])
            self.tabla.insert(parent="", index="end", values=("n",self.posicion+1, self.arbol, self.produccion,"pasamos produccion"))
            self.arbol.append(cadena[self.posicion])
            #print ("coincidencia de simbolo: ",['n',self.posicion+1,self.arbol,self.produccion])
            self.tabla.insert(parent="", index="end", values=("n",self.posicion+1, self.arbol, self.produccion,"coincidencia de simbolo"))
            self.posicion += 1
            if cadena[self.posicion] == "=":
                self.arbol.append(self.produccion[0])
                self.produccion.pop(0)
                #print ("coincidencia de simbolo: ",['n',self.posicion+1,self.arbol,self.produccion])
                self.tabla.insert(parent="", index="end", values=("n",self.posicion+1, self.arbol, self.produccion,"coincidencia de simbolo"))
                self.arbol.append(self.produccion[0])
                self.produccion.pop(0)
                self.produccion[0:0] = ["valor","operador","valor"]
                #print ("ampliacion del arbol: ",['n',self.posicion+1,self.arbol,self.produccion])
                self.tabla.insert(parent="", index="end", values=("n",self.posicion+1, self.arbol, self.produccion,"ampliacion del arbol"))

                val = self.valor(cadena)
                if val :
                    self.posicion += 1
                    ope = self.operador(cadena)
                    if ope:
                        val2 = self.valor(cadena)
                        if val2:
                            self.posicion +=1

                            print (self.posicion)
                            b= True
                            conta = 0
                            while b:
                                if cadena[self.posicion] == "+" or cadena[self.posicion] == "-" or cadena[self.posicion] == "*" or cadena[self.posicion] == "/":
                                    self.posicion += 1
                                    conta += 1
                                    if self.valores(cadena):
                                        self.posicion +=1
                                        conta += 1
                                    else:
                                        self.posicion = self.posicion - conta
                                        b = False
                                elif cadena[self.posicion] == ";":
                                    b = False
                                else:
                                    self.posicion = self.posicion - conta
                                    b= False 
                            print (self.posicion)


                            if cadena[self.posicion] == ";":
                                self.arbol.append(self.produccion[0])
                                self.produccion.pop(0)
                                #print ("coincidencia de simbolo: ",['n',self.posicion+1,self.arbol,self.produccion])
                                self.tabla.insert(parent="", index="end", values=("n",self.posicion+1, self.arbol, self.produccion,"coincidencia de simbolo"))
                                if self.posicion+1 < len(cadena):
                                    if cadena[self.posicion+1] == "?" and cadena[self.posicion+2] == "&":
                                        return True
                                    else:  
                                        self.sentencia(cadena)   
                                else:
                                    return False
                            else:
                                self.posicion -= 1
                                self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                                self.arbol.pop(len(self.arbol)-1)
                                #print ("no concordancia de simbolos: ",['n',self.posicion+1,self.arbol,self.produccion])
                                self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion,"no concordancia de simbolos"))
                                self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                                self.arbol.pop(len(self.arbol)-1)
                                #print ("retroceso en la entrada: ",['n',self.posicion+1,self.arbol,self.produccion])
                                self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion,"retroceso en la entrada"))
                                del self.produccion[0:2]
                                self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                                self.arbol.pop(len(self.arbol)-1)
                                #print ("retroceso en la entrada: ",['n',self.posicion+1,self.arbol,self.produccion])
                                self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion,"retroceso en la entrada"))
                                self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                                self.arbol.pop(len(self.arbol)-1)
                                #print ("retroceso en la entrada: ",['n',self.posicion+1,self.arbol,self.produccion])
                                self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion,"retroceso en la entrada"))
                                self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                                self.arbol.pop(len(self.arbol)-1)
                                #print ("retroceso en la entrada: ",['n',self.posicion+1,self.arbol,self.produccion])
                                self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion,"retroceso en la entrada"))
                                self.posicion -= 1
                                self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                                self.arbol.pop(len(self.arbol)-1)
                                #print ("retroceso en la entrada: ",['n',self.posicion+1,self.arbol,self.produccion])
                                self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion,"retroceso en la entrada"))
                                self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                                self.arbol.pop(len(self.arbol)-1)
                                #print ("retroceso en la entrada: ",['n',self.posicion+1,self.arbol,self.produccion])
                                self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion,"retroceso en la entrada"))
                                del self.produccion[0:2]
                                self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                                self.arbol.pop(len(self.arbol)-1)
                                #print ("retroceso en la entrada: ",['n',self.posicion+1,self.arbol,self.produccion])
                                self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion,"retroceso en la entrada"))
                                del self.produccion[0:4]
                                self.posicion -= 1
                                self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                                self.arbol.pop(len(self.arbol)-1)
                                #print ("retroceso en la entrada: ",['n',self.posicion+1,self.arbol,self.produccion])
                                self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion,"retroceso en la entrada"))
                                self.posicion -= 1
                                self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                                self.arbol.pop(len(self.arbol)-1)
                                #print ("retroceso en la entrada: ",['n',self.posicion+1,self.arbol,self.produccion])
                                self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion,"retroceso en la entrada"))
                                self.posicion -= 1
                                self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                                self.arbol.pop(len(self.arbol)-1)
                                #print ("retroceso en la entrada: ",['n',self.posicion+1,self.arbol,self.produccion])
                                self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion,"retroceso en la entrada"))
                                self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                                self.arbol.pop(len(self.arbol)-1)
                                #print ("retroceso en la entrada: ",['n',self.posicion+1,self.arbol,self.produccion])
                                self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion,"retroceso en la entrada"))
                                self.posicion -= 1
                                del self.produccion[0:6]
                                self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                                self.arbol.pop(len(self.arbol)-1)
                                #print ("retroceso en la entrada: ",['n',self.posicion+1,self.arbol,self.produccion])
                                self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion,"retroceso en la entrada"))
                                del self.produccion[0:1]
                                self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                                self.arbol.pop(len(self.arbol)-1)
                                #print ("retroceso en la entrada: ",['n',self.posicion+1,self.arbol,self.produccion])
                                self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion,"retroceso en la entrada"))
                                return False  
                        else:
                            self.produccion.pop(0)
                            self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                            self.arbol.pop(len(self.arbol)-1)
                            #print ("no concordancia de simbolos: ",['n',self.posicion+1,self.arbol,self.produccion])
                            self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion,"no concordancia de simbolos"))
                            self.posicion -= 1
                            self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                            self.arbol.pop(len(self.arbol)-1)
                            #print ("retroceso en la entrada: ",['n',self.posicion+1,self.arbol,self.produccion])
                            self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion,"retroceso en la entrada"))
                            self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                            self.arbol.pop(len(self.arbol)-1)
                            #print ("retroceso en la entrada: ",['n',self.posicion+1,self.arbol,self.produccion])
                            self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion,"retroceso en la entrada"))
                            self.posicion -= 1
                            self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                            self.arbol.pop(len(self.arbol)-1)
                            #print ("retroceso en la entrada: ",['n',self.posicion+1,self.arbol,self.produccion])
                            self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion,"retroceso en la entrada"))
                            self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                            self.arbol.pop(len(self.arbol)-1)
                            #print ("retroceso en la entrada: ",['n',self.posicion+1,self.arbol,self.produccion])
                            self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion,"retroceso en la entrada"))
                            del self.produccion[0:2]
                            self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                            self.arbol.pop(len(self.arbol)-1)
                            #print ("retroceso en la entrada: ",['n',self.posicion+1,self.arbol,self.produccion])
                            self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion,"retroceso en la entrada"))
                            del self.produccion[0:4]
                            self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                            self.arbol.pop(len(self.arbol)-1)
                            #print ("retroceso en la entrada: ",['n',self.posicion+1,self.arbol,self.produccion])
                            self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion,"retroceso en la entrada"))
                            self.posicion -= 1
                            self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                            self.arbol.pop(len(self.arbol)-1)
                            #print ("retroceso en la entrada: ",['n',self.posicion+1,self.arbol,self.produccion])
                            self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion,"retroceso en la entrada"))
                            self.posicion -= 1
                            self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                            self.arbol.pop(len(self.arbol)-1)
                            #print ("retroceso en la entrada: ",['n',self.posicion+1,self.arbol,self.produccion])
                            self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion,"retroceso en la entrada"))
                            self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                            self.arbol.pop(len(self.arbol)-1)
                            #print ("retroceso en la entrada: ",['n',self.posicion+1,self.arbol,self.produccion])
                            self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion,"retroceso en la entrada"))
                            self.posicion -= 1
                            del self.produccion[0:10]
                            self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                            self.arbol.pop(len(self.arbol)-1)
                            #print ("retroceso en la entrada: ",['n',self.posicion+1,self.arbol,self.produccion])
                            self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion,"retroceso en la entrada"))
                            del self.produccion[0:1]
                            self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                            self.arbol.pop(len(self.arbol)-1)
                            #print ("retroceso en la entrada: ",['n',self.posicion+1,self.arbol,self.produccion])
                            self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion,"retroceso en la entrada"))
                            return False
                    else:
                        self.posicion -= 1
                        self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                        self.arbol.pop(len(self.arbol)-1)
                        #print ("no concordancia de simbolos: ",['n',self.posicion+1,self.arbol,self.produccion])
                        self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion,"no concordancia de simbolos"))
                        self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                        self.arbol.pop(len(self.arbol)-1)
                        #print ("retroceso en la entrada: ",['n',self.posicion+1,self.arbol,self.produccion])
                        self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion,"retroceso en la entrada"))
                        del self.produccion[0:2]
                        self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                        self.arbol.pop(len(self.arbol)-1)
                        #print ("retroceso en la entrada: ",['n',self.posicion+1,self.arbol,self.produccion])
                        self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion,"retroceso en la entrada"))
                        del self.produccion[0:3]
                        self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                        self.arbol.pop(len(self.arbol)-1)
                        #print ("retroceso en la entrada: ",['n',self.posicion+1,self.arbol,self.produccion])
                        self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion,"retroceso en la entrada"))
                        self.posicion -= 1
                        self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                        self.arbol.pop(len(self.arbol)-1)
                        #print ("retroceso en la entrada: ",['n',self.posicion+1,self.arbol,self.produccion])
                        self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion,"retroceso en la entrada"))
                        self.posicion -= 1
                        self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                        self.arbol.pop(len(self.arbol)-1)
                        #print ("retroceso en la entrada: ",['n',self.posicion+1,self.arbol,self.produccion])
                        self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion,"retroceso en la entrada"))
                        self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                        self.arbol.pop(len(self.arbol)-1)
                        #print ("retroceso en la entrada: ",['n',self.posicion+1,self.arbol,self.produccion])
                        self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion,"retroceso en la entrada"))
                        self.posicion -= 1
                        del self.produccion[0:6]
                        self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                        self.arbol.pop(len(self.arbol)-1)
                        #print ("retroceso en la entradas: ",['n',self.posicion+1,self.arbol,self.produccion])
                        self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion,"retroceso en la entrada"))
                        del self.produccion[0:1]
                        self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                        self.arbol.pop(len(self.arbol)-1)
                        #print ("retroceso en la entrada: ",['n',self.posicion+1,self.arbol,self.produccion])
                        self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion,"retroceso en la entrada"))
                        return False
                else:
                    self.posicion -= 1
                    del self.produccion[0:1]
                    self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                    self.arbol.pop(len(self.arbol)-1)
                    #print ("no concordancia de simbolos: ",['n',self.posicion+1,self.arbol,self.produccion])
                    self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion,"no concordancia de simbolos"))
                    del self.produccion[0:3]
                    self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                    self.arbol.pop(len(self.arbol)-1)
                    #print ("retroceso en la entrada: ",['n',self.posicion+1,self.arbol,self.produccion])
                    self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion,"retroceso en la entrada"))
                    self.posicion -= 1
                    self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                    self.arbol.pop(len(self.arbol)-1)
                    #print ("retroceso en la entradas: ",['n',self.posicion+1,self.arbol,self.produccion])
                    self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion,"retroceso en la entrada"))
                    self.posicion -= 1
                    self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                    self.arbol.pop(len(self.arbol)-1)
                    #print ("retroceso en la entrada: ",['n',self.posicion+1,self.arbol,self.produccion])
                    self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion,"retroceso en la entrada"))
                    self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                    self.arbol.pop(len(self.arbol)-1)
                    #print ("retroceso en la entrada: ",['n',self.posicion+1,self.arbol,self.produccion])
                    self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion,"retroceso en la entrada"))
                    del self.produccion[0:6]
                    self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                    self.arbol.pop(len(self.arbol)-1)
                    #print ("retroceso en la entrada: ",['n',self.posicion+1,self.arbol,self.produccion])
                    self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion,"retroceso en la entrada"))
                    del self.produccion[0:1]
                    self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                    self.arbol.pop(len(self.arbol)-1)
                    #print ("retroceso en la entrada: ",['n',self.posicion+1,self.arbol,self.produccion])
                    self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion,"retroceso en la entrada"))
                    return False
            else:
                self.posicion -= 1
                self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                self.arbol.pop(len(self.arbol)-1)
                #print ("no concordancia de simbolos: ",['n',self.posicion+1,self.arbol,self.produccion])
                self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion,"no concordancia de simbolos"))
                self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                self.arbol.pop(len(self.arbol)-1)
                #print ("retroceso en la entrada: ",['n',self.posicion+1,self.arbol,self.produccion])
                self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion,"retroceso en la entrada"))
                self.posicion -= 1
                del self.produccion[0:6]
                self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                self.arbol.pop(len(self.arbol)-1)
                #print ("retroceso en la entrada: ",['n',self.posicion+1,self.arbol,self.produccion])
                self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion,"retroceso en la entrada"))
                del self.produccion[0:1]
                self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                self.arbol.pop(len(self.arbol)-1)
                #print ("retroceso en la entrada: ",['n',self.posicion+1,self.arbol,self.produccion])
                self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion,"retroceso en la entrada"))
                return False
        else:
            self.posicion -= 1
            del self.produccion[0:5]
            self.produccion.insert(0,self.arbol[len(self.arbol)-1])
            self.arbol.pop(len(self.arbol)-1)
            #print ("retroceso en la entrada: ",['n',self.posicion+1,self.arbol,self.produccion])
            self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion,"retroceso en la entrada"))
            del self.produccion[0:1]
            self.produccion.insert(0,self.arbol[len(self.arbol)-1])
            self.arbol.pop(len(self.arbol)-1)
            #print ("retroceso en la entrada: ",['n',self.posicion+1,self.arbol,self.produccion])
            self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion,"retroceso en la entrada"))
            return False
    def valor(self,cadena):
        self.posicion += 1
        variable = cadena[self.posicion]
        partes = variable.split(".")
        self.arbol.append(self.produccion[0])
        self.produccion.pop(0)
        self.produccion[0:0] = ["nomvar"]
        #print ("ampliacion del arbol: ",['n',self.posicion+1,self.arbol,self.produccion])  
        self.tabla.insert(parent="", index="end", values=("n",self.posicion+1, self.arbol, self.produccion,"ampliacion del arbol"))
        if variable[0] == ":" and variable[1:].islower():
            self.arbol.append(self.produccion[0])
            self.produccion.pop(0)
            #print ("pasamos valor: ",['n',self.posicion+1,self.arbol,self.produccion])
            self.tabla.insert(parent="", index="end", values=("n",self.posicion+1, self.arbol, self.produccion,"pasamos valor"))
            
            self.arbol.append(cadena[self.posicion])
            #print ("coincidencia de simbolo: ",['n',self.posicion+1,self.arbol,self.produccion])
            self.tabla.insert(parent="", index="end", values=("n",self.posicion+1, self.arbol, self.produccion,"coincidencia de simbolo"))
            
            return True  
        elif variable.isdigit():
            del self.produccion[0:1]
            self.produccion.insert(0,self.arbol[len(self.arbol)-1])
            self.arbol.pop(len(self.arbol)-1)
            #print ("no concordancia de simbolos: ",['n',self.posicion+1,self.arbol,self.produccion])
            self.tabla.insert(parent="", index="end", values=("n",self.posicion+1, self.arbol, self.produccion,"no concordancia de simbolos"))
            self.arbol.append(self.produccion[0])
            self.produccion.pop(0)
            self.produccion[0:0] = ["numero"]
            #print ("ampliacion del arbol: ",['n',self.posicion+1,self.arbol,self.produccion])
            self.tabla.insert(parent="", index="end", values=("n",self.posicion+1, self.arbol, self.produccion,"ampliacion del arbol"))

            self.arbol.append(self.produccion[0])
            self.produccion.pop(0)
            #print ("pasamos produccion: ",['n',self.posicion+1,self.arbol,self.produccion])
            self.tabla.insert(parent="", index="end", values=("n",self.posicion+1, self.arbol, self.produccion,"pasamos produccion"))

            self.arbol.append(cadena[self.posicion])
            #print ("coincidencia de simbolo: ",['n',self.posicion+1,self.arbol,self.produccion])
            self.tabla.insert(parent="", index="end", values=("n",self.posicion+1, self.arbol, self.produccion,"coincidencia de simbolo"))
 
            return True
        elif partes[0].isdigit() and partes[1].isdigit():
            del self.produccion[0:1]
            self.produccion.insert(0,self.arbol[len(self.arbol)-1])
            self.arbol.pop(len(self.arbol)-1)
            #print ("no concordancia de simbolos: ",['n',self.posicion+1,self.arbol,self.produccion])
            self.tabla.insert(parent="", index="end", values=("n",self.posicion+1, self.arbol, self.produccion,"no concordancia de simbolos"))

            self.arbol.append(self.produccion[0])
            self.produccion.pop(0)
            self.produccion[0:0] = ["numero"]
            #print ("ampliacion del arbol: ",['n',self.posicion+1,self.arbol,self.produccion])
            self.tabla.insert(parent="", index="end", values=("n",self.posicion+1, self.arbol, self.produccion,"ampliacion del arbol"))

            self.arbol.append(self.produccion[0])
            self.produccion.pop(0)
            #print ("pasamos produccion: ",['n',self.posicion+1,self.arbol,self.produccion])
            self.tabla.insert(parent="", index="end", values=("n",self.posicion+1, self.arbol, self.produccion,"pasamos produccion"))

            self.arbol.append(cadena[self.posicion])
            #print ("coincidencia de simbolo: ",['n',self.posicion+1,self.arbol,self.produccion])
            self.tabla.insert(parent="", index="end", values=("n",self.posicion+1, self.arbol, self.produccion,"coincidencia de simbolo"))

            return True
        else:
            return False

    def operador(self,cadena):
        if cadena[self.posicion] == "+" or cadena[self.posicion] == "-" or cadena[self.posicion] == "*" or cadena[self.posicion] == "/":
            self.arbol.append(self.produccion[0])
            self.produccion.pop(0)
            #print ("pasamos produccion: ",['n',self.posicion+1,self.arbol,self.produccion])
            self.tabla.insert(parent="", index="end", values=("n",self.posicion+1, self.arbol, self.produccion,"pasamos produccion"))

            self.arbol.append(cadena[self.posicion])
            #print ("coincidencia de simbolo: ",['n',self.posicion+1,self.arbol,self.produccion])
            self.tabla.insert(parent="", index="end", values=("n",self.posicion+1, self.arbol, self.produccion, "coincidencia de simbolo"))

            return True
        else:
            return False
                

               
    def asignacion(self,cadena):
        self.arbol.append(self.produccion[0])
        self.produccion.pop(0)
        self.produccion.insert(0,"asignar") 
        #print ("ampliacion del arbol: ",['n',self.posicion+1,self.arbol,self.produccion])
        self.tabla.insert(parent="", index="end", values=("n",self.posicion+1, self.arbol, self.produccion,"ampliacion del arbol"))
        
        self.arbol.append(self.produccion[0])
        self.produccion.pop(0)
        self.produccion[0:0] = ["nomvar","=","asignado",";","sentencias"]
        #print ("ampliacion del arbol: ",['n',self.posicion+1,self.arbol,self.produccion])
        self.tabla.insert(parent="", index="end", values=("n",self.posicion+1, self.arbol, self.produccion,"ampliacion del arbol"))
        
        self.posicion += 1
        vari = self.variable(cadena)
        if vari:
            self.arbol.append(self.produccion[0])
            self.produccion.pop(0) 
            #print ("pasamos produccion: ",['n',self.posicion+1,self.arbol,self.produccion])
            self.tabla.insert(parent="", index="end", values=("n",self.posicion+1, self.arbol, self.produccion,"pasamos produccion"))
            
            self.arbol.append(cadena[self.posicion-1])
            #print ("coincidencia de simbolo: ",['n',self.posicion+1,self.arbol,self.produccion])
            self.tabla.insert(parent="", index="end", values=("n",self.posicion+1, self.arbol, self.produccion,"coincidencia de simbolo"))
            
            if cadena[self.posicion] == "=":
                self.arbol.append(self.produccion[0])
                self.produccion.pop(0)
                #print ("coincidencia de simbolo: ",['n',self.posicion+1,self.arbol,self.produccion])
                self.tabla.insert(parent="", index="end", values=("n",self.posicion+1, self.arbol, self.produccion,"coincidencia de simbolo"))
                
                self.posicion += 1
                asi = self.asigna(cadena)
                if asi:
                    self.posicion += 1
                    if cadena[self.posicion] == ";":
                        self.arbol.append(self.produccion[0])
                        self.produccion.pop(0)
                        #print ("coincidencia de simbolo: ",['n',self.posicion+1,self.arbol,self.produccion])
                        self.tabla.insert(parent="", index="end", values=("n",self.posicion+1, self.arbol, self.produccion,"coincidencia de simbolo"))
                        
                        if self.posicion+1 < len(cadena):
                            #print ("gh " , cadena[self.posicion])
                            if cadena[self.posicion+1] == "?" and cadena[self.posicion+2] == "&":
                                return True
                            else:  
                                self.sentencia(cadena)   
                        else:
                            return False
                    else :
                        self.posicion -= 1
                        self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                        self.arbol.pop(len(self.arbol)-1)
                        #print ("no concordancia de simbolos: ",['r',self.posicion+1,self.arbol,self.produccion])
                        self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion,"no concordancia de simbolos"))
                        
                        self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                        self.arbol.pop(len(self.arbol)-1)
                        #print ("retroceso a la entrada: ",['r',self.posicion+1,self.arbol,self.produccion])
                        self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion,"retroceso a la entrada"))
                        
                        del self.produccion[0:2]
                        self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                        self.arbol.pop(len(self.arbol)-1)
                        #print ("retroceso a la entrada: ",['r',self.posicion+1,self.arbol,self.produccion])
                        self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion,"retroceso a la entrada"))
                        
                        self.posicion -= 1
                        self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                        self.arbol.pop(len(self.arbol)-1)
                        #print ("retroceso a la entrada: ",['r',self.posicion+1,self.arbol,self.produccion])
                        self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion,"retroceso a la entrada"))
                        
                        self.posicion -= 1
                        self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                        self.arbol.pop(len(self.arbol)-1)
                        #print ("retroceso a la entrada: ",['r',self.posicion+1,self.arbol,self.produccion])
                        self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion,"retroceso a la entrada"))
                        
                        self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                        self.arbol.pop(len(self.arbol)-1)
                        #print ("retroceso a la entrada: ",['r',self.posicion+1,self.arbol,self.produccion])
                        self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion,"retroceso a la entrada"))
                        
                        self.posicion -= 1
                        del self.produccion[0:6]
                        self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                        self.arbol.pop(len(self.arbol)-1)
                        #print ("retroceso a la entrada: ",['r',self.posicion+1,self.arbol,self.produccion])
                        self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion,"retroceso a la entrada"))
                        
                        del self.produccion[0:1]
                        self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                        self.arbol.pop(len(self.arbol)-1)
                        #print ("retroceso a la entrada: ",['r',self.posicion+1,self.arbol,self.produccion])
                        self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion,"retroceso a la entrada"))
                        
                        return False
                else:
                    self.posicion -= 1
                    self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                    self.arbol.pop(len(self.arbol)-1)
                    #print ("no concordancia de simbolos: ",['r',self.posicion+1,self.arbol,self.produccion])
                    self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion,"no concordancia de simbolos"))
                    
                    del self.produccion[0:2]
                    self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                    self.arbol.pop(len(self.arbol)-1)
                    #print ("retroceso a la entrada: ",['r',self.posicion+1,self.arbol,self.produccion])
                    self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion,"retroceso a la entrada"))
                    
                    self.arbol.append(self.produccion[0])
                    self.produccion.pop(0)
                    self.produccion[0:0] = ["nomvar"]
                    #print ("ampliacion del arbol: ",['n',self.posicion+1,self.arbol,self.produccion])
                    self.tabla.insert(parent="", index="end", values=("n",self.posicion+1, self.arbol, self.produccion,"ampliacion del arbol"))
                    
                    self.arbol.append(self.produccion[0])
                    self.produccion.pop(0)
                    #print ("ampliacion del arbol: ",['n',self.posicion+1,self.arbol,self.produccion])
                    self.tabla.insert(parent="", index="end", values=("n",self.posicion+1, self.arbol, self.produccion,"ampliacion del arbol"))
                    
                
                    self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                    self.arbol.pop(len(self.arbol)-1)
                    #print ("retroceso a la entrada: ",['r',self.posicion+1,self.arbol,self.produccion])
                    self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion,"retroceso a la entrada"))
                    
                    self.produccion.pop(0)
                    self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                    self.arbol.pop(len(self.arbol)-1)
                   # print ("retroceso a la entrada: ",['r',self.posicion+1,self.arbol,self.produccion])
                    self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion,"retroceso a la entrada"))

                    self.arbol.append(self.produccion[0])
                    self.produccion.pop(0)
                    self.produccion[0:0] = ["numero"]
                    #print ("ampliacion del arbol: ",['n',self.posicion+1,self.arbol,self.produccion])
                    self.tabla.insert(parent="", index="end", values=("n",self.posicion+1, self.arbol, self.produccion, "ampliacion del arbol"))
                    
                    self.arbol.append(self.produccion[0])
                    self.produccion.pop(0)
                    #print ("ampliacion del arbol: ",['n',self.posicion+1,self.arbol,self.produccion])
                    self.tabla.insert(parent="", index="end", values=("n",self.posicion+1, self.arbol, self.produccion, "ampliacion del arbol"))
                    
                    self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                    self.arbol.pop(len(self.arbol)-1)
                    #print ("retroceso a la entrada: ",['r',self.posicion+1,self.arbol,self.produccion])
                    self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion, "retroceso a la entrada"))
                    
                    self.produccion.pop(0)
                    self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                    self.arbol.pop(len(self.arbol)-1)
                    #print ("retroceso a la entrada: ",['r',self.posicion+1,self.arbol,self.produccion])
                    self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion, "retroceso a la entrada"))
                    
                    self.posicion -= 1
                    self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                    self.arbol.pop(len(self.arbol)-1)
                    #print ("retroceso a la entrada: ",['r',self.posicion+1,self.arbol,self.produccion])
                    self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion, "retroceso a la entrada"))
                    
                    self.posicion -= 1
                    self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                    self.arbol.pop(len(self.arbol)-1)
                    #print ("retroceso a la entradas: ",['r',self.posicion+1,self.arbol,self.produccion])
                    self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion, "retroceso a la entrada"))
                    
                    self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                    self.arbol.pop(len(self.arbol)-1)
                    #print ("retroceso a la entrada: ",['r',self.posicion+1,self.arbol,self.produccion])
                    self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion, "retroceso a la entrada"))
                    
                    del self.produccion[0:6]
                    self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                    self.arbol.pop(len(self.arbol)-1)
                    #print ("retroceso a la entrada: ",['r',self.posicion+1,self.arbol,self.produccion])
                    self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion, "retroceso a la entrada"))
                    
                    del self.produccion[0:1]
                    self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                    self.arbol.pop(len(self.arbol)-1)
                    #print ("retroceso a la entrada: ",['r',self.posicion+1,self.arbol,self.produccion])
                    self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion, "retroceso a la entrada"))
                    
                    return False

            else:
                self.posicion -= 1
                self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                self.arbol.pop(len(self.arbol)-1)
                #print ("no concordancia de simbolos: ",['r',self.posicion+1,self.arbol,self.produccion])
                self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion, "no concordancia de simbolos"))
                
                self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                self.arbol.pop(len(self.arbol)-1)
                #print ("retroceso a la entrada: ",['r',self.posicion+1,self.arbol,self.produccion])
                self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion, "retroceso a la entrada"))
                
                del self.produccion[0:6]
                self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                self.arbol.pop(len(self.arbol)-1)
                self.posicion -= 1
                #print ("retroceso a la entrada: ",['r',self.posicion+1,self.arbol,self.produccion])
                self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion, "retroceso a la entrada"))
                
                del self.produccion[0:1]
                self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                self.arbol.pop(len(self.arbol)-1)
                #print ("retroceso a la entrada: ",['r',self.posicion+1,self.arbol,self.produccion])
                self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion, "retroceso a la entrada"))
                
                return False    
        else:
            self.posicion -= 1
            del self.produccion[0:5]
            self.produccion.insert(0,self.arbol[len(self.arbol)-1])
            self.arbol.pop(len(self.arbol)-1)
            #print ("retroceso a la entrada: ",['r',self.posicion+1,self.arbol,self.produccion])
            self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion, "retroceso a la entrada"))
            
            del self.produccion[0:1]
            self.produccion.insert(0,self.arbol[len(self.arbol)-1])
            self.arbol.pop(len(self.arbol)-1)
            #print ("retroceso a la entrada: ",['r',self.posicion+1,self.arbol,self.produccion])
            self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion, "retroceso a la entrada"))
            
            return False
    def asigna(self,cadena):
        variable = cadena[self.posicion]
        partes = variable.split(".")
        #print ("partes: ",partes)
        self.arbol.append(self.produccion[0])
        self.produccion.pop(0)
        self.produccion[0:0] = ["parentesis",'"']
        #print ("ampliacion del arbol: ",['n',self.posicion+1,self.arbol,self.produccion])
        self.tabla.insert(parent="", index="end", values=("n",self.posicion+1, self.arbol, self.produccion, "ampliacion del arbol"))

        self.arbol.append(self.produccion[0])
        self.produccion.pop(0)
        #print ("ampliacion del arbol: ",['n',self.posicion+1,self.arbol,self.produccion])
        self.tabla.insert(parent="", index="end", values=("n",self.posicion+1, self.arbol, self.produccion, "ampliacion del arbol"))

        if cadena[self.posicion] == '"':
            self.arbol.append(self.produccion[0])
            self.produccion.pop(0)
            #print ("coincidencia de simbolo: ",['n',self.posicion+1,self.arbol,self.produccion])
            self.tabla.insert(parent="", index="end", values=("n",self.posicion+1, self.arbol, self.produccion, "coincidencia de simbolo"))

            return True
        elif variable[0] == ":" and variable[1:].islower():
            self.produccion.insert(0,self.arbol[len(self.arbol)-1])
            self.arbol.pop(len(self.arbol)-1)
            #print ("no concordancia de simbolos: ",['r',self.posicion+1,self.arbol,self.produccion])
            self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion, "no concordancia de simbolos"))

            del self.produccion[0:2]
            self.produccion.insert(0,self.arbol[len(self.arbol)-1])
            self.arbol.pop(len(self.arbol)-1)
            #print ("retroceso a la entrada: ",['r',self.posicion+1,self.arbol,self.produccion])
            self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion, "retroceso a la entrada"))

            
            self.arbol.append(self.produccion[0])
            self.produccion.pop(0)
            self.produccion[0:0] = ["nomvar"]
            #print ("siguiente alternativa: ",['n',self.posicion+1,self.arbol,self.produccion])
            self.tabla.insert(parent="", index="end", values=("n",self.posicion+1, self.arbol, self.produccion, "siguiente alternativa"))

            self.arbol.append(self.produccion[0])
            self.produccion.pop(0)
            #print ("pasamos produccion: ",['n',self.posicion+1,self.arbol,self.produccion])
            self.tabla.insert(parent="", index="end", values=("n",self.posicion+1, self.arbol, self.produccion, "pasamos produccion"))

            self.arbol.append(cadena[self.posicion])
            #print ("coincidencia de simbolo: ",['n',self.posicion+1,self.arbol,self.produccion])
            self.tabla.insert(parent="", index="end", values=("n",self.posicion+1, self.arbol, self.produccion, "coincidencia de simbolo"))

            return True
        elif cadena [self.posicion].isdigit():
            self.produccion.insert(0,self.arbol[len(self.arbol)-1])
            self.arbol.pop(len(self.arbol)-1)
            #print ("retroceso a la entrada: ",['r',self.posicion+1,self.arbol,self.produccion])
            self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion, "retroceso a la entrada"))

            del self.produccion[0:2]
            self.produccion.insert(0,self.arbol[len(self.arbol)-1])
            self.arbol.pop(len(self.arbol)-1)
            #print ("retroceso a la entrada: ",['r',self.posicion+1,self.arbol,self.produccion])
            self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion, "retroceso a la entrada"))
            
            self.arbol.append(self.produccion[0])
            self.produccion.pop(0)
            self.produccion[0:0] = ["nomvar"]
            #print ("siguiente alternativa: ",['n',self.posicion+1,self.arbol,self.produccion])
            self.tabla.insert(parent="", index="end", values=("n",self.posicion+1, self.arbol, self.produccion, "siguiente alternativa"))

            self.arbol.append(self.produccion[0])
            self.produccion.pop(0)
            #print ("pasamos produccion: ",['n',self.posicion+1,self.arbol,self.produccion])
            self.tabla.insert(parent="", index="end", values=("n",self.posicion+1, self.arbol, self.produccion, "pasamos produccion"))
            
        
            self.produccion.insert(0,self.arbol[len(self.arbol)-1])
            self.arbol.pop(len(self.arbol)-1)
            #print ("no concordancia de simbolos: ",['r',self.posicion+1,self.arbol,self.produccion])
            self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion, "no concordancia de simbolos"))
            
            self.produccion.pop(0)
            self.produccion.insert(0,self.arbol[len(self.arbol)-1])
            self.arbol.pop(len(self.arbol)-1)
            #print ("retroceso a la entrada: ",['r',self.posicion+1,self.arbol,self.produccion])
            self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion, "retroceso a la entrada"))

            self.arbol.append(self.produccion[0])
            self.produccion.pop(0)
            self.produccion[0:0] = ["numero"]
            #print ("siguiente opcion: ",['n',self.posicion+1,self.arbol,self.produccion])
            self.tabla.insert(parent="", index="end", values=("n",self.posicion+1, self.arbol, self.produccion, "siguiente opcion"))

            self.arbol.append(self.produccion[0])
            self.produccion.pop(0)
            #print ("pasamos produccion: ",['n',self.posicion+1,self.arbol,self.produccion])
            self.tabla.insert(parent="", index="end", values=("n",self.posicion+1, self.arbol, self.produccion, "pasamos produccion"))

            self.arbol.append(cadena[self.posicion])
            #print ("coincidencia de simbolo: ",['n',self.posicion+1,self.arbol,self.produccion])
            self.tabla.insert(parent="", index="end", values=("n",self.posicion+1, self.arbol, self.produccion, "coincidencia de simbolo"))

            return True
        elif variable == "FALSE" or variable == "TRUE":
            self.arbol.append(self.produccion[0])
            self.produccion.pop(0)
            #print ("coincidencia de simbolo: ",['n',self.posicion+1,self.arbol,self.produccion])
            self.tabla.insert(parent="", index="end", values=("n",self.posicion+1, self.arbol, self.produccion, "coincidencia de simbolo"))

            return True
        elif len(partes) == 2 and partes[0].isdigit() and partes[1].isdigit():
            self.arbol.append(self.produccion[0])
            self.produccion.pop(0)
            #print ("coincidencia de simbolo: ",['n',self.posicion+1,self.arbol,self.produccion])
            self.tabla.insert(parent="", index="end", values=("n",self.posicion+1, self.arbol, self.produccion, "coincidencia de simbolo"))

            return True
        else:

            return False
    def concatena(self,cadena):
        self.arbol.append(self.produccion[0])
        self.produccion.pop(0)
        self.produccion.insert(0,"concatenar") 
        #print ("ampliacion del arbol: ",['n',self.posicion+1,self.arbol,self.produccion])
        self.tabla.insert(parent="", index="end", values=("n",self.posicion+1, self.arbol, self.produccion, "ampliacion del arbol"))

        self.arbol.append(self.produccion[0])
        self.produccion.pop(0)
        self.produccion[0:0] = ["nomvar","=","concatena",",","concatena",";","sentencias"]
        #print ("ampliacion del arbol: ",['n',self.posicion+1,self.arbol,self.produccion])
        self.tabla.insert(parent="", index="end", values=("n",self.posicion+1, self.arbol, self.produccion, "ampliacion del arbol"))

        self.posicion += 1
        vari = self.variable(cadena)
        if vari:
            self.arbol.append(self.produccion[0])
            self.produccion.pop(0) 
            #print ("pasamos produccion: ",['n',self.posicion+1,self.arbol,self.produccion])
            self.tabla.insert(parent="", index="end", values=("n",self.posicion+1, self.arbol, self.produccion, "pasamos produccion"))

            self.arbol.append(cadena[self.posicion-1])
            #print ("coincidencia de simbolo: ",['n',self.posicion+1,self.arbol,self.produccion])
            self.tabla.insert(parent="", index="end", values=("n",self.posicion+1, self.arbol, self.produccion, "coincidencia de simbolo"))

            if cadena[self.posicion] == "=":
                self.arbol.append(self.produccion[0])
                self.produccion.pop(0) 
                #print ("coincidencia de simbolo: ",['n',self.posicion+1,self.arbol,self.produccion])
                self.tabla.insert(parent="", index="end", values=("n",self.posicion+1, self.arbol, self.produccion, "coincidencia de simbolo"))

                self.posicion += 1
                conca = self.concatenar(cadena)
                if conca:
                    if cadena[self.posicion] == ",":
                        self.arbol.append(self.produccion[0])
                        self.produccion.pop(0)
                        #print ("coincidencia de simbolo: ",['n',self.posicion+1,self.arbol,self.produccion])
                        self.tabla.insert(parent="", index="end", values=("n",self.posicion+1, self.arbol, self.produccion, "coincidencia de simbolo"))

                        self.posicion += 1
                        conca = self.concatenar(cadena)
                        if conca:
                            if cadena[self.posicion] == ";":
                                self.arbol.append(self.produccion[0])
                                self.produccion.pop(0)
                                #print ("coincidencia de simbolo: ",['n',self.posicion+1,self.arbol,self.produccion])
                                self.tabla.insert(parent="", index="end", values=("n",self.posicion+1, self.arbol, self.produccion, "coincidencia de simbolo"))

                                if self.posicion+1 < len(cadena):
                                    if cadena[self.posicion+1] == "?" and cadena[self.posicion+2] == "&":
                                        return True
                                    else:  
                                        self.sentencia(cadena)   
                                else:
                                    return False
                            else:
                                self.posicion -= 1
                                self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                                self.arbol.pop(len(self.arbol)-1)
                                print ("no concordancia de simbolos: ",['r',self.posicion+1,self.arbol,self.produccion, "no concordancia de simbolos"])

                                self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                                self.arbol.pop(len(self.arbol)-1)
                                #print ("retroceso en la entrada: ",['r',self.posicion+1,self.arbol,self.produccion])
                                self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion, "retroceso en la entrada"))
                                
                                del self.produccion[0:2]
                                self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                                self.arbol.pop(len(self.arbol)-1)
                                #print ("retroceso en la entrada: ",['r',self.posicion+1,self.arbol,self.produccion])
                                self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion, "retroceso en la entrada"))
                                
                                self.posicion -= 1
                                self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                                self.arbol.pop(len(self.arbol)-1)
                                #print ("retroceso en la entrada: ",['r',self.posicion+1,self.arbol,self.produccion])
                                self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion, "retroceso en la entrada"))
                                
                                self.posicion -= 1
                                self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                                self.arbol.pop(len(self.arbol)-1)
                                #print ("retroceso en la entrada: ",['r',self.posicion+1,self.arbol,self.produccion])
                                self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion, "retroceso en la entrada"))
                                
                                self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                                self.arbol.pop(len(self.arbol)-1)
                                #print ("retroceso en la entrada: ",['r',self.posicion+1,self.arbol,self.produccion])
                                self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion, "retroceso en la entrada"))
                                
                                del self.produccion[0:2]
                                self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                                self.arbol.pop(len(self.arbol)-1)
                                #print ("retroceso en la entrada: ",['r',self.posicion+1,self.arbol,self.produccion])
                                self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion, "retroceso en la entrada"))
                                
                                self.posicion -= 1
                                self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                                self.arbol.pop(len(self.arbol)-1)
                                #print ("retroceso en la entrada: ",['r',self.posicion+1,self.arbol,self.produccion])
                                self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion, "retroceso en la entrada"))
                                
                                self.posicion -= 1
                                self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                                self.arbol.pop(len(self.arbol)-1)
                                #print ("retroceso en la entrada: ",['r',self.posicion+1,self.arbol,self.produccion])
                                self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion, "retroceso en la entrada"))
                                
                                self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                                self.arbol.pop(len(self.arbol)-1)
                                #print ("retroceso en la entrada: ",['r',self.posicion+1,self.arbol,self.produccion])
                                self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion, "retroceso en la entrada"))
                                
                                self.posicion -= 1
                                del self.produccion[0:8]
                                self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                                self.arbol.pop(len(self.arbol)-1)
                                #print ("retroceso en la entrada: ",['r',self.posicion+1,self.arbol,self.produccion])
                                self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion, "retroceso en la entrada"))
                                
                                self.produccion.pop(0)
                                self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                                self.arbol.pop(len(self.arbol)-1)
                                #print ("retroceso en la entrada: ",['r',self.posicion+1,self.arbol,self.produccion])
                                self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion, "retroceso en la entrada"))
                                
                                return False
                        else:
                            self.posicion -= 1
                            del self.produccion[0:2]
                            self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                            self.arbol.pop(len(self.arbol)-1)
                            #print ("no concordancia de simbolos: ",['r',self.posicion+1,self.arbol,self.produccion])
                            self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion, "no concordancia de simbolos"))
                            
                            self.posicion -= 1
                            self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                            self.arbol.pop(len(self.arbol)-1)
                            #print ("retroceso en la entrada: ",['r',self.posicion+1,self.arbol,self.produccion])
                            self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion, "retroceso en la entrada"))
                            
                            self.posicion -= 1
                            self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                            self.arbol.pop(len(self.arbol)-1)
                            #print ("retroceso en la entrada: ",['r',self.posicion+1,self.arbol,self.produccion])
                            self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion, "retroceso en la entrada"))
                            
                            self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                            self.arbol.pop(len(self.arbol)-1)
                            #print ("no concordancia de simbolos: ",['r',self.posicion+1,self.arbol,self.produccion])
                            self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion, "no concordancia de simbolos"))
                            
                            del self.produccion[0:2]
                            self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                            self.arbol.pop(len(self.arbol)-1)
                            #print ("retroceso en la entrada: ",['r',self.posicion+1,self.arbol,self.produccion])
                            self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion, "retroceso en la entrada"))
                            
                            self.posicion -= 1
                            self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                            self.arbol.pop(len(self.arbol)-1)
                            #print ("retroceso en la entrada: ",['r',self.posicion+1,self.arbol,self.produccion])
                            self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion, "retroceso en la entrada"))
                            
                            self.posicion -= 1
                            self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                            self.arbol.pop(len(self.arbol)-1)
                            #print ("retroceso en la entrada: ",['r',self.posicion+1,self.arbol,self.produccion])
                            self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion, "retroceso en la entrada"))
                            
                            self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                            self.arbol.pop(len(self.arbol)-1)
                            #print ("retroceso en la entrada: ",['r',self.posicion+1,self.arbol,self.produccion])
                            self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion, "retroceso en la entrada"))
                            
                            del self.produccion[0:8]
                            self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                            self.arbol.pop(len(self.arbol)-1)
                            #print ("retroceso en la entrada: ",['r',self.posicion+1,self.arbol,self.produccion])
                            self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion, "retroceso en la entrada"))
                            
                            self.produccion.pop(0)
                            self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                            self.arbol.pop(len(self.arbol)-1)
                            #print ("retroceso en la entrada: ",['r',self.posicion+1,self.arbol,self.produccion])
                            self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion, "retroceso en la entrada"))
                            
                            return False
                        
                    else:
                        self.posicion -= 1
                        self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                        self.arbol.pop(len(self.arbol)-1)
                        #print ("no concordancia de simbolo: ",['r',self.posicion+1,self.arbol,self.produccion])
                        self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion, "no concordancia de simbolo"))
                        
                        self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                        self.arbol.pop(len(self.arbol)-1)
                        #print ("retroceso en la entrada: ",['r',self.posicion+1,self.arbol,self.produccion])
                        self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion, "retroceso en la entrada"))
                        
                        del self.produccion[0:2]
                        self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                        self.arbol.pop(len(self.arbol)-1)
                        #print ("retroceso en la entrada: ",['r',self.posicion+1,self.arbol,self.produccion])
                        self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion, "retroceso en la entrada"))
                        
                        self.posicion -= 1
                        self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                        self.arbol.pop(len(self.arbol)-1)
                        #print ("retroceso en la entrada: ",['r',self.posicion+1,self.arbol,self.produccion])
                        self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion, "retroceso en la entrada"))
                        
                        self.posicion -= 1
                        self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                        self.arbol.pop(len(self.arbol)-1)
                        #print ("retroceso en la entrada: ",['r',self.posicion+1,self.arbol,self.produccion])
                        self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion, "retroceso en la entrada"))
                        
                        self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                        self.arbol.pop(len(self.arbol)-1)
                        #print ("retroceso en la entrada: ",['r',self.posicion+1,self.arbol,self.produccion])
                        self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion, "retroceso en la entrada"))
                        
                        self.posicion -= 1
                        del self.produccion[0:8]
                        self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                        self.arbol.pop(len(self.arbol)-1)
                        #print ("retroceso en la entradas: ",['r',self.posicion+1,self.arbol,self.produccion])
                        self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion, "retroceso en la entrada"))
                        
                        self.produccion.pop(0)
                        self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                        self.arbol.pop(len(self.arbol)-1)
                        #print ("retroceso en la entrada: ",['r',self.posicion+1,self.arbol,self.produccion])
                        self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion, "retroceso en la entrada"))
                        
                        return False
                else:
                    self.posicion -= 1
                    del self.produccion[0:2]
                    self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                    self.arbol.pop(len(self.arbol)-1)
                    #print ("no concordancia de simbolos: ",['r',self.posicion+1,self.arbol,self.produccion])
                    self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion, "no concordancia de simbolos"))
                    
                    self.posicion -= 1
                    self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                    self.arbol.pop(len(self.arbol)-1)
                    #print ("retroceso en la entrada: ",['r',self.posicion+1,self.arbol,self.produccion])
                    self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion, "retroceso en la entrada"))
                    
                    self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                    self.arbol.pop(len(self.arbol)-1)
                    #print ("retroceso en la entrada: ",['r',self.posicion+1,self.arbol,self.produccion])
                    self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion, "retroceso en la entrada"))
                    
                    self.posicion -= 1
                    self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                    self.arbol.pop(len(self.arbol)-1)
                    #print ("retroceso en la entrada: ",['r',self.posicion+1,self.arbol,self.produccion])
                    self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion, "retroceso en la entrada"))
                    
                    del self.produccion[0:8]
                    self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                    self.arbol.pop(len(self.arbol)-1)
                    #print ("retroceso en la entrada: ",['r',self.posicion+1,self.arbol,self.produccion])
                    self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion, "retroceso en la entrada"))
                    
                    self.produccion.pop(0)
                    self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                    self.arbol.pop(len(self.arbol)-1)
                    #print ("retroceso en la entrada: ",['r',self.posicion+1,self.arbol,self.produccion])
                    self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion, "retroceso en la entrada"))
                    
                    return False
                    
            else:
                self.posicion -= 1
                self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                self.arbol.pop(len(self.arbol)-1)
                #print ("no concordancia de simbolos: ",['r',self.posicion+1,self.arbol,self.produccion])
                self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion, "no concordancia de simbolos"))
                
                self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                self.arbol.pop(len(self.arbol)-1)
                #print ("retroceso en la entrada: ",['r',self.posicion+1,self.arbol,self.produccion])
                self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion, "retroceso en la entrada"))
                
                self.posicion -= 1
                del self.produccion[0:8]
                self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                self.arbol.pop(len(self.arbol)-1)
                #print ("retroceso en la entrada: ",['r',self.posicion+1,self.arbol,self.produccion])
                self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion, "retroceso en la entrada"))
                
                self.produccion.pop(0)
                self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                self.arbol.pop(len(self.arbol)-1)
                #print ("retroceso en la entrada: ",['r',self.posicion+1,self.arbol,self.produccion])
                self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion, "retroceso en la entrada"))
                
                return False
        else: 
            self.posicion -= 1
            del self.produccion[0:7]
            self.produccion.insert(0,self.arbol[len(self.arbol)-1])
            self.arbol.pop(len(self.arbol)-1)
            #print ("retroceso en la entrada: ",['r',self.posicion+1,self.arbol,self.produccion])
            self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion, "retroceso en la entrada"))
            
            self.produccion.pop(0)
            self.produccion.insert(0,self.arbol[len(self.arbol)-1])
            self.arbol.pop(len(self.arbol)-1)
            #print ("retroceso en la entrada: ",['r',self.posicion+1,self.arbol,self.produccion])
            self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion, "retroceso en la entrada"))
            
            return False
    def concatenar(self,cadena):
        variable = cadena [self.posicion]
        self.arbol.append(self.produccion[0])
        self.produccion.pop(0)
        self.produccion[0:0] = ["parentesis",'"']
        #print ("ampliacion del arbol: ",['n',self.posicion+1,self.arbol,self.produccion])
        self.tabla.insert(parent="", index="end", values=("n",self.posicion+1, self.arbol, self.produccion, "ampliacion del arbol"))

        if variable == '"':
            self.arbol.append(self.produccion[0])
            self.produccion.pop(0)
            #print ("ampliacion del arbol: ",['n',self.posicion+1,self.arbol,self.produccion])
            self.tabla.insert(parent="", index="end", values=("n",self.posicion+1, self.arbol, self.produccion, "ampliacion del arbol"))

            self.arbol.append(self.produccion[0])
            self.produccion.pop(0)
            #print ("ampliacion del arbol: ",['n',self.posicion+1,self.arbol,self.produccion])
            self.tabla.insert(parent="", index="end", values=("n",self.posicion+1, self.arbol, self.produccion, "ampliacion del arbol"))

            self.posicion += 1
            return True
        elif variable[0] == ":" and variable[1:].islower():
            self.posicion -= 1
            del self.produccion[0:2]
            self.produccion.insert(0,self.arbol[len(self.arbol)-1])
            self.arbol.pop(len(self.arbol)-1)
            #print ("retorceso en la entrada: ",['n',self.posicion+1,self.arbol,self.produccion])
            self.tabla.insert(parent="", index="end", values=("n",self.posicion+1, self.arbol, self.produccion,  "retroceso en la entrada"))
            
            self.arbol.append(self.produccion[0])
            self.produccion.pop(0)
            self.produccion[0:0] = ['nomvar']
            #print ("siguiente alternativa: ",['n',self.posicion+1,self.arbol,self.produccion])
            self.tabla.insert(parent="", index="end", values=("n",self.posicion+1, self.arbol, self.produccion, "siguiente alternativa"))
            
            self.arbol.append(self.produccion[0])
            self.produccion.pop(0)
            #print ("pasamos produccion: ",['n',self.posicion+1,self.arbol,self.produccion])
            self.tabla.insert(parent="", index="end", values=("n",self.posicion+1, self.arbol, self.produccion, "pasamos produccion"))
            
            self.posicion +=1
            self.arbol.append(cadena[self.posicion])
            #print ("concordancia del simbolo: ",['n',self.posicion+1,self.arbol,self.produccion])
            self.tabla.insert(parent="", index="end", values=("n",self.posicion+1, self.arbol, self.produccion, "concordancia del simbolo"))
            
            self.posicion +=1
            return True
        else:
            return False       
    def insertar (self, cadena):
        self.arbol.append(self.produccion[0])
        self.produccion.pop(0)
        self.produccion.insert(0,"mandar") 
        #print ("ampliacion del arbol: ",['n',self.posicion+1,self.arbol,self.produccion])
        self.tabla.insert(parent="", index="end", values=("n",self.posicion+1, self.arbol, self.produccion, "ampliacion del arbol"))

        self.arbol.append(self.produccion[0])
        self.produccion.pop(0)
        self.produccion[0:0] = ["SND","nomvar",";","sentencias"]
        #print ("ampliacion del arbol: ",['n',self.posicion+1,self.arbol,self.produccion])
        self.tabla.insert(parent="", index="end", values=("n",self.posicion+1, self.arbol, self.produccion, "ampliacion del arbol"))

        self.posicion += 1
        if cadena[self.posicion] == "SND":
            self.arbol.append(self.produccion[0])
            self.produccion.pop(0) 
            #print ("coincidencia de simbolo: ",['n',self.posicion+1,self.arbol,self.produccion])
            self.tabla.insert(parent="", index="end", values=("n",self.posicion+1, self.arbol, self.produccion, "coincidencia de simbolo"))

            self.arbol.append(self.produccion[0])
            self.produccion.pop(0) 
            #print ("pasamos produccion: ",['n',self.posicion+1,self.arbol,self.produccion])
            self.tabla.insert(parent="", index="end", values=("n",self.posicion+1, self.arbol, self.produccion, "pasamos produccion"))

            self.posicion += 1
            var = self.variable(cadena)
            if var:
                self.arbol.append(cadena[self.posicion-1])
                #print ("coincidencia de simbolo: ",['n',self.posicion,self.arbol,self.produccion])
                self.tabla.insert(parent="", index="end", values=("n",self.posicion+1, self.arbol, self.produccion, "coincidencia de simbolo"))

                if cadena[self.posicion] == ";":
                    self.arbol.append(self.produccion[0])
                    self.produccion.pop(0) 
                    #print ("coincidencia de simbolo: ",['n',self.posicion+1,self.arbol,self.produccion])
                    self.tabla.insert(parent="", index="end", values=("n",self.posicion+1, self.arbol, self.produccion, "coincidencia de simbolo"))

                    if self.posicion+1 < len(cadena):
                        if cadena[self.posicion+1] == "?" and cadena[self.posicion+2] == "&":
                            return True
                        else:  
                            self.sentencia(cadena)   
                    else:
                        return False
                else:
                    self.posicion -= 1
                    self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                    self.arbol.pop(len(self.arbol)-1)
                    #print ("no concordancia de simbolos: ",['r',self.posicion+1,self.arbol,self.produccion])
                    self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion, "no concordancia de simbolos"))
                    
                    self.posicion -= 1
                    self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                    self.arbol.pop(len(self.arbol)-1)
                    #print ("retroceso en la entrada: ",['r',self.posicion+1,self.arbol,self.produccion])
                    self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion, "retroceso en la entrada"))
                    
                    self.posicion -= 1
                    self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                    self.arbol.pop(len(self.arbol)-1)
                    #print ("retroceso en la entrada: ",['r',self.posicion+1,self.arbol,self.produccion])
                    self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion, "retroceso en la entrada"))
                    
                    del self.produccion[0:5]
                    self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                    self.arbol.pop(len(self.arbol)-1)
                    #print ("retroceso en la entrada: ",['r',self.posicion+1,self.arbol,self.produccion])
                    self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion, "retroceso en la entrada"))
                    
                    self.produccion.pop(0)
                    self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                    self.arbol.pop(len(self.arbol)-1)
                    #print ("retroceso en la entrada: ",['r',self.posicion+1,self.arbol,self.produccion])
                    self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion, "retroceso en la entrada"))
                    
                    return False
            else:
                self.posicion -= 1
                self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                self.arbol.pop(len(self.arbol)-1)
                #print ("no concordancia de simbolos: ",['r',self.posicion+1,self.arbol,self.produccion])
                self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion, "no concordancia de simbolos"))
                
                self.posicion -= 1
                self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                self.arbol.pop(len(self.arbol)-1)
                #print ("retroceso en la entrada: ",['r',self.posicion+1,self.arbol,self.produccion]) 
                self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion, "retroceso en la entrada"))
                
                del self.produccion[0:4]
                self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                self.arbol.pop(len(self.arbol)-1)
                #print ("retroceso en la entrada: ",['r',self.posicion+1,self.arbol,self.produccion])
                self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion, "retroceso en la entrada"))
                
                self.produccion.pop(0)
                self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                self.arbol.pop(len(self.arbol)-1)
                #print ("retroceso en la entrada: ",['r',self.posicion+1,self.arbol,self.produccion])
                self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion, "retroceso en la entrada"))
                
                return False
        else:
            del self.produccion[0:4]
            self.produccion.insert(0,self.arbol[len(self.arbol)-1])
            self.arbol.pop(len(self.arbol)-1)
            self.posicion -= 1
            #print ("retroceso en la entrada: ",['r',self.posicion+1,self.arbol,self.produccion])
            self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion, "retroceso en la entrada"))
            
            self.produccion.pop(0)
            self.produccion.insert(0,self.arbol[len(self.arbol)-1])
            self.arbol.pop(len(self.arbol)-1)
            #print ("retroceso en la entrada: ",['r',self.posicion+1,self.arbol,self.produccion])
            self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion, "retroceso en la entrada"))
            
            return False
    def variable (self, cadena):
        variable = cadena[self.posicion]
        if variable[0] == ":" and variable[1:].islower():
            self.posicion +=1
            return True
        else:
            return False 
    
    def mensaje(self, cadena):
        self.arbol.append(self.produccion[0])
        self.produccion.pop(0)
        self.produccion.insert(0,"mensaje") 
        #rint ("ampliacion del arbol: ",['n',self.posicion+1,self.arbol,self.produccion])
        self.tabla.insert(parent="", index="end", values=("n",self.posicion+1, self.arbol, self.produccion, "ampliacion del arbol"))

        self.arbol.append(self.produccion[0])
        self.produccion.pop(0)
        self.produccion[0:0] = ["SND",'"',";","sentencias"]
        #print ("pasamos produccion: ",['n',self.posicion+1,self.arbol,self.produccion])
        self.tabla.insert(parent="", index="end", values=("n",self.posicion+1, self.arbol, self.produccion, "pasamos produccion"))
        

        self.posicion += 1
        if cadena[self.posicion] == "SND":
            self.arbol.append(self.produccion[0])
            self.produccion.pop(0) 
            #print ("coincidencia de simbolo: ",['n',self.posicion+1,self.arbol,self.produccion])
            self.tabla.insert(parent="", index="end", values=("n",self.posicion+1, self.arbol, self.produccion, "coincidencia de simbolo"))

            self.posicion += 1
            if cadena[self.posicion] == '"':
                self.arbol.append(self.produccion[0])
                self.produccion.pop(0) 
                #print ("coincidencia de simbolo: ",['n',self.posicion+1,self.arbol,self.produccion])
                self.tabla.insert(parent="", index="end", values=("n",self.posicion+1, self.arbol, self.produccion, "coincidencia de simbolo"))

                self.posicion += 1
                #print ("llego")
                if cadena[self.posicion] == ";":
                    self.arbol.append(self.produccion[0])
                    self.produccion.pop(0) 
                    #print ("coincidencia de simbolo: ",['n',self.posicion+1,self.arbol,self.produccion])
                    self.tabla.insert(parent="", index="end", values=("n",self.posicion+1, self.arbol, self.produccion, "coincidencia de simbolo"))

                    if self.posicion+1 < len(cadena):
                        if cadena[self.posicion+1] == "?" and cadena[self.posicion+2] == "&":
                            return True
                        else:  
                            self.sentencia(cadena)   
                    else:
                        return False
                else:
                    self.posicion -= 1
                    self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                    self.arbol.pop(len(self.arbol)-1)
                    #print ("no concordancia de simbolos: ",['r',self.posicion+1,self.arbol,self.produccion])
                    self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion, "no concordancia de simbolos"))
                    
                    self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                    self.arbol.pop(len(self.arbol)-1)
                    self.posicion -= 1
                    #print ("no concordancia de simbolos: ",['r',self.posicion+1,self.arbol,self.produccion])
                    self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion, "no concordancia de simbolos"))
                    
                    self.posicion -= 1
                    del self.produccion[0:4]
                    self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                    self.arbol.pop(len(self.arbol)-1)
                    #print ("retroceso en la entrada: ",['r',self.posicion+1,self.arbol,self.produccion])
                    self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion, "retroceso en la entrada"))
                    
                    self.produccion.pop(0)
                    self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                    self.arbol.pop(len(self.arbol)-1)
                    #print ("retroceso en la entrada: ",['r',self.posicion+1,self.arbol,self.produccion])
                    self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion, "retroceso en la entrada"))
                    
                    return False
            else:
                self.posicion -= 1
                self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                self.arbol.pop(len(self.arbol)-1)
                #print ("retroceso en la entrada: ",['r',self.posicion+1,self.arbol,self.produccion])
                self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion, "retroceso en la entrada"))
                
                del self.produccion[0:4]
                self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                self.arbol.pop(len(self.arbol)-1)
                self.posicion -= 1
                #print ("retroceso en la entrada: ",['r',self.posicion+1,self.arbol,self.produccion])
                self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion, "retroceso en la entrada"))
                
                self.produccion.pop(0)
                self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                self.arbol.pop(len(self.arbol)-1)
                #print ("retroceso en la entrada: ",['r',self.posicion+1,self.arbol,self.produccion])
                self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion, "retroceso en la entrada"))
                
                return False
        else:
            del self.produccion[0:4]
            self.produccion.insert(0,self.arbol[len(self.arbol)-1])
            self.arbol.pop(len(self.arbol)-1)
            self.posicion -= 1
            #print ("retroceso en la entrada: ",['r',self.posicion+1,self.arbol,self.produccion])
            self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion, "retroceso en la entrada"))
            
            self.produccion.pop(0)
            self.produccion.insert(0,self.arbol[len(self.arbol)-1])
            self.arbol.pop(len(self.arbol)-1)
            #print ("retroceso en la entrada: ",['r',self.posicion+1,self.arbol,self.produccion])
            self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion, "retroceso en la entrada"))
            
            return False

    def comentario(self,cadena):
        self.posicion += 1
        #print (cadena[self.posicion])
        self.arbol.append(self.produccion[0])
        self.produccion.pop(0)
        self.produccion.insert(0,"comentario") 
        #print ("ampliacion del arbol: ",['n',self.posicion+1,self.arbol,self.produccion])
        self.tabla.insert(parent="", index="end", values=("n",self.posicion+1, self.arbol, self.produccion, "ampliacion del arbol"))

        self.arbol.append(self.produccion[0])
        self.produccion.pop(0)
        self.produccion[0:0] = ["#","sentencias"]
        #print ("pasamos produccion: ",['n',self.posicion+1,self.arbol,self.produccion])
        self.tabla.insert(parent="", index="end", values=("n",self.posicion+1, self.arbol, self.produccion, "pasamos produccion"))
        
        if cadena[self.posicion] == "#":
            self.arbol.append(self.produccion[0])
            self.produccion.pop(0)
            #print ("concordancia de simbolo: ",['n',self.posicion+1,self.arbol,self.produccion])
            self.tabla.insert(parent="", index="end", values=("n",self.posicion+1, self.arbol, self.produccion, "concordancia de simbolo"))

            if self.posicion+2 < len(cadena):
                if cadena[self.posicion+1] == "?" and cadena[self.posicion+2] == "&":
                    return True 
                else: 
                    self.sentencia(cadena)
        else:
            self.posicion -= 1
            del self.produccion[0:2]
            self.produccion.insert(0,self.arbol[len(self.arbol)-1])
            self.arbol.pop(len(self.arbol)-1)
            #print ("retroceso en la entrada: ",['r',self.posicion+1,self.arbol,self.produccion])
            self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion, "retroceso en la entrada"))
            
            self.produccion.pop(0)
            self.produccion.insert(0,self.arbol[len(self.arbol)-1])
            self.arbol.pop(len(self.arbol)-1)
            #print ("retroceso en la entrada: ",['r',self.posicion+1,self.arbol,self.produccion])
            self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion, "retroceso en la entrada"))
            
            return False



    def declaravar(self, cadena):
        self.posicion += 1
        valor = cadena[self.posicion]
        self.arbol.append(self.produccion[0])
        self.produccion.pop(0)
        self.produccion.insert(0,"declaravar") 
        #print ("ampliacion del arbol: ",['n',self.posicion+1,self.arbol,self.produccion])
        self.tabla.insert(parent="", index="end", values=("n",self.posicion+1, self.arbol, self.produccion, "ampliacion del arbol"))

        self.arbol.append(self.produccion[0])
        self.produccion.pop(0)
        self.produccion[0:0] = ["tipodata","complemento",";","sentencias"]
        #print ("ampliacion del arbol: ",['n',self.posicion+1,self.arbol,self.produccion])
        self.tabla.insert(parent="", index="end", values=("n",self.posicion+1, self.arbol, self.produccion, "ampliacion del arbol"))

        self.arbol.append(self.produccion[0])
        self.produccion.pop(0)
        #print ("pasamos produccion: ",['n',self.posicion+1,self.arbol,self.produccion])
        self.tabla.insert(parent="", index="end", values=("n",self.posicion+1, self.arbol, self.produccion, "pasamos produccion"))

        tipodato = self.tipodato(cadena)
        if tipodato:
            self.arbol.append(cadena[self.posicion])
            #print ("coincidencia de simbolo: ",['n',self.posicion+1,self.arbol,self.produccion])
            self.tabla.insert(parent="", index="end", values=("n",self.posicion+1, self.arbol, self.produccion, "coincidencia de simbolo"))

            self.posicion += 1
            self.arbol.append(self.produccion[0])
            self.produccion.pop(0)
            self.produccion[0:0] = ["nomvar"]
            #print ("ampliacion del arbol: ",['n',self.posicion+1,self.arbol,self.produccion])
            self.tabla.insert(parent="", index="end", values=("n",self.posicion+1, self.arbol, self.produccion, "ampliacion del arbol"))

            complement = self.complemento(cadena)
            self.arbol.append(self.produccion[0])
            self.produccion.pop(0)
            #print ("pasamos produccion: ",['n',self.posicion+1,self.arbol,self.produccion])
            self.tabla.insert(parent="", index="end", values=("n",self.posicion+1, self.arbol, self.produccion, "pasamos produccion"))

            if complement:
                self.arbol.append(cadena[self.posicion-1])

                #print ("coincidencia de simbolo: ",['n',self.posicion+1,self.arbol,self.produccion])
                self.tabla.insert(parent="", index="end", values=("n",self.posicion+1, self.arbol, self.produccion, "coincidencia de simbolo"))
                
                
                b= True
                conta = 0
                while b:
                    print (cadena[self.posicion])
                    if cadena[self.posicion] == ",":
                        self.posicion += 1
                        conta += 1
                        v = self.variable(cadena)
                        if v :
                            conta += 1
                        else:
                            self.posicion = self.posicion - conta
                            b = False
                    elif cadena[self.posicion] == ";":
                        b = False
                    else:
                        self.posicion = self.posicion - conta
                        b= False 
                
                #self.posicion += 1
                #print ("divicion")
                if cadena[self.posicion]== ";":
                    self.arbol.append(self.produccion[0])
                    self.produccion.pop(0) 
                    #print ("coincidencia de simbolo: ",['n',self.posicion+1,self.arbol,self.produccion])
                    self.tabla.insert(parent="", index="end", values=("n",self.posicion+1, self.arbol, self.produccion, "coincidencia de simbolo"))

                    #return True
                    #print("concordancia de simbolo: ", ['n',self.posicion+1,cadena[:self.posicion+1]])
                    if self.posicion+1 < len(cadena):
                        if cadena[self.posicion+1] == "?" and cadena[self.posicion+2] == "&":
                            return True
                        else:  
                            self.sentencia(cadena)
                            
                    else:
                        
                        return False
                else: 
                    self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                    self.arbol.pop(len(self.arbol)-1)
                    #print ("no concordancia de simbolos: ",['r',self.posicion+1,self.arbol,self.produccion])
                    self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion, "no concordancia de simbolos"))
                    
                    self.posicion -= 1
                    self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                    self.arbol.pop(len(self.arbol)-1)
                    #print ("retroceso a la entrada: ",['r',self.posicion+1,self.arbol,self.produccion])
                    self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion, "retroceso a la entrada"))
                    
                    del self.produccion[0:2]
                    self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                    self.arbol.pop(len(self.arbol)-1)
                    #print ("retroceso a la entrada: ",['n',self.posicion+1,self.arbol,self.produccion])
                    self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion, "retroceso a la entrada"))
                    
                    dos = self.complemento2(cadena)
                    if dos:
                        if cadena[self.posicion] == "=":
                            self.arbol.append(self.produccion[0])
                            self.produccion.pop(0)
                            #print ("siguiente alternativa (a): ",['n',self.posicion+1,self.arbol,self.produccion])
                            self.tabla.insert(parent="", index="end", values=("n",self.posicion+1, self.arbol, self.produccion, "siguiente alternativa (a)"))

                            self.posicion +=1
                            asig = self.asignado(cadena)
                            if asig:
                                self.posicion += 1
                                if cadena[self.posicion] == ";":
                                    self.arbol.append(self.produccion[0])
                                    self.produccion.pop(0)
                                    #print ("coincidencia de simbolo: ",['n',self.posicion+1,self.arbol,self.produccion])
                                    self.tabla.insert(parent="", index="end", values=("n",self.posicion+1, self.arbol, self.produccion, "coincidencia de simbolo"))

                                    #print (cadena[self.posicion+1])
                                    #print (cadena[self.posicion+2])
                                    if self.posicion+1 < len(cadena):
                                        #print ("primero")
                                        if cadena[self.posicion+1] == "?" and cadena[self.posicion+2] == "&":
                                            #print ("true")
                                            return True
                                        else:  
                                            self.sentencia(cadena)
                                            
                                    else:
                                        #print ("tercero")
                                        return False
                                else:
                                    self.posicion -= 1
                                    self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                                    self.arbol.pop(len(self.arbol)-1)
                                    #print ("no concordancia de simbolos: ",['n',self.posicion+1,self.arbol,self.produccion])
                                    self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion, "no concordancia de simbolos"))

                                    self.posicion -= 1
                                    self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                                    self.arbol.pop(len(self.arbol)-1)
                                    #print ("no concordancia de simbolos: ",['n',self.posicion+1,self.arbol,self.produccion])
                                    self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion, "no concordancia de simbolos"))
                                    
                                    self.posicion -= 1
                                    self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                                    self.arbol.pop(len(self.arbol)-1)
                                    #print ("retroceso en la entrada: ",['n',self.posicion+1,self.arbol,self.produccion])
                                    self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion, "retroceso en la entrada"))
                                    
                                    self.posicion -= 1
                                    self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                                    self.arbol.pop(len(self.arbol)-1)
                                    #print ("retroceso en la entrada: ",['n',self.posicion+1,self.arbol,self.produccion])
                                    self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion, "retroceso en la entrada"))
                                    
                                    del self.produccion[0:4]
                                    self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                                    self.arbol.pop(len(self.arbol)-1)
                                    #print ("no concordancia de simbolos: ",['n',self.posicion+1,self.arbol,self.produccion])
                                    self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion, "no concordancia de simbolos"))
                                    
                                    self.posicion -= 1
                                    self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                                    self.arbol.pop(len(self.arbol)-1)
                                    #print ("retroceso en la entrada: ",['n',self.posicion+1,self.arbol,self.produccion])
                                    self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion, "retroceso en la entrada"))
                                    
                                    self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                                    self.arbol.pop(len(self.arbol)-1)
                                    #print ("retroceso en la entrada: ",['n',self.posicion+1,self.arbol,self.produccion])
                                    self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion, "retroceso en la entrada"))
                                    
                                    del self.produccion[0:4]
                                    self.produccion.pop(0)
                                    self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                                    self.arbol.pop(len(self.arbol)-1)
                                    #print ("retroceso en la entrada: ",['n',self.posicion+1,self.arbol,self.produccion])
                                    self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion, "retroceso en la entrada"))
                                    
                                    self.produccion.pop(0)
                                    self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                                    self.arbol.pop(len(self.arbol)-1)
                                    #print ("retroceso en la entrada: ",['n',self.posicion+1,self.arbol,self.produccion])
                                    self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion, "retroceso en la entrada"))
                                    
                                    return False
                            else:
                                self.posicion -= 1
                                self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                                self.arbol.pop(len(self.arbol)-1)
                                #print ("no concordancia de simbolos: ",['n',self.posicion+1,self.arbol,self.produccion])
                                self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion, "no concordancia de simbolos"))
                                
                                self.posicion -= 1
                                self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                                self.arbol.pop(len(self.arbol)-1)
                                #print ("retroceso en la entrada: ",['n',self.posicion+1,self.arbol,self.produccion])
                                self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion, "retroceso en la entrada"))
                                
                                self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                                self.arbol.pop(len(self.arbol)-1)
                                #print ("retroceso en la entrada: ",['n',self.posicion+1,self.arbol,self.produccion])
                                self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion, "retroceso en la entrada"))
                                
                                del self.produccion[0:4]
                                self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                                self.arbol.pop(len(self.arbol)-1)
                                #print ("no concordancia de simbolos: ",['n',self.posicion+1,self.arbol,self.produccion])
                                self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion, "no concordancia de simbolos"))
                                
                                self.posicion -= 1
                                self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                                self.arbol.pop(len(self.arbol)-1)
                                #print ("retroceso en la entrada: ",['n',self.posicion+1,self.arbol,self.produccion])
                                self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion, "retroceso en la entrada"))
                                
                                self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                                self.arbol.pop(len(self.arbol)-1)
                                #print ("retroceso en la entrada: ",['n',self.posicion+1,self.arbol,self.produccion])
                                self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion, "retroceso en la entrada"))
                                
                                self.posicion -= 1
                                del self.produccion[0:4]
                                self.produccion.pop(0)
                                self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                                self.arbol.pop(len(self.arbol)-1)
                                #print ("retroceso en la entrada: ",['n',self.posicion+1,self.arbol,self.produccion])
                                self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion, "retroceso en la entrada"))
                                
                                self.produccion.pop(0)
                                self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                                self.arbol.pop(len(self.arbol)-1)
                                #print ("retroceso en la entrada: ",['n',self.posicion+1,self.arbol,self.produccion])
                                self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion, "retroceso en la entrada"))
                                
                                return False
                        else :
                            #print ("comienza")
                            self.posicion -= 1
                            self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                            self.arbol.pop(len(self.arbol)-1)
                            #print ("no coincidencia de simbolos: ",['n',self.posicion+1,self.arbol,self.produccion])
                            self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion, "no coincidencia de simbolos"))
                            
                            self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                            self.arbol.pop(len(self.arbol)-1)
                            #print ("retroceso en la entrada: ",['n',self.posicion+1,self.arbol,self.produccion])
                            self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion, "retroceso en la entrada"))
                            
                            del self.produccion[0:4]
                            self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                            self.arbol.pop(len(self.arbol)-1)
                            #print ("no concordancia de simbolos: ",['n',self.posicion+1,self.arbol,self.produccion])
                            self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion, "no concordancia de simbolos"))
                            
                            self.posicion -= 1
                            self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                            self.arbol.pop(len(self.arbol)-1)
                            #print ("retroceso en la entrada: ",['n',self.posicion+1,self.arbol,self.produccion])
                            self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion, "retroceso en la entrada"))
                            
                            self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                            self.arbol.pop(len(self.arbol)-1)
                            #print ("retroceso en la entrada: ",['n',self.posicion+1,self.arbol,self.produccion])
                            self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion, "retroceso en la entrada"))
                            
                            del self.produccion[0:4]
                            self.produccion.pop(0)
                            self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                            self.arbol.pop(len(self.arbol)-1)
                            self.posicion -= 1
                            #print ("retroceso en la entrada: ",['n',self.posicion+1,self.arbol,self.produccion])
                            self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion, "retroceso en la entrada"))
                            
                            self.produccion.pop(0)
                            self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                            self.arbol.pop(len(self.arbol)-1)
                            #print ("retroceso en la entrada: ",['n',self.posicion+1,self.arbol,self.produccion])
                            self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion, "retroceso en la entrada"))
                            
                            return False
                    else: 
                        #print ("comienza")
                        self.posicion -= 1
                        self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                        self.arbol.pop(len(self.arbol)-1)
                        #print ("retroceso a la entrada: ",['n',self.posicion+1,self.arbol,self.produccion])
                        self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion, "retroceso a la entrada"))
                        
                        self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                        self.arbol.pop(len(self.arbol)-1)
                        #print ("retroceso a la entrada: ",['n',self.posicion+1,self.arbol,self.produccion])
                        self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion, "retroceso a la entrada"))
                        
                        del self.produccion[0:4]
                        self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                        self.arbol.pop(len(self.arbol)-1)
                        #print ("retroceso a la entrada: ",['n',self.posicion+1,self.arbol,self.produccion])
                        self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion, "retroceso a la entrada"))
                        
                        self.posicion -= 1
                        self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                        self.arbol.pop(len(self.arbol)-1)
                        #print ("no concordancia de simbolos: ",['n',self.posicion+1,self.arbol,self.produccion])
                        self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion, "no concordancia de simbolos"))
                        
                        self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                        self.arbol.pop(len(self.arbol)-1)
                        #print ("retroceso a la entrada: ",['n',self.posicion+1,self.arbol,self.produccion])
                        self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion, "retroceso a la entrada"))
                        
                        del self.produccion[0:4]
                        self.produccion.pop(0)
                        self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                        self.arbol.pop(len(self.arbol)-1)
                        #print ("retoceso a la entrada: ",['n',self.posicion+1,self.arbol,self.produccion])
                        self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion, "retoceso a la entrada"))
                        
                        self.produccion.pop(0)
                        self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                        self.arbol.pop(len(self.arbol)-1)
                        #print ("retroceso a la entrada: ",['n',self.posicion+1,self.arbol,self.produccion])
                        self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion, "retroceso a la entrada"))
                        
                        return False
            else:
                #print ("complemento")
                self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                self.arbol.pop(len(self.arbol)-1)
                #print ("retroceso a la entrada: ",['n',self.posicion+1,self.arbol,self.produccion])
                self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion, "retroceso a la entrada"))
                
                self.produccion.pop(0)
                self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                self.arbol.pop(len(self.arbol)-1)
                #print ("retroceso a la entrada: ",['n',self.posicion+1,self.arbol,self.produccion])
                self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion, "retroceso a la entrada"))
                
                self.posicion -= 1
                self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                self.arbol.pop(len(self.arbol)-1)
                #print ("retroceso a la entrada: ",['n',self.posicion+1,self.arbol,self.produccion])
                self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion, "retroceso a la entrada"))
                
                self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                self.arbol.pop(len(self.arbol)-1)
                #print ("retroceso a la entrada: ",['n',self.posicion+1,self.arbol,self.produccion])
                self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion, "retroceso a la entrada"))
                
                self.posicion -= 1
                del self.produccion[0:5]
                self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                self.arbol.pop(len(self.arbol)-1)
                #print ("retroceso a la entrada: ",['n',self.posicion+1,self.arbol,self.produccion])
                self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion, "retroceso a la entrada"))
                
                self.produccion.pop(0)
                self.produccion.insert(0,self.arbol[len(self.arbol)-1])
                self.arbol.pop(len(self.arbol)-1)
                #print ("retroceso a la entrada: ",['n',self.posicion+1,self.arbol,self.produccion])
                self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion, "retroceso a la entrada"))
                
                return False 
        else:
            self.produccion.insert(0,self.arbol[len(self.arbol)-1])
            self.arbol.pop(len(self.arbol)-1)
            #print ("retroceso en la entrada: ",['n',self.posicion+1,self.arbol,self.produccion])
            self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion, "retroceso en la entrada"))
            
            self.posicion -= 1
            del self.produccion[0:4]
            self.produccion.insert(0,self.arbol[len(self.arbol)-1])
            self.arbol.pop(len(self.arbol)-1)
            #print ("retroceso en la entrada: ",['n',self.posicion+1,self.arbol,self.produccion])
            self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion, "retroceso en la entrada"))
            
            self.produccion.pop(0)
            self.produccion.insert(0,self.arbol[len(self.arbol)-1])
            self.arbol.pop(len(self.arbol)-1)
            #print ("retroceso en la entrada: ",['n',self.posicion+1,self.arbol,self.produccion])
            self.tabla.insert(parent="", index="end", values=("r",self.posicion+1, self.arbol, self.produccion, "retroceso en la entrada"))
            
            return False  
    def complemento2(self, cadena):
        variable = cadena[self.posicion]
        if variable[0] == ":" and variable[1:].islower():
            self.arbol.append(self.produccion[0])
            self.produccion.pop(0)
            #print ("siguiente alternativa (a): ",['n',self.posicion+1,self.arbol,self.produccion])
            self.tabla.insert(parent="", index="end", values=("n",self.posicion+1, self.arbol, self.produccion, "siguiente alternativa (a)"))

            
            self.produccion[0:0] = ["nomvar","=",'"']
            #print ("ampliacion del arbol: ",['n',self.posicion+1,self.arbol,self.produccion])
            self.tabla.insert(parent="", index="end", values=("n",self.posicion+1, self.arbol, self.produccion, "ampliacion del arbol"))
            
            self.arbol.append(self.produccion[0])
            self.produccion.pop(0)
            #print ("pasamos produccion: ",['n',self.posicion+1,self.arbol,self.produccion])
            self.tabla.insert(parent="", index="end", values=("n",self.posicion+1, self.arbol, self.produccion, "pasamos produccion"))
            
            self.arbol.append(cadena[self.posicion])
            #print ("coincidencia de simbolo: ",['n',self.posicion+1,self.arbol,self.produccion])
            self.tabla.insert(parent="", index="end", values=("n",self.posicion+1, self.arbol, self.produccion, "coincidencia de simbolo"))
            
            self.posicion +=1
            return True
        else:
            return False
    def asignado (self,cadena):
        variable = cadena[self.posicion]
        #print ("asignado")
        #print (cadena[self.posicion])
        partes = variable.split('.')
        if cadena[self.posicion] == '"':
            self.arbol.append(self.produccion[0])
            self.produccion.pop(0)
            #print ("coincidencia de simbolo: ",['n',self.posicion+1,self.arbol,self.produccion])
            self.tabla.insert(parent="", index="end", values=("n",self.posicion+1, self.arbol, self.produccion, "coincidencia de simbolo"))

            return True
        elif variable == "FALSE" or variable == "TRUE":
            self.arbol.append(self.produccion[0])
            self.produccion.pop(0)
            #print ("coincidencia de simbolo: ",['n',self.posicion+1,self.arbol,self.produccion])
            self.tabla.insert(parent="", index="end", values=("n",self.posicion+1, self.arbol, self.produccion, "coincidencia de simbolo"))
            
            
            return True
        elif len(partes) == 2 and partes[0].isdigit() and partes[1].isdigit():
            self.arbol.append(self.produccion[0])
            self.produccion.pop(0)
            #print ("coincidencia de simbolo: ",['n',self.posicion+1,self.arbol,self.produccion])
            self.tabla.insert(parent="", index="end", values=("n",self.posicion+1, self.arbol, self.produccion, "coincidencia de simbolo"))
            
            return True
        elif variable.isdigit():
            self.arbol.append(self.produccion[0])
            self.produccion.pop(0)
            #print ("coincidencia de simbolo: ",['n',self.posicion+1,self.arbol,self.produccion])
            self.tabla.insert(parent="", index="end", values=("n",self.posicion+1, self.arbol, self.produccion, "coincidencia de simbolo"))
            
            return True
        else:
            return False
    def tipodato(self, cadena):
        valor = cadena[self.posicion]
        if valor == 'INT' or valor == 'STR' or valor == 'FLT' or valor == 'CHR' or valor == 'BOL':
            return True
        else:
            return False

    def complemento(self, cadena):
        variable = cadena[self.posicion]
        if variable[0] == ":" and variable[1:].islower():
            self.posicion +=1
            return True
        else:
            return False    
        
    def valores(self,cadena):
        variable = cadena[self.posicion]
        partes = variable.split('.')
        if variable[0] == ":" and variable[1:].islower():
            return True  
        elif variable.isdigit():
            return True
        elif partes[0].isdigit() and partes[1].isdigit():
            return True
        else:
            return False

 