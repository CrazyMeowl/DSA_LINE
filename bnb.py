try:
	import pygame
	from pygame import mixer
	import random
	import time
	import os
	from bnbfunc import *

	class board:
		colorList = ['bro','red','yel','gre','blu','pur']# all the color of the beans
		beanList = []
		def __init__(self):
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
		
		def placeNewBean(self):
			i = 0
			while i < 4:
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
							print('Full')
							self.isfull = True
						else:
							self.isfull = False

						done = 1
					else:
						done = 0
					if done :
						break
				i += 1
		def removeBean(self,iny,inx):
			for bean in self.beanList:
				if bean.x == inx and bean.y == iny :
					self.beanList.pop(self.beanList.index(bean))
					self.board[bean.y][bean.x] = ["   ", 0]
			#print('removed')

		def update(self):
			#print(self)
			if len(self.beanList) == 81:
				print('Full')
				self.isfull = True
			else:
				self.isfull = False
				for _ in self.beanList:
					_.grow()
					self.board[_.y][_.x] = [_.color,_.state]

		def swap(self,bean1,bean2):
			bean1.x,bean1.y,bean2.x,bean2.y=bean2.x,bean2.y,bean1.x,bean1.y
		def printboard(self):
			for _ in self.board:
				print(_)
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