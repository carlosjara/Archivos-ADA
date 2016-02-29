#Inseriton Sort
#Carlos Jaramillo
#Curso ADA 2016-1
#Se agrega main para leer archivo con python3 InsertionSort1.py < InsertionSort1.in
#Se agrega main para leer archivo con python3 InsertionSort1.py < InsertionSort1.in > InsertionSort.out


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
        print(A)
        j+=1
    return A


def main ():
    a = [5, 2, 4, 6, 1, 3]
    print("Iniciando")
    print(insertionSort1(a))
    #line = stdin.readline()
    #while len(line)!=0:
    #    a = [ int(x) for x in line.split() ]
    #    print(insertionSort1(a))
    #    line = stdin.readline()

main()
    
