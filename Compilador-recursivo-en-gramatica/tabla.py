from tkinter import *
from tkinter import ttk

class interfaz_tabla():
    def __init__(self):
        pass

    def crear_tabla(self, ventana, token):
        # Crear el Treeview
        self.tabla = ttk.Treeview(ventana, columns=('Tipo', 'Declara', 'Referencia'))
        self.tabla.heading('#0', text='Token')
        self.tabla.heading('Tipo', text='Tipo')
        self.tabla.heading('Declara', text='Declara')
        self.tabla.heading('Referencia', text='Referencia')

        #Cambia el tamaño de la letra
        style = ttk.Style()
        style.configure("Treeview", font=('JetBrains Mono', 14))

        #Ingresa los datos de la lista de listas
        for i in range(len(token)):
            self.tabla.insert('', 'end', text=token[i][0], values=(token[i][1], token[i][2], token[i][3]))

        # Mostrar la self.tabla
        self.tabla.pack(fill=BOTH, expand=1)
        return self.tabla

    def menu(self, lista):
        mainwindow = Tk()

        ancho_ventana = 1100
        alto_ventana = 750
        x_ventana = mainwindow.winfo_screenwidth() // 2 - ancho_ventana // 2
        y_ventana = mainwindow.winfo_screenheight()// 2 - alto_ventana // 2 - 42
        posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
        mainwindow.geometry(posicion)

        mainwindow.title('Compilador')
        mainwindow.config(bg='#7FADA9')

        self.tabla = self.crear_tabla(mainwindow, lista)

        mainwindow.mainloop()


