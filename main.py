

import pygame
import math
from PIL import Image,ImageFont,ImageDraw
from bnb import *
from bnbfunc import *

height = 500
width = 600

def drawloop():
	i = 0
	j = 0
	x = 38
	y = 165
	img = Image.open('bg5x6.png')
	draw = ImageDraw.Draw(img)
	while i < 11:
		
		shape = [(0,x),(599,x)]
		draw.line(shape, fill ="red", width = 0)
		x = x + 47
		#img.show()
		i = i + 1
	#img.save("test.png")

	#img = Image.open('test.png')

	draw = ImageDraw.Draw(img)

	while j < 11:
		
		shape = [(y,0),(y,499)]
		draw.line(shape, fill ="red", width = 0)
		y = y + 47
		#img.show()
		j = j + 1
	img.save("test.png")



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

	clock_tick_rate=20
	clock = pygame.time.Clock()
	mainboard = board()

	while True:
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit()
			elif event.type == pygame.MOUSEBUTTONDOWN:
				mainboard.update()
				mainboard.clearConsole()
				x,y = pygame.mouse.get_pos()
				if(x >= 165 and x <= 164+47*9 and y>=41 and y <= 40+47*9):
					col = math.floor((x-166)/47)
					row = math.floor((y-42)/47)
				else:
					col = -1
					row = -1

				print(row,col)
				#mainboard.removeBean(col,row)
				mainboard.placeNewBean()
				mainboard.removeBean(row,col)

				print(mainboard)
		
		draw(surface,mainboard)
		pygame.display.flip()
		clock.tick(clock_tick_rate)
#drawloop()

mainloop()