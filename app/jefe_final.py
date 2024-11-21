from enemigo import Enemigo
from config import jefe_final_image
from bala import Bala

import pygame

class Jefe:

    def __init__(self, x, y, jefe_final_image):
        # Inicialización del jefe con su posición e imagen
        self.rect = pygame.Rect(x, y, jefe_final_image.get_width(), jefe_final_image.get_height())
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

