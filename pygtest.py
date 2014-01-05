import sys, pygame, random
from random import choice
from pygame.locals import *
#		  R    G    B
WHITE	=	(255, 255, 255)
RED	=	(255,   0,   0)
GREEN	=	(  0, 155,   0)
BLACK	=	(  0,   0,   0)
LGREEN	=	( 51, 255,  51)
COLOR = [WHITE, RED, GREEN, BLACK]
XCORD = 25
YCORD = 25
WIDTH = 100
HEIGHT = 50
MARGIN = 5
#FPS = 30
track = []
orig = []
timer = 15
up = True
pygame.init()
clock = pygame.time.Clock()
DISPSURF = pygame.display.set_mode((300, 400))
pygame.display.set_caption('pygtest.py! ')
DISPSURF.fill(BLACK)
score = 0
#def main():
	#draw screen ! 
	#draw()
	#pygame.time.delay(500)
while True:
		#pygame.draw.rect(DISPSURF, GREEN, (XCORD, YCORD, WIDTH, HEIGHT))
		#pygame.draw.rect(DISPSURF, RED, (XCORD, WIDTH + MARGIN, WIDTH, HEIGHT))
		for elem in range(0, score + 1):
			print 'inside score loop'
			i = random.randint(1,2)
			if i == 1:
				print 'random green'
				orig.append('green')
				pygame.draw.rect(DISPSURF, WHITE, (XCORD, YCORD, WIDTH, HEIGHT))
                        	pygame.time.delay(500)
                        	pygame.draw.rect(DISPSURF, GREEN, (XCORD, YCORD, WIDTH, HEIGHT))
			if i == 2:
				print 'random red'
				orig.append('red')
				pygame.draw.rect(DISPSURF, WHITE, (XCORD, WIDTH + MARGIN, WIDTH, HEIGHT))
				pygame.time.delay(500)
				pygame.draw.rect(DISPSURF, RED, (XCORD, WIDTH + MARGIN, WIDTH, HEIGHT))
		for elem in range(0, score + 1):				
			for event in pygame.event.get():
                		print 'hey there'
				if event.type == QUIT:
					pygame.quit()
					sys.exit()
				pygame.draw.rect(DISPSURF, GREEN, (XCORD, YCORD, WIDTH, HEIGHT))
				pygame.draw.rect(DISPSURF, RED, (XCORD, WIDTH + MARGIN, WIDTH, HEIGHT))	
				if event.type == MOUSEBUTTONUP:
					x, y = event.pos
					print 'inside mouse click'
					if x > XCORD and y > YCORD and x < (XCORD + WIDTH) and y < (YCORD + HEIGHT):
                		                #print 'entering for red'
						
						pygame.draw.rect(DISPSURF, GREEN, (XCORD, YCORD, WIDTH, HEIGHT))
                		                pygame.time.delay(10)
                		                pygame.draw.rect(DISPSURF, WHITE, (XCORD, YCORD, WIDTH, HEIGHT))
					if x > XCORD and y > WIDTH + MARGIN and x < (XCORD + WIDTH) and y < (WIDTH + MARGIN + HEIGHT):
						pygame.draw.rect(DISPSURF, RED, (XCORD, WIDTH + MARGIN, WIDTH, HEIGHT))
						pygame.time.delay(10)
						pygame.draw.rect(DISPSURF, WHITE, (XCORD, WIDTH + MARGIN, WIDTH, HEIGHT))	
						track.append('red')
		pygame.display.update()
	#clock.tick(FPS)

