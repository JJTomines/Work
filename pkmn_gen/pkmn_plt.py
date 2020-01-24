from random import *
from tkinter import *

class palette:
    def __init__(self,mode):
        self.mode = mode.upper()
        grey = randint(100,240)
        self.colours = [(40,40,40),
                        (grey,grey,grey),
                        (randint(100,255),randint(100,255),randint(100,255))
                        ]
        if self.mode == "COMPLEMENTARY" or self.mode == "ANALOGOUS":
            self.colours.append((randint(100,255),randint(100,255),randint(100,255)))
        self.make_colours()

    def make_colours(self):
        if self.mode == "COMPLEMENTARY":
            #options = ["gr","yp","ob"]
            opt = randint(0,2)
            if opt == 0:
                self.green()
                self.red()
            elif opt == 1:
                self.yellow()
                self.purple()
            else:
                self.orange()
                self.blue()

        elif self.mode == "ANALOGOUS":
            #options = ["ro","oy","yg","gb","bp"]
            opt = randint(0,4)
            if opt == 0:
                self.red()
                self.orange()
            elif opt == 1:
                self.orange()
                self.yellow()
            elif opt == 2:
                self.yellow()
                self.green()
            elif opt == 3:
                self.green()
                self.blue()
            else:
                self.blue()
                self.purple()

        elif self.mode == "TRIADIC":
            #options = ["rby","ogb","pgb","ypb"]
            opt = randint(0,3)
            if opt == 0:
                self.red()
                self.blue()
                self.yellow()
            elif opt == 1:
                self.orange()
                self.green()
                self.blue()
            elif opt == 2:
                self.purple()
                self.green()
                self.blue()
            else:
                self.yellow()
                self.purple()
                self.blue()

        else: # split complementary
            #options = ["ybp","gpr","boy","ogb","obp","rgb","bro"]
            opt = randint(0,6)
            if opt == 0:
                self.yellow()
                self.blue()
                self.purple()
            elif opt == 1:
                self.green()
                self.purple()
                self.red()
            elif opt == 2:
                self.blue()
                self.orange()
                self.yellow()
            elif opt == 3:
                self.orange()
                self.green()
                self.blue()
            elif opt == 4:
                self.orange()
                self.blue()
                self.purple()
            elif opt == 5:
                self.red()
                self.green()
                self.blue()
            else:
                self.blue()
                self.red()
                self.orange()


        #All colour options

    def green(self):
        r = randint(0,100)
        g = randint(100,255)
        b = randint(0,100)
        while r==100==b and g < 110:
            g = randint(100, 255)

        self.colours.append((r,g,b))
    def red(self):
        r = randint(100,255)
        g = randint(0,70)
        b = randint(0,70)
        self.colours.append((r, g, b))
    def blue(self):
        r = randint(0,40)
        g = randint(0,100)
        b = randint(100,255)
        self.colours.append((r, g, b))
    def orange(self):
        r = randint(100,255)
        g = randint(100,175)
        b = randint(0,50)
        while abs(r-g) < 15 or abs(r - g) > 161 or r < g:
            r = randint(100, 255)
            g = randint(100, 175)
        self.colours.append((r, g, b))
    def purple(self):
        r = randint(110,255)
        g = randint(60,180)
        b = randint(220,255)
        self.colours.append((r, g, b))
    def yellow(self):
        r = randint(150,255)
        g = randint(100,255)
        b = randint(0,50)

        while abs(r-g) < 5 or abs(r-g) > 15:
            r = randint(100, 255)
            g = randint(100, 175)

        self.colours.append((r, g, b))
    def get_plt(self):
        return self.colours

    def rgb_hex(self,cols):
        new_list = []
        for col in cols:
            new_list.append('#%02x%02x%02x'% col)
        return new_list
