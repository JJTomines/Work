import time


def Bubble(drawScreen,blocklist,speed):
    worklist = blocklist.get_blocks()

    if len(worklist) > 45:
        gap = 16
    else:
        gap = 40

    for block in range(len(worklist)):
        for i in range(1,len(worklist)):

            worklist[i-1].set_colour(1)
            worklist[i].set_colour(0)

            if worklist[i-1].get_height() > worklist[i].get_height():
                for j in range(gap):
                    time.sleep(0.001 / speed.get())
                    y = 0
                    drawScreen.move(worklist[i - 1].get_block(), 0.5, y)
                    drawScreen.move(worklist[i].get_block(), -0.5, y)
                    drawScreen.update()
                worklist[i - 1], worklist[i] = worklist[i], worklist[i - 1]

            worklist[i - 1].reset_colour()
            worklist[i].reset_colour()


def Selection(drawScreen,blocklist,speed):
    user_list = blocklist.get_blocks()
    i = 0
    while i != len(user_list):
        smallest = find_min(user_list, i)
        distance = abs(i - smallest) * 20
        if i > smallest:
            for x in range(distance):
                y = 0
                time.sleep(.05 / speed.get())
                drawScreen.move(user_list[i].get_block(), -1, y)
                drawScreen.move(user_list[smallest].get_block(), 1, y)
                drawScreen.update()

        elif i < smallest:
            for x in range(distance):
                y = 0
                time.sleep(.05 / speed.get())
                drawScreen.move(user_list[i].get_block(), 1, y)
                drawScreen.move(user_list[smallest].get_block(), -1, y)
                drawScreen.update()

        user_list[i], user_list[smallest] = user_list[smallest], user_list[i]
        i = i + 1


def find_min(aList, start_position):
    # return the index of the smallest value in aList[position:]
    smallest = start_position
    for i in range(start_position + 1, len(aList)):
        if aList[i].get_height() < aList[smallest].get_height():
            smallest = i
    return smallest