if __name__ == '__main__':
    token = [['¿', 'Palabra reservada', 0, '-'], ['INT', 'Palabra reservada', 2, '-'], [':numerouno', 'Identificador', 0, '-'], ['=', 'Operador', 0, '-'], ['10', 'Caracter', 0, '-'], [';', 'Carácter', 0, '-'], ['INT', 'Palabra reservada', 2, '-'], [':numerodos', 'Identificador', 0, '-'], ['=', 'Operador', 0, '-'], ['20', 'Caracter', 0, '-'], [';', 'Carácter', 0, '-'], ['STR', 'Palabra reservada', 0, '-'], [':cadena', 'Identificador', 0, '-'], ['=', 'Operador', 0, '-'], ['"', 'Carácter', 0, '-'], [';', 'Carácter', 0, '-'], ['STR', 'Palabra reservada', 0, '-'], [':cadenados', 'Identificador', 0, '-'], ['=', 'Operador', 0, '-'], ['"', 'Carácter', 0, '-'], [';', 'Carácter', 0, '-'], ['FLT', 'Palabra reservada', 0, '-'], [':decimal', 'Identificador', 0, '-'], ['=', 'Operador', 0, '-'], ['10.5', 'Caracter', 0, '-'], [';', 'Carácter', 0, '-'], ['FLT', 'Palabra reservada', 0, '-'], [':decimaldos', 'Identificador', 0, '-'], ['=', 'Operador', 0, '-'], ['20.5', 'Caracter', 0, '-'], [';', 'Carácter', 0, '-'], ['CHR', 'Palabra reservada', 0, '-'], [':caracter', 'Identificador', 0, '-'], ['=', 'Operador', 0, '-'], ['"', 'Carácter', 0, '-'], [';', 'Carácter', 0, '-'], ['CHR', 'Palabra reservada', 0, '-'], [':nuevocaracter', 'Identificador', 0, '-'], ['=', 'Operador', 0, '-'], ['"', 'Carácter', 0, '-'], [';', 'Carácter', 0, '-'], ['BOL', 'Palabra reservada', 0, '-'], [':verdadero', 'Identificador', 0, '-'], ['=', 'Operador', 0, '-'], ['TRUE', 'Palabra reservada', 0, '-'], [';', 'Carácter', 0, '-'], ['BOL', 'Palabra reservada', 0, '-'], [':falso', 'Identificador', 0, '-'], ['=', 'Operador', 0, '-'], ['FALSE', 'Palabra reservada', 0, '-'], [';', 'Carácter', 0, '-'], ['INT', 'Palabra reservada', 2, '-'], [':suma', 'Identificador', 0, '-'], ['=', 'Operador', 0, '-'], [':numerouno', 'Identificador', 0, '-'], ['+', 'Operador', 0, '-'], [':numerodos', 'Identificador', 0, '-'], [';', 'Carácter', 0, '-'], ['INT', 'Palabra reservada', 2, '-'], [':resta', 'Identificador', 0, '-'], ['=', 'Operador', 0, '-'], [':numerouno', 'Identificador', 0, '-'], ['-', 'Operador', 0, '-'], [':numerodos', 'Identificador', 0, '-'], [';', 'Carácter', 0, '-'], ['INT', 'Palabra reservada', 2, '-'], [':multiplicacion', 'Identificador', 0, '-'], ['=', 'Operador', 0, '-'], [':numerouno', 'Identificador', 0, '-'], ['*', 'Operador', 0, '-'], [':numerodos', 'Identificador', 0, '-'], [';', 'Carácter', 0, '-'], ['INT', 'Palabra reservada', 2, '-'], [':division', 'Identificador', 0, '-'], ['=', 'Operador', 0, '-'], [':numerouno', 'Identificador', 0, '-'], ['/', 'Operador', 0, '-'], [':numerodos', 'Identificador', 0, '-'], [';', 'Carácter', 0, '-'], ['STR', 'Palabra reservada', 0, '-'], [':nuevacadena', 'Identificador', 0, '-'], ['=', 'Operador', 0, '-'], [':cadena', 'Identificador', 0, '-'], [',', 'Carácter', 0, '-'], [':cadenados', 'Identificador', 0, '-'], [';', 'Carácter', 0, '-'], ['FLT', 'Palabra reservada', 0, '-'], [':sumadecimal', 'Identificador', 0, '-'], ['=', 'Operador', 0, '-'], [':decimal', 'Identificador', 0, '-'], ['+', 'Operador', 0, '-'], [':decimaldos', 'Identificador', 0, '-'], [';', 'Carácter', 0, '-'], ['FLT', 'Palabra reservada', 0, '-'], [':restadecimal', 'Identificador', 0, '-'], ['=', 'Operador', 0, '-'], [':decimal', 'Identificador', 0, '-'], ['-', 'Operador', 0, '-'], [':decimaldos', 'Identificador', 0, '-'], [';', 'Carácter', 0, '-'], ['FLT', 'Palabra reservada', 0, '-'], [':multiplicaciondecimal', 'Identificador', 0, '-'], ['=', 'Operador', 0, '-'], [':decimal', 'Identificador', 0, '-'], ['*', 'Operador', 0, '-'], [':decimaldos', 'Identificador', 0, '-'], [';', 'Carácter', 0, '-'], ['FLT', 'Palabra reservada', 0, '-'], [':divisiondecimal', 'Identificador', 0, '-'], ['=', 'Operador', 0, '-'], [':decimal', 'Identificador', 0, '-'], ['/', 'Operador', 0, '-'], [':decimaldos', 'Identificador', 0, '-'], [';', 'Carácter', 0, '-'], ['STR', 'Palabra reservada', 0, '-'], [':nuevocaracter', 'Identificador', 0, '-'], ['=', 'Operador', 0, '-'], [':caracter', 'Identificador', 0, '-'], [',', 'Carácter', 0, '-'], [':nuevocaracter', 'Identificador', 0, '-'], [';', 'Carácter', 0, '-'], ['INS', 'Palabra reservada', 0, '-'], [':suma', 'Identificador', 0, '-'], [';', 'Carácter', 0, '-'], ['INS', 'Palabra reservada', 0, '-'], [':resta', 'Identificador', 0, '-'], [';', 'Carácter', 0, '-'], ['INS', 'Palabra reservada', 0, '-'], [':multiplicacion', 'Identificador', 0, '-'], [';', 'Carácter', 0, '-'], ['INS', 'Palabra reservada', 0, '-'], [':division', 'Identificador', 0, '-'], [';', 'Carácter', 0, '-'], ['INS', 'Palabra reservada', 0, '-'], [':nuevacadena', 'Identificador', 0, '-'], [';', 'Carácter', 0, '-'], ['INS', 'Palabra reservada', 0, '-'], [':sumadecimal', 'Identificador', 0, '-'], [';', 'Carácter', 0, '-'], ['INS', 'Palabra reservada', 0, '-'], [':restadecimal', 'Identificador', 0, '-'], [';', 'Carácter', 0, '-'], ['INS', 'Palabra reservada', 0, '-'], [':multiplicaciondecimal', 'Identificador', 0, '-'], [';', 'Carácter', 0, '-'], ['INS', 'Palabra reservada', 0, '-'], [':divisiondecimal', 'Identificador', 0, '-'], [';', 'Carácter', 0, '-'], ['INS', 'Palabra reservada', 0, '-'], [':nuevocaracter', 'Identificador', 0, '-'], [';', 'Carácter', 0, '-'], ['INS', 'Palabra reservada', 0, '-'], [':verdadero', 'Identificador', 0, '-'], [';', 'Carácter', 0, '-'], ['INS', 'Palabra reservada', 0, '-'], [':falso', 'Identificador', 0, '-'], [';', 'Carácter', 0, '-'], ['?', 'Palabra reservada', 0, '-']]
    app = interfaz_tabla()
    app.menu(token)
