import pygame
import random
pygame.init()

#creates game window
win = pygame.display.set_mode((400,300))
pygame.display.set_caption("Bagels on a Sunday")

# list of availiable toppings and bagels
toppings = ['nothing', 'butter', 'cream cheese', 'lox']
bagels = ['plain', 'everything', 'poppy seed', 'cinnamon raisin']

def random_customer_order():
    # outputs random order for customers 
    return ({
        'topping': random.choice(toppings),
        'bagel': random.choice(bagels)
    })

def display_customer_order(bagel, topping):
    # displays the customer's order on the screen
    if bagel == 'plain':
        pygame.draw.ellipse(win, (255, 204, 153), (50, 150, 100, 50))
    if topping == 'butter':
        pygame.draw.ellipse(win, (255, 255, 0), (50, 15, 90, 40))
    pygame.display.update()

customer_placed_order = False
run = True

while run == True:
    pygame.time.delay(50)

    # checks to quit program
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # generates customer order if not yet placed
    if customer_placed_order == False:
        customer_order = random_customer_order()
        display_customer_order(customer_order['bagel'], customer_order['topping'])
        customer_placed_order = True