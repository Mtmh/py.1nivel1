if True:
	import pygame 
    

	pygame.init()
	clock = pygame.time.Clock()
	screen = pygame.display.set_mode((400, 300))
	screen.fill(pygame.Color("white"))
	surface = pygame.Surface((100, 100))
	screen.blit(surface, (30, 30))
	done = False
	color = (000, 000, 000)
	
	while not done:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True
		#Espacio de Trabajo
		#pygame.draw.rect(screen, color, pygame.Rect(30, 30, 60, 60))

		pygame.display.flip()
		clock.tick(60)