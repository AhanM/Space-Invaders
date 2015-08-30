import pygame,sys, random
from classes import *

def process(player, FPS, total_frames):	
	for event in pygame.event.get():
		if event.type == pygame.QUIT: 
   			pygame.quit()
			sys.exit()

	spawn(FPS,total_frames)
	collisions()
	enemyshoot(FPS,total_frames)
	deconstruct(FPS,total_frames)
	keys = pygame.key.get_pressed()

	if keys[pygame.K_d]:
		player.velx = 5
	elif keys[pygame.K_a]:
		player.velx = -5
	elif keys[pygame.K_SPACE]:
		PlayerProjectile(player.rect.centerx,player.rect.centery,2,10,"pics/laser.jpg")
	else:
		player.velx = 0	

def enemyshoot(FPS,total_frames):

	frame_in_five_seconds = FPS * 5

	if total_frames % frame_in_five_seconds == 0:
		Enemy.shoot()

def spawn(FPS,total_frames):

	frame_in_four_seconds = FPS * 4

	if total_frames % frame_in_four_seconds == 0:
		r = random.randint(1,2)
		x = 1
		if r == 1:
			x = 400
		elif r == 2:
			x = 400

		print("Spawning")
		print(BaseClass.allsprites)
		newenemy = Enemy(x,20,50,29,"pics/greenalien.gif")
		if random.randint(1,2) == 2: newenemy.velx = -newenemy.velx

def deconstruct(FPS,total_frames):

	frames_in_three_seconds = FPS * 3

	if total_frames % frames_in_three_seconds == 0:
		for enemy in Enemy.List:
			if enemy.health == 0:
				BaseClass.allsprites.remove(enemy)
				Enemy.List.remove(enemy)
				del enemy


def collisions():

	for enemy in Enemy.List:
		enemies_hit = pygame.sprite.spritecollide(enemy, PlayerProjectile.List, True)
		if len(enemies_hit) > 0:
			if enemy.health!=0 : 
				enemy.health -= enemy.damagetaken
				print("Enemy taking damage")
				print(enemies_hit)

	for player in PlayerShip.List:
		player_hit = pygame.sprite.spritecollide(player, EnemyProjectile.List, True)
		if len(player_hit)>0:
			if player.health!=0 : player.health -= player.damagetaken

	for player in PlayerShip.List:
		player_hit = pygame.sprite.spritecollide(player, Enemy.List, False)
		if len(player_hit)!=0:
			print("Enemy Player Collision")
			# for x in player_hit: print(x)
			if player.health!=0 : 
				player.health = 0
