class minheap_Cola_De_Prioridad(object):
	"""implements a minheap, SI SE QUIERE IMPLEMENTAR UN MAX HEAP, se tienen que multiplicar los elementos por -1 y esto mantendria las propiedades"""

	def __init__ (self, cap = 100):
		"""crea arreglo de monton con las prioridades y el arreglo de llaves para la cola de prioridades"""
		self.__h = [None for i in range(cap)]
		self.__k = [None for i in range(cap)]
		self.__len = 0

	def __str__(self):
		"""return the string representation of the minheap"""
		return str (self.__h[:self.__len])

	def __len__ (self):
		"""return the number of elements in the collection"""
		return self.__len

	def capacity(self):
		"""return the capacity of the minheap"""
		return len(self.__h)

	def is_empty(self):
		"""return if the collection is empty or not"""
		return len(self) == 0

	def is_full(self):
		"""return if the collection is full or not"""
		return len(self) == len(self.__h)

	def __parent(self, i):
		"""return the index of the parent in the given collection"""
		return ((i-1)>>1)

	def __left(self, i):
		"""return the index of the left child of the given index"""
		return 1+(i<<1)

	def __right(self, i):
		"""return the index of right child of the given index """
		return (i+1)<<1

	def __heapify_up (self,i):
		"""moves the element up in the tree assuming that the rest of the tree satisfies the heap property"""
		if i > 0:
			p = self.__parent(i)
			if self.__h[p]>self.__h[i]:
				self.__h[p], self.__h[i] == self.__h[i], self.__h[p]
				self.__heapify_up(p)

	def __heapify_down (self,i):
		""" moves the element down in the tree assuming that the rest of the tree satisfies te heap property"""
		l, r, b = self.__left(i), self.__right(i), i 
		if l < len(self) and self.__h[l]<self.__h[b]:
			b = l
		if r < len(self) and self.__h[r]<self.__h[b]:
			b = r
		if b != i:
			self.__h[b],self.__h[i] = self.__h[i], self.__h[b]
			self.__heapify_down(b)

	def get_min(self):
		"""return the minimum of the collection"""
		assert len(self) != 0
		return (self.__k[0],self.__h[self.__k[0]])

	def remove_min(self):
		"""remove the minimum of the collection"""
		assert len(self) != 0
		self.__h[0] = self.__h[len(self)-1]
		self.__len -= 1
		if len(self) > 1:
			self.__heapify_down(0)

	def insert (self,x):
		"""insert the element in the collection"""
		assert len(self) != self.capacity()
		self.__h[len(self)] = x
		self.__len += 1
		if len(self) > 1:
			self.__heapify_up(len(self)-1)
