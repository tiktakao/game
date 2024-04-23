import random

enemy= [1,2,3]


maze= [
    ["#","#","#","#","#","#","#"],
    ["#"," "," "," "," "," ","#"],
    ["#"," "," "," "," "," ","#"],
    ["#"," "," ","X"," "," ","#"],
    ["#"," "," "," "," "," ","#"],
    ["#"," "," "," "," "," ","#"],
    ["#","#","#","#","#","#","#"],
]


playerX = 3
playerY = 3



for i in range(len(maze)):
    for j in range(len(maze[i])):
        if maze[i][j]==" ":
            print(random.choice(enemy))








while True:
    maze[playerY][playerX]="X"

    for i in maze:
        print(i)


    if playerX== 1:
        move = input("How to move(WSD)? ").lower()
    elif playerX== 6:
        move = input("How to move(WAS)? ").lower()
    elif playerY==1:
        move = input("How to move(ASD)? ").lower()
    elif playerY==6:
        move = input("How to move(WAD)? ").lower()
    else:
        move = input("How to move(WASD)? ").lower()

    if move == "w":
        playerY -=1
    elif move == "a":
        playerX-=1
    elif move =="d":
        playerX +=1
    elif move=="s":
        playerY +=1

    if playerX==0 or playerX==6 or playerY==0 or playerY==6:
        print("Game over.")

        break

