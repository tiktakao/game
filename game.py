import random
import operator

def initGlobals():
    global playerName
    global con
    global luck
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
    global congrat
    global taunt

    playerName = ""
    dead= None
    con = 0
    luck = 0
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

    congrat=["lucky","Amazing","You did it","Fantastic","Smart and handsome","Big brain moves","No one likes a showoff"]
    taunt= ["Idiot","Dum dummm","You ARE the weakest link","Your father smells of elderberries",
            "Boo, I'm booing you","better luck next time","mwahahaha", "you have to be tired of failing by now",
            "kick rocks"]


def display():
    global playerX
    global playerY
    global maze
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    #replaces the last player marked location with a little x instead of a big X
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == "X":
                maze[i][j] = "x"

    #marks current player position.
    maze[playerY][playerX] = "X"

    #TODO: take out this T replace. It's just for in development.
    maze[treasureX][treasureY]= "T"

    #has to loop because map is a list of lists.
    for i in maze:
        print(i)

def getMovePlayer():
    global playerName

    valid=["w","a","s","d"]

    #Gets user input on where to move(WASD). Does not prompt the player for input
    #to go to a square with lava(#) but still allows it for a game over.
    #User can also h to see help(pause menu)

    while True:
        if playerX== 1:
            move = input(f"Which way, {playerName.title()}(WSD)?\n"
                         f"or h for help: ").lower()
        elif playerX== 6:
            move = input(f"Which way, {playerName.title()}(WAS)?\n"
                         f"or h for help: ").lower()
        elif playerY==1:
            move = input(f"Which way, {playerName.title()}(ASD)?\n"
                         f"or h for help: ").lower()
        elif playerY==6:
            move = input(f"Which way, {playerName.title()}(WAD)?\n"
                         f"or h for help: ").lower()
        else:
            move = input(f"Which way, {playerName.title()}(WASD)?\n"
                         f"or h for help: ").lower()

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
        print("Uh oh! You stepped in lava!")
        dead= True

def newRoom():
    #When a player gets to a new room, this will check if they're in the treasure room.
    #If not, then it will return a random choice from the enemy list.
    global hasTreasure
    if maze[playerY][playerX]==maze[treasureX][treasureY]:
        print("YOU WON!")
        hasTreasure=True
    else:
        return random.randint(1,5)

def roomOne():
    #guessing game
    global con
    global luck
    global congrat
    global taunt
    global playerName


    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    print("Room 1")
    print(f"{playerName.title()}, I've been waiting.")

    ctr= 0
    ordinal= ["first","second","third","fourth","fifth","sixth","seventh","eighth","ninth","tenth"]
    x = random.randint(1,5)
    while ctr<(3+con):
        print(x)
        try:
            guess:int = int(input(f"Guess a number between 1 and 5!\n"
                                  f"You have {(3+con)-ctr} guesses remaining.\n"
                                  f"What's your {ordinal[ctr]} guess: "))

        except:
            print("Ya dingus, that's not a number!\n")
            continue
        if guess==x or (guess-luck)<= x <=(guess+luck):
            print(f"{(random.choice(congrat)).capitalize()}! Go on your way adventurer. ")
            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
            break

        else:
            print(f"{random.choice(taunt)}!\n")
            ctr+=1
    if ctr==(3+con):
        return True

def roomTwo():
    #Math game. add,sub, mult
    global luck
    global con
    global congrat
    global taunt
    global playerName


    operators=["+","-","x"]
    operation=[operator.add, operator.sub, operator.mul]

    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    print("Room 2")


    x=random.randint(1,20)
    y=random.randint(1,20)
    what=(random.randint(0,2)-luck)
    if what<0:
        what=0

    ctr=0
    while ctr<(3+con):
        print(f"You have {(3+con)-ctr} tries remaining.")
        try:
            z=int(input(f"What's {x}{operators[what]}{y}: "))
        except:
            print("No letters, only numbers allowed.\n")
            continue
        if z==(operation[what](x,y)):
            print(f"{(random.choice(congrat)).capitalize()}! Go on your way adventurer.")
            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
            break
        else:
            ctr+=1
            print("NO")
    if ctr==(3+con):
        return True

def roomThree():
    print("Room 3")

def roomFour():
    # room three is a level up room!!! or maybe
    # TODO: implement heal?
    print("Room 4")
    getPlayerClass()

def roomFive():
    print("Room 5")
    print("Hmmmm.... This room seems safe.")

def roomBoss():
    pass



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
    global luck
    global intel
    #Pause screen. Shows turns remaining and other stats.

    print("\nTake a rest adventurer.")
    print(f"     Turns Remaining: {turnsRemaining}")
    print(f"     Health: to see player stats")
    print("")
    print(f"Stats:\n"
          f"    Constitution: {con}\n"
          f"    Luck: {luck}\n"
          f"    Intelligence:{intel}\n")
def getPlayerName():
    global playerName
    print("\n")
    #Check for numbers and length
    while True:
        playerName= input("What's the name of our hero(3 Char. Min.): ")
        valid=True
        char=[]

        for i in playerName:
            char.append(i)
        for j in char:
            if j.isnumeric():
                valid = False

        if valid==True and (len(playerName) >= 3):
            break
        else:
            print("Sorry, 3 character minimum for the name, and no numbers.\n")
def getPlayerClass():
    global con
    global luck
    global intel
    #Class assignment. Each class gets buff to a stat that helps in the game.


    while True:
        global con
        global intel
        global luck
        #TODO subclasses?
        try:
            playerClass= int(input(f"\nIs {playerName.title()} taking a level in: \n    1. Fighter(+1 Con)\n    2. Wizard(+1 Int)\n    3. Thief(+1 Luck)\nEnter 1/2/3: "))

        except ValueError:
            print("Input 1/2/3\n")
            continue

        if playerClass== 1 or playerClass==2 or playerClass == 3:
            break
        else:
            print("")
    #Stat Assignment based on user input
    if playerClass ==1:
        con +=1
    elif playerClass ==2:
        intel +=1
    elif playerClass ==3:
        luck +=1


def gameLoop():
    global dead
    #The game itself will run as long as the player doesn't have the treasure,
    #isn't dead, and has turns remaining. The player could find the treasure

    while hasTreasure==False and dead==None and turnsRemaining>0:
        display()
        move=getMovePlayer()
        movePlayer(move)

        #If the element of the new square is blank(No X for where they've been,
        #and no T for treasure, call newRoom() to generate challenge.
        #TODO: for some reason its still calling newRoom() if theres an X in the position.
        if " " in maze[playerX][playerY] or maze[playerX][playerY]== "T":
            challenge=newRoom()
            if challenge==1:
                dead=roomOne()
            elif challenge==2:
                dead=roomTwo()
            elif challenge==3:
                dead=roomThree()
            elif challenge==4:
                dead=roomFour()
            elif challenge==5:
                dead=roomFive()
    if dead==True:
        print("\n~~~~~~YOU DIED~~~~~~\n")
    elif turnsRemaining==0:
        print(f"Womp womp! You ran out of turns.")
    elif hasTreasure==True:
        print("That's amazing! You win!")



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