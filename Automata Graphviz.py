from graphviz import Digraph
from pythonds.basic import Stack
from os import system

   
def fun_get_inicial():
    return(input('\nIngrese el estado inicial: '))


def fun_get_simbolo_pila():
    return(input('\nIngrese simbolo incial pila: '))


def fun_get_simbolo_cinta():
    return(input('\nIngrese simbolo de cinta: '))


def fun_get_alfabeto():
    alfabeto=list(map(str,input("\nIngrese el alfabeto: ").strip().split()))
    return alfabeto


def fun_get_alfabeto_pila():
    alfabeto=list(map(str,input("\nIngrese el alfabeto de la pila: ").strip().split()))
    return alfabeto


def fun_get_alfabeto_cinta():
    alfabeto=list(map(str,input("\nIngrese el alfabeto de la cinta: ").strip().split()))
    return alfabeto


def fun_get_estados():
    estados=list(map(str,input("\nIngrese los estados: ").strip().split()))
    return estados


def fun_get_transicion():
    listadoEstados = []
    listadoTrans = []
    print('Formato: q1,a=q2 separado por espacio entre transciciones')
    transiciones=list(map(str,input("\nIngrese las transiciones: ").strip().split()))
    
    for i in transiciones:
        listadoEstados.append(i.split(',',1))
        
    for cosa in (i[1] for i in listadoEstados):
        listadoTrans.append(cosa.split('=',1))
    
    return listadoEstados,listadoTrans;


def fun_get_transicion_pila():
    listadoGeneral = []
    listadoEntrada = []
    listadoSalida = []
    print('Formato: estado1,entrada,desapilar=estado2,apilar separado por espacio entre transciciones')
    transiciones=list(map(str,input("\nIngrese las transiciones: ").strip().split()))
    
    for i in transiciones:
        listadoGeneral.append(i.split('=',1))
    for cosa in (i[0] for i in listadoGeneral):
        listadoEntrada.append(cosa.split(',',2))
    for cosa in (i[1] for i in listadoGeneral):
        listadoSalida.append(cosa.split(',',1))
    return listadoGeneral,listadoEntrada,listadoSalida;


def fun_get_transicion_turing():
    listadoGeneral = []
    listadoEntrada = []
    listadoSalida = []
    print('Formato: estado1,leerCinta=estado2,escribirCinta,direcccion(R/L) separado por espacio entre transciciones')
    transiciones = list(map(str, input("\nIngrese las transiciones: ").strip().split()))

    for i in transiciones:
        listadoGeneral.append(i.split('=', 1))
    for cosa in (i[0] for i in listadoGeneral):
        listadoEntrada.append(cosa.split(',', 1))
    for cosa in (i[1] for i in listadoGeneral):
        listadoSalida.append(cosa.split(',', 2))
    return listadoGeneral, listadoEntrada, listadoSalida;


def fun_get_cadena_entrada():
    cadena=list(map(str,input("\nIngrese cadena de entrada: ").strip().split()))
    return cadena


def fun_get_cinta_entrada():
    cadena=list(map(str,input("\nIngrese cadena de entrada: ").strip().split()))
    return cadena


def fun_get_estados_finales():
    final=list(map(str,input("\nIngrese los estados finales: ").strip().split()))
    return final


def fun_AFND():
    #Recoleccion de datos
    estados = fun_get_estados()
    alfabeto = fun_get_alfabeto()
    inicial = fun_get_inicial()
    finales = fun_get_estados_finales()
    transEstados,transValores = fun_get_transicion()
    
    #Creacion de diagrama
    dot = Digraph(comment="AFND")
    dot.attr(rankdir='LR',size='5')

    #Creacion de nodo en blanco para indicar inicio de automata
    dot.attr('node',shape='none',height='.0',width='.0',label="")
    dot.node('n0')
    
    # Creacion de nodos con doble circulo para la aceptacion.
    dot.attr('node',shape='doublecircle')
    for i in finales:
        dot.node(i,i)

    # Creacion de nodos con circulo sencillo para los demas estados
    dot.attr('node',shape='circle')
    for i in estados:
        dot.node(i,i)

    # Creacion de conexiones entre nodos
    for i in range(len(transEstados)):
        dot.edge(transEstados[i][0],transValores[i][1],label=transValores[i][0])

    # Conexion del nodo invisible con el estado incial.
    dot.edge('n0',inicial)

    # Dibujar grafico y mostrarlo
    dot.render('archivos/AFND.gv',view=True)


