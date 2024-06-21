class Sintactico:
    def __init__(self) -> None:
        self.gramatica = {
            "Programa": [['¿', 'Sentencias','?']],
            "Sentencias": [['DeclaraVar'], 
                            ['Comentario'], 
                            ['Asignacion'], 
                            ['Operacion'], 
                            ['Mensaje'], 
                            ['Insertar'],
                            ['Concatenar']
                        ],
            "DeclaraVar": [['TipoDato','Complemeto', ';'],
                            ['TipoDato', 'Complemento', ';', 'Sentencias']
                        ],
            "Complemento": [['NomVar'],
                            ['NomVar', '=', 'Asignado']
                        ],
            "Asignacion": [[':', 'NomVar', "=", 'Asignado', ';'], 
                            [':', 'NomVar', "=", 'Asignado', ';', 'Sentencias']
                        ],
            "Asignado":[['All'],
                        ['Valor'],
                        ['Boleano'],
                        [':', 'NomVar']
                        ],
            "Comentario":[['#','All', '\n'],
                            ["#","All",'\n',"Sentencias"]
                        ],
            "Mensaje":[['SND', 'All',';'],
                        ["SND",'All', ';','Sentencias']
                    ],
            "Insertar":[['INS', ':','NomVar', ';'],
                        ['INS', ':','NomVar', ';','Sentencias']
                        ],
            "Operacion":[[':','NomVar', '=', 'Ecuacion',';'],
                        [':','NomVar', '=', 'Ecuacion',';','Sentencias']
                        ],
            "Ecuacion": [['Valor', 'Operador', 'Valor']],
            "Valor": [['Numero'],[':', 'NomVar']],
            "Concatenar":[[':', 'NomVar', '=', 'Concatena', ',','Concatena', ';'],
                        [':', 'NomVar', '=', 'Concatena', ',','Concatena', ';','Sentencias']
                        ],
            "Concatena":[['All'],
                        [':', 'NomVar']
                        ],
            "TipoDato":[['INT'],
                        ['STR'],
                        ['FLT'],
                        ['CHR'],
                        ['BOL']
                    ],
            "NomVar":[['Letra'],
                    ['Letra','(Letra)*']
                    ],
            "Letra":[['a-z']],
            "Numero":[['digitos','(digitos)*'],
                    ['digitos','(digitos)*]','.', 'digitos', '(digitos)*']
                    ],
            "digitos":[['0-9']],
            "Boleano":[['TRUE'],
                    ['FALSE']
                    ],
            "All":[['']],
            "Operador":[['+'], 
                        ['-'], 
                        ['*'], 
                        ['/']
                    ],
        }
        self.stack = ['n',1,'$',['Programa','$']]

    def sintax_analisis(self):
        pass

if __name__ == "__main__":
    sintactico = Sintactico()
    """ Accede a los valores de Programa """
    print(sintactico.gramatica["Programa"])
    print("--------------------------------------------------")
    """ Accede a los valores de Sentencias """
    print(sintactico.gramatica["Sentencias"])
    print("--------------------------------------------------")
    """ Accede a los valores de DeclaraVar """
    print(sintactico.gramatica["DeclaraVar"])