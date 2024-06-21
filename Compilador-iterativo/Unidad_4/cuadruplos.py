import os

class Cuadruplos:
    def __init__(self):
        self.first = ['*', '/']
        self.second = ['+', '-']
        
    def procedimiento(self, operacion):

        #* Dividir la operación en tokens
        operation_tokens = operacion.split(' ')
        jerarquías = []

        #* Asignamos una bandera falsa para saber que el elemento ya ha sido recorrido
        for i in range(len(operation_tokens)):
            aux = [operation_tokens[i], False]
            operation_tokens[i] = aux

        end = False
        contador = 1
        #* Buscamos los operadores de mayor jerarquía (self.first)
        while not end:
            incidencias = False

            for i in range(len(operation_tokens)):
                token = operation_tokens[i][0]

                if token in self.first:

                    anterior = operation_tokens[i-1][0]
                    siguiente = operation_tokens[i+1][0]
                    operador = operation_tokens[i][0]

                    if operation_tokens[i-1][1] == False and operation_tokens[i-1][1] == False:
                        incidencias = True

                        list_aux = [[anterior, operador, siguiente], 'v', contador]
                        jerarquías.append(list_aux)

                        #* reemplazamos el elemento anterior por el resultado de la operación
                        operation_tokens[i-1][0] = 'v' + str(contador)
                        operation_tokens.pop(i)
                        operation_tokens.pop(i)

                        contador += 1
                        break
            
            if incidencias == False:
                end = True
        
        end = False
        #* Buscamos los operadores de menor jerarquía (self.second)
        while not end:
            incidencias = False

            for i in range(len(operation_tokens)):
                token = operation_tokens[i][0]

                if token in self.second:

                    anterior = operation_tokens[i-1][0]
                    siguiente = operation_tokens[i+1][0]
                    operador = operation_tokens[i][0]

                    if operation_tokens[i-1][1] == False and operation_tokens[i-1][1] == False:
                        incidencias = True

                        list_aux = [[anterior, operador, siguiente], 'v', contador]
                        jerarquías.append(list_aux)

                        #* reemplazamos el elemento anterior por el resultado de la operación
                        operation_tokens[i-1][0] = 'v' + str(contador)
                        operation_tokens.pop(i)
                        operation_tokens.pop(i)

                        contador += 1
                        break
            
            if incidencias == False:
                end = True

        
        #* Asignamos el valor después del igual a la variable si existe
        if operation_tokens[1][0] == '=':
            anterior = operation_tokens[0][0]
            siguiente = operation_tokens[2][0]
            operador = operation_tokens[1][0]

            list_aux = [[anterior, operador, siguiente], 'fin']
            jerarquías.append(list_aux)

        for i in range(len(jerarquías)):
            if jerarquías[i][-1] != 'fin':
                letra = jerarquías[i][-2]
                numero = jerarquías[i][-1]
                cadena = str(letra) + str(numero)
                jerarquías[i][-2] = cadena
                jerarquías[i].pop(-1)

        return jerarquías                   

if __name__ == "__main__":
    prueba = Cuadruplos()
    operacion = "$x = 34 + 5 + 3 + 2 - 10 * 2 ;"
    #operacion = "$b = $a * $b * $c * 10 - 12 * 4;"
    prueba.procedimiento(operacion)