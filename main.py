"""
@author: Konat
Codigo principal MNIXEL 
"""

# RGB Colores
Black = (0, 0, 0)
White =(255, 255, 255)
Green = (0, 255, 0)
Red = (255, 0, 0)
Blue = (0, 0, 255) 
Gray = (127, 127, 127)

# Tamaños
scale = 2.5 # para tener mas pixeles poner un numero mayor que 1
filas = int(28*scale)
columnas = int(28*scale)
border = 2

margin = 10 # pixeles que se consideran cerca 


board_size =(560,560) #tamaño de de la sona donde se dibujara
centerboard = (board_size[0]/2,board_size[1]/2)
pixel_size = (board_size[0]/columnas,board_size[1]/filas)
size = (800, 800) # Tamaño de la ventana
centersize = (size[0]/2,size[1]/2)

# Pygame
import pygame, sys
pygame.init()
screen = pygame.display.set_mode(size) #Crear ventana
surfaceOne = pygame.Surface(board_size)

clock = pygame.time.Clock()


class Pixel():
    def __init__(self, loc) -> None:

        self.left = loc[0]
        self.top = loc[1]
        self.width = pixel_size[0]
        self.height = pixel_size[1]
        self.color = 'black'
        
        self.rect = pygame.Rect(self.left , self.top , self.width, self.height)
        self.insiderect = pygame.Rect(loc[0]+border/2, loc[1]+border/2, pixel_size[0]-border, pixel_size[1]-border)

        

    def draw(self,surface, colorborder):
        
        pygame.draw.rect(surface, colorborder, self.rect)
        pygame.draw.rect(surface, self.color, self.insiderect)

    def paint(self, mouse):
        """
        Esta funcion se encarga de colorear
        """  
        if (mouse[0]> self.left-margin) and (mouse[0] < self.left+self.width+margin):
            if (mouse[1]> self.top-margin) and (mouse[1] < self.top+self.height+margin):
                self.color = 'white'


def events():
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
array = [[Pixel((j*pixel_size[0],i*pixel_size[1])) for i in range(columnas)] for j in range(filas)]
while True:    
    events()
    screen.fill(Black) #color de fondo y limpia pantalla   
        
    #------------ ZONA DE DIBUJO -----------------#
    offset_surface = [centersize[0]-centerboard[0], centersize[1]-centerboard[1]]
    screen.blit(surfaceOne, offset_surface)
    mouse = pygame.mouse

    # Verifica si el botón izquierdo del mouse está presionado (clic)
    clic_izquierdo, _, _ = mouse.get_pressed()
    mouse_pos = mouse.get_pos()
    for raw in array:
        for pixel in raw:
            pixel.draw(surfaceOne, Gray)
            if clic_izquierdo:
                pixel.paint((mouse_pos[0]-offset_surface[0],mouse_pos[1]-offset_surface[1]))
    
    
    #-----------FIN ZONA DE DIBUJO ---------------#            
    #Actualizar pantalla
    pygame.display.flip()
    clock.tick(60)