import pygame 
from settings import *
from tile import Tile
from player import Player
from debug import debug
from support import *
from random import choice, randint
from weapon import Weapon
from ui import UI
from enemy import Enemy
from particles import AnimationPlayer
from magic import MagicPlayer
from upgrade import Upgrade
import os
import time


class Level:
	def __init__(self):

		# get the display surface 
		self.display_surface = pygame.display.get_surface()
		self.game_paused = False

		# sprite group setup
		self.visible_sprites = YSortCameraGroup()
		self.obstacle_sprites = pygame.sprite.Group()

		# attack sprites
		self.current_attack = None
		self.attack_sprites = pygame.sprite.Group()
		self.attackable_sprites = pygame.sprite.Group()

		# sprite setup
		self.create_map()

		# user interface 
		self.ui = UI()
		self.upgrade = Upgrade(self.player)

		# particles
		self.animation_player = AnimationPlayer()
		self.magic_player = MagicPlayer(self.animation_player)


		self.flower_time = 0

	def create_map(self):
		layouts = {
			'boundary' : import_csv_layout(os.path.join("Lunar's Zelda Style Game", 'level graphics', 'map', 'map_FloorBlocks.csv')),
            'grass' : import_csv_layout(os.path.join("Lunar's Zelda Style Game", 'level graphics', 'map', 'map_Grass.csv')),
            'object' : import_csv_layout(os.path.join("Lunar's Zelda Style Game", 'level graphics', 'map', 'map_Objects.csv')),
            'entities': import_csv_layout(os.path.join("Lunar's Zelda Style Game", 'level graphics', 'map', 'map_Entities.csv')),
			'diamond': import_csv_layout(os.path.join("Lunar's Zelda Style Game", 'level graphics', 'map', 'map_sims.csv')),
			'flower': import_csv_layout(os.path.join("Lunar's Zelda Style Game", 'level graphics', 'map', 'map_flower.csv'))
		}
		graphics = {
			'grass' : import_folder(os.path.join("Lunar's Zelda Style Game", 'level graphics', 'graphics', 'grass')),
            'objects' : import_folder(os.path.join("Lunar's Zelda Style Game", 'level graphics', 'graphics', 'objects')),
			'diamonds' : import_folder((os.path.join("Lunar's Zelda Style Game", 'level graphics', 'graphics', 'special', 'Diamond'))),
			'flowers' : import_folder((os.path.join("Lunar's Zelda Style Game", 'level graphics', 'graphics', 'special', 'morning_glories')))
		}

		for style,layout in layouts.items():
			for row_index,row in enumerate(layout):
				for col_index, col in enumerate(row):
					if col != '-1':
						x = col_index * TILESIZE
						y = row_index * TILESIZE
						if style == 'boundary':
							Tile((x,y),[self.obstacle_sprites],'invisible')
						if style == 'grass':
							random_grass_image = choice(graphics['grass'])
							Tile(
								(x,y),
								[self.visible_sprites,self.obstacle_sprites,self.attackable_sprites],
								'grass',
								random_grass_image)
							
						if style == 'flower':
								flower_image = choice(graphics['flowers'])
								Tile(
								(x,y),
								[self.visible_sprites,self.obstacle_sprites,self.attackable_sprites],
								'flower', flower_image)

						if style == 'diamond':
								diamond_image = choice(graphics['diamonds'])
								Tile(
								(x,y),
								[self.visible_sprites,self.obstacle_sprites,self.attackable_sprites],
								'diamond', diamond_image)

						if style == 'object':
							surf = graphics['objects'][int(col)]
							Tile((x,y),[self.visible_sprites,self.obstacle_sprites],'object',surf)

						if style == 'entities':
							if col == '394':
								self.player = Player(
									(x,y),
									[self.visible_sprites],
									self.obstacle_sprites,
									self.create_attack,
									self.destroy_attack,
									self.create_magic)
							else:
								if col == '390': monster_name = 'bamboo'
								elif col == '391': monster_name = 'spirit'
								elif col == '392': monster_name ='raccoon'
								else: monster_name = 'squid'
								Enemy(
									monster_name,
									(x,y),
									[self.visible_sprites,self.attackable_sprites],
									self.obstacle_sprites,
									self.damage_player,
									self.trigger_death_particles,
									self.add_exp)

	def create_attack(self):
		
		self.current_attack = Weapon(self.player,[self.visible_sprites,self.attack_sprites])

	def create_magic(self,style,strength,cost):
		if style == 'heal':
			self.magic_player.heal(self.player,strength,cost,[self.visible_sprites])

		if style == 'flame':
			self.magic_player.flame(self.player,cost,[self.visible_sprites,self.attack_sprites])

	def destroy_attack(self):
		if self.current_attack:
			self.current_attack.kill()
		self.current_attack = None

	

	def player_attack_logic(self, player):
		if self.attack_sprites:
			for attack_sprite in self.attack_sprites:
				collision_sprites = pygame.sprite.spritecollide(attack_sprite,self.attackable_sprites,False)
				if collision_sprites:
					for target_sprite in collision_sprites:
						if target_sprite.sprite_type == 'grass':
							pos = target_sprite.rect.center
							offset = pygame.math.Vector2(0,75)
							for leaf in range(randint(3,6)):
								self.animation_player.create_grass_particles(pos - offset,[self.visible_sprites])
							target_sprite.kill()
						elif target_sprite.sprite_type == 'flower':
							self.flower_time = pygame.time.get_ticks()
							self.ui.dialogue_box('Its nice to smell flowers. INSTANT shield regen')
							#self.ui.dialogue_box('I grew them with my sister. It was too exciting')

							if pygame.time.get_ticks() - self.flower_time > 5000:
								self.flower_time = 0

							
								
							player.shield = 100
							target_sprite.kill()
						elif target_sprite.sprite_type == 'diamond':
							self.diamond_time = pygame.time.get_ticks()
							self.ui.dialogue_box('That looks like a sims diamond  +2000Xp forr upgrades')
							if pygame.time.get_ticks() - self.diamond_time > 5000:
								self.diamond_time = 0
							player.exp += 2000
							target_sprite.kill()
						else:
							target_sprite.get_damage(self.player,attack_sprite.sprite_type)

	def damage_player(self,amount,attack_type):
		if self.player.vulnerable:
			if self.player.shield <= 0:
				self.player.health -= amount
				self.player.vulnerable = False
				self.player.hurt_time = pygame.time.get_ticks()
				self.animation_player.create_particles(attack_type,self.player.rect.center,[self.visible_sprites])

			else:
				self.player.vulnerable = False
				self.player.hurt_time = pygame.time.get_ticks()
				self.player.shield -= amount

	def trigger_death_particles(self,pos,particle_type):

		self.animation_player.create_particles(particle_type,pos,self.visible_sprites)

	def add_exp(self,amount):

		self.player.exp += amount

	def toggle_menu(self):

		self.game_paused = not self.game_paused 

	def run(self):
		self.visible_sprites.custom_draw(self.player)
		self.ui.display(self.player)
		
		if self.game_paused:
			self.upgrade.display()
		else:
			self.visible_sprites.update()
			self.visible_sprites.enemy_update(self.player)
			self.player_attack_logic(self.player)
		

