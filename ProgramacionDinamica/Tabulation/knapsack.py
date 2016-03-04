#Carlos Enrique Jaramillo Aros
#0075872
#KnapSack
from sys import stdin


def KnapSack(v,m,W):
    N = len(v)
    tab = [ 0 for i in range(W) ]
    n,w=1,W
    while n != N+1:
        if(w==-1): n,w=n+1,W
        else:
            if(m[n-1]<=w):
                tab[w]=max(tab[w],v[n-1]+tab[w-m[n-1]])
        w-=1
    return tab[W]

def main():
  test_cnt = int(stdin.readline())
  while test_cnt!=0:
    #maxCoin = int(stdin.readline())
    v = [ int(x) for x in stdin.readline().split() ]
    #maxCoin = int(stdin.readline())
    w = [ int(x) for x in stdin.readline().split() ]
    W = int(stdin.readline())
    maxValue = KnapSack(v,w,W)
    test_cnt -= 1                                 
    

main()