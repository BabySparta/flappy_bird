import pygame

class Bird:
    def __init__(self):
        self.x = 80
        self.y = 300
        self.width = 34
        self.height = 24
        self.velocity = 0
        self.gravity = 1
        self.flap_strength = -10
        self.color = (255, 0, 0)

    def flap(self):
        self.velocity = self.flap_strength

    def update(self):
        self.velocity += self.gravity
        self.y += self.velocity
        if self.y > 600 - self.height:
            self.y = 600 - self.height
        if self.y < 0:
            self.y = 0

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)
