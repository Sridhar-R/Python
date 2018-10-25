import math
def bin_search(li,element):
	bottom=0
	top=len(li)-1
	index=-1
	while top>=bottom and index==-1:
		mid=int(math.floor(top+bottom)/2.0)
		if li[mid]==element:
			index=mid
		elif li[mid]>element:
			top=mid-1
		else:
			bottom=mid+1
	return index

li=[8,9,3,5,4,12,6,19,23,15]
print(bin_search(li,19))
print(bin_search(li,12))
		