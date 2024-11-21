import pygame
import random
pygame.init()

background_image = pygame.image.load(r"C:\Users\david\Downloads\fondo.jpg")
background_width, background_height = background_image.get_size()

screen_width = int(background_width * 0.8)  
screen_height = background_height
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Space Shooter") 

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

heroe_image = pygame.image.load(r"C:\Users\david\Downloads\klipartz.com (3).png")
doncella_image = pygame.image.load(r"C:\Users\david\Downloads\klipartz.com.png")
nave_image = pygame.image.load(r"C:\Users\david\Downloads\klipartz.com (1).png")
enemigo_image = pygame.image.load(r"C:\Users\david\Downloads\klipartz.com (2).png")
jefe_final_image = pygame.image.load(r"C:\Users\david\Downloads\klipartz.com (4).png")
menu_background_image = pygame.image.load(r"C:\Users\david\Downloads\fondo_menu.jpg")

disparo_doble_image = pygame.image.load(r"C:\Users\david\Downloads\klipartz.com (5).png")
vida_image = pygame.image.load(r"C:\Users\david\Downloads\klipartz.com (6).png")
bomba_image = pygame.image.load(r"C:\Users\david\Downloads\klipartz.com (7).png")

heroe_image = pygame.transform.scale(heroe_image, (80, 80))
doncella_image = pygame.transform.scale(doncella_image, (80, 80))
nave_image = pygame.transform.scale(nave_image, (60, 60))
nave_image = pygame.transform.rotate(nave_image, -90)
enemigo_image = pygame.transform.scale(enemigo_image, (60, 60))
jefe_final_image = pygame.transform.scale(jefe_final_image, (120, 120))
disparo_doble_image = pygame.transform.scale(disparo_doble_image, (40, 40))
vida_image = pygame.transform.scale(vida_image, (40, 40))
bomba_image = pygame.transform.scale(bomba_image, (40, 40))
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))
menu_background_image = pygame.transform.scale(menu_background_image, (screen_width, screen_height))

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

class Enemigo(Nave):
    def __init__(self, x, y, image, vida=50, ataque=5, defensa=3, nivel=1):
        super().__init__(x, y, image, vida, ataque, defensa, nivel)
        self.velocidad_x = random.choice([-3, -2, -1, 1, 2, 3])
        self.velocidad_y = random.choice([-3, -2, -1, 1, 2, 3])

    def mover(self):
        self.x += self.velocidad_x
        self.y += self.velocidad_y
        if self.x <= 0 or self.x >= screen_width - self.rect.width:
            self.velocidad_x = -self.velocidad_x
        if self.y <= 0 or self.y >= screen_height - self.rect.height:
            self.velocidad_y = -self.velocidad_y
        self.rect.x = self.x
        self.rect.y = self.y

    def atacar(self, nave):
        dano_real = max(0, self.ataque - nave.defensa)
        nave.recibir_dano(dano_real)

