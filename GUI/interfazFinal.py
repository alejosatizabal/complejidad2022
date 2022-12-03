
from tkinter import *

root= Tk()
root.title("ProblemaPeriodico")

buscador = LabelFrame(root, text = "Bienvenido", padx=3, pady=3)

buscador.grid(row=0, column=0, padx=5, pady=5)


etiqueta=Label(buscador, text="¿Cuantos temas quiere ingresar?").pack()
temas=Entry(buscador, text="temas")
temas.pack()
"nroTemas=temas.get()"

etiqueta2=Label(buscador, text="¿Cuantas páginas quiere que tenga el periodico?").pack()
pagina=Entry(buscador, text="paginas")
pagina.pack()


"nroPagina=pagina.get()"

def btnAceptar():
    ventanaDatos=Toplevel()
    ventanaDatos.title("Datos")
    labelTemas = LabelFrame(ventanaDatos, text = "Nombre de los temas", padx=3, pady=3)
    labelTemas.grid(row=0, column=0, padx=5, pady=5)
    labelMaxP = LabelFrame(ventanaDatos, text = "Número máximo de páginas", padx=3, pady=3)
    labelMaxP.grid(row=0, column=1, padx=5, pady=5)
    labelMinP = LabelFrame(ventanaDatos, text = "Número mínimo de páginas", padx=3, pady=3)
    labelMinP.grid(row=0, column=2, padx=5, pady=5)
    labelRea = LabelFrame(ventanaDatos, text = "Número de lectores", padx=3, pady=3)
    labelRea.grid(row=0, column=3, padx=5, pady=5)
    nroTemas=temas.get()
    nroPagina=pagina.get()
    temasPeriodico= crearCampos(nroTemas, 0)
    for i in range(0,len(temasPeriodico)):
        exec("etiqueta=Label(labelTemas, text=' " + str(temasPeriodico[i]) +"').pack(padx=5, pady=5)")
        exec(str(temasPeriodico[i]) + "=Entry(labelTemas).pack(padx=10, pady=10)")
    MaxPaginasPeriodico= crearCampos(nroTemas, 1)
    for i in range(0,len(MaxPaginasPeriodico)):
        exec("etiqueta=Label(labelMaxP, text=' " + str(MaxPaginasPeriodico[i]) +"').pack(padx=5, pady=5)")
        exec(str(MaxPaginasPeriodico[i]) + "=Entry(labelMaxP).pack(padx=10, pady=10)")
    MinPaginasPeriodico= crearCampos(nroTemas, 2)
    for i in range(0,len(MinPaginasPeriodico)):
        exec("etiqueta=Label(labelMinP, text=' " + str(MinPaginasPeriodico[i]) +"').pack(padx=5, pady=5)")
        exec(str(MinPaginasPeriodico[i]) + "=Entry(labelMinP).pack(padx=10, pady=10)")
    lectoresPeriodico= crearCampos(nroTemas, 3)
    for i in range(0,len(lectoresPeriodico)):
        exec("etiqueta=Label(labelRea, text=' " + str(lectoresPeriodico[i]) +"').pack(padx=5, pady=5)")
        exec(str(lectoresPeriodico[i]) + "=Entry(labelRea).pack(padx=10, pady=10)")


def crearCampos(NroCampos, id):
    variables= []
    for i in range(1, int(NroCampos)+1):
        if id==0:
            variables.append("Nombre_tema" + str(i))
        elif id==1:
            variables.append("Maximo_numero_pag_tema" + str(i))
        elif id==2:
            variables.append("Minimo_numero_pag_tema" + str(i))
        elif id==3:
            variables.append("Numero_lectores_tema" + str(i))
        """variables.append("etiqueta" + str(i) + "=Label(ventanaDatos)")"""
        
    return variables






boton1=Button(buscador, text="Aceptar", command=btnAceptar).pack( side="left")
boton2=Button(buscador, text="holaboton1").pack(side="right")



buscador.mainloop()
