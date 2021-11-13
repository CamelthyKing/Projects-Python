import random
import time
highscore = 50
balance = 50
bet = 0
coin = 0

#how much bet
def makebet():
    global balance
    global bet
    print("Balance: " + str(balance))
    bet = input("how much would you like to bet:\n\n")
    if bet.isdigit() and int(bet) == 0:
        print("you cannot bet nothing.")
        makebet()
    elif bet.isdigit() and int(bet) > balance:
        print("you do not have enough money to make that bet.")
        makebet()
    elif bet.isdigit() and int(bet) > 0 and int(bet) <= balance:
        balance = balance - int(bet)
        coinguess()
    else:
        print("That isn't even a number!")
        makebet()
#heads or tails
def coinguess():
    global guess
    guess = 0
    print("balance: " + str(balance))
    coinguess = input("heads or tails?\n\n")
    if coinguess == "heads":
        guess = 1
        coinflip()
    elif coinguess == "tails":
        guess = 2
        coinflip()
    else:
        print("please guess heads or tails.")
#the coin flipping
def coinflip():
    global balance
    global bet
    global highscore
    headstails = ["ERROR", "heads", "tails"]
    print("balance: " + str(balance))
    print("\nyour guess: " + headstails[int(guess)])
    print("flipping...")
    time.sleep(2.5)
    coin = random.randint(1, 2)
    print ("\n\nIt Was " + headstails[int(coin)] + "!")
    if guess == coin:
        balance = balance + int(bet) + int(bet)
        print("Your guess was correct!")
        print("\n\n     New balance: " + str(balance) + "\n\n")
        if balance > highscore:
            highscore = int(balance)
        print("     Highscore: " + str(highscore))
        time.sleep(2)
    else:
        print("Your guess was incorrect.\n\n")
        time.sleep(2)

while balance > 0:
    makebet()
else:
    print("You are out of money!\n\n\n       YOU LOSE")
    print("\n\nyour highscore: " + str(highscore))