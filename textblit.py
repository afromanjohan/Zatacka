import pygame


class Textblit(object):
    def __init__(self, text, x, y, color, font="calibri", size=50):
        self.text = text
        self.x = x
        self.y = y
        self.color = color
        self.font = font
        self.size = size

    def blitText(self, win):
        font = pygame.font.SysFont(self.font, self.size)
        text = font.render(self.text, 1, self.color)
        x = self.x - text.get_width() // 2
        y = self.y - text.get_height() // 2
        win.blit(text, ((self.x - text.get_width() // 2), self.y - text.get_height() // 2))

    def changeText(self, text):
        self.text = text
