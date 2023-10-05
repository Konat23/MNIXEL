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
scale = 1 # para tener mas pixeles poner un numero mayor que 1
filas = int(28*scale)
columnas = int(28*scale)
border = 2




board_size =(560,560) #tamaño de de la sona donde se dibujara
centerboard = (board_size[0]/2,board_size[1]/2)
pixel_size = (board_size[0]/columnas,board_size[1]/filas)
size = (800, 800) # Tamaño de la ventana
centersize = (size[0]/2,size[1]/2)

# Pygame
import pygame, sys
from slider import Slider
pygame.init()
screen = pygame.display.set_mode(size) #Crear ventana


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

    def paint(self, mouse,margin):
        """
        Esta funcion se encarga de colorear
        """  
        if (mouse[0]> self.left-margin) and (mouse[0] < self.left+self.width+margin):
            if (mouse[1]> self.top-margin) and (mouse[1] < self.top+self.height+margin):
                self.color = (255,255,255)

class Grid():
    def __init__(self,size,offset) -> None:
        self.offset = offset
        self.surfaceOne = pygame.Surface(size)
        self.array = [[Pixel((j*pixel_size[0],i*pixel_size[1])) for i in range(columnas)] for j in range(filas)]
        self.margin = 10 # pixeles que se consideran cerca 
    
    def draw(self):
        screen.blit(self.surfaceOne, self.offset)
        for raw in self.array:
            for pixel in raw:
                pixel.draw(self.surfaceOne, Gray)
                if clic_izquierdo:
                    pixel.paint((mouse_pos[0]-offset_surface[0],mouse_pos[1]-offset_surface[1]),self.margin)
    def set_margin(self,slider):
        self.margin = slider.get_value()*20 # Va de 0 a 20 pixeles
    
    def update(self, slider):
        self.draw()
        self.set_margin(slider)





def events():
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        slider.handle_event(event)

offset_surface = [centersize[0]-centerboard[0], centersize[1]-centerboard[1]]     
mygrid = Grid(board_size,offset_surface)

slider = Slider(10, 10, 600, 20)

while True:    
    events()
    screen.fill(Black) #color de fondo y limpia pantalla   
        
    #------------ ZONA DE DIBUJO -----------------#
    
    
    mouse = pygame.mouse

    # Verifica si el botón izquierdo del mouse está presionado (clic)
    clic_izquierdo, _, _ = mouse.get_pressed()
    mouse_pos = mouse.get_pos()
    
    

    slider.update()
    slider.draw(screen)

    mygrid.update(slider)
    
    #-----------FIN ZONA DE DIBUJO ---------------#            
    #Actualizar pantalla
    pygame.display.flip()
    clock.tick(60)