from tkinter import *
from tkinter import ttk
from tkinter.font import Font

from tkinter import scrolledtext as st
from tkinter import filedialog as fd
from tkinter import messagebox as mb


class Semantico:
    def proces(self,tokens):
        self.variables=[]
        self.variablesSemanticas=[]
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
            token=k.split(" ")
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
        print (self.variables)
        print ( self.variablesSemanticas)
        if self.variables== self.variablesSemanticas:
            return self.variables,1         
        else:
            mb.showinfo("Información", "Se ah modificado el código, debe correr el análisis léxico nuevamente")
            return self.variables,0
        
    def identificarVariables(self,variables):
        variablesSemanticas=[]
        operaciones=[]
        varEnteros=[]
        varEnterosValores=[]
        varFlotantes=[]
        varFlotantesValores=[]
        varCadenas=[]
        varCadenasValores=[]
        varCaracteres=[]
        varCaracteresValores=[]
        varBooleanos=[]
        varBooleanosValores=[]
        erroresDuplicados=[]
        erroresTipoDato=[] 
        errorNoDeclaradas=[]  
        self.archivo = open("axu.txt","r") #abro el archivo en lectura
        lineas=self.archivo.read() #leo el archivo
        count=1
        codigo_separado=lineas.split("\n")
        for i in (codigo_separado):
            token=i.split(" ")
            if token[0].startswith("&"):
                variablesSemanticas.append(i)
        #print(variablesSemanticas)
        for i in variablesSemanticas:
            token=i.split(" ")
            if token[0]==("&int"):
                for j in token:
                    if j.startswith("$"):
                        if j in varEnteros or j in varFlotantes or j in varCadenas or j in varCaracteres or j in varBooleanos:
                            erroresDuplicados.append(j)
                        else:
                            varEnteros.append(j)
                            varEnterosValores.append(0)
            elif token[0]==("&float"):
                for j in token:
                    if j.startswith("$"):
                        if j in varEnteros or j in varFlotantes or j in varCadenas or j in varCaracteres or j in varBooleanos:
                            erroresDuplicados.append(j)
                        else:
                            varFlotantes.append(j)
                            varFlotantesValores.append(0)
            elif token[0]==("&str"):
                for j in token:
                    if j.startswith("$"):
                        if j in varEnteros or j in varFlotantes or j in varCadenas or j in varCaracteres or j in varBooleanos:
                            erroresDuplicados.append(j)
                        else:
                            varCadenas.append(j)
                            varCadenasValores.append("")
            elif token[0]==("&chr"):
                for j in token:
                    if j.startswith("$"):
                        if j in varEnteros or j in varFlotantes or j in varCadenas or j in varCaracteres or j in varBooleanos:
                            erroresDuplicados.append(j)
                        else:
                            varCaracteres.append(j)
                            varCaracteresValores.append("")
            elif token[0]==("&bool"):
                for j in token:
                    if j.startswith("$"):
                        if j in varEnteros or j in varFlotantes or j in varCadenas or j in varCaracteres or j in varBooleanos:
                            erroresDuplicados.append(j)
                        else:
                            varBooleanos.append(j)
                            varBooleanosValores.append("")
            else:
                print("No es una variable")
        print (varEnteros)
        print (varFlotantes)
        print (varCadenas)
        print (varCaracteres)
        print (varBooleanos)
        print (erroresDuplicados)
        for i in (codigo_separado):
            token=i.split(" ")
            if len(token)>1:
                if token[1].startswith("="):
                    operaciones.append(i)
        print (operaciones)
        for i in range(len(operaciones)):
            token=operaciones[i].split(" ")
            print (len(token))
            if len(token)==4:
                print(token[0],token[1],token[2])
                if token[0].startswith("$"):
                    
                    #Prueba los valores de las variables enteras 
                    if token[0] in varEnteros:
                        if token[2].startswith("$"):
                            if token[2] in varEnteros:
                                varEnterosValores[varEnteros.index(token[0])]=token[2]
                            elif token[2] not in varFlotantes and token[2] not in varEnteros and token[2] not in varCadenas and token[2] not in varCaracteres and token[2] not in varBooleanos:
                                errorNoDeclaradas.append(token)
                            else:
                                erroresTipoDato.append(token)
                        else:
                            try:
                                entero=int(token[2])
                                varEnterosValores[varEnteros.index(token[0])]=token[2]
                            except:
                                print ("Error1",token[0])
                                erroresTipoDato.append(token)
                                
                    #prueba los valores de las variables flotantes
                    elif token[0] in varFlotantes:
                        if token[2].startswith("$"):
                            
                            if token[2] in varFlotantes or token[2] in varEnteros:
                                varFlotantesValores[varFlotantes.index(token[0])]=token[2]
                            elif token[2] not in varFlotantes and token[2] not in varEnteros and token[2] not in varCadenas and token[2] not in varCaracteres and token[2] not in varBooleanos:
                                errorNoDeclaradas.append(token)
                            else:
                                erroresTipoDato.append(token)
                        else:
                            try:
                                flotante=float(token[2])
                                varFlotantesValores[varFlotantes.index(token[0])]=token[2]
                            except:
                                print ("Error1",token[0])
                                erroresTipoDato.append(token)
                                
                    elif token[0] in varCadenas:
                        if token[2].startswith("$"):
                            if token[2] in varCadenas or token[2] in varCaracteres:
                                varCadenasValores[varCadenas.index(token[0])]=token[2]
                            elif token[2] not in varFlotantes and token[2] not in varEnteros and token[2] not in varCadenas and token[2] not in varCaracteres and token[2] not in varBooleanos:
                                errorNoDeclaradas.append(token)
                            else:
                                erroresTipoDato.append(token)
                        elif token[2].startswith('"') and token[2].endswith('"'):
                            varCadenasValores[varCadenas.index(token[0])]=token[2]
                        else:
                            erroresTipoDato.append(token)
                            
                    elif token[0] in varCaracteres:
                        if token [2].startswith("$"):
                            if token[2] in varCaracteres:
                                varCaracteresValores[varCaracteres.index(token[0])]=token[2]
                            elif token[2] not in varFlotantes and token[2] not in varEnteros and token[2] not in varCadenas and token[2] not in varCaracteres and token[2] not in varBooleanos:
                                errorNoDeclaradas.append(token)
                            else:
                                erroresTipoDato.append(token)
                        elif token[2].startswith('"') and token[2].endswith('"') and len(token[2])==3:
                            varCaracteresValores[varCaracteres.index(token[0])]=token[2]
                        else:
                            erroresTipoDato.append(token)
                    elif token[0] in varBooleanos:
                        if token[2]=="true" or token[2]=="false":
                            varBooleanosValores[varBooleanos.index(token[0])]=token[2]
                        else:
                            erroresTipoDato.append(token)
                    else:
                        errorNoDeclaradas.append(token)
            else:
                print ("Soy una ecuacion")
                print (token)
                bandint=False
                ecuacion=""
                if token[0] in varEnteros:
                    for j in range(1,len(token)):
                        print (token[j])
                        if token[j].startswith("$"):
                            if token[j] in varEnteros:
                                ecuacion=ecuacion+token[j]
                            elif token[j] not in varFlotantes and token[j] not in varEnteros and token[j] not in varCadenas and token[j] not in varCaracteres and token[j] not in varBooleanos and token[j] not in varEnteros:
                                print (token[j])
                                errorNoDeclaradas.append(token)
                                break
                            else:
                                print (token[j])
                                erroresTipoDato.append(token)
                                break
                        elif token[j] == "+" or token[j] == "-" or token[j] == "*" or token[j] == "/" or token[j]=="=" or token[j]==";" :
                            print ("operador int")
                            ecuacion=ecuacion+token[j]
                        else:
                            try:
                                entero=int(token[j])
                                ecuacion=ecuacion+token[j]
                            except:
                                print ("Error1",token[j])
                                erroresTipoDato.append(token)
                                break
                if ecuacion!="":
                    varEnterosValores[varEnteros.index(token[0])]=ecuacion
                ecuacion=""
                if token[0] in varFlotantes:
                    for j in range(1,len(token)):
                        print (token[j])
                        if token[j].startswith("$"):
                            if token[j] in varEnteros or token[j] in varFlotantes:
                                ecuacion=ecuacion+token[j]
                            elif token[j] not in varFlotantes and token[j] not in varEnteros and token[j] not in varCadenas and token[j] not in varCaracteres and token[j] not in varBooleanos and token[j] not in varEnteros:
                                print (token[j])
                                errorNoDeclaradas.append(token)
                                break
                            else:
                                print (token[j])
                                erroresTipoDato.append(token)
                                break
                        elif token[j] == "+" or token[j] == "-" or token[j] == "*" or token[j] == "/" or token[j]=="=" or token[j]==";" :
                            print ("operador float")
                            ecuacion=ecuacion+token[j]
                        else:
                            try:
                                flotante=float(token[j])
                                ecuacion=ecuacion+token[j]
                            except:
                                print ("Error2",token[0])
                                erroresTipoDato.append(token)
                if ecuacion!="":
                    varFlotantesValores[varFlotantes.index(token[0])]=ecuacion
                if token[0] in varCadenas or token[0] in varCaracteres or token[0] in varBooleanos:
                    erroresTipoDato.append(token)
                if token[0] not in varFlotantes and token[0] not in varEnteros and token[0] not in varCadenas and token[0] not in varCaracteres and token[0] not in varBooleanos and token[0] not in varEnteros:
                    errorNoDeclaradas.append(token)
        print (varEnteros)
        print (varFlotantes)
        print ("tipo de dato")
        print (erroresTipoDato) # tipo de dato
        print ("no declaradas")
        print (errorNoDeclaradas) # no declaradas
        print ("duplicados")
        print (erroresDuplicados)

        return erroresDuplicados, errorNoDeclaradas, erroresTipoDato