import copy
class prueba:
    def __init__(self) -> None:
        self.gramatica = {
            "S": [['a','A','d'],['a','B']],
            "A": [['c'],['d']],
            "B": [['c','c','d'],['d','d','c']]
        }
        self.terminales = ['a','b','c','d']
        self.no_terminales = ['S','A','B']
        
        self.arbol = ['n',0,['▩'],['S','⋕']]
        self.alternatives = []
        self.steps = []

    def analizar(self, token_list):
        #* Paso 1: Añadir el simbolo de fin de cadena
        token_list.append('⋕')

        #* Expandimos el árbol de análisis de manera inicial
        if self.arbol[2][0] == '▩' and len(self.arbol[3]) == 2:
            self.expandir()

        #* Realizamos el ciclo para analizar la cadena
        contador = 0
        success = False
        while not success:
            apuntador = self.arbol[1]

            #* Expansion del árbol de análisis (Regla 1)
            if self.arbol[3][0] in self.no_terminales and self.arbol[0] == 'n':
                self.expandir()

            #* Concordancia de símbolos (Regla 2)
            elif self.arbol[3][0] in self.terminales and self.arbol[3][0] == token_list[apuntador] and self.arbol[0] == 'n':
                self.concordancia()

            #* Terminación con éxito (Regla 3)
            elif len(self.arbol[3]) == 1 and self.arbol[3][0] == "⋕" and self.arbol[0] == 'n':
                success = True

            #* No concordancia de un símbolo (Regla 4)
            elif self.arbol[3][0] != token_list[apuntador] and self.arbol[0] == 'n':
                self.no_concordancia()

            #* Siguiente alternativa (Reglas 6a, 6b, 6c)
            elif self.arbol[0] == 'r':
                #* Extraer el token que se está analizando
                token = self.arbol[2][-1]
                #* Verificar si existe alguna otra alternativa (Regla 6a)
                if token in self.no_terminales and len(self.gramatica[token]) > 1 and (self.alternatives[-1] -1) < len(self.gramatica[token]):
                    self.siguiente_alternativa(token)

                #* Si no existe ninguna otra alternativa 
                elif len(self.gramatica[token]) == 1:
                    self.sin_alternativa()
                #* Retroceso a la entrada
                
            if contador == 5:
                self.print_steps()
                success = True   
            contador += 1

    def expandir(self):
        #* Obtenemos el token del stack gramática (stack[3][0]) y lo eliminamos
        token = self.arbol[3][0]


        # elimina todos los dígitos de la cadena
        self.arbol[3].pop(0)

        if self.arbol[2][0] == '▩':
            self.arbol[2].pop(0)
            self.alternatives.append(1)

            #* Obtenemos la producción de la gramática y la añadimos al inicio del stack
            production = self.gramatica[token][self.alternatives[-1] -1]
            self.arbol[3] = production + self.arbol[3]

            self.arbol[2].append(token)
            self.save_step()

        else:
            #* Obtenemos la producción de la gramática y la añadimos al inicio del stack
            production = self.gramatica[token][self.alternatives[-1] -1]
            self.arbol[3] = production + self.arbol[3]
            self.alternatives.append(1)  
            self.arbol[2].extend(token)
            self.save_step()

    def concordancia(self):
        #* Aumentamos el apuntador
        self.arbol[1] += 1

        #* Obtenemos el token del stack gramática (stack[3][0])
        token = self.arbol[3][0]

        #* Eliminamos el token del stack gramática (stack[3][0])
        self.arbol[3].pop(0)

        #* Añadimos el token al stack de concordancia
        self.arbol[2].append(token)

        self.save_step()

    def no_concordancia(self):
        #* Cambiar el estado a retroceso
        self.arbol[0] = 'r'
        self.save_step()

    def siguiente_alternativa(self, token):
        #* Obtenemos la nueva producción
        alternativa = self.alternatives[-1] -1 
        nueva_alternativa = alternativa + 1
        nueva_produccion = self.gramatica[token][nueva_alternativa]
        
        #* Eliminamos la antigua producción
        antigua_produccion = self.gramatica[token][alternativa]
        
        coincidencias = True
        contador = 0
        while coincidencias:
            if len(antigua_produccion) <= contador:
                coincidencias = False

            elif antigua_produccion[contador] == self.arbol[3][0]:
                self.arbol[3].pop(0)
                contador += 1
        #* Reemplazamos con la nueva producción en el stack de la gramática por analizar (self.arbol[3])
        self.arbol[3] = nueva_produccion + self.arbol[3]
    
        #* Cambiamos el estado a normal
        self.arbol[0] = 'n'

        #* Aumentamos el valor de la alternativa
        self.alternatives[-1] = self.alternatives[-1] + 1

        self.save_step()

    def sin_alternativa(self):
        pass
    
    #TODO: Funcion para imprimir los pasos en el árbol
    def print_steps(self):
        for item in self.steps:
            print(item)

    #TODO: Funcion para realizar una copia del árbol
    def save_step(self):
        self.steps.append(copy.deepcopy(self.arbol))

if __name__ == "__main__":
    objeto = prueba()
    token_list = ['a','d','d','c']
    objeto.analizar(token_list)