#Binary Search
#Carlos Jaramillo
#Curso ADA 2016-1

from sys import stdin


def BinSearch(a,e):
    ans = -1                            #si da el caso que no este.. no se cambiar y la rta es -1
    N = len(a)
    if (N>0):                           #se revisa que el arreglo no sea vacio
        low,hi = 0,N                    #low es candidato a ser e, hi no lo es
        while low+1!=hi:                #hay al menos dos elementos en a[low,hi)
            mid = low+((hi-low)//2)    #Se encuentra punto medio ("Divide")
            if(a[mid]<=e):              #se toma ese punto medio como candidato a ser e
                low = mid       
            else:
                hi = mid                #mid no es el candidato a ser e
            if (a[low]==e):                 #se encontró un indice 
                ans = low
    return ans


def main ():
    a = [4,1,7,-2]
    x = 4
    print("Iniciando")
    print('Se busca el elemento {0} en el arreglo {1}:'.format(x,a))
    Salida = BinSearch(a,x)
    if(Salida==-1):
        print('El elemento {0} NO ESTA en el arreglo {1}:'.format(x,a))
    else:
        print('El elemento {0} ESTA en la posicion {2} del arreglo {1}:'.format(x,a,Salida+1))
    #line = stdin.readline()
    #while len(line)!=0:
    #    a = [ int(x) for x in line.split() ]
    #    print(inversions(a))
    #    line = stdin.readline()
    #print("Despues de inversion: ",a)

main()