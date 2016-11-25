"""
 Sample code for SI 507 Waiver Assignment
 Mark W. Newman
 University of Michigan School of Information
 Based on "Pygame base template for opening a window" 
     Sample Python/Pygame Programs
     Simpson College Computer Science
     http://programarcadegames.com/
     http://simpson.edu/computer-science/
 
"""
import wikipedia
import pygame
import random
import test
import json
import nltk
import sys
import getopt
# sys.argv

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

Harrypotterlist = []
Pages_list = ""
another_list = []
another_list1 = []

Harrypotterlist =wikipedia.search(sys.argv, 5)
for page in Harrypotterlist:
  Pages_list = Pages_list + (json.dumps((wikipedia.page(page)).content))

finalfi = Pages_list.split() 
parts_of_speech = nltk.pos_tag(finalfi)
finalf = [word[0] for word in parts_of_speech if word[1] == "NN"]
dictionary = {}
for word in finalf:
    if word not in dictionary:
        dictionary[word] = 0
    dictionary[word] += 1

sample_pos_dict = {}
another_list = (sorted(dictionary, reverse = True, key = lambda x: dictionary[x])[:6])
another_list1 = list(zip( another_list, (sorted(dictionary.values(), reverse = True, key = lambda x: x)[:6])))
sample_pos_dict['NN'] = another_list1


# You must construct a dictionary of this form from your wikipedia search
# See test.py for more details on the format requirements for the dict
# sample_pos_dict = {"JJ": [("happy", 5), ("sad", 4)]}
practice_dictionary = []
# You must leave this line in your submission, and you must pass the test!
if test.test(sample_pos_dict):
    print ("Yay, you passed this part of the test!")
else:
    print ("Oh noes! You didn't pass. Please try again")
for words in sample_pos_dict:
  practice_dictionary = practice_dictionary + sample_pos_dict[words]
sorted_dictionary = sorted(practice_dictionary, reverse = True, key = lambda x: x[1])
word_list = [words[0] for words in sorted_dictionary]
print (word_list)
# this is the dummy word list for testing
# you will need to replace this with words extracted from your wikipedia search
# see README for more details
# word_list = ["apple", "banana", "skank", "grape", "pineapple", "kiwi"]

# the structure that manages the balls shown on the screen
class BallManager:

    INIT_SPEED = 1
    current_index = 0

    def __init__(self):
        self.max_balls = 3
        self.active_balls = []
        for w in word_list: 
            self.active_balls.append(WordBall(w, self.INIT_SPEED))


    def create_ball(self, word):
        self.active_balls += WordBall(word, self.INIT_SPEED)
    
    def num_balls(self):
        return len(self.active_balls)

    def __str__(self):
        s = ''
        for b in self.active_balls:
            s += b.word + ", "
        return s

# the class for each ball showing on the screen
# you can play around with size, color, font, etc. 
class WordBall:

    def __init__(self, word, speed):
        self.word = word
        self.x_pos = random.randint(0, pygame.display.Info().current_w)
        self.y_pos = 0
        self.height = 100
        self.width = 100
        self.speed = speed

    def move_ball(self):
        self.y_pos += self.speed
        if (self.y_pos > pygame.display.Info().current_h - self.height):
            self.y_pos = 0

# initialize game
pygame.init()

size = (1000, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Type to Win")
clock = pygame.time.Clock()
 
# Loop until the user clicks the close button.
done = False

ball_manager = BallManager()

ball_font = pygame.font.Font(None, 36)
keys_font = pygame.font.Font(None, 60)

game_over = False
keys_typed = ''

# -------- Main Display Loop -----------
while not done:

    # handle input events
    key = ''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            key = event.unicode
            keys_typed += key


    # manipulate game objects
    for b in ball_manager.active_balls:
        b.move_ball()


    # blank the screen
    screen.fill(WHITE)

    # render game objects
    for ball in ball_manager.active_balls:
      if ball.word[0] in keys_typed:
        pass

      else:
        pygame.draw.ellipse(screen, RED, [ball.x_pos, ball.y_pos, ball.width, ball.height]) 
        text = ball_font.render(ball.word, 1, BLACK)
        textpos = text.get_rect()
        textpos.centerx = ball.x_pos + ball.width / 2
        textpos.centery = ball.y_pos + ball.height / 2
        screen.blit(text, textpos)

 
    text = keys_font.render('keys typed: ' + keys_typed, 1, GREEN)
    textpos = text.get_rect()
    textpos.centerx = pygame.display.Info().current_w / 2
    textpos.centery = pygame.display.Info().current_h - 30
    screen.blit(text, textpos)
    
    for ball in ball_manager.active_balls:
      if ball.word[0] in keys_typed:
        pygame
        


    # update the screen with what we've drawn.
    pygame.display.flip()
 
    # limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()   