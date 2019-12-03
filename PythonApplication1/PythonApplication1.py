
import pygame
import random

pygame.init()

display_width = 800
display_height = 600

display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Burning forest')
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

fire_img = [pygame.image.load('0.png'), pygame.image.load('1.png'), pygame.image.load('2.png')]
fire_options = [69, 449, 37, 410, 40, 420]

stone_img = [pygame.image.load('stone1.png'), pygame.image.load('stone2.png')]
cloud_img = [pygame.image.load('cloud1.png'), pygame.image.load('cloud2.png')]

player_img = [pygame.image.load('player0.png'), pygame.image.load('player1.png'), pygame.image.load('player2.png'), pygame.image.load('player3.png'), pygame.image.load('player4.png')]

img_counter = 0

class Object:
    def __init__(self, x, y, width, image, speed):
        self.x = x
        self.y = y
        self.width = width

        self.speed = speed
        self.image = image
    def move(self):
        if self.x >= -self.width:
            display.blit(self.image, (self.x, self.y))
            
            self.x -= self.speed
            return True
        else:
            #self.x = display_width + 100 + random.randrange(-80, 60)
            return False

    def return_self(self, radius, y, width, image):
        self.x = radius
        self.y = y
        self.width = width
        self.image = image
        display.blit(self.image, (self.x, self.y))

usr_width = 60
usr_height = 100
usr_x = display_width // 3
usr_y = display_height - usr_height - 100

fire_width = 20
fire_height = 70
fire_x = display_width -50
fire_y = display_height - fire_height - 100

clock = pygame.time.Clock()

make_jump = False
jump_counter = 30

def run_game():
    global make_jump
    game = True

    fire_arr = []
    create_fire_arr(fire_arr)

    land = pygame.image.load('land11.png')

    stone, cloud = open_random_objects()

    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            make_jump = True

        if keys[pygame.K_ESCAPE]:
            pause()

        if make_jump:
            jump()

        display.blit(land, (0, 0))
        draw_array(fire_arr)

        move_objects(stone, cloud)


        #pygame.draw.rect(display, (247, 240, 22), (usr_x, usr_y, usr_width, usr_height))
        draw_player()

        pygame.display.update()
        clock.tick(80)

def jump():
    global usr_y, make_jump, jump_counter
    if jump_counter >= - 30:
        usr_y -= jump_counter / 2.5
        jump_counter -= 1
    else:
        jump_counter = 30
        make_jump = False

def create_fire_arr(array):
    choice = random.randrange(0, 3)
    img = fire_img[choice]
    width = fire_options[choice * 2]
    height = fire_options[choice * 2 + 1]
    array.append(Object(display_width + 20, height, width, img, 4))

    choice = random.randrange(0, 3)
    img = fire_img[choice]
    width = fire_options[choice * 2]
    height = fire_options[choice * 2 + 1]
    array.append(Object(display_width + 300, height, width, img, 4))

    choice = random.randrange(0, 3)
    img = fire_img[choice]
    width = fire_options[choice * 2]
    height = fire_options[choice * 2 + 1]
    array.append(Object(display_width + 600, height, width, img, 4))


def find_radius(array):
    maximum = max(array[0].x, array[1].x, array[2].x)

    if maximum < display_width:
        radius = display_width
        if radius - maximum < 50:
            radius += 150
    else:
        radius = maximum
    choice = random.randrange(0, 5)
    if choice == 0:
        radius += random.randrange(10, 15)
    else:
        radius += random.randrange(200, 350)
    return  radius


def draw_array(array):
    for fire in array:
        check = fire.move()
        if not check:
            radius = find_radius(array)

            choice = random.randrange(0, 3)
            img = fire_img[choice]
            width = fire_options[choice * 2]
            height = fire_options[choice * 2 + 1]

            fire.return_self(radius, height, width, img)

def open_random_objects():
    choice = random.randrange(0, 2)
    img_of_stone = stone_img[choice]

    choice = random.randrange(0, 2)
    img_of_cloud = cloud_img[choice]

    stone = Object(display_width, display_height - 80, 10, img_of_stone, 4 )
    cloud = Object(display_width, 80, 70, img_of_cloud, 2 )

    return stone, cloud

def move_objects(stone, cloud):
    check = stone.move()
    if not check:
        choice = random.randrange(0, 2)
        img_of_stone = stone_img[choice]
        stone.return_self(display_width, 500 + random.randrange(10, 80), 10, img_of_stone)

    check = cloud.move()
    if not check:
        choice = random.randrange(0, 2)
        img_of_cloud = cloud_img[choice]
        cloud.return_self(display_width, random.randrange(10, 200), 100, img_of_cloud)

def draw_player():
    global img_counter
    if img_counter == 25:
        img_counter = 0

    display.blit(player_img[img_counter // 5], (usr_x, usr_y))
    img_counter += 1

def print_text(message, x, y, font_color = (84, 1, 50), font_type = '18290.ttf', font_size = 50):
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(message, True, font_color)
    display.blit(text, (x, y))

def pause():
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        print_text('Paused. Press enter to continue.', 120, 100)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            paused = False

        pygame.display.update()
        clock.tick(15)


run_game()