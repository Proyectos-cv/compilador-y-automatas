class expresiones:
    def parse_expr(self,expr):
        tokens = expr.split()  
        self.lista =[]
        return self.parse_add_sub(tokens),self.lista

    def parse_add_sub(self,tokens):
        left_operand = self.parse_mul_div(tokens)
        result = left_operand
        
        while tokens and (tokens[0] == '+' or tokens[0] == '-'):
            operator = tokens.pop(0)
            right_operand = self.parse_mul_div(tokens)
            """ print (operator) """
            self.lista.append(operator)
            """ print (right_operand) """
        return result

    def parse_mul_div(self,tokens):
        left_operand = self.parse_atom(tokens)
        result = left_operand
        
        while tokens and (tokens[0] == '*' or tokens[0] == '/'):
            operator = tokens.pop(0)
            right_operand = self.parse_atom(tokens)
            """ print (operator) """
            self.lista.append(operator)
        return result

    def parse_atom(self,tokens):
        if tokens:
            partes = tokens[0].split('.')
            parte = tokens[0]
           
            token = tokens.pop(0)
            if token.isdigit():
                result = int(token)
                self.lista.append(result)
                """ print(f"Resultado parcial: {result}") """
                return result
            elif partes[0].isdigit() and partes[1].isdigit():
                result = float(token)
                self.lista.append(result)
                """ print(f"Resultado parcial: {result}") """
                return result
            elif parte[0] == "$" and parte[1:].islower():
                result = parte[0]+parte[1:]
                self.lista.append(result)
                """ print(f"Resultado parcial: {result}") """
                return result
            else:
                raise ValueError(f"Error: Token inesperado '{token}'")
        else:
            raise ValueError("Error: La expresión está incompleta")

    def inicio(self,expresion):
        igual = expresion.split(" ")
        expresion = " "
        for u in range (2,len(igual)):
            expresion = expresion + igual[u] + " "

        resultado,lista = expresiones().parse_expr(expresion)
        """ print(f"Resultado final de la expresión '{expresion}' es: {resultado}")
        print(lista) """
        lista_final = []
        conta = 0
        for i in range(0,len(lista)):
            conta = 0
            if lista[i] in ['+','-','/','*']:
                """ print (lista[i]) """
                if i>=3:
                    """ print(i) """
                    if lista[i-1] not in ['+','-','/','*'] and lista[i-2] not in ['+','-','/','*'] and lista[i-3] not in ['+','-','/','*']:
                        lista_final.append(lista[i-1])
                        lista_final.append(lista[i-2])
                        lista_final.append(lista[i])
                        lista_final.append(lista[i-3])
                    elif lista[i-1] not in ['+','-','/','*'] and lista[i-2] not in ['+','-','/','*']:
                        lista_final.append(lista[i-1])
                        lista_final.append(lista[i-2])
                        lista_final.append(lista[i])
                    elif lista[i-1] not in ['+','-','/','*']:
                        lista_final.append(lista[i-1])
                        lista_final.append(lista[i])
                    else:
                        lista_final.append(lista[i])
                else:
                    if i>=2:
                        if lista[i-1] not in ['+','-','/','*'] and lista[i-2] not in ['+','-','/','*']:
                            lista_final.append(lista[i-1])
                            lista_final.append(lista[i-2])
                            lista_final.append(lista[i])
                    elif i>=1:
                        if lista[i-1] not in ['+','-','/','*']:
                            lista_final.append(lista[i-1])
                            lista_final.append(lista[i])
                    else:
                        lista_final.append(lista[i])
            
        lista_final.append(igual[0])
        lista_final.append(igual[1])

        """ print("segundo resultado")
        print (lista_final)
        print (lista) """
        
        #return lista_final
    
        ##__________________pilas_________________________

        lista_aux = lista
        g_operadores = []
        g_operandos = []
        g_cadena = []
        i = -1
        cad = ""
        print ("lista",lista)
        while lista:
            """ print (lista)
            print (i) """
            operandos =[igual[0]]
            operadores = [igual[1]]
        
        
            i=i+1
            """ print ("lista",lista)
            print (i) """
            """ print (len(lista)) """
            if i == len(lista):
                i=0
            if lista[i] in ['+','-','/','*']:
                if i>=2 and i==len(lista)-1:
                    if lista[i-1] not in ['+','-','/','*'] and lista[i-2] not in ['+','-','/','*'] and lista[i] in ['+','-','/','*']:
                            operandos.append(lista[i-2])
                            operandos.append(lista[i-1])
                            
                            operadores.append(lista[i])
                            cade = str(lista[i-1]) + str(lista[i-2]) + str(lista[i])
                            cad = cad + cade
                            del lista[i]
                            del lista[i-1]
                            del lista[i-2]
                            g_cadena.append(cad)
                            g_operadores.append(operadores)
                            g_operandos.append(operandos)
                            i= 0
                elif i >=2:
                    if lista[0] in ['+','-','/','*']:
                        operadores.append(lista[0])
                        cade = str(lista[0])
                        cad = cad + cade
                        del lista[0]
                        g_cadena.append(cad)
                        g_operadores.append(operadores)
                        g_operandos.append(operandos)
                        i=0
                    elif lista[i-1] not in ['+','-','/','*'] and lista[i-2] not in ['+','-','/','*'] and lista[i-3] not in ['+','-','/','*']:
                        operandos.append(lista[i-3])
                        operandos.append(lista[i-2])
                        operandos.append(lista[i-1])
                        operadores.append(lista[i+1])
                        operadores.append(lista[i])
                        cade =  str(lista[i-1]) + str(lista[i-2]) + str(lista[i])
                        cad = cad + cade
                        #eliminar los elementos utilizados 
                        #del lista[i+1]
                        del lista[i]
                        del lista[i-1]
                        del lista[i-2]
                        """ print (lista)
                        print (operadores)
                        print(operandos) """
                        g_cadena.append(cad)
                        g_operadores.append(operadores)
                        g_operandos.append(operandos)
                        i = 0
                    elif lista[i-1] not in ['+','-','/','*'] and lista[i-2] not in ['+','-','/','*'] and lista[i+1] in ['+','-','/','*']:
                        operandos.append(lista[i-2])
                        operandos.append(lista[i-1])
                        operadores.append(lista[i+1])
                        operadores.append(lista[i])
                        cade = str(lista[i-1]) + str(lista[i-2]) + str(lista[i])
                        cad = cad + cade
                        del lista[i]
                        del lista[i-1]
                        del lista[i-2]
                        g_cadena.append(cad)
                        g_operadores.append(operadores)
                        g_operandos.append(operandos)
                        i= 0
                    elif lista[i-1] not in ['+','-','/','*'] and lista[i-2] not in ['+','-','/','*']:
                        operandos.append(lista[i-2])
                        operandos.append(lista[i-1])
                        operadores.append(lista[i])
                        cade = str(lista[i-1]) + str(lista[i-2]) + str(lista[i])
                        cad = cad + cade
                        del lista[i]
                        del lista[i-1]
                        del lista[i-2]
                        g_cadena.append(cad)
                        g_operadores.append(operadores)
                        g_operandos.append(operandos)
                        i= 0
                elif i>=1:
                    if lista[0] in ['+','-','/','*']:
                        operadores.append(lista[i])
                        cade = str(lista[i])
                        cad = cad + cade
                        del lista[0]
                        g_cadena.append(cad)
                        g_operadores.append(operadores)
                        g_operandos.append(operandos)
                        i=0
                    elif lista[i-1] not in ['+','-','/','*']:
                        operandos.append(lista[i-1])
                        operadores.append(lista[i])
                        cade = str(lista[i-1]) + str(lista[i])
                        cad = cad + cade
                        del lista[i]
                        del lista[i-1]
                        g_cadena.append(cad)
                        g_operadores.append(operadores)
                        g_operandos.append(operandos)
                        i= 0
                else:
                
                    operadores.append(lista[i])
                    cade = str(lista[i])
                    cad = cad + cade
                    del lista[i]
                    g_cadena.append(cad)
                    g_operadores.append(operadores)
                    g_operandos.append(operandos)
                    i=0
        """ g_cadena.append([igual[0]])
        g_cadena.append([igual[1]]) """
        print (g_operadores)
        print (g_operandos)

        fs= igual[0] + igual[1]
        cad = cad + fs
        g_cadena.append(cad)
        g_operadores.append([igual[1]])
        g_operandos.append([igual[0]])

        f_operadores = []
        f_operandos = []
        f_operadores = [''.join(map(str, sublist)) for sublist in g_operadores]
        f_operandos = [''.join(map(str, sublist)) for sublist in g_operandos]       




        print ("-------------------------------")
        print (g_cadena)
        print (f_operadores)
        print (f_operandos)
        return g_cadena,f_operadores,f_operandos




#expresion = "$x = 100 * 2 + 3 * 5"
#expresion = "$x = 30 + 5 * 5 + 10 - 4"

#expresion = "$x = 50 * 2 / 5 * 3 + 5"
#expresion = "$x = 100 * 2 - 5 - 10 + 6 / 3"
#expresion = "$x = 20 * 3 * 2 + 10 - 5"

#expresion = "$x = 2 + 3 * 5 - 12 / 2 + 80 - 13"
#expresion = "$x = 5 + 2 * 3 - 4"
#expresion = "$x = 5 * 2 + 3 * 4"
#expresion = "$x = 5 * 2 + 3 * 4 - 10 / 2 + 5"
#expresion = "$x = 5 * 2 + 3 * 4 - 10 / 2 + 5 - 10 * 2 + 3 * 4"
#expresiones().inicio(expresion)
""" expresion = ["$b = $f + $c ;","$d = $a + $m ;","$m = $f + $d ;"]
expresion = "$m = $f + $d ;"
expresiones().inicio(expresion) """


