expresion = "$z = $a + $b * 10 - 7 * 4 ;"
exp=expresion.split(" ")
import os

class prueba:
    def __init__(self):
        self.first = ['*', '/']
        self.second = ['+', '-']
    def jerarquía(self, operacion):
            #* Dividir la operación en tokens
            operation_tokens = operacion.split(' ')
            jerarquías = []
            print (operation_tokens)

            lista_resultado=[]
            lista_op=[]
            lista_nv=[]
            lista_resultado.append("lda "+operation_tokens[0]+ " ;")
            operation_tokens.pop(1)
            operation_tokens.pop(0)
            print (operation_tokens)

            ban=False
            conta=0
            
            '''lista_resultado.append("lda "+operation_tokens[i+2]+ " ;")
            lista_resultado.append("mul "+operation_tokens[i]+ " ;")
            lista_resultado.append("sto "+operation_tokens[i+2]+ " ;")'''
            while ban==False or conta>10:
                ban_string=False
                for i in range(len(operation_tokens)):
                    print (len(operation_tokens))
                    try:
                        float(operation_tokens[i])
                        ban_string=True
                    except ValueError:
                        ban_string=False
                    if len(operation_tokens)-1>i+1:
                        print (operation_tokens[i])
                        if ban_string==False and operation_tokens[i].startswith("$") and operation_tokens[i+1] not in self.first:
                            print ("entro 1")
                            lista_resultado.append("lod "+operation_tokens[i]+ " ;")
                            operation_tokens.pop(i)
                            if len(lista_op)>0:
                                if lista_op[0]=="+":
                                    lista_resultado.append("adi ;")
                                else:
                                    lista_resultado.append("sbi ;")
                                lista_op.pop(0)
                            break                            
                        elif ban_string and operation_tokens[i+1] not in self.first:
                            print ("entro 2")
                            lista_resultado.append("ldc "+operation_tokens[i]+ " ;")
                            operation_tokens.pop(i)
                            if len(lista_op)>0:
                                if lista_op[0]=="+":
                                    lista_resultado.append("adi ;")
                                else:
                                    lista_resultado.append("sbi ;")
                                lista_op.pop(0)
                            break
                        elif ban_string==True and operation_tokens[i+1] in self.first:
                            print ("entro 3")
                            lista_resultado.append("ldc "+operation_tokens[i]+ " ;")
                            if operation_tokens[i+2].startswith("$"):
                                lista_resultado.append("lod "+operation_tokens[i+2]+ " ;")
                            else:
                                lista_resultado.append("ldc "+operation_tokens[i+2]+ " ;")
                            if operation_tokens[i+1]=="*":
                                lista_resultado.append("mpi ;")
                            else:
                                lista_resultado.append("div ;")
                            operation_tokens.pop(i)
                            operation_tokens.pop(i)
                            operation_tokens.pop(i)
                            break  
                        elif ban_string==False and operation_tokens[i].startswith("$") and operation_tokens[i+1] in self.first:
                            print ("entro 4")
                            lista_resultado.append("lod "+operation_tokens[i]+ " ;")
                            if operation_tokens[i+2].startswith("$"):
                                lista_resultado.append("lod "+operation_tokens[i+2]+ " ;")
                            else:
                                lista_resultado.append("ldc "+operation_tokens[i+2]+ " ;")
                            if operation_tokens[i+1]=="*":
                                lista_resultado.append("mpi ;")
                            else:
                                lista_resultado.append("div ;")
                            operation_tokens.pop(i)
                            operation_tokens.pop(i)
                            operation_tokens.pop(i)
                            break                  
                                    
                        elif operation_tokens[i] in self.second and len(lista_op)==0:
                            print ("entro 5")
                            lista_op.append(operation_tokens[i])
                            operation_tokens.pop(i)                            
                            break
                        elif operation_tokens[i] in self.second and len(lista_op)>0:
                            print ("entro 6")
                            if lista_op[0]=="+":
                                lista_resultado.append("adi ;")
                            else:
                                lista_resultado.append("sbi ;")
                            lista_op.pop(0)
                            lista_op.append(operation_tokens[i])
                            operation_tokens.pop(i)                            
                            break
                        elif operation_tokens[i] in self.first:
                            print ("entro 7")                            
                            if operation_tokens[i+2].startswith("$"):
                                lista_resultado.append("lod "+operation_tokens[i+1]+ " ;")
                            else:
                                lista_resultado.append("ldc "+operation_tokens[i+1]+ " ;")
                            if operation_tokens[i]=="*":
                                lista_resultado.append("mpi ;")
                            else:
                                lista_resultado.append("div ;")                                
                            operation_tokens.pop(i)
                            operation_tokens.pop(i)
                            break
                    elif len(operation_tokens)==2 and len(lista_op)>0:
                        if operation_tokens[i].startswith("$"):
                            print ("entro 11")
                            lista_resultado.append("lod "+operation_tokens[i]+ " ;")
                            operation_tokens.pop(i)
                            if len(lista_op)>0:
                                if lista_op[0]=="+":
                                    lista_resultado.append("adi ;")
                                else:
                                    lista_resultado.append("sbi ;")
                                lista_op.pop(0)
                            break                            
                        else:
                            print ("entro 21")
                            lista_resultado.append("ldc "+operation_tokens[i]+ " ;")
                            operation_tokens.pop(i)
                            if len(lista_op)>0:
                                if lista_op[0]=="+":
                                    lista_resultado.append("adi ;")
                                else:
                                    lista_resultado.append("sbi ;")
                                lista_op.pop(0)
                            break
                    elif operation_tokens[0]==";" and len(lista_op)>0:
                        print ("entro 8")
                        if lista_op[0]=="+":
                            lista_resultado.append("adi ;")
                        else:
                            lista_resultado.append("sbi ;")
                        lista_op.pop(0)
                        ban=True
                    else:
                        ban=True
                        
                        
                            
                        
                conta+=1
                print (conta, operation_tokens)
                print (lista_resultado)
            lista_resultado.append("sto ;")
            print (lista_nv)
            print (lista_op)
            print (operation_tokens)
            print (lista_resultado)
                    
            
                    
                    

            
            
if __name__ == "__main__":
    prueba = prueba()
    #expresion = "$x = 20 * 3 * 2 + 10 - 5 ;"
    #expresion = "$z = 29 - 4 * 2 * 5 ;"
    #expresion = "$z = $a + $b * 10 - 7 * 4 ;"
    #expresion = "$z = 78 * 2 + 45 - 13 / 44 ;"
    expresion = "$a = 67 + 2 * 4 / 2 + 12 * 2 ;"
    #operacion = "$b = $a * $b * $c * 10 - 12 * 4;"
    prueba.jerarquía(expresion)

