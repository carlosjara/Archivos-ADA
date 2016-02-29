from sys import stdin

MAX = 1000
tmp = [ None for i in range(MAX)]

def inversions(a,low,hi):
    ans = 0
    if (low+1<hi):
        mid = low+((hi-low)//2)      #Se encuentra la mitad
        ans+= inversions(a,low,mid)  #dividir izq 
        ans+= inversions(a,mid,hi)   #dividir der
        ans+= crossings(a,low,mid,hi)#combinar
    return ans

def crossings(a,low,mid,hi): 
    global tmp                       #una variable global para poder mod
    ans=0
    for i in range(low,hi):
        tmp[i]=a[i]                  #copiamos a en tmp
    i,j,k = low,mid,low              #invariantes : low<=i<=mid, mid<=j<=hi, low<=k<=hi
    while k!=hi:
        if (i<mid and j<hi):         #mientras los iteradores no llegen al fin
            if (a[i]<=a[j]):         #si el valor de i en a es menor que el valor de j en a
                a[k],i = tmp[i],i+1  #itero en i...
            else:
                a[k],j,ans = tmp[j],j+1, ans+(mid-i) # HAY una inversion
        elif (j==hi):
            a[k],i = tmp[i],i+1
        else:
            a[k],j = tmp[j], j+1
        k = k+1
    return ans
    
    

def main ():
    a = [4,1,7,-2]
    print("Iniciando")
    print("Antes de inversions: ", a)
    print(inversions(a,0,len(a)))
    print("Despues de inversions: ",a)
    #line = stdin.readline()
    #while len(line)!=0:
    #    a = [ int(x) for x in line.split() ]
    #    print(inversions(a,0,len(a)))
    #    line = stdin.readline()
    #print("Despues de inversion: ",a)

main()