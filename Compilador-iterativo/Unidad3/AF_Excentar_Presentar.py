from tkinter import *
from tkinter import ttk
from tkinter.font import Font
import time

class Ventana:
    def __init__(self):
        self.ventana = Tk()
        self.ventana.title("Automata finito")
        self.ventana.geometry("1200x700")
        self.ventana.configure(background="wheat1", bd="10", relief="groove")
        self.caja = Entry(self.ventana)
        self.caja.place(x=160, y=150)
        self.caja.config(width=16, font=("Verdana", 20))
        self.boton = Button(self.ventana, text="Pulsa", font=("Arial", 15), bg="tan", command=self.codigo)
        #agregar boton para limpiar
        self.label = Label(self.ventana, text=" a|ab(ab)* ", font=("Arial", 25), background="coral1", relief="groove")
        self.label.place(x=480, y=20)
        self.etiqueta1 = Label(self.ventana, text=" Cadena: ", font=("Verdana", 20), background="wheat1")
        self.etiqueta1.place(x=20, y=150)
        self.listResultados = Listbox(width=40,height=3,font=Font(family="Sans Serif", size=15))
        
        self.listResultados.place(x=700,y=152) 
        self.boton = Button(self.ventana, text="Pulsa", font=("Arial", 15), bg="tan", command=self.codigo)
        self.botonLimpia = Button(self.ventana, text="Limpiar", font=("Arial", 15), bg="tan", command=self.limpiar)
        self.boton.place(x=220, y=200)
        self.botonLimpia.place(x=350, y=200)
        self.botonAnimacion = Button(self.ventana, text="Mostrar recorrido", font=("Arial", 15), bg="gray", command=self.animacionRecorrido)
        self.botonAnimacion.place(x=100,y=430)
        self.botonAnimacion = Button(self.ventana, text="Siguiente", font=("Arial", 15), bg="gray", command=self.animacionRecorrido)
        self.botonAnimacion.place(x=500,y=550)
        
        self.respuesta = Label(self.ventana, text="", font=("ALGERIAN", 25), background="azure", relief="groove", width=10)
        self.respuesta.place(x=700,y=250)
        
        self.imagen=PhotoImage(file="Automata_Base.png")
        self.labelImagen=Label(self.ventana, image=self.imagen)
        self.labelImagen.place(x=40, y=250)
        self.listaAnimacion=[0]
        self.conta=0
        self.desplaza=0
        #self.canvas = Canvas(self.ventana, bg="azure",width=700,height=400)
        #self.canvas.place(x=20,y=300)
        
        
        self.ventana.mainloop()
        
        
    def limpiar(self):
        self.conta=0
        self.caja.delete(0, END)
        self.listResultados.delete(0,END)
        self.listaAnimacion=[0]
        self.respuesta.config(text="", font=("ALGERIAN", 25), background="azure", relief="groove", width=10)
        self.etiqueta1 = Label(self.ventana, text="                         ", font=("Verdana", 12), background="wheat1")
        self.etiqueta1.place(x=500, y=510)
    def codigo (self):
        self.conta=0
        self.etiqueta1 = Label(self.ventana, text="                                                                   ", font=("Verdana", 12), background="wheat1")
        self.etiqueta1.place(x=500, y=510)
        self.respuesta.config(text="", font=("ALGERIAN", 25), background="azure", relief="groove", width=10)        
        self.listResultados.delete(0,END)
        self.listaAnimacion=[0]
        self.caracter=str(self.caja.get()) #se recibe la cadena de entrada
        self.largoPalabra=int(len(self.caja.get()))
        self.aux=str(self.caracter)
        if self.caracter=="":
            pass
        else:
            #print(self.largoPalabra ,self.caracter)
            uno_caracter = self.Una_letra()
            #print(uno_caracter)
            
            if uno_caracter == True and (self.caracter[0] == "a"):
                print ("solo un" ,self.caracter)
                self.aux = self.aux[1:]
                self.listResultados.insert(END,str(self.conta)+" q1-> "+self.aux)
                self.conta+=1
                self.listaAnimacion.append(1)
                self.respuesta.config(text="Correcto", font=("ALGERIAN", 25), background="lawn green", relief="groove", width=10)
                
                self.listResultados.insert(END,"Es un EF valido")
                self.listResultados.itemconfig(END, bg="lawn green") 
                
                
                
            elif (uno_caracter == False) and (self.caracter[0] == "a") and (self.largoPalabra == 2):
                #print("dos" ,self.caracter)
                self.aux = self.aux[1:]
                self.listResultados.insert(END,str(self.conta)+" q2-> "+self.aux)
                self.conta+=1
                self.listaAnimacion.append(2)
                
                res = self.dos_letras()
                if res == True:
                    self.respuesta.config(text="Correcto", font=("ALGERIAN", 25), background="lawn green", relief="groove", width=10)
                    self.listResultados.insert(END,str(self.conta)+" q3-> "+self.aux)
                    self.conta+=1
                    self.listaAnimacion.append(3)
                    self.listResultados.insert(END,"Es un EF valido")
                    self.listResultados.itemconfig(END, bg="lawn green") 
                else:                
                    self.respuesta.config(text="Error", font=("ALGERIAN", 25), background="red", relief="groove", width=10)
                    self.listResultados.insert(END,"Es un EF no valido")
                    self.listResultados.itemconfig(END, bg="red") 
                
            elif (uno_caracter == False) and (self.caracter[0] == "a"):            
                self.aux = self.aux[1:]
                resp = self.mas_letras()
                if resp == True:
                    self.listResultados.insert(END,str(self.conta)+" q3->"+self.aux)
                    self.conta+=1
                    self.listaAnimacion.append(3)
                    self.aux = self.aux[1:]
                    
                    self.respuesta.config(text="Correcto", font=("ALGERIAN", 25), background="lawn green", relief="groove", width=10)
                    self.listResultados.insert(END,"Es un EF valido")
                    self.listResultados.itemconfig(END, bg="lawn green")
                else:
                    #self.listResultados.insert(END,"q3->"+self.aux)
                    #self.aux = self.aux[1:]
                    
                    if self.aux=="":
                        self.listResultados.insert(END,str(self.conta)+" q2->"+self.aux)
                        self.conta+=1
                        self.listaAnimacion.append(4)
                    self.respuesta.config(text="Error", font=("ALGERIAN", 25), background="red", relief="groove", width=10)
                    self.listResultados.insert(END,"Es un EF no valido")
                    self.listResultados.itemconfig(END, bg="red") 
            else:
                
                self.respuesta.config(text="Error", font=("ALGERIAN", 25), background="red", relief="groove", width=10)
                self.listResultados.insert(END,"Es un EF no valido")
                self.listResultados.itemconfig(END, bg="red") 
        
        
        
        
    def Una_letra(self):
        self.listResultados.insert(END,str(self.conta)+" q0-> "+self.aux)
        self.conta+=1
        if int(self.largoPalabra) == 1:
            return True
        else:
            return False
        
    def dos_letras(self):
        self.aux = self.aux[1:]
        if self.caracter[1]=="b":
            return True
        else:
            return False
        
    def mas_letras(self):
        cont = 1
        #print(self.largoPalabra)
        if self.caracter[1]=="b":
            self.listResultados.insert(END,str(self.conta)+" q2-> "+self.aux)
            self.conta+=1
            self.listaAnimacion.append(2)
            self.aux = self.aux[1:]
            
            cont += 1
        else:
            self.listResultados.insert(END,str(self.conta)+" q2-> "+self.aux)
            self.conta+=1
            self.listaAnimacion.append(2)
            return False
        while cont < self.largoPalabra:
            #print("mas 1" ,self.caracter[cont])
            print(cont,self.largoPalabra)
            if self.caracter[cont]=="a":
                cont += 1
                self.listResultados.insert(END,str(self.conta)+" q3-> "+self.aux)
                self.conta+=1
                self.listaAnimacion.append(3)
                self.aux = self.aux[1:]
            else:
                self.listResultados.insert(END,str(self.conta)+" q3-> "+self.aux)
                self.conta+=1
                self.listaAnimacion.append(3)
                #print ("retorno aqui 3")
                return False
            #print("mas 2" ,self.caracter[cont])
            
            #print(cont)
            if cont == self.largoPalabra:
                return  False
            if self.caracter[cont]=="b":
                self.listResultados.insert(END,str(self.conta)+" q2-> "+self.aux)
                self.conta+=1
                self.listaAnimacion.append(4)
                self.aux = self.aux[1:]
                cont += 1
            else:
                self.listResultados.insert(END,str(self.conta)+" q2-> "+self.aux)
                self.conta+=1
                self.listaAnimacion.append(4)
                #print ("retorno aqui 2")
                return False
            #print(cont)
            #print("mas" ,self.caracter[cont])
            print (self.aux)
        if self.caracter[-1]=="b":
            return True

        #else:
    def animacionRecorrido(self):
        print (self.listaAnimacion)        
        nomimagen=""
        print (self.desplaza)
        numero=str(self.desplaza)+" de "+str(len(self.listaAnimacion)-1)
        self.etiqueta1 = Label(self.ventana, text=numero, font=("Verdana", 12), background="wheat1")
        self.etiqueta1.place(x=500, y=510)
        if self.desplaza<len(self.listaAnimacion):
            if self.listaAnimacion[self.desplaza]==0:
                nomimagen="q0.png"
            elif self.listaAnimacion[self.desplaza]==1:
                nomimagen="q1.png"
            elif self.listaAnimacion[self.desplaza]==2:
                nomimagen="q2.png"
            elif self.listaAnimacion[self.desplaza]==3:
                nomimagen="q3.png"
            elif self.listaAnimacion[self.desplaza]==4:
                nomimagen="q2ret.png"
            print (nomimagen)
            self.imagenAn=PhotoImage(file=nomimagen)
            self.labelImagenAnimacion=Label(self.ventana, image=self.imagenAn)
            self.labelImagenAnimacion.place(x=40, y=480)
            self.desplaza+=1
            if self.desplaza==len(self.listaAnimacion):
                self.desplaza=0
                   
        
        
        
        
        
    
    
    
s = Ventana()