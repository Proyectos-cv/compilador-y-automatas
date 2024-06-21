import tkinter as tk
from maquina_de_turing import maquina

#funcion para mandar los datos de la caja al archivo de maquina_de_turing
def evaluar1():
    m = maquina()
    a = entrada1.get()
    b = entrada2.get()
    m.turing(a,b)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Ventana de ejemplo")

# Crear los labels
label1 = tk.Label(ventana, text="Texto 1:")
label1.pack()

# Crear la caja de texto 1
entrada1 = tk.Entry(ventana)
entrada1.pack()

label2 = tk.Label(ventana, text="Texto 2:")
label2.pack()

# Crear la caja de texto 2
entrada2 = tk.Entry(ventana)
entrada2.pack()

# Crear el área de texto
resultado = tk.Text(ventana, height=10, width=30)
resultado.config(state="disabled")
resultado.pack()

# Crear el botón
boton = tk.Button(ventana, text="Evaluar", command=evaluar1)
boton.pack()

# Iniciar el bucle de eventos
ventana.mainloop()


    