import pygame
from bird import Bird
from pipe import Pipe
import random

class Game:
  def __init__(self):
    self.screen = pygame.display.set_mode((1024, 512))
    self.clock = pygame.time.Clock()
    self.bird = Bird()
    self.pipes = []
    self.score = 0
    self.font = pygame.font.SysFont(None, 48)
  
  def run(self):
    running = True
    while running:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
          self.bird.flap()
      
      self.bird.update()
      self.update_pipes()
      self.check_collisions()
      self.update_score()

      self.draw()

      pygame.display.flip()
      self.clock.tick(30)

  def update_pipes(self):
      if not self.pipes or self.pipes[-1].x < 700:
          self.pipes.append(Pipe())
      for pipe in self.pipes:
          pipe.update()
      self.pipes = [pipe for pipe in self.pipes if not pipe.off_screen()]

  def check_collisions(self):
      for pipe in self.pipes:
          if pipe.collides_with(self.bird):
              self.reset_game()

  def update_score(self):
      for pipe in self.pipes:
          if not pipe.scored and pipe.x < self.bird.x:
              self.score += 1
              pipe.scored = True

  def reset_game(self):
      self.bird = Bird()
      self.pipes = []
      self.score = 0

  def draw(self):
      self.screen.fill((0, 0, 0))
      self.bird.draw(self.screen)
      for pipe in self.pipes:
          pipe.draw(self.screen)
      score_text = self.font.render(str(self.score), True, (255, 255, 255))
      self.screen.blit(score_text, (144, 50))