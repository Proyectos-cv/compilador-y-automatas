
class sintactico():
    def analizar(self, tokens):
        cadena = []

        for sublista in tokens:
            cadena.extend(sublista[1])
        cadena.append("&")
        self.producciones = ["progama", "sentencia", "declaravar", "declaravar2", "tipodato", "complemento", "complemento2", "comentario"]

        self.produccion = ["programa","&"]
        self.arbol = []

        self.posicion = 0
        print (cadena)
        print("extension del arbol: ", ['n',self.posicion+1,self.arbol,self.produccion])
        if self.programa(cadena):
            print ("cadena aceptada")
        else:
            print ("cadena no aceptada")
    def programa(self, cadena):
        self.arbol.append(self.produccion[0])
        self.produccion = [" ¿ ", "sentencia", " ?", "&"]
        print("concordancia de simbolo: ", ['n',self.posicion+1,self.arbol,self.produccion])
        if cadena[self.posicion] == '¿':
            self.arbol.append(self.produccion[0])
            self.produccion.pop(0)
            print("expansion del arbol: ", ['n',self.posicion+1,self.arbol,self.produccion])
            if self.sentencia(cadena):
                self.posicion += 1
                if self.posicion < len (cadena):
                    print("concordancia de simbolo: ", ['n',self.posicion+1,cadena[:self.posicion+1]])
                    if cadena[self.posicion] == '?':
                        return True
                else:
                    return False
            else:
                return False
        else :
            return False
    
    def sentencia(self, cadena):
        if self.declaravar(cadena):
            return True
        elif self.declaravar2(cadena):
            return True
        elif self.comentario(cadena):
            self.posicion -= 1
            return True
        else:
            return False

        """ if self.declaravar(cadena) :
            return True
        else:
           if self.declaravar2(cadena) :
               return True
           else: 
                #return False

                if self.comentario(cadena) :
                    return True
                else:
                    return False """
           
    
    def comentario(self,cadena):

        if cadena[self.posicion] == "#":
            print("concordancia de simbolo: ", ['n',self.posicion+1,cadena[:self.posicion+1]])
            if self.posicion+2 < len(cadena):
                if cadena[self.posicion+1] == "?" and self.posicion+2 <len(cadena)-1:
                    return False      
                elif cadena[self.posicion+1] == "?":
                    return True
                else: 
                    if self.sentencia(cadena):
                        return True
                    else:
                        return False
        else:
            return False


    def declaravar2(self, cadena):
        self.posicion += 1
        valor = cadena[self.posicion]

        if self.tipodato(cadena):
            self.posicion += 1
            if self.complemento2(cadena):
                self.posicion += 1

                if cadena[self.posicion]== ";":
                    #return True
                    print("concordancia de simbolo: ", ['n',self.posicion+1,cadena[:self.posicion+1]])
                    if self.posicion+1 < len(cadena):
                        if cadena[self.posicion+1] == "?" and self.posicion+2 <len(cadena)-1:
                            return False 
                        elif cadena[self.posicion+1] == "?":
                            return True
                        else: 
                            if self.sentencia(cadena):
                                return True
                            else:
                                return False
                    else:
                        return True
                else:
                   
                    self.posicion -= 1
                    self.posicion -= 1
                    return False
            else:
                
                self.posicion -= 1
                return False
        else:
            
            return False       
    
    
    def declaravar(self, cadena):
        self.posicion += 1
        valor = cadena[self.posicion]
        self.arbol.append(self.produccion[0])
        self.produccion.pop(0)
        self.produccion.insert(0,"declaravar") 
        print ("ampliacion del arbol: ",['n',self.posicion+1,self.arbol,self.produccion])
        if self.tipodato(cadena):
            self.posicion += 1
            self.arbol.append(self.produccion[0])
            self.produccion.pop(0)
            self.produccion.insert(0,"declaravar") 
            print ("ampliacion del arbol: ",['n',self.posicion+1,self.arbol,self.produccion])
            if self.complemento(cadena):
                self.posicion += 1
                if cadena[self.posicion]== ";":
                    #return True
                    #print("concordancia de simbolo: ", ['n',self.posicion+1,cadena[:self.posicion+1]])
                    if self.posicion+1 < len(cadena):
                        if cadena[self.posicion+1] == "?" and self.posicion+2 <len(cadena)-1:
                            return False 
                        elif cadena[self.posicion+1] == "?":
                            return True
                        else: 
                            if self.sentencia(cadena):
                                return True
                            else:
                                return False
                    else:
                        
                        return True
                else: 
                    print("no concordancia de simbolo: ", ['r',self.posicion+1,cadena[:self.posicion+1]])
                    self.posicion -= 1
                    print("no concordancia de simbolo: ", ['r',self.posicion+1,cadena[:self.posicion+1]])
                    self.posicion -= 1
                    print("no concordancia de simbolo: ", ['r',self.posicion+1,cadena[:self.posicion+1]])
                    self.posicion -= 1
                    return False
            else:
                print("no concordancia de simbolo: ", ['r',self.posicion+1,cadena[:self.posicion+1]])
                self.posicion -= 1
                print("no concordancia de simbolo: ", ['r',self.posicion+1,cadena[:self.posicion+1]])
                self.posicion -= 1
                return False 
        else:
            print("no concordancia de simbolo: ", ['r',self.posicion+1,cadena[:self.posicion+1]])
            self.posicion -= 1
            return False    

    def tipodato(self, cadena):
        valor = cadena[self.posicion]
        if valor == 'INT' or valor == 'STR' or valor == 'FLT' or valor == 'CHR' or valor == 'BOL':
            print("concordancia de simbolo: ", ['n',self.posicion+1,cadena[:self.posicion+1]])
            return True
        else:
            return False

    def complemento(self, cadena):
        variable = cadena[self.posicion]
        if variable[0] == ":" and variable[1:].islower():
            print("concordancia de simbolo: ", ['n',self.posicion+1,cadena[:self.posicion+1]])
            return True
        else:
            return False
    def complemento2(self, cadena):
        variable = cadena[self.posicion]
        if variable[0] == ":" and variable[1:].islower():
            print("concordancia de simbolo: ", ['n',self.posicion+1,cadena[:self.posicion+1]])
            self.posicion +=1
            if cadena[self.posicion] == "=":
                print("concordancia de simbolo: ", ['n',self.posicion+1,cadena[:self.posicion+1]])
                self.posicion +=1
                if self.asignado(cadena):
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    def asignado (self,cadena):
        variable = cadena[self.posicion]
        if cadena[self.posicion] == '"':
            print("concordancia de simbolo: ", ['n',self.posicion+1,cadena[:self.posicion+1]])
            return True
        elif variable[0] == ":" and variable[1:].islower():
            print("concordancia de simbolo: ", ['n',self.posicion+1,cadena[:self.posicion+1]])
            return True
        elif cadena [self.posicion].isdigit():
            print("concordancia de simbolo: ", ['n',self.posicion+1,cadena[:self.posicion+1]])
            return True
        else:
            return False
        
        

        
