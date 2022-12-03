from tkinter import *
root = Tk()

entrada = Entry(root)
entrada.grid(row=0, column=0)

def click_boton():
	texto = Label(root,
				 text=f'Se almacenó "{entrada.get()}" correctamente').grid(row=2, column=0)

boton1 = Button(root,
				text="Envíar",
				bg="red",
				padx=50,
				pady=10,
				command=click_boton).grid(row=1, column=0)

root.mainloop()