class dforest(object):
  """union-find with union-by-rank and path compression"""

  def __init__(self,cap=100):
    """creates a disjoint forest with the given capacity"""
    self.__parent = [ i for i in range(cap) ]
    self.__rank = [ 0 for i in range(cap) ]
    self.__ccount = cap

  def __str__(self):
    """return the string representation of the disjoint forest"""
    return str(self.__parent)

  def __len__(self):
    """return the length of the disjoint forest"""
    return len(self.__parent)

  def find(self,x):
    """return the representative of x in the disjoint forest"""
    ans = self.__parent[x]
    if ans!=x:
      self.__parent[x] = ans = self.find(ans)
    return ans

  def union(self,x,y):
    """union of the trees of x and y"""
    rx,ry = self.find(x),self.find(y)
    if rx!=ry:
      kx,ky = self.__rank[rx],self.__rank[ry]
      if kx>=ky:
        self.__parent[ry] = rx
        if kx==ky:
          self.__rank[rx] += 1
      else:
        self.__parent[rx] = ry
      self.__ccount -= 1

  def ccount(self):
    """return the number of trees in the dijoint forest"""
    return self.__ccount