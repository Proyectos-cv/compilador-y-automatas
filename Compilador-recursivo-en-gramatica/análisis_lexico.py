from tabla import interfaz_tabla
class procedimiento:
    def __init__(self):
        pass

    def split_texto_into_lines(self, text):
        lines = text.split('\n')
        result = [[i+1, line] for i, line in enumerate(lines)]
        self.separate_tokens(result)

    def separate_tokens(self, split_text):
        for i in range(len(split_text)):
            content = split_text[i][1]
            content = content.replace("¿", "¿ ")
            content = content.replace("INT", " INT ")
            content = content.replace("STR", " STR ")
            content = content.replace("FLT", " FLT ")
            content = content.replace("CHR", " CHR ")
            content = content.replace("BOL", " BOL ")
            content = content.replace("SND", " SND ")
            content = content.replace(":", " :")
            content = content.replace(";", " ; ")
            content = content.replace("?", " ? ")
            content = content.replace("#", " # ")
            content = content.replace("\"", " \" ")

            split_text[i][1] = content
        self.split_into_tokens(split_text)

    def split_into_tokens(self, split_text):
        for i in range(len(split_text)):
            content = split_text[i][1]
            content = content.split()
            split_text[i][1] = content

        self.eliminate_coments(split_text)

    def eliminate_coments(self, split_text):
        for i in range(len(split_text)):
            content = split_text[i][1]
            
            for j in range(len(content)):
                if content[j] == "#":
                    content = content[:j+1]
                    break
            split_text[i][1] = content

        self.eliminate_messages(split_text)

    def eliminate_messages(self, split_text):
        for my_list in split_text:
            start = None
            end = None
            for i, word in enumerate(my_list[1]):
                if word == '"' and start is None:
                    start = i
                elif word == '"' and start is not None:
                    end = i
                    break
            if start is not None:
                if end is not None:
                    del my_list[1][start+1:end+1]
                elif end is None:
                    del my_list[1][start+1: ]

        self.classify_tokens(split_text)

    def classify_tokens(self, split_text):
        save_results = []
        reserved_words = ["INT", "STR", "FLT", "CHR", "BOL", "SND","¿", "?"]
        operators = ["+", "-", "*", "/", "="]
        characters = [":", ",", ";", "#", "\""]
        boolean = ["FALSE", "TRUE"]
        numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]

        positions_question_open = []
        positions_int = []
        positions_str = []
        positions_flt = []
        positions_chr = []
        positions_bol = []
        positions_snd = []
        positions_ins = []
        positions_plus = []
        positions_minus = []
        positions_times = []
        positions_divide = []
        positions_equal = []
        positions_colon = []
        positions_comma = []
        positions_semicolon = []
        positions_question_close = []
        positions_double_quote = []
        positions_hash = []
        positions_false = []
        positions_true = []
        positions_integers = []
        positions_floats = []

        for list in split_text:
            for word in list[1]:
                if word == "¿":
                    positions_question_open.append(list[0])
                
                    if len(save_results) > 0:
                        for element in save_results:
                            if "¿" not in element[0]:
                                save_results.append([word,"Palabra reservada"])
                                break
                    else:
                        save_results.append([word,"Palabra reservada"])

                elif word == "INT":
                    positions_int.append(list[0])

                    if len(save_results) > 0:
                        for element in save_results:
                            if "INT" not in element[0]:
                                save_results.append([word,"Palabra reservada"])
                                break
                    else:
                        save_results.append([word,"Palabra reservada"])

                elif word == "STR":
                    positions_str.append(list[0])

                    if len(save_results) > 0:
                        for element in save_results:
                            if "STR" not in element[0]:
                                save_results.append([word,"Palabra reservada"])
                                break

                    else:
                        save_results.append([word,"Palabra reservada"])

                elif word == "FLT":
                    positions_flt.append(list[0])

                    if len(save_results) > 0:
                        for element in save_results:
                            if "FLT" not in element[0]:
                                save_results.append([word,"Palabra reservada"])
                                break
                    else:
                        save_results.append([word,"Palabra reservada"])

                elif word == "CHR":
                    positions_chr.append(list[0])

                    if len(save_results) > 0:
                        for element in save_results:
                            if "CHR" not in element[0]:
                                save_results.append([word,"Palabra reservada"])
                                break
                    else:
                        save_results.append([word,"Palabra reservada"])

                elif word == "BOL":
                    positions_bol.append(list[0])

                    if len(save_results) > 0:
                        for element in save_results:
                            if "BOL" not in element[0]:
                                save_results.append([word,"Palabra reservada"])
                                break
                    else:
                        save_results.append([word,"Palabra reservada"])

                elif word == "SND":
                    positions_snd.append(list[0])

                    if len(save_results) > 0:
                        for element in save_results:
                            if "SND" not in element[0]:
                                save_results.append([word,"Palabra reservada"])
                                break
                    else:
                        save_results.append([word,"Palabra reservada"])

                elif word == "?":
                    positions_question_close.append(list[0])

                    if len(save_results) > 0:
                        for element in save_results:
                            if "?" not in element[0]:
                                save_results.append([word,"Palabra reservada"])
                                break
                    else:
                        save_results.append([word,"Palabra reservada"])

                elif word == "+":
                    before_word = list[1][list[1].index(word)-1]
                    if before_word not in operators:
                        positions_plus.append(list[0])

                        if len(save_results) > 0:
                            for element in save_results:
                                if "+" not in element[0]:
                                    save_results.append([word,"Operador"])
                                    break
                        else:
                            save_results.append([word,"Operador"])
                    else:
                        #Manda mensaje de error al archivo
                        archivo = open("errores.txt", "w", encoding="utf-8")
                        archivo.write("Error: No se puede tener dos operadores seguidos")
                        archivo.close()
                        return False

                elif word == "-":
                    positions_minus.append(list[0])

                    if len(save_results) > 0:
                        for element in save_results:
                            if "-" not in element[0]:
                                save_results.append([word,"Operador"])
                                break
                    else:
                        save_results.append([word,"Operador"])

                elif word == "*":
                    positions_times.append(list[0])

                    if len(save_results) > 0:
                        for element in save_results:
                            if "*" not in element[0]:
                                save_results.append([word,"Operador"])
                                break
                    else:
                        save_results.append([word,"Operador"])

                elif word == "/":
                    positions_divide.append(list[0])

                    if len(save_results) > 0:
                        for element in save_results:
                            if "/" not in element[0]:
                                save_results.append([word,"Operador"])
                                break
                    else:
                        save_results.append([word,"Operador"])

                elif word == "=":
                    positions_equal.append(list[0])

                    if len(save_results) > 0:
                        for element in save_results:
                            if "=" not in element[0]:
                                save_results.append([word,"Operador"])
                                break
                    else:
                        save_results.append([word,"Operador"])

                elif word[0] == ":":
                    if word[0] == ":":
                        for letra in word[1:]:
                            if not letra.islower():
                                archivo = open("results.txt", "w", encoding="utf-8")
                                archivo.write("Error en la linea " + str(list[0]) + " el simbolo " + word + " no es valido como identificador")
                                archivo.close()

                                #Termina el programa
                                print("Error en la linea " + str(list[0]) + " el simbolo " + word + " no es valido como identificador")
                                return False
                        
                        flag_exists = False

                        for position in positions_colon:
                            if word == position[0]:
                                position[1].append(list[0])
                                flag_exists = True
                                break
                        
                        if not flag_exists:
                            positions_colon.append([word,[list[0]]])

                        if len(save_results) > 0:
                            for element in save_results:
                                if word not in element[0]:
                                    save_results.append([word,"Identificador"])
                                    break
                        else:
                            save_results.append([word,"Identificador"])
                    else:
                        return False

                elif word == ",":
                    positions_comma.append(list[0])

                    if len(save_results) > 0:
                        for element in save_results:
                            if "," not in element[0]:
                                save_results.append([word,"Caracter"])
                                break
                    else:
                        save_results.append([word,"Caracter"])

                elif word == ";":
                    positions_semicolon.append(list[0])

                    if len(save_results) > 0:
                        for element in save_results:
                            if ";" not in element[0]:
                                save_results.append([word,"Caracter"])
                                break
                    else:
                        save_results.append([word,"Caracter"])

                elif word == "\"":
                    positions_double_quote.append(list[0])

                    if len(save_results) > 0:
                        for element in save_results:
                            if "\"" not in element[0]:
                                save_results.append([word,"Caracter"])
                                break
                    else:
                        save_results.append([word,"Caracter"])

                elif word == "#":
                    positions_hash.append(list[0])

                    if len(save_results) > 0:
                        for element in save_results:
                            if "#" not in element[0]:
                                save_results.append([word,"Caracter"])
                                break
                    else:
                        save_results.append([word,"Caracter"])

                elif word == "FALSE":
                    positions_false.append(list[0])

                    if len(save_results) > 0:
                        for element in save_results:
                            if "FALSE" not in element[0]:
                                save_results.append([word,"Booleano"])
                                break
                    else:
                        save_results.append([word,"Booleano"])

                elif word == "TRUE":
                    positions_true.append(list[0])

                    if len(save_results) > 0:
                        for element in save_results:
                            if "TRUE" not in element[0]:
                                save_results.append([word,"Booleano"])
                                break
                    else:
                        save_results.append([word,"Booleano"])

                elif word == "":
                    pass

                elif word[0] in numbers:
                    decimal = False
                    point = 0
                    for i in range(len(word)):
                        if word[i] not in numbers:
                            archivo = open("results.txt", "w", encoding="utf-8")
                            archivo.write("Error en la linea " + str(list[0]) + " el valor " + word + " no es valida como numero")
                            archivo.close()

                            #Termina el programa
                            print("Error en la linea " + str(list[0]) + " el valor " + word + " no es valida como numero")
                            return False
                        
                        if word[i] == ".":
                            decimal = True
                            point = point + 1

                    if decimal and point == 1:
                        
                        flag_exists = False

                        for position in positions_floats:
                            if word == position[0]:
                                position[1].append(list[0])
                                flag_exists = True
                                break
                        
                        if not flag_exists:
                            positions_floats.append([word,[list[0]]])

                        if len(save_results) > 0:
                            for element in save_results:
                                if word not in element[0]:
                                    save_results.append([word,"Caracter"])
                                    break
                        else:
                            save_results.append([word,"Caracter"])

                    elif decimal and point > 1:
                        archivo = open("results.txt", "w", encoding="utf-8")
                        archivo.write("Error en la linea " + str(list[0]) + " el valor " + word + " no es valida como numero")
                        archivo.close()

                        #Termina el programa
                        print("Error en la linea " + str(list[0]) + " el valor " + word + " no es valida como numero")
                        return False
                    else:
                        flag_exists = False

                        for position in positions_integers:
                            if word == position[0]:
                                position[1].append(list[0])
                                flag_exists = True
                                break
                        
                        if not flag_exists:
                            positions_integers.append([word,[list[0]]])

                        if len(save_results) > 0:
                            for element in save_results:
                                if word not in element[0]:
                                    save_results.append([word,"Caracter"])
                                    break
                        else:
                            save_results.append([word,"Caracter"])

                elif len(word) <= 3: #Verifica si la palabra es una palabra reservada erronea
                    archivo = open("results.txt", "w", encoding="utf-8")
                    archivo.write("Error en la linea " + str(list[0]) + " la cadena " + word + " no es valida como palabra reservada")
                    archivo.close()

                    #Termina el programa
                    print("Error en la linea " + str(list[0]) + " la cadena " + word + " no es valida como palabra reservada")
                    return False

                elif word[0] in operators and len(word) > 1: #Verifica si tiene sobrecarga de operadores
                    archivo = open("results.txt", "w", encoding="utf-8")
                    archivo.write("Error en la linea " + str(list[0]) + " el simbolo " + word + " no es valido como operador")
                    archivo.close()

                    #Termina el programa
                    print("Error en la linea " + str(list[0]) + " el simbolo " + word + " no es valido como operador")
                    return False

                elif len(word) <= 5: #Verifica si la palabra es una bandera false erronea
                    if word[0].isupper():
                        archivo = open("results.txt", "w", encoding="utf-8")
                        archivo.write("Error en la linea " + str(list[0]) + " la cadena " + word + " no es valida como bandera")
                        archivo.close()

                        #Termina el programa
                        print("Error en la linea " + str(list[0]) + " la cadena " + word + " no es valida como bandera")
                        return False
                    else:
                        archivo = open("results.txt", "w", encoding="utf-8")
                        archivo.write("Error en la linea " + str(list[0]) + " la cadena " + word + " no es reconocible en la sintaxis")
                        archivo.close()
                        return False

                elif len(word) <= 4: #Verifica si la palabra es una bandera true erronea:
                    if word[0].isupper():
                        archivo = open("results.txt", "w", encoding="utf-8")
                        archivo.write("Error en la linea " + str(list[0]) + " la cadena " + word + " no es valida como bandera")
                        archivo.close()

                        #Termina el programa
                        print("Error en la linea " + str(list[0]) + " la cadena " + word + " no es valida como bandera")
                        return False
                    else:
                        archivo = open("results.txt", "w", encoding="utf-8")
                        archivo.write("Error en la linea " + str(list[0]) + " la cadena " + word + " no es reconocible en la sintaxis")
                        archivo.close()
                        return False

                elif word not in reserved_words and word not in operators and word[0] not in numbers:
                    archivo = open("results.txt", "w", encoding="utf-8")
                    archivo.write("Error en la linea " + str(list[0]) + " el simbolo " + word + " no es reconocible en la sintaxis")
                    archivo.close()

                    #Termina el programa
                    print("Error en la linea " + str(list[0]) + " el simbolo " + word + " no es reconocible en la sintaxis")
                    return False

        #Abre el archivo y escribe los resultados válidos
        archivo = open("results.txt", "w", encoding="utf-8")
        archivo.write("Análisis léxico exitoso\n\n")
        archivo.close()

        all_positions = [positions_question_open, 
                        positions_int, 
                        positions_str, 
                        positions_flt, 
                        positions_chr, 
                        positions_bol, 
                        positions_snd, 
                        positions_ins, 
                        positions_plus, 
                        positions_minus, 
                        positions_times, 
                        positions_divide, 
                        positions_equal,
                        positions_colon,
                        positions_comma,
                        positions_semicolon,
                        positions_question_close,
                        positions_double_quote,
                        positions_hash,
                        positions_false,
                        positions_true,
                        positions_integers,
                        positions_floats]
        
        save_results = self.delete_repeated(save_results)

        self.assign_positions(save_results, all_positions)

    def delete_repeated(self, list_results):
        viewed = set()
        new_list_results = []

        for element in list_results:
            tupla = tuple(element)
            if tupla not in viewed:
                viewed.add(tupla)
                new_list_results.append(element)
        
        return new_list_results

    def assign_positions(self, list_results, list_positions):
        positions_question_open = list_positions[0]
        positions_int = list_positions[1]
        positions_str = list_positions[2]
        positions_flt = list_positions[3]
        positions_chr = list_positions[4]
        positions_bol = list_positions[5]
        positions_snd = list_positions[6]
        positions_ins = list_positions[7]
        positions_plus = list_positions[8]
        positions_minus = list_positions[9]
        positions_times = list_positions[10]
        positions_divide = list_positions[11]
        positions_equal = list_positions[12]
        positions_colon = list_positions[13]
        positions_comma = list_positions[14]
        positions_semicolon = list_positions[15]
        positions_question_close = list_positions[16]
        positions_double_quote = list_positions[17]
        positions_hash = list_positions[18]
        positions_false = list_positions[19]
        positions_true = list_positions[20]
        positions_integers = list_positions[21]
        positions_floats = list_positions[22]

        for element in list_results:
            if element[0] == "¿":
                if len(positions_question_open) == 1:
                    first_element = positions_question_open[0]
                    element.append(first_element)
                    element.append("-")
                else:
                    first_element = positions_question_open[0]
                    last_elements = " - ".join(str(x) for x in positions_question_open[1:])
                    element.append(first_element)
                    element.append(last_elements)

            elif element[0] == "INT":
                if len(positions_int) == 1:
                    first_element = positions_int[0]
                    element.append(first_element)
                    element.append("-")
                else:
                    first_element = positions_int[0]
                    last_elements = " - ".join(str(x) for x in positions_int[1:])
                    element.append(first_element)
                    element.append(last_elements)

            elif element[0] == "STR":
                if len(positions_str) == 1:
                    first_element = positions_str[0]
                    element.append(first_element)
                    element.append("-")
                else:
                    first_element = positions_str[0]
                    last_elements = " - ".join(str(x) for x in positions_str[1:])
                    element.append(first_element)
                    element.append(last_elements)

            elif element[0] == "FLT":
                if len(positions_flt) == 1:
                    first_element = positions_flt[0]
                    element.append(first_element)
                    element.append("-")
                else:
                    first_element = positions_flt[0]
                    last_elements = " - ".join(str(x) for x in positions_flt[1:])
                    element.append(first_element)
                    element.append(last_elements)

            elif element[0] == "CHR":
                if len(positions_chr) == 1:
                    first_element = positions_chr[0]
                    element.append(first_element)
                    element.append("-")
                else:
                    first_element = positions_chr[0]
                    last_elements = " - ".join(str(x) for x in positions_chr[1:])
                    element.append(first_element)
                    element.append(last_elements)

            elif element[0] == "BOL":
                if len(positions_bol) == 1:
                    first_element = positions_bol[0]
                    element.append(first_element)
                    element.append("-")
                else:
                    first_element = positions_bol[0]
                    last_elements = " - ".join(str(x) for x in positions_bol[1:])
                    element.append(first_element)
                    element.append(last_elements)

            elif element[0] == "SND":
                if len(positions_snd) == 1:
                    first_element = positions_snd[0]
                    element.append(first_element)
                    element.append("-")
                else:
                    first_element = positions_snd[0]
                    last_elements = " - ".join(str(x) for x in positions_snd[1:])
                    element.append(first_element)
                    element.append(last_elements)

            elif element[0] == "INS":
                if len(positions_ins) == 1:
                    first_element = positions_ins[0]
                    element.append(first_element)
                    element.append("-")
                else:
                    first_element = positions_ins[0]
                    last_elements = " - ".join(str(x) for x in positions_ins[1:])
                    element.append(first_element)
                    element.append(last_elements)

            elif element[0] == "+":
                if len(positions_plus) == 1:
                    first_element = positions_plus[0]
                    element.append(first_element)
                    element.append("-")
                else:
                    first_element = positions_plus[0]
                    last_elements = " - ".join(str(x) for x in positions_plus[1:])
                    element.append(first_element)
                    element.append(last_elements)

            elif element[0] == "-":
                if len(positions_minus) == 1:
                    first_element = positions_minus[0]
                    element.append(first_element)
                    element.append("-")
                else:
                    first_element = positions_minus[0]
                    last_elements = " - ".join(str(x) for x in positions_minus[1:])
                    element.append(first_element)
                    element.append(last_elements)

            elif element[0] == "*":
                if len(positions_times) == 1:
                    first_element = positions_times[0]
                    element.append(first_element)
                    element.append("-")
                else:
                    first_element = positions_times[0]
                    last_elements = " - ".join(str(x) for x in positions_times[1:])
                    element.append(first_element)
                    element.append(last_elements)

            elif element[0] == "/":
                if len(positions_divide) == 1:
                    first_element = positions_divide[0]
                    element.append(first_element)
                    element.append("-")
                else:
                    first_element = positions_divide[0]
                    last_elements = " - ".join(str(x) for x in positions_divide[1:])
                    element.append(first_element)
                    element.append(last_elements)

            elif element[0] == "=":
                if len(positions_equal) == 1:
                    first_element = positions_equal[0]
                    element.append(first_element)
                    element.append("-")
                else:
                    first_element = positions_equal[0]
                    last_elements = " - ".join(str(x) for x in positions_equal[1:])
                    element.append(first_element)
                    element.append(last_elements)

            elif element[0] == "TRUE":
                if len(positions_true) == 1:
                    first_element = positions_true[0]
                    element.append(first_element)
                    element.append("-")
                else:
                    first_element = positions_true[0]
                    last_elements = " - ".join(str(x) for x in positions_true[1:])
                    element.append(first_element)
                    element.append(last_elements)

            elif element[0] == "FALSE":
                if len(positions_false) == 1:
                    first_element = positions_false[0]
                    element.append(first_element)
                    element.append("-")
                else:
                    first_element = positions_false[0]
                    last_elements = " - ".join(str(x) for x in positions_false[1:])
                    element.append(first_element)
                    element.append(last_elements)

            elif element[0] == ",":
                if len(positions_comma) == 1:
                    first_element = positions_comma[0]
                    element.append(first_element)
                    element.append("-")
                else:
                    first_element = positions_comma[0]
                    last_elements = " - ".join(str(x) for x in positions_comma[1:])
                    element.append(first_element)
                    element.append(last_elements)

            elif element[0] == ";":
                if len(positions_semicolon) == 1:
                    first_element = positions_semicolon[0]
                    element.append(first_element)
                    element.append("-")
                else:
                    first_element = positions_semicolon[0]
                    last_elements = " - ".join(str(x) for x in positions_semicolon[1:])
                    element.append(first_element)
                    element.append(last_elements)

            elif element[0] == "#":
                if len(positions_hash) == 1:
                    first_element = positions_hash[0]
                    element.append(first_element)
                    element.append("-")
                else:
                    first_element = positions_hash[0]
                    last_elements = " - ".join(str(x) for x in positions_hash[1:])
                    element.append(first_element)
                    element.append(last_elements)

            elif element[0] == "\"":
                if len(positions_double_quote) == 1:
                    first_element = positions_double_quote[0]
                    element.append(first_element)
                    element.append("-")
                else:
                    first_element = positions_double_quote[0]
                    last_elements = " - ".join(str(x) for x in positions_double_quote[1:])
                    element.append(first_element)
                    element.append(last_elements)

            elif element[0] == "?":
                if len(positions_question_close) == 1:
                    first_element = positions_question_close[0]
                    element.append(first_element)
                    element.append("-")
                else:
                    first_element = positions_question_close[0]
                    last_elements = " - ".join(str(x) for x in positions_question_close[1:])
                    element.append(first_element)
                    element.append(last_elements)

        list_results = self.assign_positions_extension(list_results, positions_integers)
        list_results = self.assign_positions_extension(list_results, positions_floats)
        list_results = self.assign_positions_extension(list_results, positions_colon)

        self.list_results = list_results

    def assign_positions_extension(self, list_results, list_to_assing):
        for list in list_to_assing:
            index = list[0]
            list_of_positions = list[1]

            for new_list in list_results:
                if new_list[0] == index:
                    if len(list_of_positions) == 1:
                        first_element = list_of_positions[0]
                        new_list.append(first_element)
                        new_list.append("-")
                    else:
                        first_element = list_of_positions[0]
                        last_elements = " - ".join(str(x) for x in list_of_positions[1:])
                        new_list.append(first_element)
                        new_list.append(last_elements)

        return list_results

    def send_table(self):
        tabla = interfaz_tabla()
        tabla.menu(self.list_results)
