import pygame, random, os
pygame.init()

try:
    # Change the current working Directory    
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    print('Directory changed')
except OSError:
    print('Cannot change the Current Working Directory')

class Object:
    # class for objects on screen
    def __init__(self, x, y):
        self.x = x
        self.y = y

bagel_info = Object(35, 9)
customer_info = Object(2, 0)

class Screen:
    # class for surfaces
    def __init__(self, width, height):
        self.width = width
        self.height = height

# creates game surfaces
screen_scale = 20
miniscreen = Screen(64, 36)
gamescreen = Screen(miniscreen.width * screen_scale, miniscreen.height * screen_scale)

miniscreen_surface = pygame.Surface((miniscreen.width, miniscreen.height))
gamescreen_surface = pygame.display.set_mode((gamescreen.width, gamescreen.height))
pygame.display.set_caption("Bagels on a Sunday")

# list of availiable toppings and bagels
toppings = ['nothing', 'butter', 'cream cheese', 'lox']
bagels = ['plain', 'everything', 'poppy seed', 'cinnamon raisin']

# player keybind dictionary for bagel customization
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

# image dictionary
images = {
    'misc' : {
        'background' : pygame.image.load('img/background.png'),
        'counter' : pygame.image.load('img/counter.png'),
        'customer' : pygame.image.load('img/customer_concept.png')},
    'bagel' : {
        'plain' : pygame.image.load('img/bagel_plain.png'),
        'everything' : pygame.image.load('img/bagel_everything.png'),
        'poppy seed' : pygame.image.load('img/bagel_poppyseed.png'),
        'cinnamon raisin' : pygame.image.load('img/bagel_cinnamonraisin.png')},
    'topping' : {
        'butter' : pygame.image.load('img/topping_butter.png'),
        'cream cheese' : pygame.image.load('img/topping_creamcheese.png'),
        'lox' : pygame.image.load('img/topping_lox.png')
    }
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

def update_screen():
    # displays game
    miniscreen_surface.blit(images['misc']['background'], (0,0))
    miniscreen_surface.blit(images['misc']['customer'], (customer_info.x, customer_info.y))
    for bagel in bagels:
        if player_order['bagel'] == bagel:
            miniscreen_surface.blit(images['bagel'][bagel], (bagel_info.x, bagel_info.y))
    for topping in toppings:
        if player_order['topping'] == topping and player_order['topping'] != 'nothing':
            miniscreen_surface.blit(images['topping'][topping], (bagel_info.x, bagel_info.y))    
    miniscreen_surface.blit(images['misc']['counter'], (0,0))
    pygame.transform.scale(miniscreen_surface, (gamescreen.width, gamescreen.height), gamescreen_surface)
    pygame.display.update()

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
                        if player_order['bagel'] == '':
                            player_order['bagel'] = 'plain'
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

    update_screen()