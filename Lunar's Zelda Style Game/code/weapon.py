import pygame 
import os

class Weapon(pygame.sprite.Sprite):
	def __init__(self,player,groups):
		super().__init__(groups)
		self.sprite_type = 'weapon'
		direction = player.status.split('_')[0]

		# graphic
		graphics_dir = os.path.join("Lunar's Zelda Style Game", 'level graphics', 'graphics', 'weapons')
		weapon_dir = player.weapon
		image_filename = f'{direction}.png'
		full_path = os.path.join(graphics_dir, weapon_dir, image_filename)
		self.image = pygame.image.load(full_path).convert_alpha()
		
		# placement
		if direction == 'right':
			self.rect = self.image.get_rect(midleft = player.rect.midright + pygame.math.Vector2(0,16))
		elif direction == 'left': 
			self.rect = self.image.get_rect(midright = player.rect.midleft + pygame.math.Vector2(0,16))
		elif direction == 'down':
			self.rect = self.image.get_rect(midtop = player.rect.midbottom + pygame.math.Vector2(-10,0))
		else:
			self.rect = self.image.get_rect(midbottom = player.rect.midtop + pygame.math.Vector2(-10,0))