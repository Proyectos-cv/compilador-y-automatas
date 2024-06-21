class triplo:
    def evaluate_expression(self,expression):
        operators = {'+': 1, '-': 1, '*': 2, '/': 2}
        output = []
        operator_stack = []
        lista_completa = []
        producciones = []
        operadores = []
        def apply_operator():
            
            print (operator_stack)
            lista_completa.append(operator_stack[-1])
            operator = operator_stack.pop()
            print(output)
            lista_completa.append(output[-1])
            lista_completa.append(output[-2])
            right = output.pop()
            left = output.pop()
            output.append(str(left) + operator[-1] + str(right))
            producciones.append(str(left) + operator[-1] + str(right))

        i = 0
        while i < len(expression):
            if expression[i].isdigit():
                j = i
                while j < len(expression) and (expression[j].isdigit() or expression[j] == '.'):
                    j += 1
                output.append(float(expression[i:j]))
                i = j
            elif expression[i] in operators:
                while (operator_stack and operator_stack[-1] in operators and
                    operators[operator_stack[-1]] >= operators[expression[i]]):
                    apply_operator()
                operator_stack.append(expression[i])
                operadores.append(expression[i])
                i += 1
            elif expression[i] == "$":
                print("es una variable")
                ban= True
                cadena = ""
                while ban:
                    print("entro al while")
                    if i+1 > len(expression):
                        ban = False
                    elif expression[i].islower() or expression[i] == "$":
                        cadena = cadena + expression[i]
                        i=i+1
                    else:
                        ban=False
                output.append(cadena)
            elif expression[i] == '(':
                operator_stack.append(expression[i])
                i += 1
            elif expression[i] == ')':
                while operator_stack[-1] != '(':
                    apply_operator()
                print(operator_stack)
                operator_stack.pop()
                i += 1
            else:
                i += 1

        while operator_stack:
            apply_operator()
        return output[0],operadores,lista_completa,producciones

    def inicio(self,expresion):
        resultado, operadores,lista_completa,producciones = self.evaluate_expression(expresion)
        print(f"Resultado de la expresión '{expresion}' es: {resultado}")

        aux_operadores = []

        for h in range(0, len (operadores)):
            if operadores[h] == "*" or operadores[h] == "/":
                aux_operadores.append(operadores[h])       

        for h in range(0, len (operadores)):
            if operadores[h] == "+" or operadores[h] == "-":
                aux_operadores.append(operadores[h])
            
        arreglo = []
        tabla = []
        for m in range(0, len(aux_operadores)):
            band = True
            conta =0
            columna= []
            while band:
                if lista_completa[conta] == aux_operadores[m]:
                    band = False
                    columna.append(lista_completa[conta])
                    columna.append(lista_completa[conta+2])
                    columna.append(lista_completa[conta+1])
                    arreglo.append(str(lista_completa[conta+2]) + str(lista_completa[conta]) + str(lista_completa[conta+1]))
                    tabla.append(columna)
                    lista_completa.pop(conta)
                else:
                    conta = conta + 1

        for t in range(0,len(tabla)):
            for c in range(0,len(columna)):
                if tabla[t][c] in arreglo:
                    tabla [t][c] = "["+str(arreglo.index(tabla[t][c]))+"]"

        igual = expresion.split(" ")
        print(igual)
        ultima = []
        ultima.append(igual[1])
        ultima.append(igual[0])
        ultima.append("["+str(len(arreglo)-1)+"]")
        tabla.append(ultima)

        for i, lista in enumerate(tabla):
            lista.insert(0, f'[{i}]')
        print (tabla)
        return tabla

""" expresion = "$x = 2 + 3 - 1 * 2"
triplo().inicio(expresion) """