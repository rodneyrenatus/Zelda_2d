import os

#Open the image
# image = Image.open(os.path.join("Lunar's Zelda Style Game", 'level graphics', 'graphics', 'particles', 'heal', 'chicken_wing_final.png'))
# rock_image = Image.open(os.path.join("Lunar's Zelda Style Game", 'level graphics', 'graphics', 'particles', 'flame', 'mdako_rocks.png'))
# flower_image = Image.open(os.path.join("Lunar's Zelda Style Game", 'level graphics', 'graphics', 'special', 'morning_glories', 'morning_glories.png'))
# diamond_image = Image.open(os.path.join("Lunar's Zelda Style Game", 'level graphics', 'graphics', 'special', 'Diamond', 'sims_diamond.png'))
# # Resize the image to 64x64
# resized_image = image.resize((64, 64))
# resized_rock = rock_image.resize((64, 64))
# resized_flower = flower_image.resize((128, 128))
# resized_diamond = diamond_image.resize((64, 64))

# # Save the resized image
# resized_image.save(os.path.join("Lunar's Zelda Style Game", 'level graphics', 'graphics', 'particles', 'heal', 'chicken_wing_final_res.png'))
# resized_rock.save((os.path.join("Lunar's Zelda Style Game", 'level graphics', 'graphics', 'particles', 'flame', 'mdako_rocks_res.png')))
# resized_flower.save((os.path.join("Lunar's Zelda Style Game", 'level graphics', 'graphics', 'special', 'morning_glories', 'morning_glories_res.png')))
# resized_diamond.save((os.path.join("Lunar's Zelda Style Game", 'level graphics', 'graphics', 'special', 'Diamond', 'sims_diamond_res.png')))
# game setup
WIDTH    = 1280	
HEIGTH   = 720
FPS      = 60
TILESIZE = 64
HITBOX_OFFSET = {
	'player': -26,
	'object': -40,
	'grass': -10,
    'flower' : -10,
    'diamond' : -10,
	'invisible': 0}

# ui 
BAR_HEIGHT = 20
SHIELD_BAR_WIDTH = 200
HEALTH_BAR_WIDTH = 200
ENERGY_BAR_WIDTH = 140
ITEM_BOX_SIZE = 80
UI_FONT = os.path.join("Lunar's Zelda Style Game", 'level graphics', 'graphics', 'font', 'joystix.ttf')
UI_FONT_SIZE = 18

# general colors
WATER_COLOR = '#71ddee'
UI_BG_COLOR = '#222222'
UI_BORDER_COLOR = '#111111'
TEXT_COLOR = '#EEEEEE'

# ui colors
SHIELD_COLOR = 'blue'
HEALTH_COLOR = 'red'
ENERGY_COLOR = 'purple'
UI_BORDER_COLOR_ACTIVE = 'gold'

# upgrade menu
TEXT_COLOR_SELECTED = '#111111'
BAR_COLOR = '#EEEEEE'
BAR_COLOR_SELECTED = '#111111'
UPGRADE_BG_COLOR_SELECTED = '#EEEEEE'

# weapons 
weapon_data = {
    'sword' : {'cooldown' : 100, 'damage' : 15, 'graphic' : os.path.join("Lunar's Zelda Style Game", 'level graphics', 'graphics', 'weapons', 'sword', 'full.png')},
    'lance' : {'cooldown' : 400, 'damage' : 30, 'graphic' : os.path.join("Lunar's Zelda Style Game", 'level graphics', 'graphics', 'weapons', 'lance', 'full.png')},
    'axe' : {'cooldown' : 300, 'damage' : 20, 'graphic' : os.path.join("Lunar's Zelda Style Game", 'level graphics', 'graphics', 'weapons', 'axe', 'full.png')},
    'rapier' : {'cooldown' : 50, 'damage' : 8, 'graphic' : os.path.join("Lunar's Zelda Style Game", 'level graphics', 'graphics', 'weapons', 'rapier', 'full.png')},
    'sai' : {'cooldown' : 80, 'damage' : 10, 'graphic' : os.path.join("Lunar's Zelda Style Game", 'level graphics', 'graphics', 'weapons', 'sai', 'full.png')}
}

magic_data = {
    'flame' : {'strength' : 5, 'cost' : 20, 'graphic': os.path.join("Lunar's Zelda Style Game", 'level graphics', 'graphics', 'particles', 'flame', 'mdako_rocks_res.png')},
    'heal' : {'strength' : 20, 'cost' : 10, 'graphic': os.path.join("Lunar's Zelda Style Game", 'level graphics', 'graphics', 'particles', 'heal', 'chicken_wing_final_res.png')}
}

# enemy
monster_data = {
    'squid': {'health': 100, 'exp': 100, 'damage': 5, 'attack_type': 'slash', 'attack_sound': os.path.join("Lunar's Zelda Style Game", 'level graphics', 'audio', 'attack', 'slash.wav'), 'speed': 3, 'resistance': 3, 'attack_radius': 80, 'notice_radius': 360},
    'raccoon': {'health': 300, 'exp': 250, 'damage': 40, 'attack_type': 'claw', 'attack_sound': os.path.join("Lunar's Zelda Style Game", 'level graphics', 'audio', 'attack', 'claw.wav'), 'speed': 2, 'resistance': 3, 'attack_radius': 120, 'notice_radius': 400},
    'spirit': {'health': 100, 'exp': 110, 'damage': 8, 'attack_type': 'thunder', 'attack_sound': os.path.join("Lunar's Zelda Style Game", 'level graphics', 'audio', 'attack', 'fireball.wav'), 'speed': 4, 'resistance': 3, 'attack_radius': 60, 'notice_radius': 350},
    'bamboo': {'health': 100, 'exp': 100, 'damage': 3, 'attack_type': 'leaf_attack', 'attack_sound': os.path.join("Lunar's Zelda Style Game", 'level graphics', 'audio', 'attack', 'slash.wav'), 'speed': 3, 'resistance': 3, 'attack_radius': 50, 'notice_radius': 300}
}