class YSortCameraGroup(pygame.sprite.Group):
	def __init__(self):

		# general setup 
		super().__init__()
		self.display_surface = pygame.display.get_surface()
		self.half_width = self.display_surface.get_size()[0] // 2
		self.half_height = self.display_surface.get_size()[1] // 2
		self.offset = pygame.math.Vector2()

		# creating the floor
		self.floor_surf = pygame.image.load(os.path.join("Lunar's Zelda Style Game", 'level graphics', 'graphics', 'tilemap', 'ground.png'))
		self.floor_rect = self.floor_surf.get_rect(topleft = (0,0))

	def custom_draw(self,player):

		# getting the offset 
		self.offset.x = player.rect.centerx - self.half_width
		self.offset.y = player.rect.centery - self.half_height

		# drawing the floor
		floor_offset_pos = self.floor_rect.topleft - self.offset
		self.display_surface.blit(self.floor_surf,floor_offset_pos)

		# for sprite in self.sprites():
		for sprite in sorted(self.sprites(),key = lambda sprite: sprite.rect.centery):
			offset_pos = sprite.rect.topleft - self.offset
			self.display_surface.blit(sprite.image,offset_pos)

	def enemy_update(self,player):
		enemy_sprites = [sprite for sprite in self.sprites() if hasattr(sprite,'sprite_type') and sprite.sprite_type == 'enemy']
		for enemy in enemy_sprites:
			enemy.enemy_update(player)
