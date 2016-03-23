from sys import stdin

class dforest(object):
  """union-find with union-by-rank and path compression"""

  def __init__(self,cap,d):
    """crea el dforest con una capacidad dada y el arreglo de deudas"""
    self.__parent = [ i for i in range(cap) ]
    self.__rank = [ 0 for i in range(cap) ]
    self.__ccount = cap
    self.__debt = d

  def __str__(self):
    """devuelve la represetacion en arreglo del dforest"""
    return str(self.__parent)

  def __len__(self):
    """devuelve el largo del dforest"""
    return len(self.__parent)

  def find(self,x):
    """devuelve el respresentante de x en dforest"""
    ans = self.__parent[x]
    if ans!=x:
      self.__parent[x] = ans = self.find(ans)
    return ans

  def union(self,x,y):
    """union de árboles x e y"""
    rx,ry = self.find(x),self.find(y)
    if rx!=ry:
      kx,ky = self.__rank[rx],self.__rank[ry]
      if kx>=ky:
        self.__debt[rx] = self.__debt[rx] + self.__debt[ry]
        self.__parent[ry] = rx
        if kx==ky:
          self.__rank[rx] += 1
      else:
        self.__debt[ry] = self.__debt[rx] + self.__debt[ry]
        self.__parent[rx] = ry
      self.__ccount -= 1

  def ccount(self):
    """devuelve el numero de árboles en el dforest"""
    return self.__ccount
    
  def balance(self):
    """revisa que las deudas sean cero para determinar balance"""
    inicio = 0
    balanced = True
    while inicio < len(self.__parent):
      if(self.__debt[self.find(inicio)]!=0):
        balanced = False
      inicio+=1
    return balanced
      
    
def main():
    casos = int(stdin.readline())
    while casos!=0:
        relaciones = [ int(x) for x in stdin.readline().split() ]
        #print(relaciones)
        pers = relaciones[0]
        frnds = relaciones[1]
        personas = []
        while (pers>0):
          personas.append(int(stdin.readline()))
          pers-=1
        #print(personas)
        pedro = dforest(len(personas),personas)
        while (frnds>0):
          amistades = [ int(x) for x in stdin.readline().split() ]
          #print(amistades)
          pedro.union(amistades[0],amistades[1])        
          frnds-=1
        if(pedro.balance()):
          print("POSSIBLE")
        else:
          print("IMPOSSIBLE")
        casos-=1
main()