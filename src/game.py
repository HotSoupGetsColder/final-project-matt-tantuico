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

class Score:
    # class for player score
    def __init__(self, correct, incorrect):
        self.correct = correct
        self.incorrect = incorrect

score = Score(0, 0)

# creates font object
font = pygame.font.SysFont("Times New Roman", 5)

# creates game surfaces
screen_scale = 15
miniscreen = Screen(64, 36)
gamescreen = Screen(miniscreen.width * screen_scale, miniscreen.height * screen_scale)

miniscreen_surface = pygame.Surface((miniscreen.width, miniscreen.height))
gamescreen_surface = pygame.display.set_mode((gamescreen.width, gamescreen.height))
pygame.display.set_caption("Bagels on a Sunday")

# list of availiable toppings and bagels
toppings = ['nothing', 'butter', 'cream cheese', 'lox']
bagels = ['plain', 'everything', 'poppy seed', 'cinnamon raisin']

# list of customers' non-essential features
faces = ['red', 'yellow', 'green', 'blue']

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
        'customer' : pygame.image.load('img/concept_customer.png')},
    'bagel' : {
        'plain' : pygame.image.load('img/bagel_plain.png'),
        'everything' : pygame.image.load('img/bagel_everything.png'),
        'poppy seed' : pygame.image.load('img/bagel_poppyseed.png'),
        'cinnamon raisin' : pygame.image.load('img/bagel_cinnamonraisin.png')},
    'topping' : {
        'butter' : pygame.image.load('img/topping_butter.png'),
        'cream cheese' : pygame.image.load('img/topping_creamcheese.png'),
        'lox' : pygame.image.load('img/topping_lox.png')},
    'shirt' : {
        'plain' : pygame.image.load('img/shirt_plain.png'),
        'everything' : pygame.image.load('img/shirt_everything.png'),
        'poppy seed' : pygame.image.load('img/shirt_poppyseed.png'),
        'cinnamon raisin' : pygame.image.load('img/shirt_cinnamonraisin.png')},
    'hat' : {
        'butter' : pygame.image.load('img/hat_butter.png'),
        'cream cheese' : pygame.image.load('img/hat_creamcheese.png'),
        'lox' : pygame.image.load('img/hat_lox.png')},
    'face' : {
        'red' : pygame.image.load('img/face_red.png'),
        'yellow' : pygame.image.load('img/face_yellow.png'),
        'green' : pygame.image.load('img/face_green.png'),
        'blue' : pygame.image.load('img/face_blue.png')} 
    }

def random_customer_order():
    # outputs random order for customers 
    return ({
        'topping': random.choice(toppings),
        'bagel': random.choice(bagels)
    })

def random_customer_features():
    return ({
        'face': random.choice(faces)
    })

def blank_order():
    # outputs blank order
    return ({
        'topping': toppings[0],
        'bagel': ''
    })

def animate_screen():
    global customer_info
    if customer_info.y > 0:
        customer_info.y -= 1

def update_screen():
    # displays game
    miniscreen_surface.blit(images['misc']['background'], (0,0))
    for bagel in bagels:
        if customer_order['bagel'] == bagel:
            miniscreen_surface.blit(images['shirt'][bagel], (customer_info.x, customer_info.y))
    for face in faces:
        if customer_features['face'] == face:
            miniscreen_surface.blit(images['face'][face], (customer_info.x, customer_info.y))
    for topping in toppings:
        if customer_order['topping'] == topping and customer_order['topping'] != 'nothing':
            miniscreen_surface.blit(images['hat'][topping], (customer_info.x, customer_info.y))    
    for bagel in bagels:
        if player_order['bagel'] == bagel:
            miniscreen_surface.blit(images['bagel'][bagel], (bagel_info.x, bagel_info.y))
    for topping in toppings:
        if player_order['topping'] == topping and player_order['topping'] != 'nothing':
            miniscreen_surface.blit(images['topping'][topping], (bagel_info.x, bagel_info.y))    
    miniscreen_surface.blit(images['misc']['counter'], (0,0))

    text_score_correct = font.render(str(score.correct), True, (0, 0, 0))
    text_score_incorrect = font.render(str(score.incorrect), True, (0, 0, 0))
    miniscreen_surface.blit(text_score_correct, (4, miniscreen.height - 8))
    pygame.transform.scale(miniscreen_surface, (gamescreen.width, gamescreen.height), gamescreen_surface)
    pygame.display.update()

new_round = True
run = True
while run == True:
    pygame.time.delay(25)

    # runs start of round code
    if new_round:
        # gets new customer order and resets player's order
        customer_order = random_customer_order()
        customer_features = random_customer_features()
        player_order = blank_order()

        # reset image locations
        customer_info.y = miniscreen.height

        new_round = False
    
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

            # serves and checks order
            if event.key == pygame.K_SPACE:
                if player_order != blank_order():
                    if player_order == customer_order:
                        print('AYY')
                        score.correct += 1
                    else:
                        print('WRONG')
                        score.incorrect += 1
                    new_round = True
            
            # checks to exit fullscreen
            if event.key == pygame.K_ESCAPE:
                pygame.display.toggle_fullscreen()
    
    animate_screen()
    update_screen()