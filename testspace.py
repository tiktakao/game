import random
# #
# # enemy= [1,2,3]
# #
# #
# maze= [
#     ["#","#","#","#","#","#","#"],
#     ["#"," "," "," "," "," ","#"],
#     ["#"," "," "," "," "," ","#"],
#     ["#"," "," ","X"," "," ","#"],
#     ["#"," "," "," "," "," ","#"],
#     ["#"," "," "," "," "," ","#"],
#     ["#","#","#","#","#","#","#"],
# ]
# #
# # for i in maze:
# #     for j in i:
# #         p
#
#
# #
# # playerX = 3
# # playerY = 3
# #
# #
# #
# for i in range(len(maze)):
#     for j in range(len(maze[i])):
#         if maze[i][j]=="X":
#             maze[i][j]="x"
# #
# #
# #
# #
# #
# #
# #
# #
# # while True:
# #     maze[playerY][playerX]="X"
# #
# #     for i in maze:
# #         print(i)
# #
# #
# #     if playerX== 1:
# #         move = input("How to move(WSD)? ").lower()
# #     elif playerX== 6:
# #         move = input("How to move(WAS)? ").lower()
# #     elif playerY==1:
# #         move = input("How to move(ASD)? ").lower()
# #     elif playerY==6:
# #         move = input("How to move(WAD)? ").lower()
# #     else:
# #         move = input("How to move(WASD)? ").lower()
# #
# #     if move == "w":
# #         playerY -=1
# #     elif move == "a":
# #         playerX-=1
# #     elif move =="d":
# #         playerX +=1
# #     elif move=="s":
# #         playerY +=1
# #
# #     if playerX==0 or playerX==6 or playerY==0 or playerY==6:
# #         print("Game over.")
# #
# #         break
# #
# # # while True:
# # #     playerName = input("What's the name of our hero(3 Char. Min.): ")
# # #     valid=True
# # #     char= []
# # #     for i in playerName:
# # #         char.append(i)
# # #     for j in char:
# # #         if j.isnumeric():
# # #             valid=False
# # #     break
# # # print(playerName)
# # # print(valid)
# # # print(char)
#
# # intel=1
# # hintChance=0
# #
# #
# # problems= [
# # #1
# #     "True or False",
# # #2
# #     "False or True",
# # #3
# #     "This or that"
# # ]
# #
# # hints= [
# # #1
# #     "Hmmm, I think it's True",
# # #2
# #     "hmm, false?",
# # #3
# #     "that"
# #         ]
# #
# # answer= [
# # #1
# #     "true",
# # #2
# #     "false",
# # #3
# #     "that"
# # ]
# #
# #
# # which= random.randint(0,(len(problems)-1))
# # if intel>0:
# #     hintChance=(random.randint(1,5)+intel)
# #
# #
# #
# # print(f"{problems[which]}")
# # print("hint chance",hintChance)
# #
# # if hintChance >=5:
# #     print(f"{hints[which]}")
# #
# # guess= input("Enter: ").lower()
# #
# #
# # if guess == answer[which]:
# #     print("Congratulations!")
#
# #Implement intel. With 4 answer questions, it narrows down to 4-intel
# #shows those options but next to it, tags them as incorrect
#
# lst= iter(["Red","Blue","Green","Orange"])
#
# x= next(lst)
# x= next(lst)
#
#
# print(x)
#


art=(r"""

 _______  __          ___   ____    ____  ______   .______     .___________.  ______   ____    __    ____ .__   __. 
|   ____||  |        /   \  \   \  /   / /  __  \  |   _  \    |           | /  __  \  \   \  /  \  /   / |  \ |  | 
|  |__   |  |       /  ^  \  \   \/   / |  |  |  | |  |_)  |   `---|  |----`|  |  |  |  \   \/    \/   /  |   \|  | 
|   __|  |  |      /  /_\  \  \      /  |  |  |  | |      /        |  |     |  |  |  |   \            /   |  . `  | 
|  |     |  `----./  _____  \  \    /   |  `--'  | |  |\  \----.   |  |     |  `--'  |    \    /\    /    |  |\   | 
|__|     |_______/__/     \__\  \__/     \______/  | _| `._____|   |__|      \______/      \__/  \__/     |__| \__| 
                                                                                                                    

""")


#Towers of hanoi

for _ in range(3):
    print('meow', end="")




