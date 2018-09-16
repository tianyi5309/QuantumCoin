import time
from pyquil.quil import Program
from pyquil.gates import H
from pyquil.api import QVMConnection
from math import *
# import pygame
# from pygame import Color

# pygame.init()
# screen = pygame.display.set_mode((1000, 1000))
# done = False

quantum_simulator = QVMConnection()
coin_flip = Program(H(0)).measure(0, 0)


def getbit():
    """
    Randomly generates a bit using the coin_flip.
    :return: either 0 or 1.
    """
    return quantum_simulator.run(coin_flip, [0])[0][0]


def heads_or_tails(boolean):
    """
    Interprets true as heads, false as tails.
    :param boolean: a bool
    :return: 'Heads' or 'Tails'
    """
    return 'Heads' if boolean else 'Tails'


def get_coin_flip():
    """
    Uses quantum mechanics to flip a coin.
    :return: Nothing is returned.
    """
    # quantum stuff
    animation = ['-', '\\', '|', '/']
    print('innie minnie miny moe')
    for i in range(20):
        print('\r' + animation[i%4], end="")
        time.sleep(5/20)
    coin = getbit()
    print('\r'+heads_or_tails(coin))
    # return quantum_simulator.run(coin_flip, [0])[0][0]


def get_next_power_two(pos_int):
    """
    :param pos_int: a positive integer
    :return: smallest n s.t. 2 ^ n >= pos_int
    """
    logarithm_rounded_down = int(log(pos_int, 2))
    power = 2 ** logarithm_rounded_down
    while power > pos_int:
        logarithm_rounded_down -= 1
        power /= 2
    while 2 ** logarithm_rounded_down < pos_int:
        logarithm_rounded_down += 1
        power *= 2
    return logarithm_rounded_down


def getrandbits(nnint):
    """
    Randomly uniformly generates a nonnegative integer with nnint bits.
    :param nnint: a nonnegative integer
    :return: An x s.t. 0 <= x < 2 ** nnint
    """
    final_ans = 0
    for dummy_i in range(nnint):
        bit = getbit()
        final_ans *= 2
        final_ans += bit
    return final_ans


def randrange(pos_int):
    """
    Generates uniformly a random nonnegative integer 0 <= x < pos_int.  Equivalent to random.randrange(pos_int).
    :param pos_int: any positive integer
    :return: randomly generated integer described above
    """
    next_power_of_two = get_next_power_two(pos_int)
    ans = getrandbits(next_power_of_two)
    while ans > pos_int:
        ans = getrandbits(next_power_of_two)
    return ans


def random():
    """
    Generates uniformly a 64-bit floating point number in [0, 1).  Equivalent to random.random().  Assumes that
    on the system running this code, the floating point data type is at least 64 bits.
    :return: a random float.
    """
    # In a 64-bit floating point number, the mantissa is (essentially) 53 bits and the exponent is 7 bits.
    x = getrandbits(53)
    return x * (2 ** -53)


get_coin_flip()

# 
# # class TestSprite(pygame.sprite.Sprite):
# #     def __init__(self):
# #         super(TestSprite, self).__init__()
# #         self.images = []
# #         for i in range(53):
# #             self.images.append(pygame.image.load('coin/coin-'+str(i)+'.png'))
# #         # assuming both images are 64x64 pixels
# # 
# #         self.index = 0
# #         self.image = self.images[self.index]
# #         self.rect = pygame.Rect(5, 5, 64, 64)
# # 
# #     def update(self):
# #         '''This method iterates through the elements inside self.images and 
# #         displays the next one each tick. For a slower animation, you may want to 
# #         consider using a timer of some sort so it updates slower.'''
# #         print(self.index)
# #         pygame.time.wait(100)
# #         # for i in range(1000000):
# #             # x = i
# #         self.index += 1
# #         if self.index >= len(self.images):
# #             self.index = 0
# #         self.image = self.images[self.index]
# # 
# #     def draw(self):
# #         screen.blit(self.image, self.rect)
# 
# # my_sprite = TestSprite()
# # my_group = pygame.sprite.Group(my_sprite)
# 
# coin_flip = Program(H(0)).measure(0, 0)
# def get_coin_flip():
#     # quantum stuff
#     # print(quantum_simulator.wavefunction(coin_flip).get_outcome_probs())
#     # Load gif
#     for i in range(150):
#         pygame.draw.circle(screen, (255, 255, 255, 0) if i%2 else (0, 0, 0, 0), (100, 100), 100)
#         time.sleep(1/30)
#     # for i in range(159):
#     #     # my_group.update()
#     #     my_sprite.update()
#     #     my_sprite.draw()
#     #     # my_group.draw(screen)
#     #     # pygame.display.update()
#     #     pygame.display.flip()
#     #     # time.sleep(1/30)
# 
#     coin = quantum_simulator.run(coin_flip, [0])[0][0]
#     print(coin)
#     # return quantum_simulator.run(coin_flip, [0])[0][0]
# 
# -\|/-\|/-\|/-\|/-\|/-\|/-\
# # def button_action():
#     # print("hi :D")
# 
# def button(msg,x,y,w,h,ic,ac,action=None):
#     mouse = pygame.mouse.get_pos()
#     click = pygame.mouse.get_pressed()
#     # print(click)
#     if x+w > mouse[0] > x and y+h > mouse[1] > y:
#         pygame.draw.rect(screen, ac,(x,y,w,h))
# 
#         if click[0] == 1 and action != None:
#             action()
#     else:
#         pygame.draw.rect(screen, ic,(x,y,w,h))
# 
#     # smallText = pygame.font.SysFont("comicsansms",20)
#     # textSurf, textRect = text_objects(msg, smallText)
#     # textRect.center = ( (x+(w/2)), (y+(h/2)))
#     # screen.blit(textSurf, textRect)
# 
# while not done:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             done = True
#     # pygame.draw.rect(screen, Color(255, 255, 255, 0), (0, 0, 100, 100))
#     button("hi", 0, 0, 100, 100, Color(0, 255, 255, 0), Color(255, 0, 0, 0), get_coin_flip)
#     pygame.display.flip()
