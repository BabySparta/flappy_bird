import pygame
import random

class Pipe: 
  def __init__(self):
    self.x = 900
    self.gap = 100
    self.width = 50
    self.top_height =  random.randint(50, 300)
    self.bottom_height = 600 - self.top_height - self.gap
    self.velocity = -5
    self.color = 0, 255, 0
    self.scored = False
  
  def update(self):
    self.x += self.velocity
  
  def off_screen(self):
    return self.x < -self.width
  
  def collides_with(self, bird):
    bird_rect = bird.get_rect()
    top_rect = pygame.Rect(self.x, 0, self.width, self.top_height)
    bottom_rect = pygame.Rect(self.x, 600 - self.bottom_height, self.width, self.bottom_height)
    return bird_rect.colliderect(top_rect) or bird_rect.colliderect(bottom_rect)

  def draw(self, screen):
    pygame.draw.rect(screen, self.color, (self.x, 0, self.width, self.top_height))
    pygame.draw.rect(screen, self.color, (self.x, 600 - self.bottom_height, self.width, self.bottom_height))

