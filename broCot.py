#The Stern-Brocot Number System
#Carlos Jaramillo
#Curso ADA 2016-1

from sys import stdin


def broCot(a,b):                     # a numerador, b denominador
    salida = ""
    Lni,Lnd = 0,1                    # lni Limite Numerador Izquierdo, lnd Limite Numerador Derecho
    Ldi,Ldd = 1,0                    # ldd Limite Denominador Izquierdo, ldd Limite Denominador Derecho
    m,n = 1,1                        # valor de analisis actual
    while a!=m or b!=n:
        if (a/b < m/n):
            tmp1,tmp2 = m,n
            Lnd,Ldd = tmp1,tmp2
            m,n = (Lni+Lnd),(Ldi+Ldd)
            salida+="L"
        else:
            tmp1,tmp2 = m,n
            Lni,Ldi = tmp1,tmp2
            m,n = (Lni+Lnd),(Ldi+Ldd)
            salida+="R"
    return (salida)


def main ():
    Valores = [ int(x) for x in stdin.readline().split() ]
    while Valores[0] != 1 or Valores[1] != 1:
        print(broCot(Valores[0],Valores[1]))
        Valores = [ int(x) for x in stdin.readline().split() ]

main()