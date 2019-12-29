import sys
import pygame

# Initialize pygame so it runs in the background and manages things
pygame.init()


# Screen size parameters
display_width, display_height = 800, 600


# Returns text as a surface and a rectangle
def text_objects(text, color, font_type, size):
    font = pygame.font.SysFont(font_type, size)
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

# Displays text at center of screen
def message_to_screen(msg,color, font_type="Cambria", size=20):
    textSurf, textRect = text_objects(msg, color, font_type, size)
    textRect.center = (display_width / 2), (display_height / 2)
    screen.blit(textSurf, textRect)


# Create a display. Size must be a tuple, which is why it's in parentheses
screen = pygame.display.set_mode( (display_width, display_height) )

# fill the screen with white
screen.fill( (255,255,255) )
# draw text to screen
message_to_screen("Bagels on a Sunday", (0,0,0), "Times New Roman", 30)
# update the display
pygame.display.flip()

# Main loop. Your game would go inside this loop
while True:
    # do something for each event in the event queue (list of things that happen)
    for event in pygame.event.get():

        # This line will print each event to the terminal
        print(event)

        # Check to see if the current event is a QUIT event
        if event.type == pygame.QUIT:
            # If so, exit the program
            sys.exit()