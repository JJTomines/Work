from tkinter import *
class BlockList(object):
    def __init__(self,draw_screen):
        self.blocks = []
        self.draw_screen = draw_screen

    def add_block(self,block):
        self.blocks.append(block)

    def clear(self):
        self.blocks = []

    def get_blocks(self):
        return self.blocks
