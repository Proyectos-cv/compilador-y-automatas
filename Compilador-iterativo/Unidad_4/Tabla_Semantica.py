import pandas as pd
from pandastable import Table, TableModel
from tkinter import *

def load_excel_data(filepath):
    # Carga los datos de Excel en un DataFrame de pandas
    df = pd.read_excel(filepath)
    return df

def show_data_in_tkinter(df):
    # Crea una ventana de Tkinter
    root = Tk()
    
    # Cambia el tamaño de la ventana
    root.geometry('1400x700')
    root.title('Tabla Semántica')
    
    # Crea un frame
    frame = Frame(root)
    frame.pack(fill=BOTH, expand=True)

    pt = Table(frame, dataframe=df, showtoolbar=True, showstatusbar=True, maxcellwidth=650)
    pt.adjustColumnWidths()
    pt.show()


    # Inicia el bucle principal de Tkinter
    root.mainloop()
def correr():
    # Ruta al archivo de Excel
    filepath = 'C:\\Users\\ALEXG\\OneDrive\\Documentos\\Compilador-1\\Regla-Semantica.xlsx'

    # Carga los datos de Excel
    df = load_excel_data(filepath)

    # Muestra los datos en Tkinter
    show_data_in_tkinter(df)
