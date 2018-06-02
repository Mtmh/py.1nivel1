if True:
	import pygame

	pygame.init()
	clock = pygame.time.Clock()
	screen = pygame.display.set_mode((400, 300))
	screen.fill(pygame.Color("white"))
	surface = pygame.Surface((100, 100))
	screen.blit(surface, (20, 20))
	pygame.display.flip()

	done = False

	while not done:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True
		#Espacio de Trabajo
		# surface = pygame.Surface((100, 100))
		# pygame.display.flip()
		clock.tick(60)	