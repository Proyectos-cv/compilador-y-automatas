from tkinter import *
from tkinter import ttk
from tkinter.font import Font

from tkinter import scrolledtext as st
from tkinter import filedialog as fd
from tkinter import messagebox as mb




class Lex:
    def __init__(self,lista):
        print ("Lexico")
        
        #lista.insert(END,"Hola")
        #self.Tabla_()
        self.listaOperadores=['+','-','*','/','=']
        self.listaSignos=[',',')','(','{','}','_',';','#','"']
        self.listaplabrasreservadas=["&int","&float","&chr","&str","&bool","&Start","&End","&print","&read"]
        self.variables=[]
        self.valorVariables=[]
        self.tablaTokens=[]
        self.tablaTipo=[]
        self.tablaDeclara=[]
        self.tablaReferencia=[]
        self.tablaReferencia2=[]
        self.tablaErrores=[]    
        self.proces()
    def proces(self):
        self.archivo = open("axu.txt","r") #abro el archivo en lectura
        lineas=self.archivo.read() #leo el archivo
        count=1
        codigo_separado=lineas.split("\n") #separo el codigo en lineas
        listaNumeros=[]
        listaLineas=[]
        banComentario1=False
        banComentario2=False
        #print(len (codigo_separado))
        for k in codigo_separado:
            listaNumeros.append(count)
            listaLineas.append(k)
            print("Linea",count,k)
            
            token=k.split(" ")
            print (token)
            if count==len(codigo_separado)-1:
                    print("Fin de archivo")
                    break
            else:
                for j in token:
                    banTabla=False
                    banIdentificador=False
                    banOperador=False
                    banCaracter=False
                    banPReservada=False
                    banComentario2=False
                    print ("Token",j)
                    tokens=j
                    if tokens=='':
                        break
                    elif tokens[0].startswith('$'): #verifica si es una variable
                        valid=self.verificacionCadena(j)
                        if valid==True:
                            banTabla=True
                            banIdentificador=True
                            self.variables.append(j)
                            print("Variable")
                            
                        else:
                            print("Error")
                            self.tablaErrores.append("Error de léxico! en línea "+str(count)+" en la variable "+j)
                            
                    elif tokens[0].startswith('&'):#verifica si es una palabra reservada y si esta bien escrita
                        if tokens in self.listaplabrasreservadas: 
                            print("Palabra reservada")
                            banTabla=True
                            banPReservada=True
                        else :
                            print("Error")
                            self.tablaErrores.append("Error de léxico! en línea "+str(count)+" en la palabra reservada "+j)
                            
                            
                    #elif tokens=='Start':
                    #    print ("Inicio de programa")
                    #elif tokens=='}End':
                    #    print("Fin de programa")
                    
                    
                    elif tokens[0].isdigit(): #verifica si es un numero
                        bannum=self.verificacionNumero(tokens)
                        if bannum=="decimal" or bannum=="entero":
                            self.valorVariables.append(tokens)
                            banTabla=True
                            banCaracter=True
                            print("Numero")
                        else:
                            print("Error de numero")
                            self.tablaErrores.append("Error de léxico! en línea "+str(count)+" en el número"+j)
                            
                            
                    #elif tokens[0] == "(":
                    #    print("inicio area de imprecion")
                    #    banComentario1 = True
                    #elif tokens[0] == ")":
                    #    print("finalizo area de imprecion")
                    #    banComentario1 = True
                        
                    elif tokens[0] in self.listaSignos: #valida simbolos aceptados
                        print("Simbolo aceptado")
                        banTabla=True
                        banCaracter=True
                        
                        
                    elif (tokens[0] in self.listaOperadores and len(tokens)<=1): #valida operadores aceptados
                        print("Operador")
                        print(len(tokens))
                        banTabla=True
                        banOperador=True
                        
                        
                    elif tokens[0]=="#": #valida comentarios
                        print("Comentario")
                        banTabla=True
                        banCaracter=True
                        banComentario2=True
                    
                    elif tokens[0]=='"': #valida cadenas
                        banTabla=True
                        print (banComentario1)
                        if tokens.endswith('"') and banComentario1==True:
                            print("Cadena")
                        else:
                            print("Error")                    
                    else:
                        print("Error")
                        self.tablaErrores.append("Error de léxico! en línea "+str(count)+" en el token"+j+" No es un token valido en el lenguaje") 
                    #print("Tokens: ",tokens)
                    ubicacion=0
                    print(banIdentificador,banOperador,banCaracter,banPReservada,banTabla)
                    if (banTabla==True and banIdentificador==True):
                        self.tablaTokens.append(tokens)
                        self.tablaTipo.append("Identificador")
                        self.tablaDeclara.append("Local")
                        self.tablaReferencia.append(str(count))
                    elif(banTabla==True and banOperador==True):
                        self.tablaTokens.append(tokens)
                        self.tablaTipo.append("Operador")
                        self.tablaDeclara.append("Local")
                        self.tablaReferencia.append(str(count))
                    elif (banCaracter==True and banTabla==True):
                        if tokens[0] == '#':
                            self.tablaTokens.append("#")
                            self.tablaTipo.append("Caracter")
                            self.tablaDeclara.append("Local")
                            self.tablaReferencia.append(str(count))
                        elif tokens[0] == '"':
                            self.tablaTokens.append('"')
                            self.tablaTipo.append("Caracter")
                            self.tablaDeclara.append("Local")
                            self.tablaReferencia.append(str(count))
                            self.tablaTokens.append('"')
                            self.tablaTipo.append("Caracter")
                            self.tablaDeclara.append("Local")
                            self.tablaReferencia.append(str(count))
                        else:    
                            self.tablaTokens.append(tokens)
                            self.tablaTipo.append("Caracter")
                            self.tablaDeclara.append("Local")
                            self.tablaReferencia.append(str(count))
                    elif (banPReservada==True and banTabla==True):
                        self.tablaTokens.append(tokens)
                        self.tablaTipo.append("Palabra reservada")
                        self.tablaDeclara.append("Local")
                        self.tablaReferencia.append(str(count))                                                        
            count+=1            
        print("Variables",self.variables)
        #print(self.tablaTokens)
        #print(self.tablaTipo)
        #print(self.tablaDeclara)
        #print(self.tablaReferencia)
        #print(self.tablaErrores)
        mostrarToken=[]
        mostrarTipo=[]
        mostrarDeclara=[]
        mostrarReferencia=[]
        for i in range(len(self.tablaTokens)):
            #print (self.tablaTokens[i],self.tablaTipo[i],self.tablaDeclara[i],self.tablaReferencia[i])
            if self.tablaTokens[i] in mostrarToken:
                s=mostrarToken.index(self.tablaTokens[i])
                mostrarReferencia[s]+=" , "+str(self.tablaReferencia[i])
            else:
                mostrarToken.append(self.tablaTokens[i])
                mostrarTipo.append(self.tablaTipo[i])
                mostrarDeclara.append(self.tablaDeclara[i])
                mostrarReferencia.append(self.tablaReferencia[i])
        for i in range(len(mostrarToken)):
            print (mostrarToken[i],mostrarTipo[i],mostrarDeclara[i],mostrarReferencia[i])
        print (mostrarToken)
        for i in self.tablaErrores:
            print(i)
        self.ventanaTabla(mostrarToken,mostrarTipo,mostrarDeclara,mostrarReferencia,self.tablaErrores)
    
    def ventanaTabla(self,Tokens,tipo,declara,referencia,errores):
       #hazme una ventana para mostrar las ñistas que mande
       #hasme una ventana para mostrar las listas que mande
       
       ventanaTabla = Toplevel()
       ventanaTabla.title("Tabla de tokens")
       ventanaTabla.geometry("1000x400")
       ventanaTabla.configure(background="wheat1", bd="10", relief="groove")
       tablaMostrar=ttk.Treeview(ventanaTabla,columns=("Tokens","Tipo","Declara","Referencia"))
       tablaMostrar.heading("#0",text="No.")
       tablaMostrar.heading("Tokens",text="Tokens")
       tablaMostrar.heading("Tipo",text="Tipo")
       tablaMostrar.heading("Declara",text="Declara")
       tablaMostrar.heading("Referencia",text="Referencia")
       tablaMostrar.insert("",0,text="1",values=(Tokens[0],tipo[0],declara[0],referencia[0]))       
       for i in range(1,len(Tokens)):
           tablaMostrar.insert("",i,text=str(i+1),values=(Tokens[i],tipo[i],declara[i],referencia[i]))
       tablaMostrar.pack()
       lista = Listbox(width = 200,height=5,font=Font(family="Sans Serif", size=10))        
       lista.place(x=450,y=550)
       lista.delete(0,END)
       for i in errores:
           lista.insert(END,i)
       ventanaTabla.mainloop()      
    
    def verificacionCadena(self,cadena):
        if not cadena.startswith('$'): #comprueba que inicie con $
            #print ("La cadena no empieza con $")
            return False
        if not cadena[1].isalpha(): #comprueba que la segunda posicion sea una letra
            #print ("La cadena no empieza con una letra")
            return False
        for caracter in cadena[2:]: #comprueba que los caracteres restantes sean letras, numeros o _
            if not (caracter.isalpha() or caracter.isdigit() or caracter=='_'):
                #print ("La cadena contiene caracteres no permitidos")
                return False
        #print ("La cadena es correcta")
        return True
                
    
    def verificacionNumero(self,cadena):
        try:
            float(cadena)
        except ValueError:
            return "No es un número"
        else:
            if "." in cadena:
                return "decimal"
            else:
                return "entero"

    
    
    
    
