import pygame

pygame.init()

# 13 x 10 tiles
WINDOW_WIDTH = 832
WINDOW_HEIGHT = 640
TILE_SIZE = 64

game_window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("My first platformer")

# Images
floor_img = pygame.image.load("assets/floor_tile.png")

class World:

	def __init__(self, level, floor_img):
		self.level = level
		self.floor_img = floor_img
	
	def draw_world(self, game_window):
		row_count = 0
		for row in self.level:
			col_count = 0
			for column in row:
				if column == 1:
					game_window.blit(self.floor_img, (col_count * TILE_SIZE, row_count * TILE_SIZE))
				col_count += 1
			row_count += 1




temp_level = [
	[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
	[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
	[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
	[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
	[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
	[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
	[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
	[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
	[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
	[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

run = True
game_world = World(temp_level, floor_img)

while run:

	game_world.draw_world(game_window)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	pygame.display.update()


pygame.quit()