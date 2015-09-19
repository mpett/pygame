from classes import *
from process import process

# Init
pygame.init()
SCREENWIDTH, SCREENHEIGHT = 1280, 720
screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT), 0, 32)
clock = pygame.time.Clock()
background = pygame.image.load("images/underwater_background/background2.png")
narwhal1 = Narwhal(0, SCREENHEIGHT - 90, 261, 92, "images/single_narwhal.png", 7)
helmetfish = HelmetFish(40, 100, 78, 36, "images/helmetfish.png")
helmetfish2 = HelmetFish(60, 400, 78, 36, "images/helmetfish.png")
helmetfish3 = HelmetFish(90, 800, 78, 36, "images/helmetfish.png")
FPS = 24

# Colors
clr1 = (123, 23, 34)
clr2 = (55, 233, 12)
clr3 = (25, 44, 123)
changing_color = 0

# ----------- Main game loop -----------
while True:
    # Processes
    process(narwhal1)
    # Logic
    narwhal1.motion(SCREENWIDTH)
    HelmetFish.movement(SCREENWIDTH)

    #Draw
    screen.blit(background, (0, 0))
    BaseClass.all_sprites.draw(screen)

    # Flip y-axis
    pygame.display.flip()

    # Clock
    clock.tick(FPS)
# ----------- Main game loop -----------