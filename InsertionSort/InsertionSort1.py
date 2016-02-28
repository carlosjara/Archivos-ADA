from sys import stdin

def insertionSort1(A):
    largo= len(A)
    j=1
    while j<largo:
        key = A[j]
        i=j-1
        #print('i= {0}, A[i]= {1}, key= {2}'.format(i,A[i],key))
        while (i>=0 and A[i]>key):
            print("mayor")
            A[i+1] = A[i]
            i= i-1
        A[i+1]=key
        j+=1
    return A


def main ():
    a = [22,3,6,7]
    print("Iniciando")
    print(insertionSort1(a))

main()
    
