from sys import stdin

MAX = 100000
tmp = [ None for i in range(MAX) ]

def mergesort(a,low,hi):
    global tmp,MAX
    assert 0 <= low <= hi <= len(a) <= MAX
    if low+1<hi:
        mid = low +((hi-low)//2)
        mergesort(a,low,mid)
        mergesort(a,mid,hi)
        merge(a,low,mid,hi)

def merge(a,low,mid,hi):
    global tmp
    for k in range(low,hi):
        tmp[k] = a[k]
    l,r,k = low,mid,low
    
    while k!=hi:
        if l==mid:
            a[k] = tmp[r] ; r += 1
        elif r==hi:
            a[k] = tmp[l] ; l += 1
        else:
            if tmp[l] <= tmp[r]:
                a[k] = tmp[l] ; l += 1
            else:
                a[k] = tmp[r] ; r += 1
        k+=1
    
def main ():
    a = [5, 2, 4, 6, 1, 3]
    print("Iniciando")
    print("Antes de mergesort: ", a)
    mergesort(a,0,len(a))
    print("Despues de mergesort: ",a)
    #line = stdin.readline()
    #while len(line)!=0:
    #    a = [ int(x) for x in line.split() ]
    #    mergesort(a,0,len(a))
    #    line = stdin.readline()
    #print("Despues de mergesort: ",a)

main()