if __name__ == '__main__':
    text = "¿\nINT :numerouno = 10;\nINT :numerodos = 20;\n\nSTR :cadena = \"hola\";\nSTR :cadenados = \"mundo\";\n\n# este es un comentario para ver que es lo que procede con espacio\n\nFLT :decimal = 10.5; #aquí se puede poner un comentario\nFLT :decimaldos = 20.5;\n\nCHR :caracter = \"a\";\nCHR :nuevocaracter = \"b\";\n\n#Este es un comentario sin espacio para ver que es lo que procede\n\nBOL :verdadero = TRUE;\nBOL :falso = FALSE;\n\nINT :suma = :numerouno + :numerodos;\nINT :resta = :numerouno - :numerodos;\nINT :multiplicacion = :numerouno * :numerodos;\nINT :division = :numerouno / :numerodos;\n\nSTR :nuevacadena = :cadena , :cadenados;\n\nFLT :sumadecimal = :decimal + :decimaldos;\nFLT :restadecimal = :decimal - :decimaldos;\nFLT :multiplicaciondecimal = :decimal * :decimaldos;\nFLT :divisiondecimal = :decimal / :decimaldos;\n\nSTR :nuevocaracter = :caracter , :nuevocaracter;\n\nINS :suma;\nINS :resta;\nINS :multiplicacion;\nINS :division;\n\nINS :nuevacadena;\n\nINS :sumadecimal;\nINS :restadecimal;\nINS :multiplicaciondecimal;\nINS :divisiondecimal;\n\nINS :nuevocaracter;\n\nINS :verdadero;\nINS :falso;\n?"
    cadena = "¿\nSTR :suma = \"hola mundo;\n?"
    obj = procedimiento()
    obj.split_texto_into_lines(cadena)