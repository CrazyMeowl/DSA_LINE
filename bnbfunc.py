from itertools import groupby


def canpath(in1,in2,inboard):
	board = createtempboard(inboard)
	startY,startX = in1
	endY,endX = in2
	count = 0
	for i in board:
		for j in i:
			if j == 0:
				count == count + 1
	if board[endY][endX] == 1:
		return False
	if endX == startX and startY == endY:
		return True
	
	visitedlist = [(startY,startX)]
	nextlist = []
	for i in findnextpath((startY,startX),board):
		nextlist.append(i)

	iteration = 1
	while (endY,endX) not in nextlist and (endY,endX) not in visitedlist:
		afternextlist = []
		for i in nextlist:
			for j in findnextpath(i,board):
				if j not in visitedlist and j not in afternextlist:
					afternextlist.append(j)



		for _ in nextlist:
			visitedlist.append(_)
		nextlist = afternextlist.copy()
		iteration += 1
		#print(iteration)
		#print(visitedlist)
		#print(nextlist)
		#print(afternextlist)

		if afternextlist == []:
			return False

		#if iteration > 16:
		#	return False
		#	break
	return True

def findnextpath(coord,board):
	(Y,X) = coord
	nextpath = []
	if Y+1 >= 0 and Y+1 <=8:
		if board[Y + 1][X] == 0:
			nextpath.append((Y+1,X))
	if Y-1 >= 0 and Y-1 <=8:
		if board[Y - 1][X] == 0:
			nextpath.append((Y-1,X))
	if X+1 >= 0 and X+1 <=8:
		if board[Y][X + 1] == 0: 
			nextpath.append((Y,X + 1))
	if X-1 >= 0 and X-1 <=8:
		if board[Y][X - 1] == 0:
			nextpath.append((Y,X - 1))
	return nextpath

def createtempboard(board): #tempboard for pathfinding
	tempboard = []
	for i in board :
		tempi = []
		for _ in i:

			if _[1] == 0 or _[1] == 1:
				tempi.append(0)

			elif _[1] == 2 :
				tempi.append(1)
		tempboard.append(tempi)
	return tempboard

def createtempboard2(board): #tempboard for color checking
	tempboard = []
	for i in board :
		tempi = []
		for _ in i:

			if _[1] == 0 or _[1] == 1:
				tempi.append('   ')

			elif _[1] == 2 :
				tempi.append(_[0])
		tempboard.append(tempi)
	return tempboard

def searchdupe(inList):
	counter = 0
	for i,j in groupby(inList):
		#print(i)
		length = len(list(j))
		#print('index: ',counter,i,length)
		if i != "   ":
			if length >= 5:

				index = counter
				indexcounter = index + length
				newlist = []
				for i in range(index,indexcounter):
					newlist.append(i)
				return newlist 
		counter += length

def awd(inList,inObj):
	if inObj != None:
		if inObj not in inList:
			inList.append(inObj)
			return 1
		else:
			return 0
	else:
		return 0
'''
tempboard = createtempboard(board)
for i in tempboard:
	print(i)

print(canpath(1,1,8,8,tempboard))
'''