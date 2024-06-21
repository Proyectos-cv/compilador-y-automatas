elif siguiente.startswith('"'):
                produccion=["NomVar","=","LoQueSea",";"]
                return produccion
            elif siguiente.isdigit() and not (operacion in ["+","-","*","/"]):
                produccion=["NomVar","=","Entero",";"]
                return produccion
            elif siguiente.replace(".", "").isdigit() and not (operacion in ["+","-","*","/"]):
                produccion=["NomVar","=","Decimal",";"]
                return produccion
            elif siguiente.isdigit() and (operacion in ["+","-","*","/"]):
                produccion=["NomVar","=","Operacion",";"]
                return produccion
            elif siguiente.replace(".", "").isdigit() and (operacion in ["+","-","*","/"]):
                produccion=["NomVar","=","Operacion",";"]