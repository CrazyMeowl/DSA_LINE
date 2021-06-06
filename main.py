
import numpy as np
import pygame
import math
from PIL import Image,ImageFont,ImageDraw
from bnb import *
from bnbfunc import *

height = 500
width = 600

def printf(hehe):
	print(hehe)

class mice:
	def __init__(self):
		self.state = None
		self.selected = None
		self.col = -1
		self.row = -1
		self.coord = (self.row,self.col)
	def select(self):
		self.selected = self.coord

	def get(self):
		x,y = pygame.mouse.get_pos()
		if(x >= 165 and x <= 164+47*9 and y>=41 and y <= 40+47*9):
			self.col = math.floor((x-166)/47)
			self.row = math.floor((y-42)/47)
			self.coord = (self.row,self.col)
		else:
			self.col = -1
			self.row = -1
			self.coord = (self.row,self.col)

def mainloop():
	def draw(surface,mainboard):
		surface.blit(bg, [0, 0])
		normal = [bro,red,yel,gre,blu,pur]
		smo = [smobro,smored,smoyel,smogre,smoblu,smopur]
		for _ in mainboard.beanList:
			x = 165 + (_.x * 47)
			y = 41 +(_.y * 47)

			if _.state == 1:
				surface.blit(smo[_.colorid],[x,y])
			else:
				surface.blit(normal[_.colorid],[x,y])


			


	pygame.init()
	surface = pygame.display.set_mode((width,height))

	pygame.display.set_caption("Line98 x PvZ DSA Project")

	bg = pygame.image.load("Resources/bg5x6.png")
	bro = pygame.image.load("Resources/bro.png")
	red = pygame.image.load("Resources/red.png")
	yel = pygame.image.load("Resources/yel.png")
	gre = pygame.image.load("Resources/gre.png")
	blu = pygame.image.load("Resources/blu.png")
	pur = pygame.image.load("Resources/pur.png")

	smobro = pygame.image.load("Resources/smobro.png")
	smored = pygame.image.load("Resources/smored.png")
	smoyel = pygame.image.load("Resources/smoyel.png")
	smogre = pygame.image.load("Resources/smogre.png")
	smoblu = pygame.image.load("Resources/smoblu.png")
	smopur = pygame.image.load("Resources/smopur.png")

	FPS = 20
	clock = pygame.time.Clock()
	mainboard = board()
	mouse = mice()
	update = False
	i = 0
	while True:
		
		for event in pygame.event.get():

			if event.type == pygame.QUIT:
				printf('hehe')
				quit()

			elif event.type == pygame.MOUSEBUTTONDOWN:
				mainboard.clearConsole()
				mouse.get()
				print(mainboard)
				if mouse.coord	!= (-1,-1):
					if mouse.state == None:
						if mainboard.get(mouse.coord)[1] == 2:
							mouse.select()
							mouse.state = "move"
							#print('Selected: ',mouse.selected)
					elif mouse.state == "move":
						if canpath(mouse.selected,mouse.coord,mainboard.board):
							mainboard.move(mouse.selected,mouse.coord)
							mouse.state = None
							#print('moved')
							update = True
						else:
							mouse.state = None
						i += 1
					mainboard.checkBoard()
					
				
			'''
			elif event.type == pygame.MOUSEBUTTONDOWN:
				mainboard.update()   #UPDATE part is here
				mainboard.clearConsole()
				x,y = pygame.mouse.get_pos()
				if(x >= 165 and x <= 164+47*9 and y>=41 and y <= 40+47*9):
					col = math.floor((x-166)/47)
					row = math.floor((y-42)/47)
				else:
					col = -1
					row = -1

				#print(row,col)
				#mainboard.removeBean(col,row)
				mainboard.checkBoard()
				mainboard.placeNewBean()
				#mainboard.removeBean(row,col)

				#	print(mainboard)
				printBoard(mainboard.board)
			'''
			
		if update == True:
			mainboard.update()
			mainboard.placeNewBean()
			update = False
		if i == 5:
			mainboard.restart()
			i = 0
		draw(surface,mainboard)
		pygame.display.flip()
		clock.tick(FPS)

#drawloop()

mainloop()