class JefeFinal(Enemigo):
    def __init__(self, x, y):
        super().__init__(x, y, jefe_final_image, vida=500, ataque=20, defensa=10, nivel=3)
        self.balas = []

    def atacar(self, nave):
        bala = Bala(self.x + self.rect.width // 2, self.y + self.rect.height)
        bala.velocidad_y = 5
        self.balas.append(bala)

class Bala:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocidad_y = -5
        self.rect = pygame.Rect(x, y, 5, 5)

    def mover(self):
        self.y += self.velocidad_y
        self.rect.y = self.y

class PowerUp:
    def __init__(self, x, y, tipo, image):
        self.x = x
        self.y = y
        self.tipo = tipo
        self.image = image
        self.rect = self.image.get_rect(topleft=(x, y))

    def dibujar(self):
        screen.blit(self.image, (self.x, self.y))

class Juego:
    def __init__(self):
        self.nave = None
        self.balas = []
        self.enemigos = [Enemigo(random.randint(0, screen_width - 60), random.randint(0, screen_height - 60), enemigo_image) for _ in range(10)]
        self.power_ups = []
        self.jefe_final = None
        self.reloj = pygame.time.Clock()
        self.ejecutando = True
        self.en_menu = True
        self.jefe_final_aparecido = False
        self.ancho_pantalla = 100
        self.margen_barra_vida = 20
        self.mensaje = ""
        self.juego_terminado = False
        self.tiempo_inicio_mensaje = 0
        self.mensaje_final = ""
        self.color_mensaje_final = WHITE

    def generar_power_up(self):
        tipos = [
            ("disparo_doble", disparo_doble_image),
            ("vida", vida_image),
            ("bomba", bomba_image)
        ]
        tipo, imagen = random.choice(tipos)
        x = random.randint(0, screen_width - 40)
        y = random.randint(0, screen_height - 40)
        self.power_ups.append(PowerUp(x, y, tipo, imagen))

    def manejar_eventos(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                self.ejecutando = False
            
            if self.en_menu:
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_1:
                        self.nave = Nave(screen_width // 2, screen_height - 100, heroe_image)
                        self.en_menu = False
                    elif evento.key == pygame.K_2:
                        self.nave = Nave(screen_width // 2, screen_height - 100, doncella_image)
                        self.en_menu = False
                    elif evento.key == pygame.K_3:
                        self.nave = Nave(screen_width // 2, screen_height - 100, nave_image)
                        self.en_menu = False
                    elif evento.key == pygame.K_ESCAPE:
                        self.ejecutando = False
            elif not self.juego_terminado:
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_LEFT:
                        self.nave.velocidad_x = -4
                    if evento.key == pygame.K_RIGHT:
                        self.nave.velocidad_x = 4
                    if evento.key == pygame.K_UP:
                        self.nave.velocidad_y = -4
                    if evento.key == pygame.K_DOWN:
                        self.nave.velocidad_y = 4
                    if evento.key == pygame.K_SPACE:
                        if not self.nave.puede_disparar_doble:
                            self.balas.append(Bala(self.nave.x + 30, self.nave.y))
                        else:
                            self.balas.append(Bala(self.nave.x + 20, self.nave.y))
                            self.balas.append(Bala(self.nave.x + 40, self.nave.y))

                if evento.type == pygame.KEYUP:
                    if evento.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                        self.nave.velocidad_x = 0
                    if evento.key in [pygame.K_UP, pygame.K_DOWN]:
                        self.nave.velocidad_y = 0

                for power_up in self.power_ups[:]:
                    if self.nave.rect.colliderect(power_up.rect):
                        if power_up.tipo == "disparo_doble":
                            self.nave.puede_disparar_doble = True
                        elif power_up.tipo == "vida":
                            self.nave.vida += 50
                        elif power_up.tipo == "bomba":
                            self.enemigos.clear()
                        self.power_ups.remove(power_up)

    def mostrar_menu(self):
        screen.blit(menu_background_image, (0, 0))
        fuente = pygame.font.SysFont(None, 48)
        texto_titulo = fuente.render("Space Shooter", True, WHITE)
        texto_heroe = fuente.render("1 - Héroe", True, WHITE)
        texto_doncella = fuente.render("2 - Doncella", True, WHITE)
        texto_nave = fuente.render("3 - Nave", True, WHITE)
        texto_escape = fuente.render("Presiona ESC para salir", True, WHITE)
        
        screen.blit(texto_titulo, (screen_width // 2 - texto_titulo.get_width() // 2, 100))
        screen.blit(texto_heroe, (screen_width // 2 - texto_heroe.get_width() // 2, 200))
        screen.blit(heroe_image, (screen_width // 2 - heroe_image.get_width() // 2, 250))
        screen.blit(texto_doncella, (screen_width // 2 - texto_doncella.get_width() // 2, 400))
        screen.blit(doncella_image, (screen_width // 2 - doncella_image.get_width() // 2, 450))
        screen.blit(texto_nave, (screen_width // 2 - texto_nave.get_width() // 2, 600))
        screen.blit(nave_image, (screen_width // 2 - nave_image.get_width() // 2, 650))
        screen.blit(texto_escape, (screen_width // 2 - texto_escape.get_width() // 2, 800))
        pygame.display.flip()

    def actualizar(self):
        if self.juego_terminado:
            tiempo_actual = pygame.time.get_ticks()
            if tiempo_actual - self.tiempo_inicio_mensaje > 5000:  
                self.reiniciar_juego()
            return

        if self.nave:
            self.nave.mover()

        for bala in self.balas[:]:
            bala.mover()
            if bala.y < 0 or bala.y > screen_height:
                self.balas.remove(bala)

        for enemigo in self.enemigos[:]:
            enemigo.mover()
            if self.nave.rect.colliderect(enemigo.rect):
                self.nave.recibir_dano(10)
                self.enemigos.remove(enemigo)

        if self.nave.nivel == 3 and not self.jefe_final_aparecido:
            self.jefe_final = JefeFinal(screen_width // 2, 50)
            self.enemigos = [Enemigo(random.randint(0, screen_width - 60), 
                                     random.randint(0, screen_height - 60), 
                                     enemigo_image) for _ in range(6)]
            self.jefe_final_aparecido = True

        if self.jefe_final:
            self.jefe_final.mover()
            if random.random() < 0.02:
                self.jefe_final.atacar(self.nave)

            if self.nave.rect.colliderect(self.jefe_final.rect):
                self.nave.recibir_dano(20)

            for bala in self.jefe_final.balas[:]:
                bala.mover()
                if bala.rect.colliderect(self.nave.rect):
                    self.nave.recibir_dano(10)
                    self.jefe_final.balas.remove(bala)
                elif bala.y > screen_height:
                    self.jefe_final.balas.remove(bala)

        for bala in self.balas[:]:
            if self.jefe_final and bala.rect.colliderect(self.jefe_final.rect):
                self.balas.remove(bala)
                self.jefe_final.recibir_dano(self.nave.ataque)
            
            for enemigo in self.enemigos[:]:
                if bala.rect.colliderect(enemigo.rect):
                    self.balas.remove(bala)
                    self.enemigos.remove(enemigo)
                    self.nave.enemigos_eliminados += 1
                    if self.nave.enemigos_eliminados >= 5 and self.nave.nivel < 3:
                        self.nave.subir_nivel()
                        self.mensaje = f"¡Nivel {self.nave.nivel}!"
                    if self.nave.vida <= 70:
                        self.nave.vida += 10
                    break

        if self.jefe_final and self.jefe_final.vida <= 0:
            self.mostrar_mensaje_final("¡GANADOR!", YELLOW)

        if not self.enemigos and not self.jefe_final:
            self.enemigos = [Enemigo(random.randint(0, screen_width - 60), 
                                     random.randint(0, screen_height - 60), 
                                     enemigo_image) for _ in range(10 + self.nave.nivel * 2)]

        if random.random() < 0.02 and self.nave and self.nave.nivel > 1 and self.nave.nivel <= 10:
            self.generar_power_up()

        if self.nave and self.nave.vida <= 0:
            self.mostrar_mensaje_final("HAS PERDIDO", RED)

    def dibujar(self):
        screen.blit(background_image, (0, 0))
        
        if self.juego_terminado:
            self.mostrar_mensaje_final(self.mensaje_final, self.color_mensaje_final)
        else:
            if self.nave:
                self.nave.dibujar()

            for bala in self.balas:
                pygame.draw.rect(screen, WHITE, bala.rect)

            for enemigo in self.enemigos:
                enemigo.dibujar()

            for power_up in self.power_ups:
                power_up.dibujar()

            if self.jefe_final:
                self.jefe_final.dibujar()
                for bala in self.jefe_final.balas:
                    pygame.draw.rect(screen, WHITE, bala.rect)

            if self.jefe_final:
                fuente = pygame.font.SysFont(None, 48)
                texto_vida_jefe = fuente.render("Vida del Jefe:", True, WHITE)
                screen.blit(texto_vida_jefe, (screen_width - 400, 20))
                texto_batalla_final = fuente.render("¡Batalla Final!", True, WHITE)
                screen.blit(texto_batalla_final, (screen_width // 2 - texto_batalla_final.get_width() // 2, 50))

                barra_vida_jefe = pygame.Rect(screen_width - 160, 30, int(self.jefe_final.vida * 0.3), 10)
                pygame.draw.rect(screen, RED, barra_vida_jefe)

            if self.nave:
                fuente = pygame.font.SysFont(None, 36)
                texto_vida = fuente.render(f"Vida: {self.nave.vida}", True, WHITE)
                texto_nivel = fuente.render(f"Nivel: {self.nave.nivel}", True, WHITE)
                texto_enemigos = fuente.render(f"Enemigos eliminados: {self.nave.enemigos_eliminados}", True, WHITE)
                
                screen.blit(texto_vida, (10, 10))
                screen.blit(texto_nivel, (10, 50))
                screen.blit(texto_enemigos, (10, 90))

            if self.mensaje:
                fuente_mensaje = pygame.font.SysFont(None, 36)
                texto_mensaje = fuente_mensaje.render(self.mensaje, True, WHITE)
                screen.blit(texto_mensaje, (screen_width // 2 - texto_mensaje.get_width() // 2, screen_height - 50))

        pygame.display.flip()

    def mostrar_mensaje_final(self, mensaje, color):
        self.mensaje_final = mensaje
        self.color_mensaje_final = color
        self.juego_terminado = True
        self.tiempo_inicio_mensaje = pygame.time.get_ticks()

        fuente = pygame.font.SysFont(None, 100)
        texto = fuente.render(mensaje, True, color)
        texto_rect = texto.get_rect(center=(screen_width//2, screen_height//2))
        
        s = pygame.Surface((screen_width, screen_height), pygame.SRCALPHA)
        s.fill((0,0,0,128))
        screen.blit(s, (0,0))
        
        screen.blit(texto, texto_rect)
        pygame.display.flip()

    def reiniciar_juego(self):
        self.en_menu = True
        self.juego_terminado = False
        self.nave = None
        self.jefe_final = None
        self.jefe_final_aparecido = False
        self.enemigos = [Enemigo(random.randint(0, screen_width - 60), random.randint(0, screen_height - 60), enemigo_image) for _ in range(10)]
        self.balas = []
        self.power_ups = []
        self.mensaje = ""
        self.mensaje_final = ""
        self.color_mensaje_final = WHITE

def juego():
    juego = Juego()
    
    while juego.ejecutando:
        juego.manejar_eventos()
        if juego.en_menu:
            juego.mostrar_menu()
        else:
            juego.actualizar()
            juego.dibujar()
        juego.reloj.tick(60)

juego()

pygame.quit()