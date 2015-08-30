import pygame,sys 
from classes import *
from process import process
pygame.init()

black = 0,0,0
white = 255,255,255

dimensions = SCREENWIDTH,SCREENHEIGHT = 640,480
screen = pygame.display.set_mode(dimensions)
clock = pygame.time.Clock()
FPS = 24
total_frames = 0

background = pygame.image.load("pics/background.jpg")
gameover = pygame.image.load("pics/gameover.png")

GameRunning = True

player = PlayerShip(SCREENWIDTH/2,400,50,61,"pics/playership.gif")

print("Player range: ",(player.width+20,SCREENWIDTH - player.width - 20))

# GAME LOOP
while True:
	# PROCESSES
	if GameRunning:
		process(player,FPS, total_frames)

		Enemy.checkHealth()
		GameRunning = PlayerShip.checkHealth()
		
		total_frames+=1

		
		screen.blit(background,(0,0))
		
		player.move(SCREENWIDTH)
		
		
		for enemy in Enemy.List:	
			enemy.move(SCREENWIDTH)
		
		BaseClass.allsprites.draw(screen)
		Projectile.allproj.draw(screen)

		PlayerProjectile.movement(SCREENHEIGHT)
		EnemyProjectile.movement(SCREENHEIGHT)

		pygame.display.flip()
		clock.tick(FPS)

	else:
		screen.fill(black)
		screen.blit(gameover,(-20,40))
		pygame.display.flip()

		for sprite in BaseClass.allsprites:
			BaseClass.allsprites.remove(sprite)
			del sprite
		for proj in Projectile.allproj:
			Projectile.allproj.remove(proj)
			del proj
			
		for event in pygame.event.get():
			if event.type == pygame.QUIT: 
	   			pygame.quit()
				sys.exit()

