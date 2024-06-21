from tkinter import *
from tkinter import ttk

from tkinter.font import Font

from tkinter import scrolledtext as st
from tkinter import filedialog as fd
from tkinter import messagebox

import time

class Suma:
    def __init__(self) -> None:
        self.ventana = Tk()
        self.ventana.title("Maquina de turing")
        self.ventana.geometry("1200x700+0+0")
        self.ventana.configure(background="wheat1", bd="10", relief="groove")
        validation = self.ventana.register(self.validar_longitud)
        self.Label1 = Label(self.ventana,font=("Arial", 15),text="Caja 1", background="coral1", relief="groove")
        self.Label1.place(x=100,y=60)
        self.caja1 = Entry(self.ventana,font=("Arial", 15),  validate="key", validatecommand=(validation, '%P'))
        self.caja1.place(x=200,y=60)
        
        self.Label2 = Label(self.ventana,font=("Arial", 15),text="Caja 2", background="coral1", relief="groove")
        self.Label2.place(x=100,y=100)
        self.caja2 = Entry(self.ventana,font=("Arial", 15),  validate="key", validatecommand=(validation, '%P'))
        self.caja2.place(x=200,y=100)
        
        #self.calcular = Button(self.ventana,font=("Arial", 15),text="Calcular", relief="groove",command=self.corrido)
        #self.calcular.place(x=200,y=140)
        
        self.calcular = Button(self.ventana,font=("Arial", 15),text="Llenar", relief="groove",command=self.una__por_una)
        self.calcular.place(x=380,y=140)
        
        self.calcular = Button(self.ventana,font=("Arial", 15),text="Paso", relief="groove",command=self.Pasos)
        self.calcular.place(x=300,y=140)
        
        self.calcular = Button(self.ventana,font=("Arial", 15),text="Limpiar", relief="groove",command=self.limpiar)
        self.calcular.place(x=480,y=140)
        
        self.Tabla()
        
        self.ventana.mainloop()
    def Tabla(self):    
        #label
        self.Label_1 =  Label(self.ventana,font=("Arial", 15),text=" B ", relief="groove",height=1,width=2)
        self.Label_1.place(x=100,y=300)
        
        self.Label_2 =  Label(self.ventana,font=("Arial", 15),text="   ", relief="groove",height=1,width=2)
        self.Label_2.place(x=150,y=300)
        
        self.Label_3 =  Label(self.ventana,font=("Arial", 15),text="   ", relief="groove",height=1,width=2)
        self.Label_3.place(x=200,y=300)
        
        self.Label_4 =  Label(self.ventana,font=("Arial", 15),text="   ", relief="groove",height=1,width=2)
        self.Label_4.place(x=250,y=300)
        
        self.Label_5 =  Label(self.ventana,font=("Arial", 15),text="   ", relief="groove",height=1,width=2)
        self.Label_5.place(x=300,y=300)
        
        self.Label_6 =  Label(self.ventana,font=("Arial", 15),text="   ", relief="groove",height=1,width=2)
        self.Label_6.place(x=350,y=300)
        
        self.Label_7 =  Label(self.ventana,font=("Arial", 15),text="   ", relief="groove",height=1,width=2)
        self.Label_7.place(x=400,y=300)
        
        self.Label_8 =  Label(self.ventana,font=("Arial", 15),text="   ", relief="groove",height=1,width=2)
        self.Label_8.place(x=450,y=300)
        
        self.Label_9 =  Label(self.ventana,font=("Arial", 15),text="   ", relief="groove",height=1,width=2)
        self.Label_9.place(x=500,y=300)
        
        self.Label_10 =  Label(self.ventana,font=("Arial", 15),text="   ", relief="groove",height=1,width=2)
        self.Label_10.place(x=550,y=300)
        
        self.Label_11 =  Label(self.ventana,font=("Arial", 15),text="   ", relief="groove",height=1,width=2)
        self.Label_11.place(x=600,y=300)
        
        #2
        self.Label_1_2 =  Label(self.ventana,font=("Arial", 15),text=" B ", relief="groove",height=1,width=2)
        self.Label_1_2.place(x=100,y=350)
        
        self.Label_2_2 =  Label(self.ventana,font=("Arial", 15),text="   ", relief="groove",height=1,width=2)
        self.Label_2_2.place(x=150,y=350)
        
        self.Label_3_2 =  Label(self.ventana,font=("Arial", 15),text="   ", relief="groove",height=1,width=2)
        self.Label_3_2.place(x=200,y=350)
        
        self.Label_4_2 =  Label(self.ventana,font=("Arial", 15),text="   ", relief="groove",height=1,width=2)
        self.Label_4_2.place(x=250,y=350)
        
        self.Label_5_2 =  Label(self.ventana,font=("Arial", 15),text="   ", relief="groove",height=1,width=2)
        self.Label_5_2.place(x=300,y=350)
        
        self.Label_6_2 =  Label(self.ventana,font=("Arial", 15),text="   ", relief="groove",height=1,width=2)
        self.Label_6_2.place(x=350,y=350)
        
        self.Label_7_2 =  Label(self.ventana,font=("Arial", 15),text="   ", relief="groove",height=1,width=2)
        self.Label_7_2.place(x=400,y=350)
        
        self.Label_8_2 =  Label(self.ventana,font=("Arial", 15),text="   ", relief="groove",height=1,width=2)
        self.Label_8_2.place(x=450,y=350)
        
        self.Label_9_2 =  Label(self.ventana,font=("Arial", 15),text="   ", relief="groove",height=1,width=2)
        self.Label_9_2.place(x=500,y=350)
        
        self.Label_10_2 =  Label(self.ventana,font=("Arial", 15),text="   ", relief="groove",height=1,width=2)
        self.Label_10_2.place(x=550,y=350)
        
        self.Label_11_2 =  Label(self.ventana,font=("Arial", 15),text="   ", relief="groove",height=1,width=2)
        self.Label_11_2.place(x=600,y=350)
        
        #Resultado
        self.Label_1_R =  Label(self.ventana,font=("Arial", 15),text=" B ", relief="groove",height=1,width=2)
        self.Label_1_R.place(x=100,y=400)
        
        self.Label_2_R =  Label(self.ventana,font=("Arial", 15),text=" B  ", relief="groove",height=1,width=2)
        self.Label_2_R.place(x=150,y=400)
        
        self.Label_3_R =  Label(self.ventana,font=("Arial", 15),text=" B ", relief="groove",height=1,width=2)
        self.Label_3_R.place(x=200,y=400)
        
        self.Label_4_R =  Label(self.ventana,font=("Arial", 15),text=" B ", relief="groove",height=1,width=2)
        self.Label_4_R.place(x=250,y=400)
        
        self.Label_5_R =  Label(self.ventana,font=("Arial", 15),text=" B ", relief="groove",height=1,width=2)
        self.Label_5_R.place(x=300,y=400)
        
        self.Label_6_R =  Label(self.ventana,font=("Arial", 15),text=" B ", relief="groove",height=1,width=2)
        self.Label_6_R.place(x=350,y=400)
        
        self.Label_7_R =  Label(self.ventana,font=("Arial", 15),text=" B ", relief="groove",height=1,width=2)
        self.Label_7_R.place(x=400,y=400)
        
        self.Label_8_R =  Label(self.ventana,font=("Arial", 15),text=" B ", relief="groove",height=1,width=2)
        self.Label_8_R.place(x=450,y=400)
        
        self.Label_9_R =  Label(self.ventana,font=("Arial", 15),text=" B ", relief="groove",height=1,width=2)
        self.Label_9_R.place(x=500,y=400)
        
        self.Label_10_R =  Label(self.ventana,font=("Arial", 15),text=" B ", relief="groove",height=1,width=2)
        self.Label_10_R.place(x=550,y=400)
        
        self.Label_11_R =  Label(self.ventana,font=("Arial", 15),text=" B ", relief="groove",height=1,width=2)
        self.Label_11_R.place(x=600,y=400)
        
        #Q
        self.Label_1_q =  Label(self.ventana,font=("Arial", 15),text="", relief="groove",height=1,width=2)
        self.Label_1_q.place(x=100,y=450)
        
        self.Label_2_q =  Label(self.ventana,font=("Arial", 15),text="   ", relief="groove",height=1,width=2)
        self.Label_2_q.place(x=150,y=450)
        
        self.Label_3_q =  Label(self.ventana,font=("Arial", 15),text="   ", relief="groove",height=1,width=2)
        self.Label_3_q.place(x=200,y=450)
        
        self.Label_4_q =  Label(self.ventana,font=("Arial", 15),text="   ", relief="groove",height=1,width=2)
        self.Label_4_q.place(x=250,y=450)
        
        self.Label_5_q =  Label(self.ventana,font=("Arial", 15),text="   ", relief="groove",height=1,width=2)
        self.Label_5_q.place(x=300,y=450)
        
        self.Label_6_q =  Label(self.ventana,font=("Arial", 15),text="   ", relief="groove",height=1,width=2)
        self.Label_6_q.place(x=350,y=450)
        
        self.Label_7_q =  Label(self.ventana,font=("Arial", 15),text="   ", relief="groove",height=1,width=2)
        self.Label_7_q.place(x=400,y=450)
        
        self.Label_8_q =  Label(self.ventana,font=("Arial", 15),text="   ", relief="groove",height=1,width=2)
        self.Label_8_q.place(x=450,y=450)
        
        self.Label_9_q =  Label(self.ventana,font=("Arial", 15),text="   ", relief="groove",height=1,width=2)
        self.Label_9_q.place(x=500,y=450)
        
        self.Label_10_q =  Label(self.ventana,font=("Arial", 15),text="   ", relief="groove",height=1,width=2)
        self.Label_10_q.place(x=550,y=450)
        
        self.Label_11_q =  Label(self.ventana,font=("Arial", 15),text="   ", relief="groove",height=1,width=2)
        self.Label_11_q.place(x=600,y=450)
        
        #self.ciclos = 0
    def una__por_una(self):
        self.ciclos = 0
        self.Toma()
    def corrido(self):
        #while True:
        self.Tabla()
        self.ciclos = "pass"
        self.Toma()
    def limpiar(self):
        self.Tabla()
        
    def Pasos(self):
        #print (self.texto1)
        #print (self.texto2)
        #estas listas son para poder cambiar los valores de las etiquetas
        self.Labels_R = [self.Label_1_R, self.Label_2_R, self.Label_3_R, self.Label_4_R, self.Label_5_R, 
                    self.Label_6_R, self.Label_7_R, self.Label_8_R, self.Label_9_R, self.Label_10_R, self.Label_11_R]
        self.Labels_q = [self.Label_1_q, self.Label_2_q, self.Label_3_q, self.Label_4_q, self.Label_5_q, 
                    self.Label_6_q, self.Label_7_q, self.Label_8_q, self.Label_9_q, self.Label_10_q, self.Label_11_q]
        if self.Qedo!="q3" and self.ultimo!=2:
            if self.conta==0:
                print (self.Qedo,self.texto1[10-self.conta],self.texto2[10-self.conta])
                axu=self.resuelve(self.Qedo,self.texto1[10-self.conta],self.texto2[10-self.conta])
                self.Labels_R[self.conta].config(background="snow")
                self.Labels_q[self.conta].config(text=" ")
                self.Labels_R[self.conta-1].config(background="red", text=str(axu[3]))
                self.Labels_q[self.conta-1].config(text=str(self.Qedo))
                self.Qedo=axu[0]
                
                self.conta+=axu[4]
            else:
                print (self.Qedo,self.texto1[10-self.conta],self.texto2[10-self.conta],self.ultimo)
                axu=self.resuelve(self.Qedo,self.texto1[10-self.conta],self.texto2[10-self.conta])
                self.Labels_R[11-self.conta].config(background="snow")
                self.Labels_q[11-self.conta].config(text=" ")
                self.Labels_R[11-self.conta-1].config(background="red", text=str(axu[3]))
                self.Labels_q[11-self.conta-1].config(text=str(self.Qedo))
                self.Qedo=axu[0]
                if self.Qedo=="q3":
                    self.ultimo=1
                self.conta+=axu[4]
        else:
            print (self.Qedo,self.texto1[10-self.conta],self.texto2[10-self.conta],self.ultimo)
            print (11-self.conta)
            self.Labels_R[11-self.conta-2].config(background="snow")
            self.Labels_q[11-self.conta-2].config(text=" ")
            self.Labels_R[11-self.conta-1].config(background="red")
            self.Labels_q[11-self.conta-1].config(text=str(self.Qedo))
            messagebox.showinfo("Alerta", "Cadena aceptada!")
            
    def mostrar_alerta():
        messagebox.showinfo("Alerta", "Esto es una alerta!")
        
       
    def Toma(self):
        #print("Hola")
        self.ultimo=0
        texto1 = str(self.caja1.get())
        texto2 = str(self.caja2.get())
        #print(texto1,texto2)
        self.Qedo="q0"
        if len(texto1) < len(texto2):
            texto1 = texto1.zfill(len(texto2))
        else:
            texto2 = texto2.zfill(len(texto1))
        self.long=len(texto1)
        self.conta=0
        texto1 = self.agregar_a_lista(texto1)
        texto2 = self.agregar_a_lista(texto2)
        
        
        #print(texto1,texto2)
        self.Label_2.config(text=str(texto1[1]))
        self.Label_3.config(text=str(texto1[2]))
        self.Label_4.config(text=str(texto1[3]))
        self.Label_5.config(text=str(texto1[4]))
        self.Label_6.config(text=str(texto1[5]))
        self.Label_7.config(text=str(texto1[6]))
        self.Label_8.config(text=str(texto1[7]))
        self.Label_9.config(text=str(texto1[8]))
        self.Label_10.config(text=str(texto1[9]))
        self.Label_11.config(text=str(texto1[10]))
        
        
        self.Label_2_2.config(text=str(texto2[1]))
        self.Label_3_2.config(text=str(texto2[2]))
        self.Label_4_2.config(text=str(texto2[3]))
        self.Label_5_2.config(text=str(texto2[4]))
        self.Label_6_2.config(text=str(texto2[5]))
        self.Label_7_2.config(text=str(texto2[6]))
        self.Label_8_2.config(text=str(texto2[7]))
        self.Label_9_2.config(text=str(texto2[8]))
        self.Label_10_2.config(text=str(texto2[9]))
        self.Label_11_2.config(text=str(texto2[10]))
        self.texto1 = texto1
        self.texto2 = texto2
        #self.pasos(texto1,texto2)
        
    def separa(self,texto):
        tamaño = len(texto)
        r = ["B"]
        print(tamaño)
        if int(tamaño)<=10:
            t = 10-int(tamaño)
            for i in range(t):
                r.append("0")
        for j in texto:
            r.append(j)
        #print(r)
        return r
    #agrega 
    def agregar_a_lista(self,cadena):
        lista_resultado = []
        for i in range (10):
            if i<len(cadena):
                lista_resultado.append(cadena[i])
            else:
                lista_resultado.insert(0, "B")
        lista_resultado.insert(0, "B")
        return lista_resultado
    

    def pasos(self,texto1,texto2):
        axu = self.resuelve(Q="q0",n1=texto1[10],n2=texto2[10])
        self.Label_11_R.config(background="snow")
        self.Label_11_q.config(text=" ")
        self.Label_11_R.config(background="red",text=str(axu[3]))
        self.Label_11_q.config(text=str(axu[0]))
        
        axu = self.resuelve(Q=axu[0],n1=texto1[9],n2=texto2[9])
        self.Label_11_R.config(background="snow")
        self.Label_11_q.config(text=" ")
        self.Label_10_R.config(background="red",text=str(axu[3]))
        self.Label_10_q.config(text=str(axu[0]))
        
        axu = self.resuelve(Q=axu[0],n1=texto1[8],n2=texto2[8])
        self.Label_10_R.config(background="snow")
        self.Label_10_q.config(text=" ")
        self.Label_9_R.config(background="red",text=str(axu[3]))
        self.Label_9_q.config(text=str(axu[0]))
        
        axu = self.resuelve(Q=axu[0],n1=texto1[7],n2=texto2[7])
        self.Label_9_R.config(background="snow")
        self.Label_9_q.config(text=" ")
        self.Label_8_R.config(background="red",text=str(axu[3]))
        self.Label_8_q.config(text=str(axu[0]))
        
        axu = self.resuelve(Q=axu[0],n1=texto1[6],n2=texto2[6])
        self.Label_8_R.config(background="snow")
        self.Label_8_q.config(text=" ")
        self.Label_7_R.config(background="red",text=str(axu[3]))
        self.Label_7_q.config(text=str(axu[0]))
        
        axu = self.resuelve(Q=axu[0],n1=texto1[5],n2=texto2[5])
        self.Label_7_R.config(background="snow")
        self.Label_7_q.config(text=" ")
        self.Label_6_R.config(background="red",text=str(axu[3]))
        self.Label_6_q.config(text=str(axu[0]))
        
        axu = self.resuelve(Q=axu[0],n1=texto1[4],n2=texto2[4])
        self.Label_6_R.config(background="snow")
        self.Label_6_q.config(text=" ")
        self.Label_5_R.config(background="red",text=str(axu[3]))
        self.Label_5_q.config(text=str(axu[0]))
        
        axu = self.resuelve(Q=axu[0],n1=texto1[3],n2=texto2[3])
        self.Label_5_R.config(background="snow")
        self.Label_5_q.config(text=" ")
        self.Label_4_R.config(background="red",text=str(axu[3]))
        self.Label_4_q.config(text=str(axu[0]))
        
        axu = self.resuelve(Q=axu[0],n1=texto1[2],n2=texto2[2])
        self.Label_4_R.config(background="snow")
        self.Label_4_q.config(text=" ")
        self.Label_3_R.config(background="red",text=str(axu[3]))
        self.Label_3_q.config(text=str(axu[0]))
        
        axu = self.resuelve(Q=axu[0],n1=texto1[1],n2=texto2[1])
        self.Label_3_R.config(background="snow")
        self.Label_3_q.config(text=" ")
        self.Label_2_R.config(background="red",text=str(axu[3]))
        self.Label_2_q.config(text=str(axu[0]))
        
        axu = self.resuelve(Q=axu[0],n1=texto1[0],n2=texto2[0])
        self.Label_2_R.config(background="snow")
        self.Label_2_q.config(text=" ")
        self.Label_1_R.config(background="red",text=str(axu[3]))
        self.Label_1_q.config(text=str(axu[0]))
        
        
        
        
    def resuelve(self,Q,n1,n2):
        if (Q == "q0" and n1 == "0" and n2 == "1"):
            axu  = ["q0", "0", "1","1",1]
            return axu
        elif (Q == "q0" and n1 == "1" and n2 == "0"):
            axu  = ["q0", "1", "0","1",1]
            return axu
        elif (Q == "q0" and n1 == "0" and n2 == "0"):
            axu  = ["q0", "0", "0","0",1]
            return axu
        elif (Q == "q0" and n1 == "1" and n2 == "1"):
            axu  = ["q1", "1", "1","0",1]
            return axu
        elif (Q == "q0" and n1 == "B" and n2 == "B"):
            axu  = ["q3", "B","B","B",-1]
            return axu
        elif (Q == "q1" and n1 == "0" and n2 == "0"):#6
            axu  = ["q0", "0", "0","1",1]
            return axu
        elif (Q == "q1" and n1 == "0" and n2 == "1"):
            axu  = ["q1", "0", "1","0",1]
            return axu
        elif (Q == "q1" and n1 == "1" and n2 == "0"):
            axu  = ["q1", "1", "0","0",1]
            return axu
        elif (Q == "q1" and n1 == "1" and n2 == "1"):
            axu  = ["q1", "1", "1","1",1]
            return axu
        elif (Q == "q1" and n1 == "B" and n2 == "B"):
            axu  = ["q3", "B", "B","1",-1]
            return axu
     
    #funcion para limitar la longitud de los numeros    
    def validar_longitud(self,text):
        if len(text) <= 10 and all(char in ['0', '1'] for char in text):
            return True
        else:
            return False
        
        
s = Suma()