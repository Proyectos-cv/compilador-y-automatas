
class expresiones:
    def parse_expr(self,expr):
        tokens = expr.split()  # Divide la cadena de entrada en tokens (por ejemplo, "2 + 3" se convierte en ['2', '+', '3'])
        self.lista =[]
        return self.parse_add_sub(tokens)

    def parse_add_sub(self,tokens):
        left_operand = self.parse_mul_div(tokens)
        result = left_operand
        
        while tokens and (tokens[0] == '+' or tokens[0] == '-'):
            operator = tokens.pop(0)
            right_operand = self.parse_mul_div(tokens)
            print (operator)
            self.lista.append(operator)
            print (right_operand)
            if operator == '+':
                result += right_operand
            elif operator == '-':
                result -= right_operand
            else:
                print("entro aqui")
            self.lista.append(result)
            print(f"Resultado parcial: {result}")
            print (self.lista)
        
        return result

    def parse_mul_div(self,tokens):
        left_operand = self.parse_atom(tokens)
        result = left_operand
        
        while tokens and (tokens[0] == '*' or tokens[0] == '/'):
            operator = tokens.pop(0)
            right_operand = self.parse_atom(tokens)
            print (operator)
            self.lista.append(operator)
            print (right_operand)
            if operator == '*':
                result *= right_operand
            elif operator == '/':
                result /= right_operand
            self.lista.append(result)
            print(f"Resultado parcial: {result}")
            print (self.lista)
        return result

    def parse_atom(self,tokens):
        if tokens:
            partes = tokens[0].split('.')
            parte = tokens[0]
            #partes = tokens.split('.')
            token = tokens.pop(0)
            if token.isdigit():
                result = int(token)
                self.lista.append(result)
                print(f"Resultado parcial: {result}")
                return result
            elif partes[0].isdigit() and partes[1].isdigit():
                result = float(token)
                self.lista.append(result)
                print(f"Resultado parcial: {result}")
                return result
            elif parte[0] == ":" and parte[1:].islower():
                result = 0
                self.lista.append(result)
                print(f"Resultado parcial: {result}")
                return result
            else:
                raise ValueError(f"Error: Token inesperado '{token}'")
        else:
            raise ValueError("Error: La expresión está incompleta")

    def inicio (expresion):
        # Ejemplo de uso
        """ expresion = ["$s = 2 + 1 + 4 * 1.1 + 2",
                     "$r = 3 + $a",
                     "$s = 2 + 1 + 4 * 1.1 * 2",
                     "$s = 2 + 1 + 4 * 1.1 + $f", 
                     "$f = $f", 
                     "$g = 4 + 5",
                     "&int d ;",
                     "#comentario"] """
       # expresion = "$s = 2 + 1 + 4 * 1.1 + 2"
        for i in range (0,len(expresion)):
            if expresion[i] != "":
                if expresion[i][0] == "$" and len(expresion[i]) > 3 :
                    if "+" in expresion[i] or "-" in expresion[i] or "*" in expresion[i] or "/" in expresion[i]:

                        ecuacion = expresion[i].split('=')
                        operacion = ecuacion[1].strip()
                        if "$" not in operacion:
                            resultado = expresiones().parse_expr(operacion)
                            pre = resultado % 1
                            if pre == 0:
                                cadena = ecuacion[0].strip() + " = " + str(int(resultado)) + " ; "
                                expresion[i] = cadena 
                            else:
                                cadena = ecuacion[0].strip() + " = " + str(resultado) + " ; "
                                expresion[i] = cadena
                        else:
                            print("ecuacion no valida")
                            #resultado = expresiones().parse_expr(expresion)
        print (expresion)
        return expresion



""" expresiones.inicio() """