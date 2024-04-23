import random

def initGlobals():
    global playerName
    global con
    global dex
    global intel
    global playerX
    global playerY
    global treasureX
    global treasureY
    global turnsRemaining
    global test
    global maze
    global hasTreasure
    global dead
    global enemy

    playerName = ""
    dead= False
    con = 0
    dex = 0
    intel = 0

    playerX = 3
    playerY = 3

    treasureX=3
    treasureY=3
    hasTreasure=False

    while True:
        if treasureX == 3 and treasureY== 3:
            treasureX = random.randint(1,5)
            treasureY = random.randint(1,5)
        else:
            break

    turnsRemaining = 20

    maze= [
        ["#","#","#","#","#","#","#"],
        ["#"," "," "," "," "," ","#"],
        ["#"," "," "," "," "," ","#"],
        ["#"," "," "," "," "," ","#"],
        ["#"," "," "," "," "," ","#"],
        ["#"," "," "," "," "," ","#"],
        ["#","#","#","#","#","#","#"],
    ]

    enemy= [1,2,3]

def display():
    global playerX
    global playerY
    global maze
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    #prints the game map.
    maze[playerY][playerX] = "X"

    #TODO: take out this T replace. It's just for in development.
    maze[treasureX][treasureY]= "T"

    #has to loop because map is a list of lists.
    for i in maze:
        print(i)

def getMovePlayer():

    valid=["w","a","s","d"]

    #Gets user input on where to move(WASD). Does not prompt the player for input
    #to go to a square with lava(#) but still allows it for a game over.
    #User can also h to see help(pause menu)

    while True:
        if playerX== 1:
            move = input("Which way would you like to go(WSD)? ").lower()
        elif playerX== 6:
            move = input("Which way would you like to go(WAS)? ").lower()
        elif playerY==1:
            move = input("Which way would you like to go(ASD)? ").lower()
        elif playerY==6:
            move = input("Which way would you like to go(WAD)? ").lower()
        else:
            move = input("Which way would you like to go(WASD)? ").lower()

        if move in valid:
            return move
        elif move=="h" or move=="help":
            help()
        else:
            print(f"Sorry, {move} is not a valid direction.\n")

def movePlayer(move):
    global playerX
    global playerY
    global dead
    global turnsRemaining

    #Implements the move returned by getMovePlayer. Decrements turns remaining.

    if move == "w":
        playerY -=1
    elif move == "a":
        playerX-=1
    elif move =="d":
        playerX += 1
    elif move=="s":
        playerY +=1
    elif move== "h" or move=="help":
        help()
        getMovePlayer()

    turnsRemaining -=1
    if playerX==0 or playerX==6 or playerY==0 or playerY==6:
        print("Game over.")
        dead= True

def newRoom():
    #When a player gets to a new room, this will check if they're in the treasure room.
    #If not, then it will return a random choice from the enemy list.
    global enemy
    global hasTreasure
    if maze[playerY][playerX]==maze[treasureX][treasureY]:
        print("YOU WON!")
        hasTreasure=True
    else:
        return random.choice(enemy)

def roomOne():
    pass
def roomTwo():
    pass
def roomThree():
    #room three is a level up room!!! or maybe
    #TODO: implement heal?
    getPlayerClass()



def showInstructions():
    up="W"
    left = "A"
    right = "D"
    down = "S"

    # TODO: add explanaition of what con, dex, int do.
    #Initial print at start game.
    print("Welcome to Dungeons, Diners, and Dives")
    print("In this immersive simulation you'll be looking for the lost treasure.")
    print("Controls: ")
    print(f"        {up: ^7}")
    print(f"        {left:-<3}+{right:->3}")
    print(f"        {down:^7}")
    print("\n")
    print("Don't step in the lava(#)!")

def help():
    global turnsRemaining
    global con
    global dex
    global intel
    #Pause screen. Shows turns remaining and other stats.

    print("\nTake a rest adventurer.")
    print(f"     Turns Remaining: {turnsRemaining}")
    print(f"     Health: to see player stats")
    print("")
    print(f"Stats:\n"
          f"    Constitution: {con}\n"
          f"    Dexterity: {dex}\n"
          f"    Intelligence:{intel}\n")
def getPlayerName():
    global playerName
    print("\n")
    #Check for numbers and length
    while True:
        playerName= input("What's the name of our hero(3 Char. Min.): ")

        for i in playerName:
            if i.isdigit():
                valid=False
            elif i.isalpha():
                valid=True
        if valid==True and (len(playerName) >= 3):
            break
        else:
            print("Sorry, 3 character minimum for the name, and no numbers.")
def getPlayerClass():
    global con
    global dex
    global intel
    #Class assignment. Each class gets buff to a stat that helps in the game.


    while True:
        global con
        global intel
        global dex
        #TODO subclasses?
        try:
            playerClass= int(input(f"Is {playerName.title()} taking a level in: \n    1. Fighter(+2 Con)\n    2. Wizard(+2 Int)\n    3. Thief(+2 Dex)\nEnter 1/2/3: "))

        except ValueError:
            print("Input 1/2/3\n")
            continue

        if playerClass== 1 or playerClass==2 or playerClass == 3:
            break
        else:
            print("")
    #Stat Assignment based on user input
    if playerClass ==1:
        con +=2
    elif playerClass ==2:
        intel +=2
    elif playerClass ==3:
        dex +=2
def showPlayerStats():
    print(f"Constitution: {con}")
    print(f"Dexterity: {dex}")
    print(f"Intelligence: {int}")


def gameLoop():
    #The game itself will run as long as the player doesn't have the treasure,
    #isn't dead, and has turns remaining. The player could find the treasure
    #in the final room so turns go down to 0.
    while hasTreasure==False and dead==False and turnsRemaining>=0:
        display()
        move=getMovePlayer()
        movePlayer(move)

        #If the element of the new square is blank(No X for where they've been,
        #and no T for treasure, call newRoom() to generate challenge.
        if maze[playerX][playerY]==" ":
            challenge=newRoom()
            if challenge==1:
                print(1)
                roomOne()
            elif challenge==2:
                print(2)
                roomTwo()
            elif challenge==3:
                print(3)
                roomThree()

def startGame():
    #Start Screen
    initGlobals()
    showInstructions()
    getPlayerName()
    getPlayerClass()
    print("Great! Let's begin :D\n")
    gameLoop()


def main():
    while True:
        startGame()
        again:str=str(input("Thanks for playing!\nWould you like to play again?")).lower()
        if again=="y" or again=="yes":
            continue
        else:
            break
main()