import import_handler as shared

class Circle(shared.pygame.sprite.Sprite):
    def __init__(self, image, position):
        shared.pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.position = position
        if self.position == 0:
            self.rect.center = (shared.screen_width/7, shared.screen_height/2)
        elif self.position == 1:
            self.rect.center = (shared.screen_width/3.4, shared.screen_height/2)
        elif self.position == 2:
            self.rect.center = (shared.screen_width/2.3, shared.screen_height/2)
        elif self.position == 3:
            self.rect.center = (shared.screen_width/1.73, shared.screen_height/2)
        elif self.position == 4:
            self.rect.center = (shared.screen_width/1.4, shared.screen_height/2)
        elif self.position == 5:
            self.rect.center = (shared.screen_width * 6 / 7, shared.screen_height/2)
    
    def draw(self):
        shared.screen.blit(self.image, self.rect)

        
