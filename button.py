import pygame


class Button(object):
    def __init__(self, x, y, width, height, color, text=""):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.text = text
        self.active = True

    def draw(self, win):
        if self.active is False:
            return
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))
        if self.text is not "":
            font = pygame.font.SysFont('calibri', 50)
            text = font.render(self.text, 1, (0, 0, 0))
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2),
                            self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self, pos):
        if self.active is False:
            return False
        if self.x < pos[0] < self.x + self.width:
            if self.y < pos[1] < self.height + self.y:
                return True
        return False

    def toggleButton(self):
        if self.active is False:
            self.active = True
        else:
            self.active = False
