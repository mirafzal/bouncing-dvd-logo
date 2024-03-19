# Import and initialize the pygame library
import random

import pygame


def getNewFruit():
    return pygame.Rect(random.randint(0, int(screenWidth / squareSize) - 1) * squareSize,
                       random.randint(0, int(screenHeight / squareSize) - 1) * squareSize, squareSize, squareSize)


def isRectEqual(rect1, rect2):
    return rect1.x == rect2.x and rect1.y == rect2.y


def lengthenSnake():
    return snake.append(snake[-1].copy())


pygame.init()

squareSize = 10

squareSize = int(squareSize)

widthSquaresCount = 40
heightSquaresCount = 40

screenHeight = heightSquaresCount * squareSize
screenWidth = widthSquaresCount * squareSize

whiteColor = (255, 255, 255)
blackColor = (0, 0, 0)
blueColor = (0, 0, 255)
redColor = (255, 0, 0)
yellowColor = (255, 255, 0)

# Set up the drawing window
screen = pygame.display.set_mode([screenWidth, screenHeight])

x = 0
y = 0

fruit = getNewFruit()

snakeSize = 4

snakeHead = pygame.Rect(x + squareSize * (snakeSize - 1), y, squareSize, squareSize)

snake = []

for i in range(snakeSize - 2, -1, -1):
    snake.append(pygame.Rect(x + squareSize * i, y, squareSize, squareSize))

direction = 'right'

xSpeed = squareSize
ySpeed = 0

# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN and direction != 'up':
                xSpeed = 0
                ySpeed = squareSize
                direction = 'down'
            elif event.key == pygame.K_UP and direction != 'down':
                xSpeed = 0
                ySpeed = -squareSize
                direction = 'up'
            elif event.key == pygame.K_LEFT and direction != 'right':
                xSpeed = -squareSize
                ySpeed = 0
                direction = 'left'
            elif event.key == pygame.K_RIGHT and direction != 'left':
                xSpeed = squareSize
                ySpeed = 0
                direction = 'right'

    # Fill the background with white
    screen.fill(blackColor)

    # Draw a solid blue circle in the center
    # pygame.draw.rect(screen, whiteColor, (x, y, rectWidth, rectHeight))

    if isRectEqual(fruit, snakeHead):
        fruit = getNewFruit()
        lengthenSnake()

    nextX = snakeHead.x
    nextY = snakeHead.y

    for i, rect in enumerate(snake):
        pygame.draw.rect(screen, whiteColor, rect)

        tempX = rect.x
        tempY = rect.y

        rect.x = nextX
        rect.y = nextY

        nextX = tempX
        nextY = tempY

    pygame.draw.rect(screen, yellowColor, fruit)

    pygame.draw.rect(screen, whiteColor, snakeHead)

    snakeHead.x += xSpeed
    snakeHead.y += ySpeed

    if snakeHead.x >= screenWidth:
        snakeHead.x = 0

    if snakeHead.x < 0:
        snakeHead.x = screenWidth - squareSize

    if snakeHead.y >= screenHeight:
        snakeHead.y = 0

    if snakeHead.y < 0:
        snakeHead.y = screenHeight - squareSize

    # Flip the display
    pygame.display.flip()

    pygame.time.wait(40)

# Done! Time to quit.
pygame.quit()
