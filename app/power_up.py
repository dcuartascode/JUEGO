from config import screen
class PowerUp:
    def __init__(self, x, y, tipo, image):
        self.x = x 
        self.y = y  
        self.tipo = tipo
        self.image = image
        self.rect = self.image.get_rect(topleft=(x, y))

    def dibujar(self):
        screen.blit(self.image, (self.x, self.y))

