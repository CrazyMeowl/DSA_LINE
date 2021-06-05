from itertools import groupby
import numpy as np
def searchdupe(inList):
	counter = 0
	for i,j in groupby(inList):
		print(i)
		print(j)
		length = len(list(j))
		
		if length >= 5:
			#print('index: ',counter,i,length)
			index = counter
			indexcounter = index + length
			newlist = []
			for i in range(index,indexcounter):
				newlist.append(i)
			return newlist 
		counter += length
	#return 


def awd(inList,inObj):
	if inObj != None:
		if inObj not in inList:
			inList.append(inObj)
			return 1
		else:
			return 0
	else:
		return 0


board =[
		[["   ",0],["   ",0],["   ",0],["   ",0],["   ",0],["   ",0],["   ",0],["   ",0],["   ",0]],

		[["   ",0],["   ",0],["   ",0],["   ",0],["   ",0],["   ",0],["   ",0],["   ",0],["   ",0]],

		[["   ",0],["   ",0],["   ",0],["   ",0],["   ",0],["   ",0],["   ",0],["   ",0],["   ",0]],

		[["   ",0],["   ",0],["   ",0],["   ",0],["   ",0],["   ",0],["   ",0],["   ",0],["   ",0]],

		[["   ",0],["   ",0],["   ",0],["   ",0],["   ",0],["   ",0],["   ",0],["   ",0],["   ",0]],

		[["   ",0],["   ",0],["   ",0],["   ",0],["   ",0],["   ",0],["   ",0],["   ",2],["   ",0]],

		[["   ",0],["   ",0],["   ",0],["   ",0],["   ",0],["   ",0],["   ",0],["   ",2],["   ",0]],

		[["   ",0],["   ",0],["   ",0],["   ",0],["   ",0],["   ",0],["   ",0],["   ",2],["   ",0]],
		
		[["   ",0],["   ",0],["   ",0],["   ",0],["   ",0],["   ",0],["   ",0],["   ",2],["   ",0]]
		]

def createtempboard2(board):
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

def printboard(board):
			for _ in board:
				print(_)

def removelist(inBoard,inList):
	for y,x in inList:
		remove(inBoard,(y,x))
def remove(board,coord):
	y,x = coord
	board[y][x] = ["   ",0]
def checkboard(inboard):
	board = createtempboard2(inboard)
	vlist = []
	hlist = []
	
	for i in range(0,9):
		hlist.append(board[i])
		newlist = []
		for j in range(0,9):
			newlist.append(board[j][i])
		vlist.append(newlist)

	
	a =np.array(board)
	diags = [a[::-1,:].diagonal(i) for i in range(-a.shape[0]+1,a.shape[1])]
	diags2 = [a.diagonal(i) for i in range(a.shape[1]-1,-a.shape[0],-1)]
	dlist1 = [n.tolist() for n in diags]
	dlist2 = [n.tolist() for n in diags2]
	
	print('hlist')
	printboard(hlist)
	print('vlist')
	printboard(vlist)
	print('dlist1')
	printboard(dlist1)
	
	print('dlist2')
	printboard(dlist2)
	
	removelist = []
	rowcounter = 0
	colcounter = 0
	for row in hlist:
		_ = searchdupe(row)
		if _ != None:
			for ele in _:
				awd(removelist,(rowcounter,ele))
		rowcounter += 1

	for col in vlist:
		_ = searchdupe(col)
		if _ != None:
			for ele in _:
				awd(removelist,(ele,colcounter))
		colcounter += 1

	linecounter = 0
	for line in dlist1:
		if linecounter <= 8:
			startx = 0
			starty = linecounter
		else:
			startx = linecounter - 8
			starty = 8
		#print(starty,startx)
		_ = searchdupe(line)
		if _ != None:
			for ele in _:
				#print("Remove")
				y = starty - ele
				x = startx + ele
				awd(removelist,(y,x))			
		linecounter +=1
	
	linecounter = 0
	for line in dlist2:
		if linecounter <= 8:
			startx = 8 - linecounter
			starty = 0
		else:
			startx = 0
			starty = linecounter - 8
		print(starty,startx)
		_ = searchdupe(line)
		if _ != None:
			
			for ele in _:
				#print("Remove")
				print(ele)
				y = starty + ele
				x = startx + ele
				print((y,x))
				awd(removelist,(y,x))			
		linecounter +=1
	print(removelist)
	return removelist

removelist(board,checkboard(board))
printboard(board)