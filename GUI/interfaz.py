#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import ttk

"Hacer for para crear los entry necesarios y ordenarlos de ser necesario dentro de un labelframe, funcion que crea cada espacio"

class Application(ttk.Frame):
    
    def __init__(self, main_window):
        super().__init__(main_window)
        main_window.title("Posicionar elementos en Tcl/Tk")
        
        main_window.configure(width=500, height=400)


        
        # Ignorar esto por el momento.
        self.pack(padx=90, pady=90)
        texto1 = ttk.Entry(self)
        texto1.pack()
        etiqueta1 = ttk.Label(self, text="etiqueta1")
        etiqueta1.pack(before=texto1)
        texto2 = ttk.Entry(self)
        texto2.pack()
        etiqueta2 = ttk.Label(self, text="etiqueta2")
        etiqueta2.pack(before=texto2)
        texto3 = ttk.Entry(self)
        texto3.pack()
        etiqueta3 = ttk.Label(self, text="etiqueta3")
        etiqueta3.pack(before=texto3)
        texto4 = ttk.Entry(self)
        texto4.pack()
        etiqueta4 = ttk.Label(self, text="etiqueta4")
        etiqueta4.pack(before=texto4)
        texto5 = ttk.Entry(self)
        texto5.pack()
        etiqueta5 = ttk.Label(self, text="etiqueta5")
        etiqueta5.pack(before=texto5)

        boton1 = ttk.Button(self, text="boton1")
        boton1.pack(pady=10)
        boton2 = ttk.Button(self, text="agregar campo")
        boton2.pack(before=boton1, side="right")

        def agregarCampo():
            nuevaEtiqueta

        

main_window = tk.Tk()
app = Application(main_window)
app.mainloop()

"""ventana = tkinter.Tk()
ventana.geometry("400x300")

boton1=tkinter.Button(ventana, text="boton1", width=10,height=5)

boton1.grid(row=0, column=0-1)
ventana.mainloop() """