import pygame
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
