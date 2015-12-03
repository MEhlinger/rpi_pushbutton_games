#ShapeChaser by Francis King


import pygame, random
import Player, Collectable, Enemy
 


def main():

    pygame.init()

    font = pygame.font.SysFont("Monospace", 15)

    pygame.key.set_repeat(1,5)

    clock = pygame.time.Clock()

    display_width = 320 # default width (pixels)
    display_height = 240 # default height (pixels)
    gameScreen = pygame.display.set_mode((display_width, display_height))
    pygame.display.set_caption("ShapeChaser")

    # Colors
    white = (255, 255, 255)
    black = (0, 0, 0)
 

    #Keep the game running loop
    RUNNING = True


    #Variables
    maxSize = 0
    speed = 8
    collectables = []
    enemies = []
    enemySpawnCounter = 500
    collectableSpawnCounter = 400

    #method for outputting text to the screen.
    def showText(text):
        messageToDisplay = font.render(text, True, black)
        gameScreen.blit(messageToDisplay, [15, 15])


    #explain the game to the player.
    def intro():
        counter = 0
        while counter < 140:
            clock.tick(20)
            gameScreen.fill(white)
            if(counter < 20):
                showText("The goal of this game.")
            elif(counter < 40):
                showText("Is to grow your square.")
            elif(counter < 60): 
                showText("Grow by eating green squares.")
            elif(counter < 80):
                showText("But red squares make you shrink.")
            elif(counter < 100):
                showText("Too many and you'll disappear.")
            elif(counter < 120):
                showText("Ready...set...")
            elif(counter < 140):
                showText("GO!")
            counter+=1
            pygame.display.update()


    #losing screen
    def lose():
        counter = 0
        while counter < 100:
            clock.tick(10)
            gameScreen.fill(white)
            if counter < 20:
                showText("Game over")
            elif counter < 40:
                showText("Play again, or press q to quit.")
            elif counter < 60:
                showText("Ready...set...")
            elif counter < 80:
                showText("GO!")
            elif counter < 99:
                player.sideLength = 15
                del collectables[:]
                del enemies[:]
                maxSize = 0
            counter += 1
            pygame.display.update()
    #Create player
    player = Player.Player(160, 120, gameScreen, 15)
    
    #introducing the player to the game.     
    intro()
    
    #Game loop
    while RUNNING:
        
        #Set up conditions of the playing field.
        clock.tick(60)
        gameScreen.fill(white)
        
        
        
        #event handling.
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.moveLeft(speed)
                if event.key == pygame.K_RIGHT:
                    player.moveRight(speed)
                if event.key == pygame.K_UP:
                    player.moveUp(speed)
                if event.key == pygame.K_DOWN:
                    player.moveDown(speed)
                elif event.key == pygame.K_q:
                    pygame.key.set_repeat()
                    return            
            
        #Adding Enemies and Collectables to lists
        if enemySpawnCounter == 0:
            enemies.append(Enemy.Enemy(gameScreen))
            enemySpawnCounter = random.randint(200, 500)
        if collectableSpawnCounter == 0:
            collectables.append(Collectable.Collectable(gameScreen))
            collectableSpawnCounter = random.randint(200, 400)
        
        
        
        #putting enemies and Collectables on field
        for i in enemies:
            if i.isHit == False:
                i.redraw()
                i.checkIfPlayerTouched(player)
            else:
                enemies.remove(i)
            
        for i in collectables:
            if i.isHit == False:
                i.redraw()
                i.checkIfPlayerTouched(player)
            else:
                collectables.remove(i)
                
                
        enemySpawnCounter -= 1
        collectableSpawnCounter -= 1
        if player.sideLength > maxSize:
            maxSize = player.sideLength
        showText("Max Size: " + str(maxSize))
        player.redraw()
        if player.sideLength < 1:
            lose()
        pygame.display.update()


if __name__ == "__main__":
    main()