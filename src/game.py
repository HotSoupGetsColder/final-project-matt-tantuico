import pygame, random, os, sys
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
text_info = Object(4, 27)

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

# clock variables
clock = pygame.time.Clock()
fps = 60

class Timer:
    # class for game timers
    def __init__(self, original):
        self.original = original * fps
        self.current = original * fps
        self.run = False
    def reset(self):
        self.current = self.original

# timers used in program
reaction = Timer(.5)
day = Timer(30)

# creates font object
font = pygame.font.SysFont("Comic Sans", 12)

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
emotions = ['neutral', 'happy', 'sad']

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
        'main menu' : pygame.image.load('img/menu_main.png'),
        'pause menu' : pygame.image.load('img/menu_pause.png'),
        'background' : pygame.image.load('img/background.png'),
        'counter' : pygame.image.load('img/counter.png'),
        'closed' : pygame.image.load('img/background_closed.png'),
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
        'blue' : pygame.image.load('img/face_blue.png')},
    'emotion' : {
        'neutral' : pygame.image.load('img/emotion_neutral.png'),
        'happy' : pygame.image.load('img/emotion_happy.png'),
        'sad' : pygame.image.load('img/emotion_sad.png')}
    }

def random_customer_order():
    # outputs random order for customers 
    return ({
        'topping': random.choice(toppings),
        'bagel': random.choice(bagels)
    })

def random_customer_features():
    return ({
        'face': random.choice(faces),
        'emotion': 'neutral'
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

def update_scale_display():
    pygame.transform.scale(miniscreen_surface, (gamescreen.width, gamescreen.height), gamescreen_surface)
    pygame.display.update()    

def update_main_screen():
    # displays game
    miniscreen_surface.blit(images['misc']['background'], (0,0))
    for bagel in bagels:
        if customer_order['bagel'] == bagel:
            miniscreen_surface.blit(images['shirt'][bagel], (customer_info.x, customer_info.y))
    for face in faces:
        if customer_feature['face'] == face:
            miniscreen_surface.blit(images['face'][face], (customer_info.x, customer_info.y))
    for emotiton in emotions:
        if customer_feature['emotion'] == emotiton:
            miniscreen_surface.blit(images['emotion'][emotiton], (customer_info.x, customer_info.y))
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
    text_score = font.render(str(day.current // fps), False, (0, 50, 0))
    miniscreen_surface.blit(text_score, (text_info.x, text_info.y))
    update_scale_display()

def update_main_menu():
    miniscreen_surface.blit(images['misc']['main menu'], (0, 0))
    update_scale_display()

def update_pause_menu():
    miniscreen_surface.blit(images['misc']['pause menu'], (0, 0))
    update_scale_display()

def update_gameover_menu():
    miniscreen_surface.blit(images['misc']['closed'], (0, 0))
    text_score = font.render('Y: ' + str(score.correct) + "  N: " + str(score.incorrect), False, (0, 50, 0))
    miniscreen_surface.blit(text_score, (text_info.x, text_info.y))    
    update_scale_display()

def update_timers():
    global reaction, new_round, day, at_gameover_menu
    if reaction.run:
        reaction.current -= 1
    if reaction.current <= 0:
        new_round = True
        reaction.reset()
        reaction.run = False
    if day.run:
        day.current -= 1
    if day.current <= 0:
        day.run = False
        at_gameover_menu = True
        day.reset

# new program variables
at_main_menu = True
at_pause_menu = False
at_gameover_menu = False
new_game = True
run = True

while run == True:
    clock.tick(fps)

    while at_main_menu:
        update_main_menu()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                at_main_menu = False
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    at_main_menu = False
                    run = False
                elif event.key == pygame.K_SPACE:
                    new_game = True
                    at_pause_menu = True
                    at_main_menu = False
    
    if new_game:
        new_round = True
        score.correct, score.incorrect = 0, 0
        reaction.run = False
        reaction.reset()
        day.run = True
        day.reset()
        at_gameover_menu = False
        new_game = False

    while at_pause_menu:
        update_pause_menu()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                at_pause_menu = False
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    at_main_menu = True
                    at_pause_menu = False
                elif event.key == pygame.K_SPACE:
                    at_pause_menu = False

    while at_gameover_menu:
        update_gameover_menu()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                at_gameover_menu = False
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    at_gameover_menu = False
                    at_main_menu = True

    # runs start of round code
    if new_round:
        # gets new customer order and resets player's order
        customer_order = random_customer_order()
        customer_feature = random_customer_features()
        player_order = blank_order()

        # resets image locations
        customer_info.y = miniscreen.height - 10

        new_round = False

    if not at_main_menu and not at_pause_menu and not at_gameover_menu and run:
        for event in pygame.event.get():    
            # checks to quit program
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                # doesn't allow player to change bagel if customer is emoting
                if not reaction.run:
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
                                customer_feature['emotion'] = 'happy'
                                score.correct += 1
                            else:
                                print('WRONG')
                                score.incorrect += 1
                                customer_feature['emotion'] = 'sad'
                            reaction.run = True

                if event.key == pygame.K_ESCAPE:
                    at_pause_menu = True

        update_timers()
        animate_screen()
        update_main_screen()
        
pygame.quit()
sys.exit()