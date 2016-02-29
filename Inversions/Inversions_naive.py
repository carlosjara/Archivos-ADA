from sys import stdin

MAX = 1000
tmp = [ None for i in range(MAX)]

def inversions(a):
    ans = 0
    for i in range(0,len(a)):
        for j in range(i+1,len(a)):
            if(a[i]>a[j]):
                temp = a[i]
                a[i]=a[j]
                a[j] = temp
                ans +=1
    return ans


def main ():
    a = [4,1,7,-2]
    print("Iniciando")
    print("Antes de inversions: ", a)
    print(inversions(a))
    print("Despues de inversions: ",a)
    #line = stdin.readline()
    #while len(line)!=0:
    #    a = [ int(x) for x in line.split() ]
    #    mergesort(a,0,len(a))
    #    line = stdin.readline()
    #print("Despues de mergesort: ",a)

main()