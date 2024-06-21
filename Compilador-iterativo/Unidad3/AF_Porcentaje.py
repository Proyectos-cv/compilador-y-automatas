from tkinter import *
from tkinter import ttk
from tkinter.font import Font


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
        self.label = Label(self.ventana, text=" a|ab(ab)* ", font=("ALGERIAN", 25), background="coral1", relief="groove")
        self.label.place(x=480, y=20)
        self.etiqueta1 = Label(self.ventana, text=" Cadena: ", font=("Verdana", 20), background="wheat1")
        self.etiqueta1.place(x=20, y=150)
        self.listResultados = Listbox(width=40,height=3,font=Font(family="Sans Serif", size=15))
        
        self.listResultados.place(x=700,y=152) 
        self.boton = Button(self.ventana, text="Pulsa", font=("Arial", 15), bg="tan", command=self.codigo)
        self.botonLimpia = Button(self.ventana, text="Limpiar", font=("Arial", 15), bg="tan", command=self.limpiar)
        self.boton.place(x=220, y=200)
        self.botonLimpia.place(x=350, y=200)
        
        self.respuesta = Label(self.ventana, text="", font=("ALGERIAN", 25), background="azure", relief="groove", width=10)
        self.respuesta.place(x=700,y=250)
        
        
        self.canvas = Canvas(self.ventana, bg="azure",width=700,height=400)
        self.canvas.place(x=20,y=300)
        
        
        self.ventana.mainloop()
        
        
    def limpiar(self):
        self.caja.delete(0, END)
        self.listResultados.delete(0,END)
        self.respuesta.config(text="", font=("ALGERIAN", 25), background="azure", relief="groove", width=10)
    def codigo (self):
        self.respuesta.config(text="", font=("ALGERIAN", 25), background="azure", relief="groove", width=10)
        
        self.listResultados.delete(0,END)
        self.caracter=str(self.caja.get()) #se recibe la cadena de entrada
        self.largoPalabra=int(len(self.caja.get()))
        self.aux=str(self.caracter)
        
        print(self.largoPalabra ,self.caracter)
        uno_caracter = self.Una_letra()
        if uno_caracter == True and (self.caracter[0] == "a" or self.caracter[0] == "A"):
            print ("solo un" ,self.caracter)
            self.aux = self.aux[1:]
            self.listResultados.insert(END,"q1-> "+self.aux)
            self.respuesta.config(text="Correcto", font=("ALGERIAN", 25), background="lawn green", relief="groove", width=10)
            
            self.listResultados.insert(END,"es valido")
            self.listResultados.itemconfig(END, bg="lawn green") 
            
            
            
        elif (uno_caracter == False) and (self.caracter[0] == "a" or self.caracter[0] == "A") and (self.largoPalabra == 2):
            print("dos" ,self.caracter)
            self.listResultados.insert(END,"q1-> "+self.aux)
            self.aux = self.aux[1:]
            self.listResultados.insert(END,"q2-> "+self.aux)
            
            res = self.dos_letras()
            if res == True:
                self.respuesta.config(text="Correcto", font=("ALGERIAN", 25), background="lawn green", relief="groove", width=10)
                self.listResultados.insert(END,"q3-> "+self.aux)
                
                self.listResultados.insert(END,"es valido")
                self.listResultados.itemconfig(END, bg="lawn green") 
            else:
                self.listResultados.insert(END,"q3-> "+self.aux)
                
                self.respuesta.config(text="Error", font=("ALGERIAN", 25), background="red", relief="groove", width=10)
                self.listResultados.insert(END,"es un caracter no valido")
                self.listResultados.itemconfig(END, bg="red") 
            
        elif (uno_caracter == False) and (self.caracter[0] == "a" or self.caracter[0] == "A"):
            self.listResultados.insert(END,"q1-> "+self.aux)
            
            self.aux = self.aux[1:]
            self.listResultados.insert(END,"q2-> "+self.aux)
            resp = self.mas_letras()
            if resp == True:
                self.listResultados.insert(END,"q3->"+self.aux)
                self.aux = self.aux[1:]
                
                self.respuesta.config(text="Correcto", font=("ALGERIAN", 25), background="lawn green", relief="groove", width=10)
                self.listResultados.insert(END,"es valido")
                self.listResultados.itemconfig(END, bg="lawn green")
            else:
                self.listResultados.insert(END,"q3->"+self.aux)
                self.aux = self.aux[1:]
                
                self.respuesta.config(text="Error", font=("ALGERIAN", 25), background="red", relief="groove", width=10)
                self.listResultados.insert(END,"es un caracter no valido")
                self.listResultados.itemconfig(END, bg="red") 
        else:
            
            self.respuesta.config(text="Error", font=("ALGERIAN", 25), background="red", relief="groove", width=10)
            self.listResultados.insert(END,"es un caracter no valido")
            self.listResultados.itemconfig(END, bg="red") 
        
        
        
        
    def Una_letra(self):
        self.listResultados.insert(END,"q0-> "+self.aux)
        
        if int(self.largoPalabra) == 1:
            return TRUE
        else:
            return False
        
    def dos_letras(self):
        self.aux = self.aux[1:]
        if self.caracter[1]=="b":
            return TRUE
        else:
            return False
        
    def mas_letras(self):
        cont = 1
        print(self.largoPalabra)
        if self.caracter[1]=="b":
            self.listResultados.insert(END,"q2->"+self.aux)
            self.aux = self.aux[1:]
            
            cont += 1
        else:
            return False
        while cont < self.largoPalabra:
            #print("mas 1" ,self.caracter[cont])
            #print(cont)
            if self.caracter[cont]=="a":
                cont += 1
                self.listResultados.insert(END,"q3->"+self.aux)
                self.aux = self.aux[1:]
            else:
                return False
            #print("mas 2" ,self.caracter[cont])
            
            #print(cont)
            if cont == self.largoPalabra:
                return  False
            if self.caracter[cont]=="b":
                self.listResultados.insert(END,"q2->"+self.aux)
                self.aux = self.aux[1:]
                cont += 1
            else:
                return False
            #print(cont)
            #print("mas" ,self.caracter[cont])
        if self.caracter[-1]=="b":
            return TRUE
        
        
        
        
        
        
        
    
    
    
s = Ventana()