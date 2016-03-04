#Carlos Enrique Jaramillo Aros
#0075872
#KnapSack
from sys import stdin


def KnapSack(coins,medSum):
    N = len(coins)
    tab = [ 0 for i in range(N) ]
    n,partSum=1,medSum
    while n != N+1:
        if(partSum==-1): n,partSum=n+1,medSum
        else:
            if(coins[n-1]<=medSum):
                tab[n]=max(tab[n],coins[n-1]+tab[n-coins[n-1]])
            partSum-=1
    return tab[N]

def main():
  test_cnt = int(stdin.readline())
  while test_cnt!=0:
    cantCoins = int(stdin.readline())
    coins = [ int(x) for x in stdin.readline().split() ]
    coinsSum = sum(coins)
    maxValue = KnapSack(coins,coinsSum>>1)
    Value = (coinsSum - maxValue) - maxValue
    print(Value)
    test_cnt -= 1                                 
    

main()