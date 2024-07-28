stone = 1
paper = -1
scissor = 0

computer = -1  
youstr = input("Enter your choice (s for stone, w for paper, g for scissor): ")
youDict = {"s": 1, "w": -1, "g": 0}
you = youDict[youstr]

reverseDict = {1: "stone", -1: "paper", 0: "scissor"}

print(f"You choose {reverseDict[you]}\nComputer choose {reverseDict[computer]}")

if computer == you:
    print("It's a draw")
elif (computer == 1 and you == -1) or (computer == 0 and you == 1) or (computer == -1 and you == 0):
    print("You win")
else:
    print("You lost")
