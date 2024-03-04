# Simple pygame program
import math

# Import and initialize the pygame library
import pygame
pygame.init()

screenHeight = 500
screenWidth = 500

whiteColor = (255, 255, 255)
blackColor = (0, 0, 0)
blueColor = (0, 0, 255)

# Set up the drawing window
screen = pygame.display.set_mode([screenWidth, screenHeight])

rectHeight = 100
rectWidth = 100

x = rectWidth / 2
y = screenHeight - rectHeight

speed = 0.025
minSpeed = speed
maxSpeed = 10

xSpeed = speed * 1.51
ySpeed = -speed

# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill(blackColor)

    # Draw a solid blue circle in the center
    pygame.draw.rect(screen, blueColor, (x, y, rectHeight, rectHeight))

    # Flip the display
    pygame.display.flip()

    if x > (screenWidth - rectWidth):
        xSpeed = -xSpeed
    elif x < 0:
        xSpeed = -xSpeed

    if y > (screenHeight - rectHeight):
        ySpeed = -ySpeed
    elif y < 0:
        ySpeed = -ySpeed

    x += xSpeed
    y += ySpeed

    # if xSpeed > maxSpeed:
    #     xSpeed *= 0.9999
    # elif xSpeed < minSpeed:
    #     xSpeed *= 1.0001
    #
    # if ySpeed > maxSpeed:
    #     ySpeed *= 0.9999
    # elif ySpeed < minSpeed:
    #     ySpeed *= 1.0001

# Done! Time to quit.
pygame.quit()