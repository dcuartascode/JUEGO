from nave import Nave
import random
class Enemigo(Nave):
    def __init__(self, x, y, image, vida=50, ataque=5, defensa=3, nivel=1, screen_width=800, screen_height=600):
        super().__init__(x, y, image, vida, ataque, defensa, nivel)
        self.velocidad_x = random.choice([-3, -2, -1, 1, 2, 3])
        self.velocidad_y = random.choice([-3, -2, -1, 1, 2, 3])
        self.screen_width = screen_width
        self.screen_height = screen_height

    def mover(self):
        self.x += self.velocidad_x
        self.y += self.velocidad_y
        if self.x <= 0 or self.x >= self.screen_width - self.rect.width:
            self.velocidad_x = -self.velocidad_x
        if self.y <= 0 or self.y >= self.screen_height - self.rect.height:
            self.velocidad_y = -self.velocidad_y
        self.rect.x = self.x
        self.rect.y = self.y

    def atacar(self, nave):
        dano_real = max(0, self.ataque - nave.defensa)
        nave.recibir_dano(dano_real)
