import pygame
import random
pygame.init()

#creates game window
win = pygame.display.set_mode((400,300))
pygame.display.set_caption("Bagels on a Sunday")

# list of availiable toppings and bagels
toppings = ['nothing', 'butter', 'cream cheese', 'lox']
bagels = ['plain', 'everything', 'poppy seed', 'cinnamon raisin']

keybinds = {
    'toppings': {
        pygame.K_q : toppings[0],
        pygame.K_w : toppings[1],
        pygame.K_e : toppings[2],
        pygame.K_r : toppings[3]},
    'bagels' : {
        pygame.K_a : bagels[0],
        pygame.K_s : bagels[1],
        pygame.K_d : bagels[2],
        pygame.K_f : bagels[3]}
}

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

generate_customer_order = True
reset_player_order = True
run = True
while run == True:
    pygame.time.delay(25)

    # generates customers order
    if generate_customer_order == True:
        customer_order = random_customer_order()
        generate_customer_order = False
        print(customer_order)

    # resets player's order
    if reset_player_order == True:
        player_order = blank_order()
        reset_player_order = False

    # checks to quit program
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            # checks player key presses to modify bagel
            for category in keybinds:
                if event.key in keybinds[category]:
                    if category == 'toppings':
                        player_order['topping'] = keybinds['toppings'][event.key]
                    elif category == 'bagels':
                        player_order['bagel'] = keybinds['bagels'][event.key]
                    print(player_order)

            # serves and checks order
            if event.key == pygame.K_SPACE:
                if player_order == customer_order:
                    print('AYY')
                else:
                    print('WRONG')
                generate_customer_order = True
                reset_player_order = True