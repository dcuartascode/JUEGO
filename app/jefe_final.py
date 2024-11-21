from bala import Bala
class Jefe:

    def __init__(self, x, y, jefe_final_image):
        self.x = x
        self.y = y
        self.rect = jefe_final_image.get_rect(topleft=(x, y))
        self.imagen = jefe_final_image
        self.vida = 500
        self.ataque = 20
        self.defensa = 10
        self.nivel = 3
        self.balas = []  # Lista para almacenar las balas del jefe

    def actualizar(self):
        """Actualiza la posición de las balas"""
        for bala in self.balas[:]:
            bala.actualizar()
            if bala.rect.top > 800:  # Si las balas salen de la pantalla
                self.balas.remove(bala)

    def atacar(self):
        """Método para crear y agregar una nueva bala"""
        bala = Bala(self.rect.centerx, self.rect.bottom)  # Crea una nueva bala
        self.balas.append(bala)

    def dibujar(self, pantalla):
        """Dibuja al jefe y sus balas en la pantalla"""
        pantalla.blit(self.imagen, self.rect)  # Dibuja la imagen del jefe
        
        # Dibuja las balas
        for bala in self.balas:
            bala.dibujar(pantalla)

