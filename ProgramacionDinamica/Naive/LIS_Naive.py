from sys import stdin

## Implementacion de LIS Naive recorriendo con while y for

#Usando WHILE
def LIS_naive1(a,n):
    ans = None 
    if(n == 0): ans = 1
    else:
        ans,i = 0,0
        while i<n:
            if(a[i]<=a[n]):
                ans = max(ans,LIS_naive1(a,i))
            i+=1
        ans = ans+1
    return ans
    
#Usando FOR
def LIS_naive2(a,n):
    ans = None 
    if(n == 0): ans = 1
    else:
        ans= 0
        for i in range (0,n):
            if(a[i]<=a[n]):
                ans = max(ans,LIS_naive2(a,i))
        ans = ans+1
    return ans


def main ():
    a = [2, 3, 7, 10, 15]
    #a = [0, 8, 4, 12, 2, 10, 6, 14, 6, 9, 5]
    #a = [15, 10, 7, 3, 2]
    #a= [1,9,4,5]
    print("Iniciando")
    rta2 = LIS_naive2(a,len(a)-1)
    rta1 = LIS_naive1(a,len(a)-1)
    print("Despues de LIS_naive1: ",a,"Respuesta: ",rta1)
    print("Despues de LIS_naive2: ",a,"Respuesta: ",rta2)
    #line = stdin.readline()
    #while len(line)!=0:
    #    a = [ int(x) for x in line.split() ]
    #    print(inversions(a))
    #    line = stdin.readline()
    #print("Despues de inversion: ",a)

main()