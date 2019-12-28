import sys
import pygame

# Initialize pygame so it runs in the background and manages things
pygame.init()

# Create a font object
font = pygame.font.SysFont("Cambria", 20)
# Create text using the font
text = font.render("Bagels on a Sunday", True, (0,0,0))


# Create a display. Size must be a tuple, which is why it's in parentheses
screen = pygame.display.set_mode( (400, 300) )

# fill the screen with white
screen.fill( (255,255,255) )
# draw text to screen
screen.blit(text, (200, 150) )
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