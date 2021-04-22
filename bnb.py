try:
	import pygame
	import random
	import time
	import os

	def clearConsole():
		 os.system("cls")
	class board:
		colorList = ['red','gre','blu','yel','bro','pin']# all the color of the beans
		beanList = []
		def __init__(self):
			self.isfull = False
			self.board = [
					["   ","   ","   ","   ","   ","   ","   ","   ","   "],

					["   ","   ","   ","   ","   ","   ","   ","   ","   "],

					["   ","   ","   ","   ","   ","   ","   ","   ","   "],

					["   ","   ","   ","   ","   ","   ","   ","   ","   "],

					["   ","   ","   ","   ","   ","   ","   ","   ","   "],

					["   ","   ","   ","   ","   ","   ","   ","   ","   "],

					["   ","   ","   ","   ","   ","   ","   ","   ","   "],

					["   ","   ","   ","   ","   ","   ","   ","   ","   "],

					["   ","   ","   ","   ","   ","   ","   ","   ","   "]]
		
			
		'''
		def swap(self,inX,inY):
			_ = self.board[self.x][self.y] 
			self.board[self.x][self.y] = self.board[inX][inY]
			self.board[inX][inY] = _
		'''
		def __str__(self):
			line = '=======================================================\n'
			i = '' + line
			for _ in self.board:
				a = '| '
				for __ in _ :
					a = a + str(__) + ' | '
				i = i + a + '\n' + line
			#i = i + '-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-='
			return i

		def placeNewBean(self):
			while True:
				randx = random.randint(0,8)
				#print(randx)
				randy = random.randint(0,8)
				#print(randy)
				randcolor = random.choice(self.colorList)
				#print(randcolor)
				newbean = bean(randx,randy,randcolor)
				
				if self.board[randx][randy] == "   ":
					self.beanList.append(newbean)
					self.board[randx][randy] = newbean.color
					self.update()
					break
				else:
					pass

		def removeBean(self,inx,iny):
			for bean in beanList:
				if bean.x == inx and bean.y == iny :
					self.beanList.pop(self.beanList.index(bean))
					self.board[bean.x][bean.y] = "   "
			self.update()

		def update(self):
			if len(self.beanList) == 81:
				self.isfull = True
			else:
				self.infull = False
	class bean:
		#constructor
		def __init__(self,inx,iny,incolor):
			self.x = inx
			self.y = iny
			self.state = 1
			self.color = incolor #random color 
		#grow
		def grow():
			if self.state < 3:
				self.state += 1

	a = board()
	
	'''
	while not a.isfull:
		clearConsole()
		a.placeNewBean()
		print(a)
		#time.sleep(0.5)
	'''


	
## for bug and print out bug (only for compile error or runtime error) [ DO NOT FIX ]
except Exception as Bug:
	print("game.py:",Bug)
	print("Please report the bug")
	input("Double Press Enter to continue !!")
	input()