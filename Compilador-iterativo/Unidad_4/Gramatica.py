class Regla1:
        
    def manda(self,axu,posicion):
        if (axu == "Programa"):
            texto_cadena = ["End","}","Sentencias","{","Star"]
            return texto_cadena
            
            
        elif (axu == "Sentencias"):
            if (posicion == 1):
                texto_cadena = ["Sentencias","DeclaVar"]
                return texto_cadena
            elif(posicion == 2):
                texto_cadena = ["Sentencias","Comentario"]
                return texto_cadena
            elif(posicion == 3):
                texto_cadena = ["Sentencias","MensajePantalla"]
                return texto_cadena
            elif(posicion == 4):
                texto_cadena = ["Sentencias","Pedir"]
                return texto_cadena
            elif(posicion == 5):
                texto_cadena = ["Sentencias","Asignar"]
                return texto_cadena
            elif(posicion == 6):
                texto_cadena = ["DeclaVar"]
                return texto_cadena
            elif(posicion == 7):
                texto_cadena = ["Comentario"]
                return texto_cadena
            elif(posicion == 8):
                texto_cadena = ["MendajePantalla"]
                return texto_cadena
            elif(posicion == 9):
                texto_cadena = ["Pedir"]
                return texto_cadena
            elif(posicion == 10):
                texto_cadena = ["Asignar"]
                return texto_cadena
            
        elif (axu == "DeclaraVar"):
            if (posicion == 1):
                texto_cadena = [";","nomVar","tipoDato"]
                return texto_cadena
            elif(posicion == 2):
                texto_cadena = [";","nomVarMul","nomVar","tipoDato"]
                return texto_cadena
        
        elif (axu == "nomVarMul"):
            if (posicion == 1):
                texto_cadena = ["nomVar",","]
                return texto_cadena
            elif(posicion == 2):
                texto_cadena = ["nomVarMul",",","nomVar",","]
                return texto_cadena
        
        elif (axu == "tipoDato"):
            if (posicion == 1):
                texto_cadena = ["&int"]
                return texto_cadena
            elif(posicion == 2):
                texto_cadena = ["&float"]
                return texto_cadena
            elif(posicion == 3):
                texto_cadena = ["&chr"]
                return texto_cadena
            elif(posicion == 4):
                texto_cadena = ["&str"]
                return texto_cadena
            elif(posicion == 5):
                texto_cadena = ["&bool"]
                return texto_cadena
        
        elif (axu == "NomVar"):
            if (posicion == 1):
                texto_cadena = ["$letra"]
                return texto_cadena
            elif(posicion == 2):
                texto_cadena = ["letnum","$letra"]
                return texto_cadena
        
        elif (axu == "letra"):
            if (posicion == 1):
                texto_cadena = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r",]
                letras=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r",]
                return texto_cadena
        
        elif (axu == "letnum"):
            if (posicion == 1):
                texto_cadena = ["letra"]
                return texto_cadena
            elif(posicion == 2):
                texto_cadena = ["_"]
                return texto_cadena
            elif(posicion == 3):
                texto_cadena = ["num"]
                return texto_cadena
            elif(posicion == 4):
                texto_cadena = ["letra"]
                return texto_cadena
            elif(posicion == 5):
                texto_cadena = ["letnum","_"]
                return texto_cadena
            elif(posicion == 6):
                texto_cadena = ["letnum","num"]
                return texto_cadena
        elif (axu == "num"):
            if (posicion == 1):
                texto_cadena = ["0","1","2","3","4","5","6","7","8","9"]
                return texto_cadena
        
        elif (axu == "Comentario"):
            if (posicion == 1):
                texto_cadena = ["LoQueSea","#"]
                return texto_cadena
        elif (axu == "LoQueSea"):
            if (posicion == 1):
                texto_cadena = [None]
                return texto_cadena
        
        elif (axu == "Mensaje"):
            if (posicion == 1):
                texto_cadena = ["LoQueSea"]
                return texto_cadena
        
        elif (axu == "MensajePatalla"):
            if (posicion == 1):
                texto_cadena = [";",")","Imprimier","(","&print"]
                return texto_cadena
        
        elif (axu == "Imprimir"):
            if (posicion == 1):
                texto_cadena = ["imprime"]
                return texto_cadena
            elif (posicion == 2):
                texto_cadena = ["Imprimir",",","imprime"]
                return texto_cadena
        
        elif (axu == "imprime"):
            if (posicion == 1):
                texto_cadena = ["nomVar"]
                return texto_cadena
            elif (posicion == 2):
                texto_cadena = ['"',"Mensaje",'"']
                return texto_cadena
        
        elif (axu == "Pedir"):
            if (posicion == 1):
                texto_cadena = [";","nomVar","&read"]
                return texto_cadena
            elif (posicion == 2):
                texto_cadena = [";","nomVarMul","nomVar","&read"]
                return texto_cadena
        elif (axu == "Asignar"):
            if (posicion == 1):
                
                texto_cadena = ["Bandera","=","nomVar"]
                return texto_cadena
            elif(posicion == 2):
                texto_cadena = ["Entero","=","nomVar"]
                return texto_cadena
            elif(posicion == 3):
                texto_cadena = ["Decimal","=","nomVar"]
                return texto_cadena
            elif(posicion == 4):
                texto_cadena = ['"',"LoQueSea",'"',"=","nomVar"]
                return texto_cadena
            elif(posicion == 5):
                texto_cadena = ["Operacion","=","nomVar"]
                return texto_cadena
        elif (axu == "Bandera"):
            if (posicion == 1):
                texto_cadena = ["true"]
                return texto_cadena
            elif(posicion == 2):
                texto_cadena = ["false"]
                return texto_cadena
        elif (axu == "Entero"):
            if (posicion == 1):
                texto_cadena = ["num"]
                return texto_cadena
            elif(posicion == 2):
                texto_cadena = ["Entero","num"]
                return texto_cadena
        elif (axu == "Decimal"):
            if (posicion == 1):
                texto_cadena = ["Entero",".","Entero"]
                return texto_cadena
        elif (axu == "Operacion"):
            if (posicion == 1):
                texto_cadena = ["operando","operador","operando"]
                return texto_cadena
            elif(posicion == 2):
                texto_cadena = ["Continuacion","operando","operador","operando"]
                return texto_cadena
        
        elif (axu == "Continuacion"):
            if (posicion == 1):
                texto_cadena = ["operador","operando"]
                return texto_cadena
            elif(posicion == 2):
                texto_cadena = ["Continuacion","operando","operador"]
                return texto_cadena
        elif (axu == "Operando"):
            if (posicion == 1):
                texto_cadena = ["Entero"]
                return texto_cadena
            elif(posicion == 2):
                texto_cadena = ["Decimal"]
                return texto_cadena
            elif(posicion == 3):
                texto_cadena = ["nomVar"]
                return texto_cadena
        elif (axu == "Operador"):
            if (posicion == 1):
                texto_cadena = ["+"]
                return texto_cadena
            elif(posicion == 2):
                texto_cadena = ["-"]
                return texto_cadena
            elif(posicion == 3):
                texto_cadena = ["*"]
                return texto_cadena
            elif(posicion == 4):
                texto_cadena = ["/"]
                return texto_cadena
            
s = Regla1()
l=s.manda("letra",1)
print(l)