try:
	import numpy as np
	import pygame
	from pygame import mixer
	import random
	import time
	import os
	from bnbfunc import *
	def printBoard(board):
			for _ in board:
				print(_)
	class board:
		colorList = ['bro','red','yel','gre','blu','pur']# all the color of the beans
		#colorList = ['red']
		beanList = []
		def __init__(self):
			self.point = 0
			self.isfull = False	
			self.board =[
						[["   ",0],["   ",0],["   ",0],["   ",0],["   ",0],["   ",0],["   ",0],["   ",0],["   ",0]],

						[["   ",0],["   ",0],["   ",0],["   ",0],["   ",0],["   ",0],["   ",0],["   ",0],["   ",0]],

						[["   ",0],["   ",0],["   ",0],["   ",0],["   ",0],["   ",0],["   ",0],["   ",0],["   ",0]],

						[["   ",0],["   ",0],["   ",0],["   ",0],["   ",0],["   ",0],["   ",0],["   ",0],["   ",0]],

						[["   ",0],["   ",0],["   ",0],["   ",0],["   ",0],["   ",0],["   ",0],["   ",0],["   ",0]],

						[["   ",0],["   ",0],["   ",0],["   ",0],["   ",0],["   ",0],["   ",0],["   ",0],["   ",0]],

						[["   ",0],["   ",0],["   ",0],["   ",0],["   ",0],["   ",0],["   ",0],["   ",0],["   ",0]],

						[["   ",0],["   ",0],["   ",0],["   ",0],["   ",0],["   ",0],["   ",0],["   ",0],["   ",0]],
						
						[["   ",0],["   ",0],["   ",0],["   ",0],["   ",0],["   ",0],["   ",0],["   ",0],["   ",0]]
						]
			self.placeNewBean()
			self.update()
			self.placeNewBean()
			
		'''
		def swap(self,inX,inY):
			_ = self.board[self.x][self.y] 
			self.board[self.x][self.y] = self.board[inX][inY]
			self.board[inX][inY] = _
		'''
		def clearConsole(self):
		 os.system("cls")

		def __str__(self):
			line = '=========================================================================\n'
			i = '' + line
			for _ in self.board:
				a = '| '
				for __ in _ :
					a = a + str(__[0])+','+str(__[1]) + ' | '
				i = i + a + '\n' + line
			#i = i + '-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-='
			#for j in self.board:
			#	print(j)
			#print(self.board)
			return i
		

		def move(self,in1,in2):
			startY,startX = in1
			endY,endX = in2
			if self.board[endY][endX][1] == 1:
				self.removeBean(endY,endX)
			self.board[startY][startX] = ["   ",0]
			for bean in self.beanList:
				if bean.y == startY and bean.x == startX :
					bean.y,bean.x = endY,endX
					self.board[endY][endX] = [bean.color,2]

		def placeNewBean(self):
			i = 0
			while i < 3:
				while not self.isfull:
					#print('try to place')
					randx = random.randint(0,8)
					#print(randx)
					randy = random.randint(0,8)
					#print(randy)
					randcolor = random.choice(self.colorList)
					#print(randcolor)
					newbean = bean(randx,randy,randcolor)
					
					if self.board[randy][randx][0] == "   ":
						self.beanList.append(newbean)
						self.board[randy][randx] = [newbean.color, 1]

						if len(self.beanList) == 81:
							#print('Full')
							self.isfull = True
						else:
							self.isfull = False

						done = 1
					else:
						done = 0
					if done :
						break
				i += 1
		def removeList(self,inList):
			for y,x in inList:
				self.removeBean(y,x)

			addpoint = len(inList)
			if addpoint != 5:
				self.point += addpoint*2
			else:
				self.point += 5
			print(self.point)
		def removeBean(self,iny,inx):
			for bean in self.beanList:
				if bean.x == inx and bean.y == iny :
					self.beanList.pop(self.beanList.index(bean))
					self.board[iny][inx] = ["   ", 0]
			#print('removed')

		def update(self):
			#print(self)
			if len(self.beanList) == 81:
				#print('Full')
				self.isfull = True
			else:
				self.isfull = False
				for _ in self.beanList:
					_.grow()
					self.board[_.y][_.x] = [_.color,_.state]

		def swap(self,bean1,bean2):
			bean1.x,bean1.y,bean2.x,bean2.y=bean2.x,bean2.y,bean1.x,bean1.y
		
		def checkBoard(self):
			board = createtempboard2(self.board)
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
			
			#print('hlist')
			#printBoard(hlist)
			#print('vlist')
			#printBoard(vlist)
			#print('dlist1')
			#printBoard(dlist1)
			#print('dlist2')
			#printBoard(dlist2)
			
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
				#print(starty,startx)
				_ = searchdupe(line)
				if _ != None:
					
					for ele in _:
						#print("Remove")
						#print(ele)
						y = starty + ele
						x = startx + ele
						#print((y,x))
						awd(removelist,(y,x))			
				linecounter +=1
			#print(removelist)
			#return removelist
			self.removeList(removelist)
		def get(self,coord):
			y,x = coord
			return self.board[y][x]
		def restart(self):
			self.point = 0
			board.beanList = []
			self.board =[
						[["   ",0],["   ",0],["   ",0],["   ",0],["   ",0],["   ",0],["   ",0],["   ",0],["   ",0]],

						[["   ",0],["   ",0],["   ",0],["   ",0],["   ",0],["   ",0],["   ",0],["   ",0],["   ",0]],

						[["   ",0],["   ",0],["   ",0],["   ",0],["   ",0],["   ",0],["   ",0],["   ",0],["   ",0]],

						[["   ",0],["   ",0],["   ",0],["   ",0],["   ",0],["   ",0],["   ",0],["   ",0],["   ",0]],

						[["   ",0],["   ",0],["   ",0],["   ",0],["   ",0],["   ",0],["   ",0],["   ",0],["   ",0]],

						[["   ",0],["   ",0],["   ",0],["   ",0],["   ",0],["   ",0],["   ",0],["   ",0],["   ",0]],

						[["   ",0],["   ",0],["   ",0],["   ",0],["   ",0],["   ",0],["   ",0],["   ",0],["   ",0]],

						[["   ",0],["   ",0],["   ",0],["   ",0],["   ",0],["   ",0],["   ",0],["   ",0],["   ",0]],
						
						[["   ",0],["   ",0],["   ",0],["   ",0],["   ",0],["   ",0],["   ",0],["   ",0],["   ",0]]
						]
			self.placeNewBean()
			self.update()
			self.placeNewBean()
	class bean:
		#constructor
		def __init__(self,inx,iny,incolor):
			self.x = inx
			self.y = iny
			self.state = 1
			self.color = incolor #random color
			if incolor == "bro":
				self.colorid = 0
			elif incolor == "red":
				self.colorid = 1
			elif incolor == "yel":
				self.colorid = 2
			elif incolor == "gre":
				self.colorid = 3
			elif incolor == "blu":
				self.colorid = 4
			elif incolor == "pur":
				self.colorid = 5
			
		#grow
		def grow(self):
			if self.state < 2:
				self.state += 1
## for bug and print out bug (only for compile error or runtime error) [ DO NOT FIX ]
except Exception as Bug:
	print("game.py:",Bug)
	print("Please report the bug")
	input("Double Press Enter to continue !!")
	input()