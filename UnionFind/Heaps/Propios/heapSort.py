from minheap import minheap

def heapsort(a):
	h = minheap(len(a))
	for x in a : h.insert(x)
	for i in range (len(a)):
		a[i] = h.get_min()
		h.remove_min()
