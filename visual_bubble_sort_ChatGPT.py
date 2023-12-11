# importing pygame
import pygame
import random
 
pygame.init()
 
# setting window size
win = pygame.display.set_mode((800, 400))
 
# setting title to the window
pygame.display.set_caption("Bubble sort")
 
# initial position
x = 40
y = 40
 
# width of each bar
width = 20
 
# height of each bar (data to be sorted)
height = [200, 50, 130, 90, 250, 61, 110,
            88, 33, 80, 70, 159, 180, 20]

height = []
for num in range(25):
    height.append(random.randint(1,255))

 
run = True
 
# method to show the list of height
def show(height):
 
    # loop to iterate each item of list
    for i in range(len(height)):
 
        # drawing each bar with respective gap
        pygame.draw.rect(win, (255 , height[i], height[i]), (x + 30 * i, y, width, height[i]))
 
        # pygame.draw.rect(win, (255, 0, 0), (x + 30 * i, y, width, height[i]))
 
# infinite loop
while run:
 
    # execute flag to start sorting
    execute = False
 
    # time delay
    ##pygame.time.delay(10)
 
    # getting keys pressed
    keys = pygame.key.get_pressed()
 
    # iterating events
    for event in pygame.event.get():
 
        # if event is to quit
        if event.type == pygame.QUIT:
 
            # making run = false so break the while loop
            run = False
 
    # if space bar is pressed
    if keys[pygame.K_SPACE]:
        # make execute flag to true
        execute = True
 
    # checking if execute flag is false
    if execute == False:
 
        # fill the window with black color
        win.fill((0, 0, 0))
 
        # call the height method to show the list items
        show(height)
 
        # update the window
        pygame.display.update()
 
    # if execute flag is true
    else:
 
        # start sorting using bubble sort technique
        for i in range(len(height) - 1):
 
            # after this iteration max element will come at last
            for j in range(len(height) - i - 1):
 
                # starting is greater than next element
                if height[j] > height[j + 1]:
 
                    # save it in temporary variable
                    # and swap them using temporary variable
                    # t = height[j]
                    # height[j] = height[j + 1]
                    # height[j + 1] = t
                    
                    height[j], height[j + 1] = height[j + 1], height[j]
                    # pygame.time.delay(50)
 
                # fill the window with black color
                win.fill((0, 0, 0))
 
                # call show method to display the list items
                show(height)
 
                # create a time delay
                pygame.time.delay(50)
 
                # update the display
                pygame.display.update()
 
# exiting the main window
pygame.quit()


# Bubble sort visualizer using PyGame

# https://www.geeksforgeeks.org/bubble-sort-visualizer-using-pygame/
# https://stackoverflow.com/questions/31374721/what-is-the-logic-for-x-y-y-x-to-swap-the-values
# https://www.youtube.com/watch?v=jkgcfCiewnU


""" Tuple Comment

How to Pack and Unpack a Tuple

Tuples are immutable and hence
cannot have any changes in them
once they are created in Python.
This is because they support the
same sequence operations as strings.
"""

# import random


# height = []
# for num in range(25):
#     height.append(random.randint(1,300))


# height[j], height[j + 1] = height[j + 1], height[j]
# pygame.time.delay(1000)


# create a time delay
# pygame.time.delay(500)