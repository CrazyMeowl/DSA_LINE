from itertools import groupby

x = [["   ",0],["red",2],["red",2],["red",2],["red",2],["red",2],["red",2],["red",2],["   ",0]]

def searchdupe(inList):
	counter = 0
	for i,j in groupby(inList):
		length = len(list(j))
		print('index: ',counter,i,length)
		if length >= 5:
			index = counter
			indexcounter = index + length 
		counter += length
	newlist = []
	for i in range(index,indexcounter):
		newlist.append(i)
	return newlist
print(searchdupe(x))