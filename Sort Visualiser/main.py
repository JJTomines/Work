# Sort Visualiser
#Purpose is to visually show how sorting algorithms operate using blocks.

from tkinter import *
from blocklist import *
from block import *
from buttonfunctions import *
#Intialize main window
window = Tk()
window.title("Sort Visualiser")
window.geometry("960x540")
window.resizable(width=False,height=False)

#Initialize sort canvas
canvas = Canvas(window,height=320,width=960,bd=0,bg='#e0e0e0')
canvas.grid(row=0,column=0,columnspan=5,sticky=N+E+S+W)

blockList = BlockList(canvas)

#Sort Options
sortOptions = LabelFrame(window,text="Options")
sortOptions.grid(row=1,column=0,columnspan=5,sticky=N+E+S+W)

#Sort Types
Label(sortOptions,text="Sort Type").grid(row=0,column=0)
curType = StringVar()
curType.set("Bubble")
sortType = OptionMenu(sortOptions,curType,"Bubble","Selection","Insertion")
sortType.grid(row=0,column=1)

#Size of sorting list
Label(sortOptions,text="Sort Size").grid(row=0,column=2)
sortSize = IntVar()
sortSize = Spinbox(sortOptions,from_=20, to=100)
sortSize.grid(row=0,column=3)

displaySource = LabelFrame(sortOptions,text="Source Code")
displaySource.grid(rowspan=2,columnspan=4,row=2)
scroll = Scrollbar(displaySource)
scroll.grid(row=0,column=1,sticky=N+S)
sourceCode = Text(displaySource,bd=0,yscrollcommand=scroll.set,height=8,width=60)
sourceCode.insert(END,"Source Code"*100)
scroll.config(command=sourceCode.yview)
sourceCode.grid(row=0,column=0)

Label(sortOptions,text="Speed").grid(row=1,column=0)
sortSpeed = Scale(sortOptions,from_=0.25,to=2,resolution=0.25,orient=HORIZONTAL)
sortSpeed.grid(row=1,column=1,columnspan=2,sticky=W)


setSortButton = Button(sortOptions,text="Set Sort",command=lambda:setSort(int(sortSize.get()),canvas,blockList,curType.get())).grid(row=1,column=4)
startButton = Button(sortOptions,text="Start Sort",command=lambda:startSort(canvas,blockList,curType.get(),sortSpeed)).grid(row=2,column=4)
mainloop()