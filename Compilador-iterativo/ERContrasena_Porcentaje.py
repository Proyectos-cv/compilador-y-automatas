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
        self.etiquetaInstrucciones6 = Label(self.ventana, text="*Solo puede llevar UN caracter especial (*,-,@) y debe ocupar la última posición.", font=("Verdana", 12), background="wheat1")
        self.etiquetaInstrucciones6.place(x=20, y=350)
        #Lista para mandar resultados a pantalla
        self.etiquetaResultados = Label(self.ventana, text=" Resultados: ", font=("Verdana", 20), background="wheat1")
        self.etiquetaResultados.place(x=530, y=150)
        self.listResultados = Listbox(width=40,height=3,font=Font(family="Sans Serif", size=15))
        self.listResultados.place(x=700,y=152)
        
        self.ER = Label(self.ventana, text=" ER: /^((([0-9][a-z][A-Z])([0-9][a-z][A-Z]){4,12}(\*\|\-\|\@\)){8,16})$/  ",font=("Verdana", 15), background="old lace")
        self.ER.place(x=20, y=390)
                
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
        self.listaMinusculas=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        self.listaMayusculas=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.listaNumeros=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.listaSimbolos=['@','-','*']
        
        condicion=False
        self.contrasena=str(self.caja.get()) #se recibe la cadena de entrada
        self.largoPalabra=len(self.caja.get()) #se obtiene el largo de la cadena
        self.listRecorridoExc.insert(END, "qo"+self.aux)
        #print (self.largoPalabra)
        condicion=self.verificarLongitud()
        if condicion==True:
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
        else:
            print ("Contraseña invalida: Numero de caracteres incorrecto")
            self.listResultados.insert(END, "Contraseña invalida: Numero de caracteres incorrecto")
            self.listResultados.itemconfig(END, bg="red")
    #1aCaballero
    def verificarPrimeros3(self):
        exitos=0
        #print("Entro a verificar")
        if self.contrasena[0] in self.listaNumeros:
            #print (self.contrasena[0])
            exitos+=1
            #eliminar primer letra de self.aux
            self.aux
            self.listRecorridoExc.insert(END, "qo"+self.aux)
        if self.contrasena[1] in self.listaMinusculas:
            exitos+=1
        if self.contrasena[2] in self.listaMayusculas:
            exitos+=1
        #print (exitos)
        if exitos==3:
            return True
        else:
            return False
    def verificarLongitud(self):
        #print("Entro a longitud")
        #Comprueba que la contraseña tenga entre 8 y 16 caracteres
        if self.largoPalabra < 8 or self.largoPalabra > 16:
            #print ("La contraseña debe tener entre 8 y 16 caracteres")
            self.listResultados.insert(END, "La contraseña debe tener entre 8 y 16 caracteres")
            self.listResultados.itemconfig(END, bg="red")
            return False
        else:
            #print ("La contraseña es valida")
            #self.listResultados.insert(END, "La contraseña es valida")
            #self.listResultados.itemconfig(END, bg="green")
            return True
        
        #saber si la letra esta dentro de uno de esos arreglos
        #if self.caja.get() in listaMinusculas:
        #    print ("La contraseña debe tener al menos una letra minuscula")
        #dame la ultima letra de la palabra
        ultima=self.caja.get()[-1]
        print (ultima)

    def Verifica_los_del_medio(self):
        print(" ")
        con = 3
        limite = self.largoPalabra -1
        while con < limite:
            if (self.contrasena[con] in self.listaNumeros) or (self.contrasena[con] in self.listaMinusculas) or (self.contrasena[con] in self.listaMayusculas):
                print(self.contrasena[con])

            else:
                return False
            con += 1

        return True
        
    def Verifica_el_ultimo(self):
        #print (self.contrasena[-1])
        if self.contrasena[-1] in self.listaSimbolos:
            return True
        else:
            return False

        
m=Ventana()
