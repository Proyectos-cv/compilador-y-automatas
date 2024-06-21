from tkinter import *
from tkinter.font import Font
class Ventana:
    def __init__(self):
        self.ventana = Tk()
        self.ventana.title("Validador de contraseñas")
        self.ventana.geometry("1200x700")
        self.ventana.configure(background="wheat1", bd="10", relief="groove")
        self.caja = Entry(self.ventana)
        self.caja.place(x=160, y=150)
        self.caja.config(width=16, font=("Verdana", 20))
        self.boton = Button(self.ventana, text="Pulsa", font=("Arial", 15), bg="tan", command=self.pulsar)
        #agregar boton para limpiar
        self.label = Label(self.ventana, text=" Contraseña ", font=("ALGERIAN", 25), background="coral1", relief="groove")
        self.label.place(x=480, y=20)
        self.etiqueta1 = Label(self.ventana, text=" Cadena: ", font=("Verdana", 20), background="wheat1")
        self.etiqueta1.place(x=20, y=150)
        #Instrucciones para fromar contraseña
        self.etiquetaInstrucciones = Label(self.ventana, text="Para formar la Contraseña debe ser de la siguiente manera: ", font=("Verdana", 12), background="wheat1")
        self.etiquetaInstrucciones.place(x=20, y=250)
        self.etiquetaInstrucciones2 = Label(self.ventana, text="*Extension mínima de 8 caracteres y máximo 16.", font=("Verdana", 12), background="wheat1")
        self.etiquetaInstrucciones2.place(x=20, y=270)
        self.etiquetaInstrucciones3 = Label(self.ventana, text="*Empezar con un número.", font=("Verdana", 12), background="wheat1")
        self.etiquetaInstrucciones3.place(x=20, y=290)
        self.etiquetaInstrucciones4 = Label(self.ventana, text="*El segundo caracter debe ser minúscula.", font=("Verdana", 12), background="wheat1")
        self.etiquetaInstrucciones4.place(x=20, y=310)
        self.etiquetaInstrucciones5 = Label(self.ventana, text="*El tercer caracter debe ser mayúscula.", font=("Verdana", 12), background="wheat1")
        self.etiquetaInstrucciones5.place(x=20, y=330)
        self.etiquetaInstrucciones7 = Label(self.ventana, text="*Colocar entre 4 y 12 veces mayúsculas,minúsculas o números.", font=("Verdana", 12), background="wheat1")
        self.etiquetaInstrucciones7.place(x=20, y=350)
        self.etiquetaInstrucciones6 = Label(self.ventana, text="*Solo puede llevar UN caracter especial (*,-,@) y debe ocupar la última posición.", font=("Verdana", 12), background="wheat1")
        self.etiquetaInstrucciones6.place(x=20, y=370)
        #Lista para mandar resultados a pantalla
        self.etiquetaResultados = Label(self.ventana, text=" Resultados: ", font=("Verdana", 20), background="wheat1")
        self.etiquetaResultados.place(x=530, y=150)
        self.listResultados = Listbox(width=40,height=3,font=Font(family="Sans Serif", size=15))
        self.listResultados.place(x=700,y=152)
        
        #self.ER = Label(self.ventana, text=" ER: /^((([0-9][a-z][A-Z])([0-9][a-z][A-Z]){4,12}(\*\|\-\|\@\)){8,16})$/  ",font=("Verdana", 15), background="old lace")
        self.ER = Label(self.ventana, text=" ER: /^([0-9])([a-z])([A-Z])([0-9]|[a-z]|[A-Z]){4,12}(\*\|\-\|\@\)$/  ",font=("Verdana", 15), background="old lace")
        self.ER.place(x=20, y=390)
        self.imagen=PhotoImage(file="Automata.png")
        self.labelImagen=Label(self.ventana, image=self.imagen)
        self.labelImagen.place(x=20, y=420)
                
        #Lista para ir recorriendo el proceso
        self.etiquetaProcesoExc = Label(self.ventana, text=" Proceso Autómata: ", font=("Verdana", 20), background="wheat1")
        self.etiquetaProcesoExc.place(x=20, y=550)
        self.listRecorridoExc = Listbox(width=40,height=3,font=Font(family="Sans Serif", size=15))
        self.listRecorridoExc.place(x=290,y=552)
        self.botonLimpia = Button(self.ventana, text="Limpiar", font=("Arial", 15), bg="tan", command=self.limpiar)
        self.boton.place(x=220, y=200)
        self.botonLimpia.place(x=350, y=200)
        self.ventana.mainloop()
        #agregar un boton para limpirar la caja de texto
        
        #Lista de letras minusculas, mayusculas, numeros y simbolos aceptados
        
        
    def limpiar(self):
        self.caja.delete(0, END)
        self.listResultados.delete(0,END)
    def pulsar(self):
        self.listResultados.delete(0,END)
        self.listRecorridoExc.delete(0,END)
        self.listaMinusculas=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        self.listaMayusculas=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.listaNumeros=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.listaSimbolos=['@','-','*']
        
        condicion=False
        self.contrasena=str(self.caja.get()) #se recibe la cadena de entrada
        if self.contrasena=="":
            pass
        else:
            self.largoPalabra=len(self.caja.get()) #se obtiene el largo de la cadena
            self.aux=self.contrasena
            #self.listRecorridoExc.insert(END, "qo->"+self.aux)
            #print (self.largoPalabra)
            condicion2=self.verificarPrimeros3()
            if condicion2==True:
                #condicion3 la verificacion los caracteres del medio
                condicion3 = self.Verifica_los_del_medio()
                if condicion3 == True:
                    #condicion4 verifica la ultima condicion
                    condicion4 = self.Verifica_el_ultimo()#verifica el ultimo caracter
                    if condicion4 == True:
                        #print ("La contraseña es valida")
                        #cambiar color del mensaje a verde
                        self.listResultados.insert(END, "La contraseña es valida!")
                        self.listResultados.itemconfig(END, bg="green")
                        self.listRecorridoExc.insert(END, "q4 es un estado final valido")
                        self.listRecorridoExc.itemconfig(END, bg="green")
                    else:
                        #print("No tiene simbolo especial, no cumple la contraseña")
                        self.listResultados.insert(END, "No tiene símbolo especial, no cumple la contraseña")
                        self.listResultados.itemconfig(END, bg="red")
                        
                else:
                    #print("los caracteres internos no cumplen")
                    self.listResultados.insert(END, "Los caracteres internos no cumplen")
                    self.listResultados.itemconfig(END, bg="red")
            else:
                #print("La contraseña no es valida: alguno de los primeros 3 caracteres no cumplen")
                self.listResultados.insert(END, "La contraseña no es valida: alguno de los primeros 3 caracteres no cumplen")
                self.listResultados.itemconfig(END, bg="red")

    #1aCaballero
    def verificarPrimeros3(self):
        #print("Entro a verificar")
        if self.contrasena[0] in self.listaNumeros:
            #self.listRecorridoExc.insert(END, "q0->"+self.aux)
            self.agregarCorrecto("q0->")
        else:
            self.agregarInvalido("q0->")
            return False
        
        if self.contrasena[1] in self.listaMinusculas:            
            self.agregarCorrecto("q1->")
        else:
            self.agregarInvalido("q1->")
            return False
        
        if self.contrasena[2] in self.listaMayusculas:            
            self.agregarCorrecto("q2->")
            return True
        else:
            self.agregarInvalido("q2->")
            return False
     #Agrega a la lista de recorrido de automata un estado valido   
    def agregarCorrecto(self,automata):
        self.listRecorridoExc.insert(END, automata+self.aux)
        self.aux=self.aux[1:]
    #agrega a la lista un recorrido no valido del automata    
    def agregarInvalido(self,automata):
        self.listRecorridoExc.insert(END, automata+self.aux)
        self.listRecorridoExc.insert(END, automata+" no es un EF valido")
        self.listRecorridoExc.itemconfig(END, bg="red")                        
    def agregarInvalidoLong(self,automata):
        self.listRecorridoExc.insert(END, automata+self.aux)
        self.listRecorridoExc.insert(END, automata+" no es un EF valido, tamaño erroneo")
        self.listRecorridoExc.itemconfig(END, bg="red")
    def Verifica_los_del_medio(self):
        print(" ")
        con = 3
        limite = self.largoPalabra -1
        while con < limite and con<=15:
            if (self.contrasena[con] in self.listaNumeros) or (self.contrasena[con] in self.listaMinusculas) or (self.contrasena[con] in self.listaMayusculas):                
                self.agregarCorrecto("q3->")

            else:
                self.agregarInvalido("q3->")
                return False
            con += 1
        print (con)
        if con>=7 and con<=15:
            self.agregarCorrecto("q3->")
            return True
        else:
            self.agregarInvalidoLong("q3->")
            return False
        
    def Verifica_el_ultimo(self):
        #print (self.contrasena[-1])
        if self.contrasena[-1] in self.listaSimbolos:
            self.agregarCorrecto("q4->")
            return True
        else:
            self.agregarInvalido("q3->")
            return False

        
m=Ventana()
