import pygame

pygame.init()

# display dimensions
display_width = 1200
display_height = 640

white = (255, 255, 255)

displayScreen = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Somegame')
clock = pygame.time.Clock()

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    
    displayScreen.fill(white)
         
    pygame.display.update()
    clock.tick(60)