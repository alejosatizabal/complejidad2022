
from tkinter import *
from pymzn import dzn
from os import system

root= Tk()
root.title("ProblemaPeriodico")

buscador = LabelFrame(root, text = "Bienvenido", padx=3, pady=3)

buscador.grid(row=0, column=0, padx=5, pady=5)


etiqueta=Label(buscador, text="¿Cuantos temas quiere ingresar?").pack()
temas=Entry(buscador)
temas.pack()
"nroTemas=temas.get()"

etiqueta2=Label(buscador, text="¿Cuantas páginas quiere que tenga el periodico?").pack()
pagina=Entry(buscador, text="paginas")
pagina.pack()
"""------------------------------------------------"""
nTemasPeriodico=temas.get()
nPaginasPeriodico=pagina.get()
arrayTemasPeriodico=[]
arrayMaxPagsPeriodico=[]
arrayMinPagsPeriodico=[]
arrayLectores=[]
"""------------------------------------------------"""

"nroPagina=pagina.get()"

def nuevaVentana():
    ventanaDatos=Toplevel()
    ventanaDatos.title("ProblemaPeriodico")
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
    temasPeriodico= crearEtiquetaCampos(nroTemas, 0)
    varNombre=StringVar()
    for i in range(0,len(temasPeriodico)):
        exec("etiqueta=Label(labelTemas, text=' " + str(temasPeriodico[i]) +"').pack(padx=5, pady=5)")
        """exec(str(temasPeriodico[i]) + "=Entry(labelTemas).pack(padx=10, pady=10)")"""
        varNombre='temasPeriodico'+str(i)
        temasPeriodico[i]=Entry(labelTemas, textvariable=varNombre)
        temasPeriodico[i].pack(padx=10, pady=10)
        """print(temasPeriodico[i])"""
        """exec("varA=" + str(temasPeriodico[i]) + ".get()")"""
        """lambda : print(Nombre_tema)"""
    MaxPaginasPeriodico= crearEtiquetaCampos(nroTemas, 1)
    for i in range(0,len(MaxPaginasPeriodico)):
        exec("etiqueta=Label(labelMaxP, text=' " + str(MaxPaginasPeriodico[i]) +"').pack(padx=5, pady=5)")
        """exec(str(MaxPaginasPeriodico[i]) + "=Entry(labelMaxP).pack(padx=10, pady=10)")"""
        varNombre='MaxPaginasPeriodico'+str(i)
        MaxPaginasPeriodico[i]=Entry(labelMaxP, textvariable=varNombre)
        MaxPaginasPeriodico[i].pack(padx=10, pady=10)
    MinPaginasPeriodico= crearEtiquetaCampos(nroTemas, 2)
    for i in range(0,len(MinPaginasPeriodico)):
        exec("etiqueta=Label(labelMinP, text=' " + str(MinPaginasPeriodico[i]) +"').pack(padx=5, pady=5)")
        """exec(str(MinPaginasPeriodico[i]) + "=Entry(labelMinP).pack(padx=10, pady=10)")"""
        varNombre='MinPaginasPeriodico'+str(i)
        MinPaginasPeriodico[i]=Entry(labelMinP, textvariable=varNombre)
        MinPaginasPeriodico[i].pack(padx=10, pady=10)
    lectoresPeriodico= crearEtiquetaCampos(nroTemas, 3)
    for i in range(0,len(lectoresPeriodico)):
        exec("etiqueta=Label(labelRea, text=' " + str(lectoresPeriodico[i]) +"').pack(padx=5, pady=5)")
        """exec(str(lectoresPeriodico[i]) + "=Entry(labelRea).pack(padx=10, pady=10)")"""
        varNombre='lectoresPeriodico'+str(i)
        lectoresPeriodico[i]=Entry(labelRea, textvariable=varNombre)
        lectoresPeriodico[i].pack(padx=10, pady=10)

    def guardarDatos():
        nroTemas=temas.get()
        for i in range(0, len(temasPeriodico)):
            """print(temasPeriodico[i].get())"""
            arrayTemasPeriodico.append(str(temasPeriodico[i].get()))
            arrayMaxPagsPeriodico.append(int(MaxPaginasPeriodico[i].get()))
            arrayMinPagsPeriodico.append(int(MinPaginasPeriodico[i].get()))
            arrayLectores.append(int(lectoresPeriodico[i].get()))
        print(nroTemas)
        print(nroPagina)
        print(arrayTemasPeriodico)
        print(arrayMaxPagsPeriodico)
        print(arrayMinPagsPeriodico)
        print(arrayLectores)

        data = {
                "t": nroTemas,
                "p": nroPagina,
                "minp": arrayMinPagsPeriodico,
                "maxp": arrayMaxPagsPeriodico,
                "rea": arrayLectores,
            }
        print(data)
        with open("entrada.dzn", "w") as f:
            f.write("\n".join(dzn.dict2dzn(data)))
        system("minizinc --solver Gecode periodicoGenerico.mzn entrada.dzn > resultado.txt")

        


    
    botonEnviarDatos=Button(ventanaDatos, text="Enviar", command=guardarDatos)
    botonEnviarDatos.grid(row=1, column=3, padx=10, pady=5)

    
    


def crearEtiquetaCampos(nroCampos, id):
    variables= []
    for i in range(1, int(nroCampos)+1):
        if id==0:
            variables.append("Nombre_tema" + str(i))
        elif id==1:
            variables.append("Maximo_numero_pag_tema" + str(i))
        elif id==2:
            variables.append("Minimo_numero_pag_tema" + str(i))
        elif id==3:
            variables.append("Numero_lectores_tema" + str(i))    
    return variables



        

boton1=Button(buscador, text="Aceptar", command=nuevaVentana).pack( side="left")
boton2=Button(buscador, text="holaboton1").pack(side="right")




buscador.mainloop()
