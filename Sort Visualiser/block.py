from tkinter import *

class Block(object):
    def __init__(self,drawScreen,dimensions,posX):
        self.drawScreen = drawScreen
        self.width = dimensions[0]
        self.height = dimensions[1]
        self.posX = posX
        self.posY = 250
        self.colour = "#888e94"
        self.rect = self.drawScreen.create_rectangle(self.posX, self.posY-self.height*2, self.posX+self.width, self.posY, fill = self.colour)
        self.swapitem1 = "#9c001a"
        self.swapitem2 = "#005999"

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_block(self):
        return self.rect

    def set_colour(self,num):
        if num:
            self.colour = self.swapitem1
        else:
            self.colour = self.swapitem2
        self.drawScreen.itemconfig(self.rect, fill=self.colour)
    def reset_colour(self):
        self.colour = "#888e94"
        self.drawScreen.itemconfig(self.rect, fill=self.colour)