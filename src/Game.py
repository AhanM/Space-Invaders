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
myfont = pygame.font.SysFont("serif", 18)

background = pygame.image.load("../pics/background.jpg")
gameover = pygame.image.load("../pics/gameover.png")
music = pygame.mixer.Sound("../sounds/spacemusic.wav")
music.play(-1)

playerlasersound = pygame.mixer.Sound("../sounds/laser2.wav")
playerlasersound.set_volume(0.1)
enemylasersound = pygame.mixer.Sound("../sounds/enemy_laser1.wav")

GameRunning = True

player = PlayerShip(SCREENWIDTH/2,400,50,61,"../pics/playership.gif")


pygame.display.set_caption("Space-Invaders")
# GAME LOOP
while True:
	# PROCESSES
	if GameRunning:
		process(player,FPS, total_frames,playerlasersound,enemylasersound)

		Enemy.checkHealth()
		GameRunning = PlayerShip.checkHealth()
		
		total_frames+=1

		
		screen.blit(background,(0,0))
		
		player.move(SCREENWIDTH)
		
		scoretext = myfont.render("Score = "+str(Spacecraft.score), 1, white)
		screen.blit(scoretext, (5, 10))
		
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
		screen.blit(gameover,(-20,0))
		music.stop()
		scoretext = myfont.render("Score = "+str(Spacecraft.score), 1, white)
		screen.blit(scoretext, (SCREENWIDTH, 400))
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



