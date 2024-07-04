import pygame
import sys

def main():

  pygame.init()

  screen_width, screen_height = 800, 600
  screen = pygame.display.set_mode((screen_width, screen_height))
  pygame.display.set_caption('Flappy Bird')

  running = True
  while running:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
    
    screen.fill((255, 255, 255))
    
    pygame.display.flip()
    
  pygame.quit()
  sys.exit()


main()