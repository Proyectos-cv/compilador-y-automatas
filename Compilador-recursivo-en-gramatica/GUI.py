from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from análisis_lexico import procedimiento
from tokens import procedimientos
from sintactico import sintactico
from tkinter import messagebox

class interfaz:
    def menu(self):
        mainwindow = Tk()
        self.bandera = False
        ancho_ventana = 1100
        alto_ventana = 750
        x_ventana = mainwindow.winfo_screenwidth() // 2 - ancho_ventana // 2
        y_ventana = mainwindow.winfo_screenheight()// 2 - alto_ventana // 2 - 42
        posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
        mainwindow.geometry(posicion)

        mainwindow.title('Compilador')
        mainwindow.config(bg='#7FADA9')

        self.text_area = Text(mainwindow, width=80, height=30, bg='#F2F2F2', fg='#000000')
        self.text_area.grid(row=0, column=0, padx=10, pady=10, rowspan=10)  
        self.text_area.config(font=("JetBrains Mono", 13))
        """ self.text_area.bind("<Return>", self.on_event_pressed) """

        self.label = Label(mainwindow, text='Esperando resultados...', bg='#7FADA9', fg='#000000')
        #self.label = Label(mainwindow, text='Resultados apropiados', bg='#7FADA9', fg='#000000')
        self.label.config(font=("JetBrains Mono", 20))
        self.label.grid(row=10, column=0, padx=10, pady=10)
        
        cargar = Button(mainwindow, text='Cargar programa', width=25, height=2, bg='#597a77', fg='#FFF', activebackground='#b7f9f3', activeforeground='#000', command=self.call_cargar)
        cargar.grid(row=0, column=1, padx=40, pady=10)

        analizador_lexico = Button(mainwindow, text='Analizador léxico', width=25, height=2, bg='#597a77', fg='#FFF', activebackground='#b7f9f3', activeforeground='#000', command=self.call_analizador)
        analizador_lexico.grid(row=1, column=1, padx=40, pady=10)

        analizador_sintactico = Button(mainwindow, text='Analizador sintáctico', width=25, height=2, bg='#597a77', fg='#FFF', activebackground='#b7f9f3', activeforeground='#000', command = self.call_sintactico)
        analizador_sintactico.grid(row=2, column=1, padx=40, pady=10)

        analizador_semantico = Button(mainwindow, text='Analizador semántico', width=25, height=2, state="disabled", bg='#597a77', fg='#FFF', activebackground='#b7f9f3', activeforeground='#000')
        analizador_semantico.grid(row=3, column=1, padx=40, pady=10)

        generador_codigo = Button(mainwindow, text='Generador de código', width=25, height=2, state="disabled", bg='#597a77', fg='#FFF', activebackground='#b7f9f3', activeforeground='#000')
        generador_codigo.grid(row=4, column=1, padx=40, pady=10)

        optimizador_codigo = Button(mainwindow, text='Optimizador de código', width=25, height=2, state="disabled", bg='#597a77', fg='#FFF', activebackground='#b7f9f3', activeforeground='#000')
        optimizador_codigo.grid(row=5, column=1, padx=40, pady=10)

        generador_fuente = Button(mainwindow, text='Generador de codigo fuente', width=25, height=2, state="disabled", bg='#597a77', fg='#FFF', activebackground='#b7f9f3', activeforeground='#000')
        generador_fuente.grid(row=6, column=1, padx=40, pady=10)

        guardar = Button(mainwindow, text='Guardar archivo', width=25, height=2, bg='#597a77', fg='#FFF', activebackground='#b7f9f3', activeforeground='#000', command=self.call_guardar)
        guardar.grid(row=7, column=1, padx=40, pady=10)

        """ mainwindow.resizable(0,0) """
        mainwindow.mainloop()
        # Obtenemos la posición del cursor en el text_area
        pos_cursor = self.text_area.index(INSERT)

        # Obtenemos el texto previo al cursor
        texto_anterior = self.text_area.get('1.0', pos_cursor)

        # Obtenemos la última línea del texto previo al cursor
        ultima_linea = texto_anterior.split('\n')[-1]

        # Agregamos 4 espacios al inicio de la última línea si es que no está vacía
        if ultima_linea.strip():
            self.text_area.insert(INSERT, '\n' + ' ' * 4)
        #si esta vacía solo damos un salto de línea
        else:
            self.text_area.insert(INSERT, '\n')
        
        # Devolvemos 'break' para evitar que se agregue un salto de línea adicional
        return 'break'

    def call_guardar(self):
        print("Guardar programa")
        archivo = filedialog.asksaveasfilename(initialdir = "../",title = "Select file",filetypes = (("txt files","*.txt"),("all files","*.*")))
        archivo = open(archivo, "w", encoding="utf-8")
        contenido = self.text_area.get("1.0", "end-1c")
        archivo.write(contenido)
        archivo.close()
        return 'break'

    def call_cargar(self):
        print("Cargar programa")
        archivo = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("txt files","*.txt"),("all files","*.*")))
        archivo = open(archivo, "r", encoding="utf-8")
        contenido = archivo.read()
        archivo.close()
        self.text_area.insert(INSERT, contenido)
        return 'break'

    def call_analizador(self):
        print("Analizador léxico")
        contenido = self.text_area.get("1.0", "end-1c")
        if contenido == "":
            messagebox.showwarning("Advertencia", "La caja de texto está vacía")
        else:
            self.bandera = True
            obj = procedimiento()
            obj.split_texto_into_lines(contenido)
        
            #extrae lo que tiene el archivo results.txt e insetalo en self.label
            archivo = open("results.txt", "r", encoding="utf-8")
            contenido = archivo.read()
            archivo.close()
            self.label.config(text=contenido, font=("JetBrains Mono", 13))

            obj.send_table()

    def call_sintactico(self):
        texto = self.label.cget('text')
        texto = texto.rstrip()

        contenido = self.text_area.get("1.0", "end-1c")
        if texto != "Análisis léxico exitoso":
            messagebox.showinfo("Alerta", "Análisis léxico fallido")
        elif contenido == "":
            messagebox.showwarning("Advertencia", "La caja de texto está vacía")
        elif self.bandera == False:
            messagebox.showinfo("Alerta", "primero tienes de analizar lexicamente")
        else:
            print("Analizador sintactico")
            contenido = self.text_area.get("1.0", "end-1c")
            obj = procedimientos()
            i = obj.split_texto_into_lines(contenido)

            #manda a otro archivo la lista con los tokens para hacer el analisis
            sintactic = sintactico()
            sintactic.analizar(i)

if __name__ == '__main__':
    app = interfaz()
    app.menu()