import pygame
from config import screen
class PowerUp:
    def __init__(self,x,y,tipo,image):
         # Inicializar posición y tipo de power-up.
         self.x=x 
         # Tipo de power-up.
         self.tipo=tipo 
         # Imagen del power-up.
         self.image=image 
         # Crear un rectángulo para colisiones.
         self.rect=self.image.get_rect(topleft=(x,y))

    def dibujar(self):
         # Dibujar el power-up en pantalla.
         screen.blit(self.image,(self.x,self.y))

