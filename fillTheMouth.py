import pygame
from pygame.locals import *
from sys import exit
import random 
import ipdb;

score = 0

screen_width = 900
screen_height= 700

mouth_x = 300
mouth_y = screen_height - 200

class Mers:
	x = 0
	y = 0
	dy = 0
	def __init__(self):
		self.x = random.randint(10, screen_width)
		self.y = 0
		self.dy = random.randint(3,10)

	def update(self):
		self.y += self.dy
		if self.y > mouth_y:
			self.y = 0
			self.x = random.randint(10, screen_width)
		self.x += random.randint(-5,5)
		if self.x < 10:
			self.x = 10
		if self.x > screen_width - 20:
			self.x = screen_width - 20
		screen.blit(mers_image, (self.x, self.y))

	def is_eaten(self):
		return self.y >= mouth_y and self.x >= mouth_x and self.x < mouth_x + 200 


clock = pygame.time.Clock()

mers_bites = [Mers(), Mers(), Mers()]

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("FILL THE MOUTH")

mouth = pygame.image.load('moofer.png').convert_alpha()
mers_image = pygame.image.load('mers.png').convert_alpha()

def update_mouth():
	global mouth_x
	global mouth_y
	mouth_x, ignore = pygame.mouse.get_pos()
	screen.blit(mouth, (mouth_x,mouth_y))

def check_for_eat():
	global score
	for m in mers_bites:
		if m.is_eaten():
			score += 1

def display(message):
	font = pygame.font.Font(None, 36)
	text = font.render(message, 1, (10,10,10))
	screen.blit(text, (0,0))


while True:

	for event in pygame.event.get():
		if event.type == QUIT:
			exit()

	screen.fill((255,255,255))
	for m in mers_bites:
		m.update()
	update_mouth()
	check_for_eat()
	display("SCORE: " +str(score))
	pygame.display.update()
	clock.tick(30)

