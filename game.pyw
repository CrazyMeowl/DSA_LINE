#For error catching for the entire code
try:

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
		#colorcode = 0
		def draw(surface,mainboard):
			surface.blit(bg, [0, 0])
			normal = [bro,red,yel,gre,blu,pur]
			smo = [smobro,smored,smoyel,smogre,smoblu,smopur]

			surface.blit(restartButton,[10,440])
			pygame.draw.rect(surface,(0,0,0),restart_clickbox, 2)
			surface.blit(sunLabel,[10,10])
			surface.blit(mainboard.updatePoint(),(10+40,20))
			#random.randint(0,255)
			
			#colorcode = colorcode + 1
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

		sunLabel = pygame.image.load("Resources/sunCounter.png")
		restartButton = pygame.image.load("Resources/restart.png")
		
		restart_clickbox = pygame.Rect(10,500-60,50,50)

		FPS = 30
		clock = pygame.time.Clock()
		mainboard = board()
		mouse = mice()
		update = False
		mainboard.backgroundMusic()
		state = "game"
		losesound = 'not played'

		while True:
			while state == "game" :
				mainboard.checkBoard()
				
				for event in pygame.event.get():
					#print(event)
					if event.type == pygame.QUIT:
						#printf('hehe')
						#quit()
						return 0

					elif event.type == pygame.MOUSEBUTTONDOWN: # check if player clicked mouse
						#mainboard.clearConsole()
						#print(mainboard)
						mouse.get()
						#print(mouse.coord)
						if mouse.coord	!= (-1,-1):
							if mouse.state == None and not mainboard.isfull : # check if mouse state is in idle mode
								if mainboard.get(mouse.coord)[1] == 2: # if mouse click into any grown walnut:
									mouse.select() # add that wallnut into selected
									mouse.state = "move" # change mouse state to "Move" so the next step will be check for move
									mainboard.seedSound.play() # play sound
									#print('Selected: ',mouse.selected)
							elif mouse.state == "move": # check if the mouse state is in move or idle
								if canpath(mouse.selected,mouse.coord,mainboard.board): # if can find any path to the target block
									mainboard.move(mouse.selected,mouse.coord) # move from the selected block to the target block
									mouse.state = None #put mouse back to idle state
									#print('moved')
									update = True # moved successfully and tell the game to place more bean and update the small bean
								else:
									mainboard.shovelSound.play() #play sound
									mouse.state = None #put mouse back to idle state

						elif restart_clickbox.collidepoint(event.pos):
							#print("noice")
							mainboard.restart()
							losesound = 'not played'
							
							
						
					
					
				if update == True:
					mainboard.update()
					mainboard.placeNewBean()
					update = False

				if mainboard.isfull and losesound == 'not played':
					mainboard.loseSound.play()
					losesound = 'played'
				draw(surface,mainboard)
				#colorcode
				pygame.display.flip()
				clock.tick(FPS)

		#drawloop()

	mainloop()

## for bug and print out bug (only for compile error or runtime error) [ DO NOT FIX ]
except Exception as Bug:
	print("game.py:",Bug)
	print("Please report the bug")
	input("Double Press Enter to continue !!")
	input()

#end of error catching
