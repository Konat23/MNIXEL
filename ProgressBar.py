import pygame
import sys

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

class ProgressBar:
    def __init__(self, screen):
        self.screen = screen
        self.count = 0

    def update(self, count):
        self.count = count

    def draw(self):
        # Size of rectangles and spacing
        rect_width = 44
        rect_height = 44
        posx = 14
        posy = 530
        spacing = 0

        for i in range(10):
            if i < self.count:
                color = GREEN  # Change color based on self.count
            else:
                color = RED

            pygame.draw.rect(self.screen, color,  (posx +i * (rect_width + spacing), posy, rect_width, rect_height))
            pygame.draw.rect(self.screen, WHITE,  (posx +i * (rect_width + spacing), posy, rect_width, rect_height),1)

def main():
    pygame.init()
    screen = pygame.display.set_mode((500, 60))
    pygame.display.set_caption("Progress Bar")

    clock = pygame.time.Clock()
    progress_bar = ProgressBar(screen)

    running = True
    count = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        count += 1
        if count > 10:
            count = 0

        progress_bar.update(count)

        screen.fill(BLACK)
        progress_bar.draw()
        pygame.display.flip()

        clock.tick(2)  # Controls the update speed

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
