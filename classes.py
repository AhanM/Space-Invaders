import pygame

class BaseClass(pygame.sprite.Sprite):
	
	allsprites = pygame.sprite.Group()
	def __init__(self,x,y,width,height,image_string):
		pygame.sprite.Sprite.__init__(self)
		BaseClass.allsprites.add(self)

		self.image = pygame.image.load(image_string)
		self.rect = self.image.get_rect()

		self.width = width
		self.height = height

		self.rect.centerx = x
		self.rect.centery = y 

	def draw(self,surface):
		surface.blit(self.image,(self.rect.x-self.rect.width/2,self.rect.y-self.rect.height))	

	def destroy(self,ClassName):
		ClassName.List.remove(self)
		BaseClass.allsprites.remove(self)
		del self

class Spacecraft(BaseClass):
	
	List = pygame.sprite.Group()
	def __init__(self,x,y,width,height,image_string):
		BaseClass.__init__(self,x,y,width,height,image_string)
		Spacecraft.List.add(self)
		self.health = 150
		self.velx = 0

	def draw(self,surface):
		surface.blit(self.image,(self.rect.x-self.rect.width/2,self.rect.y-self.rect.height))

	def move(self,width):
		self.rect.x += self.velx

class PlayerShip(Spacecraft):

	List = pygame.sprite.Group()
	projectile_list = [] 
	def __init__(self,x,y,width,height,image_string):
		Spacecraft.__init__(self,x,y,width,height,image_string)
		PlayerShip.List.add(self)
		self.damagetaken = 50

	def move(self,SCREENWIDTH):
		if self.rect.centerx > 570 and self.velx > 0:
			self.velx = 0
		elif self.rect.centerx < 20 + (self.width) and self.velx < 0:
			self.velx = 0
		self.rect.x += self.velx

	@staticmethod
	def checkHealth():
		for player in PlayerShip.List:
			if player.health == 0:
				print("GAME OVER!!")
				return False
			else:
				return True

class Enemy(Spacecraft):

	List = pygame.sprite.Group()
	def __init__(self,x,y,width,height,image_string):
		Spacecraft.__init__(self,x,y,width,height,image_string)
		Enemy.List.add(self)
		BaseClass.allsprites.add(self)

		self.velx = 3

		self.damagetaken = 50

	def move(self,SCREENWIDTH):
		if self.rect.centerx > SCREENWIDTH - (self.width) - 20  or self.rect.centerx < 20 + (self.width):
			self.velx = -self.velx
			self.rect.centery += 50
		self.rect.x += self.velx
	
	@staticmethod
	def shoot():
		for enemy in Enemy.List:
			EnemyProjectile(enemy.rect.centerx,enemy.rect.centery,2,10,"pics/enemy_laser.jpg")

	@staticmethod
	def checkHealth():
		for enemy in Enemy.List:
			if enemy.health == 0:
				enemy.image = pygame.image.load("pics/explosion.gif")
				enemy.velx = 0
	
class Projectile(pygame.sprite.Sprite):

	allproj = pygame.sprite.Group()
	def __init__(self,x,y,width,height,image_string):		
		pygame.sprite.Sprite.__init__(self)

		self.image = pygame.image.load(image_string)
		self.rect = self.image.get_rect()

		self.width = width
		self.height = height

		self.rect.x = x
		self.rect.y = y 
		self.vely = -8
			
		Projectile.allproj.add(self)

class PlayerProjectile(Projectile):
	List = pygame.sprite.Group()
	normal_list = []
	def __init__(self,x,y,width,height,image_string):
		Projectile.__init__(self,x,y,width,height,image_string)


		if(len(PlayerProjectile.normal_list)!=0):
			last_element = PlayerProjectile.normal_list[-1]
			difference = abs(self.rect.y - last_element.rect.y)

			if difference <= self.height+50:
				Projectile.allproj.remove(self)
				# Projectile.normal_list.pop()
				return
			

		PlayerProjectile.List.add(self)
		PlayerProjectile.normal_list.append(self)

	@staticmethod
	def movement(height):
		for projectile in PlayerProjectile.List:
			projectile.rect.y += projectile.vely

			if projectile.rect.y < 10:
				Projectile.allproj.remove(projectile)
				EnemyProjectile.List.remove(projectile)
				del projectile

			elif projectile.rect.y > height-10:
				Projectile.allproj.remove(projectile)
				PlayerProjectile.List.remove(projectile)
				del projectile

class EnemyProjectile(Projectile):
	
	List = pygame.sprite.Group()
	normal_list = []
	def __init__(self,x,y,width,height,image_string):
		Projectile.__init__(self,x,y,width,height,image_string)

		self.vely = 8

		if(len(EnemyProjectile.List)!=0):
			last_element = EnemyProjectile.normal_list[-1]
			difference = abs(self.rect.y - last_element.rect.y)

			if difference <= self.height+50:
				Projectile.allproj.remove(self)
				return

		EnemyProjectile.List.add(self)
		EnemyProjectile.normal_list.append(self)

	@staticmethod
	def movement(height):
		for projectile in EnemyProjectile.List:
			projectile.rect.y += projectile.vely

			if projectile.rect.y < 10:
				Projectile.allproj.remove(projectile)
				EnemyProjectile.List.remove(projectile)
				del projectile

			elif projectile.rect.y > height-10:
				Projectile.allproj.remove(projectile)
				PlayerProjectile.List.remove(projectile)
				del projectile

