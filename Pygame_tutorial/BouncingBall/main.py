import pygame

# initialize the pygame
pygame.init()

# create the screen
X = 800
Y = 600
screen = pygame.display.set_mode((X, Y))
running = True

# title
pygame.display.set_caption("Bouncing Ball")

# Ball
ballImg = pygame.image.load("ball.png")
ballX = 10  # position x
ballY = 10  # position y
ballX_change = 2  # velocity x
ballY_change = 2  # velocity y

# Game Loop
while running:
    # set background
    screen.fill((0, 0, 0))

    # set ball
    screen.blit(ballImg, (ballX, ballY))

    # check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # update ball
    ballX += ballX_change
    ballY += ballY_change

    # collision detection
    # top
    if ballX >= X - 64:
        ballX_change = -1.5
    # bottom
    elif ballX <= 0:
        ballX_change = 1.5

    # right
    if ballY >= Y - 64:
        ballY_change = -1.5
    # left
    elif ballY <= 0:
        ballY_change = 1.5

    credit_font = pygame.font.Font("freesansbold.ttf", 12)
    credit = credit_font.render("Created By: KUMAR SHANU", True, (255, 255, 0))
    screen.blit(credit, (10, 580))
    # update frame
    pygame.display.update()
