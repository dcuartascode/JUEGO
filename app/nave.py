from config import screen_width,screen_height,screen
class Nave:
    def __init__(self, x, y, image, vida=100, ataque=10, defensa=5, nivel=1):
        self.x = x
        self.y = y
        self.image = image
        self.velocidad_x = 0
        self.velocidad_y = 0
        self.rect = self.image.get_rect(topleft=(x, y))
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa
        self.nivel = nivel
        self.enemigos_eliminados = 0
        self.puede_disparar_doble = False

    def mover(self):
        self.x += self.velocidad_x
        self.y += self.velocidad_y
        self.x = max(0, min(self.x, screen_width - self.rect.width))
        self.y = max(0, min(self.y, screen_height - self.rect.height))
        self.rect.x = self.x
        self.rect.y = self.y

    def dibujar(self):
        screen.blit(self.image, (self.x, self.y))

    def recibir_dano(self, danio):
        dano_real = max(0, danio - self.defensa)
        self.vida -= dano_real
        if self.vida <= 0:
            self.vida = 0

    def subir_nivel(self):
        if self.nivel < 10:
            self.nivel += 1
            self.vida += 20
            self.ataque += 5
            self.defensa += 2