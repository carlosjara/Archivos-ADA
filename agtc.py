#Carlos Enrique Jaramillo Aros
#0075872
#AGTC

from sys import stdin

def agct(N,C1,M,C2):
    arreglo1,arreglo2 = C1[1],C2[1]
    tab = [ [ 0 for n in range(N+1)] for m in range(M+1)] 
    for m in range(1,M+1):
        tab[m][0] = m
        for n in range(1,N+1):
            tab[0][n] = n
            if(arreglo1[n-1]!=arreglo2[m-1]):
                igual= 1
            else:
                igual = 0
            tab[m][n] = min(tab[m-1][n]+1, tab[m][n-1]+1, tab[m-1][n-1]+igual)
            
    return tab[M][N]


def main ():
    Caracter1 = [ x for x in stdin.readline().split() ]
    while len(Caracter1)!=0:
        Caracter2 = [ x for x in stdin.readline().split() ]
        LargoC1,LargoC2 = int(Caracter1[0]), int(Caracter2[0])
        print(agct(LargoC1,Caracter1,LargoC2,Caracter2))
        Caracter1 = [ x for x in stdin.readline().split() ]        
main()