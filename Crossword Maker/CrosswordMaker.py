#prints board
def printboard(board):
    print("0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9")
    print("_"*40)
    for i in range(20):
        line = ""
        for j in range(20):
            #create line off crossword
            line += " "+board[i][j]
        print(line+"| "+str(i))

# place first word @ row[9]
def addFirstWord(board,word):
    #if word longer than row
    if len(word) > 20:
        return False
    #find where to start placing word
    place = 10 - (len(word)//2)
    #place word into matrix
    for i in range(len(word)):
        board[9][place] = word[i]
        place += 1
    return True

# check if word can be placed vertically
def checkvertical(board,word,row,col):
    #check if word longer than row
    if len(word) + row > 20:
        return False
    illegal = False
    valid = False
    intersect = -1
    for i in range(len(word)):
        #find intersection
        if board[row+i][col] == word[i] and intersect == -1:
            intersect = row+i
            valid = True
        #check very beginning of word
        if i == 0 and row - 1 > 0:
            if board[row - 1][col] != " ":
                illegal = True
        #check very end of word
        if i == len(word)-1 and row + i + 1 < 19:
            if board[row + i + 1][col] != " ":
                illegal = True
        # check that space below is occupied
        if intersect != row + i and board[row + i][col] != " ":
            valid = False
        # left,right illegal
        if col != 0 and col != 19:
            if (board[row + i][col - 1] != " " or board[row + i][col + 1] != " ") and intersect != row+i:
                illegal = True
        #if on far left
        elif col == 0:
            if board[row+i][col + 1] != " " and intersect != row+i:
                illegal = True
        #if on far right
        else:
            if board[row+i][col-1] != " " and intersect != row+i:
                illegal = True

    return valid and not illegal

# Add word vertically
def addvertical(board,word):
    for row in range(20):
        for col in range(20):
            # check if can be placed
            if checkvertical(board,word,row,col):
                # place word in matrix
                for i in range(len(word)):
                    board[row+i][col] = word[i]
                return True

# check if word can be placed horizontally
def checkhorizontal(board,word,row,col):
    if len(word) + col > 20:
        return False
    illegal = False
    valid = False
    intersect = -1
    for i in range(len(word)):
        #find intersection
        if board[row][col+i] == word[i]:
            intersect = col + i
            valid = True
        #check very beginning
        if i == 0 and col - 1 > 0:
            if board[row][col - 1] != " ":
                illegal = True

        #check very end of word
        if i == len(word)-1 and col + i + 1 < 19:
            if board[row][col + i + 1] != " ":
                illegal = True

        # if there is space to right that is occupied
        if intersect != col + i and board[row][col + i] != " ":
            valid = False

        #illegal adjancy
        if row != 0 and row != 19:
            #letter above or below
            if (board[row-1][col+i] != " " or board[row+1][col+i] != " ") and intersect != col+i:
                illegal = True
        #if at top
        elif row == 0:
            if board[row+1][col+i] != " ":
                illegal = True
        #if at bottom
        else:
            if board[row-1][col+i] != " ":
                illegal = True
    #return if can be placed
    return valid and not illegal

# Add word horizontally
def addhorizontal(board,word):
    for row in range(20):
        for col in range(20):
            # check if word can be placed
            if checkhorizontal(board,word,row,col):
                #place word into matrix
                for i in range(len(word)):
                    board[row][col+i] = word[i]
                return True

#create output.txt file
def output(board):
    f = open('output.txt','w')
    for i in range(20):
        line = ""
        for j in range(20):
            #create line off crossword
            line += " "+board[i][j]
        f.write(line+"\n")
    f.close()

#go through list of words and place into the board
def addwords(board,L):
    word = 0
    # determine which is the first word
    while not addFirstWord(board,L[word]):
        word += 1
        if word == len(L):
            print("All the words are too long!")
            break
    # start at word after first word
    L = L[word+1:] + L[:word]
    x = 0
    loop_count = 0
    loops = len(L)*2
    #break loop when gone through L L*2 times
    while loop_count <= loops:
        #if reached end of L, return to first word
        if x >= len(L)-1:
            x = 0
            #check vertical
        if addvertical(board,L[x]):
            #remove if added
            L.remove(L[x])
            #exit if list is empty
            if len(L) == 0:
                break
        if addhorizontal(board,L[x]):
            #remove if added
            L.remove(L[x])
            #exit if list is empty
            if len(L) == 0:
                break
        #iterate to next word in L
        x += 1
        #if go through loop too many times, exit
        loop_count += 1

    #print words that do not fit
    print('\n')
    for i in range(len(L)):
        print(L[i].capitalize(),"did not fit into crossword.")
    print("\n")

#Evil Test Case
L =["abcdefghijklmnopqrst",
               "fffffggg",
               "ttttttttttuuuuuuuuuz",
               "yzzz",
               "qqqqqqqqqqqqqqy",
               "xxxxxxxxxaaaaaaa",
               "aaaaggg",
               "xxwwww",
               "wwwwvvvvve",
               "vvvvvvvvvvvvq",
               "mat",
               "mat",
               "make",
               "make",
               "maker",
               "remake",
               "hat"]

#Own Test Case
J = ['interesting','popcorn','task','nor','enter','kite','sound','shoot','kilt','turnip','usurp','piano','piano','nautilus',
     'ant','ant','tone','tattoo','turn','turning','prepare','pick','catnip','kaiser','rod','tarantula','flippers','flaming',
     'roller','sanguine','black','dented','astrologically','wicker']

#create board
blank = " "
board = [[blank]*20 for e in range(20)]

#add words, print board and update output.txt
addwords(board,J)
printboard(board)
output(board)
