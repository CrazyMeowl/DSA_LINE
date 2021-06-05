from itertools import groupby
import numpy as np
def searchdupe(inList):
	counter = 0
	for i,j in groupby(inList):
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


board =[[['gre', 2], ['red', 2], ['red', 2], ['blu', 2], ['yel', 2], ['red', 2], ['gre', 2], ['bro', 2], ['gre', 2]],
		[['gre', 2], ['gre', 2], ['   ', 0], ['yel', 2], ['yel', 2], ['blu', 2], ['bro', 2], ['blu', 2], ['pur', 2]],
		[['pur', 2], ['bro', 2], ['pur', 2], ['bro', 2], ['yel', 2], ['blu', 2], ['red', 2], ['blu', 2], ['yel', 2]],
		[['   ', 0], ['blu', 2], ['gre', 2], ['gre', 2], ['yel', 2], ['blu', 2], ['bro', 2], ['blu', 2], ['yel', 2]],
		[['blu', 2], ['red', 2], ['   ', 0], ['pur', 2], ['pur', 2], ['yel', 2], ['bro', 2], ['yel', 2], ['bro', 2]],
		[['blu', 2], ['bro', 1], ['   ', 0], ['bro', 2], ['gre', 2], ['gre', 2], ['bro', 2], ['bro', 2], ['blu', 2]],
		[['gre', 2], ['pur', 2], ['yel', 2], ['bro', 2], ['bro', 2], ['blu', 2], ['bro', 2], ['pur', 2], ['blu', 2]],
		[['   ', 0], ['bro', 2], ['bro', 2], ['bro', 2], ['bro', 2], ['bro', 2], ['bro', 2], ['red', 2], ['yel', 2]],
		[['yel', 2], ['pur', 2], ['pur', 2], ['gre', 2], ['red', 2], ['gre', 2], ['   ', 0], ['   ', 0], ['blu', 2]]]

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
		print(inBoard[y][x])

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
	'''
	print('hlist')
	printboard(hlist)
	print('vlist')
	printboard(vlist)
	print('dlist1')
	printboard(dlist1)
	print('dlist2')
	printboard(dlist2)
	'''
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
	print(removelist)
	return removelist

removelist(board,checkboard(board))