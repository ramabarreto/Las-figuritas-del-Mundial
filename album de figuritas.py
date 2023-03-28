# Las figuritas del Mundial.
# El álbum de figuritas del Mundial tiene aproximadamente 600 figuritas. Se sabe que
# no hay figuritas difíciles (todas las figuritas tienen la misma posibilidad de salir).
# Se quiere realizar un programa para calcular cuántas figuritas es necesario comprar
# para completar el álbum (A medida que vamos completando el álbum, las figuritas que
# compramos tienen más posibilidades de estar repetidas). Para ello, realizar un programa
# que simule la compra de figuritas hasta completar el álbum (Se puede suponer que se compran
# de a una) y cuente la cantidad de figuritas compradas. Repetir el ciclo 100 veces e
# indicar el promedio de figuritas compradas para completar el álbum.
from random import randint
figuritas = 15
ciclos = 10
def buscar(lista, elemento):
    for i in range (0, len(lista)):
        if lista[i] == elemento:
            return -1
    return 1
def programa():
    album = [0]
    albumcompleto = [0]
    cont1 = 0
    for i in range (1, figuritas):
        cont1 = cont1 + 1
        albumcompleto.append(cont1)
    cont2 = 0
    acumulador = 0
    for i in range (0, ciclos):
        cont2 = 0
        album = [0]
        while len(album) != len(albumcompleto):
            n = randint(1, figuritas-1)
            cont2 = cont2 + 1
            nola = buscar(album, n)
            if nola == 1:
                album.append(n)
            album.sort()
        print(cont2)
        acumulador = cont2 + acumulador
    prom = (acumulador/ciclos)
    print("En promedio, la cantidad de paquetes comprados para completar el album fue de:", prom)
programa()       
    