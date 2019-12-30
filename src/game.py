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

def blank_order():
    # outputs blank order
    return ({
        'topping': toppings[0],
        'bagel': ''
    })

def display_customer_order(bagel, topping):
    # displays the customer's order on the screen
    if bagel == bagels[0]:
        pygame.draw.ellipse(win, (255, 204, 153), (50, 150, 100, 50))
    if topping == toppings[1]:
        pygame.draw.ellipse(win, (255, 255, 0), (50, 100, 90, 40))
    pygame.display.update()

generate_customer_order = True
reset_player_order = True
run = True
keys_b = pygame.key.get_pressed()


while run == True:
    pygame.time.delay(25)

    # checks to quit program
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # generates customers order
    if generate_customer_order == True:
        customer_order = random_customer_order()
        display_customer_order(customer_order['bagel'], customer_order['topping'])
        generate_customer_order = False
        print(customer_order)

    # resets player's order
    if reset_player_order == True:
        player_order = blank_order()
        reset_player_order = False

    # checks and updates player's order
    keys_a = pygame.key.get_pressed()
    if keys_a[pygame.K_q]:
        player_order['topping'] = toppings[0]
    elif keys_a[pygame.K_w]:
        player_order['topping'] = toppings[1]
    elif keys_a[pygame.K_e]:
        player_order['topping'] = toppings[2]
    elif keys_a[pygame.K_r]:
        player_order['topping'] = toppings[3]
    if keys_a[pygame.K_a]:
        player_order['bagel'] = bagels[0]
    elif keys_a[pygame.K_s]:
        player_order['bagel'] = bagels[1]
    elif keys_a[pygame.K_d]:
        player_order['bagel'] = bagels[2]
    elif keys_a[pygame.K_f]:
        player_order['bagel'] = bagels[3]

    # serves and checks order
    if keys_a[pygame.K_SPACE] > keys_b[pygame.K_SPACE]:
        if player_order == customer_order:
            print('SWEET BEANS')
        else:
            print('''('_J')''')
        generate_customer_order = True
        reset_player_order = True
    
    # used to check whether or not keys are pressed or released by comparing with keys_a
    keys_b = pygame.key.get_pressed()