# Main class
# Coded in Python 2.7.10 with PyGame
# by Brett Burley-Inners
# Update :: 11/19/2015

import pygame, time, random, sys
import player, skyChunk

def main():

    # Initial setup
    pygame.init()

    font = pygame.font.SysFont("monospace", 15)

    pygame.key.set_repeat(1, 5)

    clock = pygame.time.Clock() # clock object for fps/ticks

    display_width = 320 # default width (pixels)
    display_height = 240 # default height (pixels)
    gameScreen = pygame.display.set_mode((display_width, display_height))
    pygame.display.set_caption("The Sky is Falling")

    # Colors
    white = (255, 255, 255)
    darkGray = (50, 50, 50)
    darkerGray = (25, 25, 25)
    lightGray = (150, 150, 150)
    rLightGray = (200, 200, 200)
    rrLightGray = (220, 220, 220)
    black = (0, 0, 0)
    darkRed = (150, 0, 0)
    lightBlue = (55, 210, 225)


    # Keep the game loop running
    RUNNING = True
    notPlaying = True # for the menu loop
    skyIsFalling = True # for the loop to make stuff fall

    # Initialize a few variables

    tickCounter = 0 # count the number of ticks
    score = 0
    xChange = 0 # change in x-coordinate to move player along x-axis
    xPosition = display_width / 2 # player start location
    size = 20 # size of player
    fallingSkies = [] # list of falling sky objects on the screen

    # The Player!
    thePlayer = player.Player(gameScreen, 15, xPosition, display_height - 35, lightGray, display_width)

    # to display Play, Quit, and Score messages
    def message(text, color, x, y):
        messageToDisplay = font.render(text, True, color)
        gameScreen.blit(messageToDisplay, [x, y])

    # Game loop
    while RUNNING:

        clock.tick(30) # number of times the screen refreshes each second

        while notPlaying:
            gameScreen.fill(darkerGray)
            message("'RETURN' to Play.", rLightGray, 5, 5)
            message("'Q' to Quit.", rLightGray, 5, 20)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        pygame.key.set_repeat()
                        return
                    if event.key == pygame.K_RETURN:
                        notPlaying = False
                        skyIsFalling = True

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and not isOverLeftBound:
                    xChange -= 10
                if event.key == pygame.K_RIGHT and not isOverRightBound:
                    xChange += 10

        gameScreen.fill(darkerGray)

        # Score display
        message(("Score: " + str(score)), rLightGray, 10, display_height - 18)

        # Movement logic:
        xPosition += xChange # add the change in direction to current position
        thePlayer.redrawPlayer(xPosition) # redraw Player at new position
        isOverLeftBound = thePlayer.isOverLeftBound() # check left bound
        isOverRightBound = thePlayer.isOverRightBound() # check right bound
        xChange = 0 # set change back to 0 (stops accelerating effect)

        tickCounter += 1

        # Sky fall loop (appends FallingSky object every 10 ticks)
        if skyIsFalling and tickCounter > 10:

            # Append FallingSky objects to the list
            fallingSkies.append(skyChunk.SkyChunk(gameScreen, random.randrange(5, 15), random.randrange(1, display_width), -5, lightBlue, random.randrange(1, 2), score, display_height, fallingSkies))

            tickCounter = 0

        # Using the list of FallingSky objects
        for i in fallingSkies:
            i.fall() # makes them move
            score += i.returnScore()

            if len(fallingSkies) > 1000:
                del fallingSkies[0] # remove first item if list is too large
            if i.collideWithPlayer(thePlayer.getPlayerX(), thePlayer.getPlayerY(), thePlayer.getPlayerSize()):
                skyIsFalling = False
                del fallingSkies[:] # clear the entire list
                notPlaying = True
                score = 0 # reset the score

        # *screen tick*
        pygame.display.update()

# That's all, folks!

if __name__ == "__main__":
    main()
