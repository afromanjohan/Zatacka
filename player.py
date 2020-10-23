import random
import pygame
from numpy import sin, cos, deg2rad
from color import colorTransformer as ct

stepsPerMove = 3
holeLikelihood = 0.95

def decision():
    return random.random() < holeLikelihood


class Player(object):
    def __init__(self, score, left, right, width, height, name):
        self.x = random.randint(100, 1400)
        self.y = random.randint(100, 1100)
        self.color = ct(name)
        self.score = score
        self.alive = True
        self.left = left
        self.right = right
        self.path = []
        self.direction = random.randint(0, 360)
        self.path.append([self.x - 1, self.y - 1, False])
        self.originalDirection = self.direction
        self.xBound = width
        self.yBound = height
        self.name = name

    def startNewRound(self):
        self.x = random.randint(100, 1400)
        self.y = random.randint(100, 1100)
        self.path = []
        self.alive = True
        self.direction = random.randint(0, 360)

    def moveIsOutOfBounds(self, x, y):
        if not 0 < x < self.xBound:
            return True
        if not 0 < y < self.yBound:
            return True
        return False

    def playerDies(self):
        self.alive = False

    def draw(self, win):
        for position in range(len(self.path) - 1):
            if self.path[position][2] is True:
                pygame.draw.line(win, self.color, (self.path[position][0], self.path[position][1]),
                             (self.path[position + 1][0], self.path[position + 1][1]), 3)

    def doMove(self, moveType, win):
        if self.alive is False:
            print(self.name + " died!!")
            return
        degrees = self.originalDirection - self.direction
        if moveType is self.right:
            degrees -= 3
            calculatedX = stepsPerMove * cos(deg2rad(degrees))
            calculatedY = stepsPerMove * sin(deg2rad(degrees))
            self.direction -= 3
        elif moveType is self.left:
            degrees += 3
            calculatedX = stepsPerMove * cos(deg2rad(degrees))
            calculatedY = stepsPerMove * sin(deg2rad(degrees))
            self.direction += 3
        else:
            calculatedX = stepsPerMove * cos(deg2rad(degrees))
            calculatedY = stepsPerMove * sin(deg2rad(degrees))
        calculatedX = (self.x + calculatedX)
        calculatedY = (self.y + calculatedY)

        visible = decision()
        if visible is False:
            size = random.randint(8, 12)
            if len(self.path) > 6:
                for i in range(0, size):
                    try:
                        self.path[-i][2] = False
                    except IndexError:
                        pass
        self.path.append([calculatedX, calculatedY, visible])
        self.x = calculatedX
        self.y = calculatedY
        if self.moveIsOutOfBounds(self.x, self.y):
            self.alive = False
        #pixelArray = pygame.PixelArray(win)[self.x][self.y]
        #if pixelArray is not (0, 0, 0):
        #    self.alive = False
        self.draw(win)
