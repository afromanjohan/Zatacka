import pygame
import sys

from color import colorTransformer as ct
from button import Button
from player import Player
from textblit import Textblit

#################################################################################################
# Board size, game update tickrate, and alterable controller list and round number              #
#################################################################################################
WINDOW_WIDTH = 1500
WINDOW_HEIGHT = 1200
tickrate = 40
timedelay = 10
clock = pygame.time.Clock()

controllerList = [(pygame.K_LEFT, pygame.K_RIGHT), (pygame.K_q, pygame.K_a), (pygame.K_z, pygame.K_x),
                  (pygame.K_1, pygame.K_2), (pygame.K_6, pygame.K_9), (pygame.K_v, pygame.K_b)]

remainingRounds = 5

#################################################################################################
# Initialize pygame window and required lists for game / gameloop                               #
#################################################################################################
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
window.fill(ct("Black"))
pygame.display.set_caption("Achtung die Kurve - Zatacka")
colors = ["White", "Red", "Cyan", "Yellow", "Pink", "Green", "Blue", "Orange"]
playerList = []
buttons = []

#################################################################################################
# Initialize the first player and add it to the playerlist                                      #
#################################################################################################
man = Player(0, controllerList[0][0],
             controllerList[0][1]
             , WINDOW_WIDTH, WINDOW_HEIGHT, colors[0])
playerList.append(man)

startButton = Button(200, 1000, 200, 70, "Red", "Start")
morePlayersButton = Button(450, 1000, 200, 70, "Red", "+1 Player")
fewerPlayersButton = Button(700, 1000, 200, 70, "Red", "-1 Player")

buttons.append(startButton)
buttons.append(morePlayersButton)
buttons.append(fewerPlayersButton)


def setUpGame():
    numberOfPlayers = 1
    settingUpGame = True
    while settingUpGame:
        clock.tick(40)
        pygame.time.delay(10)
        drawStartscreen(numberOfPlayers)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()

                if startButton.isOver(pos):
                    window.fill((0, 0, 0))
                    settingUpGame = False
                    try:
                        gameLoop()
                    except pygame.error:
                        pass
                elif morePlayersButton.isOver(pos):
                    if numberOfPlayers < 6:
                        numberOfPlayers += 1
                        playerList.append(Player(0, controllerList[numberOfPlayers - 1][0],
                                                 controllerList[numberOfPlayers - 1][1], WINDOW_WIDTH, WINDOW_HEIGHT,
                                                 colors[numberOfPlayers - 1]))
                elif fewerPlayersButton.isOver(pos):
                    if numberOfPlayers > 1:
                        numberOfPlayers -= 1
                        playerList.pop()


def gameLoop():
    runGame = True
    global remainingRounds
    remainingRounds -= 1
    if remainingRounds is 0:
        pygame.quit()
        sys.exit()
    alivePlayers = list(playerList)
    prepareRound()
    while runGame and alivePlayers:
        clock.tick(tickrate)
        pygame.time.delay(timedelay)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                runGame = False
                pygame.quit()
        try:
            keys = pygame.key.get_pressed()
        except pygame.error:
            pygame.quit()
        for index, player in enumerate(alivePlayers):
            if keys[player.left]:
                player.doMove(player.left, window)
            elif keys[player.right]:
                player.doMove(player.right, window)
            else:
                player.doMove(0, window)
            if player.alive is False:
                alivePlayers.pop(index)
                if len(alivePlayers) is 1:
                    p = alivePlayers.pop()
                    p.score += 1
                    print(p.name)

        drawWindow()
    drawScore()


def drawScore():
    window.fill(ct("Black"))
    restartButton = Button(WINDOW_WIDTH // 2 - 150, WINDOW_HEIGHT // 2 - 37, 300, 75, "Red", "New round")
    restartButton.draw(window)
    for index, player in enumerate(playerList):
        textblit = Textblit(player.name + ": " + str(player.score), 500, 100 + index * 40, player.color, "calibri", 20)
        textblit.blitText(window)
    drawWindow()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if restartButton.isOver(pos):
                    window.fill(ct("Black"))
                    gameLoop()


def makeButtonsInactive():
    for button in buttons:
        button.toggleButton()


def prepareRound():
    for player in playerList:
        player.startNewRound()


def drawWindow():
    try:
        pygame.display.update()
    except pygame.error:
        pygame.quit()


def drawStartscreen(numOfPlayers):
    window.fill(ct("Black"))
    for button in buttons:
        button.draw(window)
    participantText = Textblit("There are currently " + str(numOfPlayers) + " participant(s)",
                               WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2, ct("Cyan"))
    participantText.blitText(window)
    drawWindow()


#################################################################################################
# Start the menuscreen and prompt the user to select number of players and to start game        #
#################################################################################################
setUpGame()

pygame.quit()