def fun_pila():
    # Recoleccion de datos
    estados = fun_get_estados()
    alfabetoEntrada=fun_get_alfabeto()
    alfabetoCinta=fun_get_alfabeto_cinta()
    estadoActual=fun_get_inicial()
    finales=fun_get_estados_finales()
    simbolo=fun_get_simbolo_pila()
    general,entrada,salida=fun_get_transicion_pila()
    cadenaEntrada=fun_get_cadena_entrada()

    # Creacion de diagrama
    dot = Digraph(comment="ADP")
    dot.attr(rankdir='LR',size='5')

    # Creacion de nodo en blanco para indicar inicio de automata
    dot.attr('node',shape='none',height='.0',width='.0',label="")
    dot.node('n0')

    # Creacion de nodos con doble circulo para la aceptacion.
    dot.attr('node',shape='doublecircle')
    for i in finales:
        dot.node(i,i)

    # Creacion de nodos con circulo sencillo para los demas estados
    dot.attr('node',shape='circle')
    for i in estados:
        dot.node(i,i)

    # Creacion de conexiones entre nodos
    for i in range(len(general)):
        etiqueta = str(entrada[i][1]) + ',' + str(entrada[i][2] + ';' + str(salida[i][1]))
        dot.edge(entrada[i][0],salida[i][0],label=etiqueta)

    # Conexion del nodo invisible con el estado incial.
    dot.edge('n0',estadoActual)

    # Dibujar grafico y mostrarlo
    dot.render('archivos/ADP.gv',view=True)

    pila = []
    pila.append(simbolo)
    print('Valor pila antes de empezar: ', pila)
    for i in range(len(cadenaEntrada)):
        print('Cadena de entrada a trabajar: ',cadenaEntrada[i])
        for j in range(len(entrada)):
            if estadoActual == entrada[j][0]:
                if cadenaEntrada[i] == entrada[j][1]:
                    if entrada[j][2] == 'e':
                        estadoActual = salida[j][0]
                    else:
                        if len(pila) == 0:
                            estadoActual = salida[j][0]
                            print('La pila esta vacia y hay elementos que sacar')
                            fun_salir('Cadena no aceptada')
                        else:
                            desapilado = pila.pop()
                            if entrada[j][2] == desapilado:
                                estadoActual = salida[j][0]
                                if len(pila) == 0:
                                    print('La pila esta vacia 2: \n')
                            else:
                                pila.append(desapilado)
                                print('Valor a desapilar no existe en la pila')
                                fun_salir('Cadena no aceptada')
                    if salida[j][1] == 'e':
                        print()
                    else:
                        pila.append(salida[j][1])
                        print('Valor pila al terminar cadena: ', str(pila))
                else:
                    print()
            else:
                print()
    print('Valor de la pila al terminar la cadena de entrada: ',pila)
    print('Valor del estado actual al terminar la cadena: ' ,estadoActual)


def fun_turing():
    print ("\nOpcion Turing seleccionada\n")
    estados = fun_get_estados()
    alfabetoEntrada = fun_get_alfabeto()
    alfabetoCinta=fun_get_alfabeto_cinta()
    simbolo = fun_get_simbolo_cinta()
    estadoActual = fun_get_inicial()
    finales = fun_get_estados_finales()
    general,entrada,salida = fun_get_transicion_turing()
    cintaEntrada=fun_get_cinta_entrada()
    indice=0

    # Creacion de diagrama
    dot = Digraph(comment="Turing")
    dot.attr(rankdir='LR',size='5')

    # Creacion de nodo en blanco para indicar inicio de automata
    dot.attr('node',shape='none',height='.0',width='.0',label="")
    dot.node('n0')

    # Creacion de nodos con doble circulo para la aceptacion.
    dot.attr('node',shape='doublecircle')
    for i in finales:
        dot.node(i,i)

    # Creacion de nodos con circulo sencillo para los demas estados
    dot.attr('node',shape='circle')
    for i in estados:
        dot.node(i,i)

    # Creacion de conexiones entre nodos
    for i in range(len(general)):
        etiqueta = str(entrada[i][1]) + ';' + str(salida[i][1] + ',' + str(salida[i][2]))
        dot.edge(entrada[i][0],salida[i][0],label=etiqueta)

    # Conexion del nodo invisible con el estado incial.
    dot.edge('n0',estadoActual)

    # Dibujar grafico y mostrarlo
    dot.render('archivos/Turing.gv',view=True)

    print('Valor de la cinta antes de empezar: ', cintaEntrada)
    print('Ubicado actualmente en indice ' + str(indice) + ' con valor: ' ,cintaEntrada[indice])

    while estadoActual not in finales:
        for i in range(len(entrada)):
            if estadoActual == entrada[i][0]:
                if cintaEntrada[indice] == entrada[i][1]:
                    print('Ubicado actualmente en indice ' + str(indice) + ' con valor: ', cintaEntrada[indice])
                    print('Adentro adentro del if')
                    estadoActual = salida[i][0]
                    cintaEntrada[indice] = salida[i][0]
                    if indice < len(cintaEntrada)-1:
                        if salida[i][2] == 'R':
                            indice = indice + 1
                            print('Valor actual indice+1: ',indice)
                        elif salida[i][2] == 'L':
                            indice = indice - 1
                            print('Valor actual indice-1: ',indice)
                        else:
                            print('Simbolo L o R no encontrado')
                    elif indice == len(cintaEntrada) or indice == -1:
                        fun_salir('Finalizacion de ejecucion')


        print('Valor de la cinta al final: ', cintaEntrada)
        fun_salir('Finalizacion de ejecucion')

def fun_salir(mensaje):
    print('\n'+mensaje+'\n')
    raise SystemExit

def invalido():
    print ("Opcion Invalida")
    
menu= {"1":("AFND",fun_AFND),
       "2":("Pila",fun_pila),
       "3":("Turing",fun_turing),
       "4":("Salir",fun_salir)
       }
system('cls')
print('Bienvenido al programa para graficar automatas.\n')
print('Creditos:\nMiguel Angel Leon Sagastume - 0910-15-19360\nUniversidad Mariano Galvez de Guatemala\nSede Antigua Guatemala\n')

for key in sorted(menu.keys()):
    print (key+":" + menu[key][0])
    

seleccion = input("Elige una opción: ")

menu.get(seleccion,[None,invalido])[1]()
