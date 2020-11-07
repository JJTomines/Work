from tkinter import*
from block import *
from blocklist import *
from allSorts import *
from random import shuffle


def makeBlocks(blocknum,drawScreen,blocklist):
    drawScreen.delete("all")
    blocklist.clear()

    templist = []
    for i in range(1,blocknum+1):
        templist.append(i)
    shuffle(templist)
    if blocknum <= 45:
        for i in range(len(templist)):
            cur_block = Block(drawScreen,[5,templist[i]],20*i+20)
            blocklist.add_block(cur_block)
    else:
        for i in range(len(templist)):
            cur_block = Block(drawScreen,[5,templist[i]],8*i+20)
            blocklist.add_block(cur_block)

def setSort(blocknum,drawScreen,blocklist,sortType):
    swapitem1 = "#9c001a"
    swapitem2 = "#005999"

    if sortType == "Bubble" or sortType == "Selection" or sortType == "Insertion":
        makeBlocks(blocknum, drawScreen, blocklist)
        drawScreen.create_rectangle(20,270,30,280,fill=swapitem1)
        drawScreen.create_text(50,275,fill=swapitem1,text="Item 1")
        drawScreen.create_rectangle(20, 290, 30, 300, fill=swapitem2)
        drawScreen.create_text(50, 295, fill=swapitem2, text="Item 2")

def startSort(drawScreen,blocklist,sortType,speed):
    if sortType == "Bubble":

        Bubble(drawScreen,blocklist,speed)

    elif sortType == "Selection":

        Selection(drawScreen,blocklist,speed)