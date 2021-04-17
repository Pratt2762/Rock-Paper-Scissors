import random
import pyttsx3
import sys
from termcolor import colored, cprint
engine = pyttsx3.init()

print("Let's play Rock, Paper, Scissors! Best of 5 wins!\n")
engine.say("Let's play Rock, Paper, Scissors! Best of 5 wins!")
engine.runAndWait()
u,c=0,0
x = colored("It's a tie.",'blue', attrs=['bold'])
y = colored("You won this round!", 'green', attrs=['bold'])
z = colored("You lost this round.", 'red', attrs=['bold'])

for i in range(1,6):
    round = "ROUND " + str(i)
    print(round.center(70))
    print("\n")
    engine.say(round)
    engine.runAndWait()
    user = input("Enter 'r' for Rock, 'p' for Paper and 's' for Scissors.\n")
    com = random.choice(['r','p','s'])

    def win(p1,p2):
        if (p1=='r' and p2=='s') or (p1=='s' and p2=='p') or (p1=='p' and p2=='r'):
            return True

    if user == com:
        print(x.center(80))
        engine.say("It's a tie.")
        engine.runAndWait()
    elif win(user,com):
        print(y.center(80))
        engine.say("You won this round!")
        engine.runAndWait()
        u+=1
    else:
        print(z.center(80))
        engine.say("You lost this round.")
        engine.runAndWait()
        c+=1

    print("\n")
    score = "USER: " + str(u) + " COMPUTER: " + str(c)
    print(score.center(70))
    print("\n")

if u>c:
    result = colored("Congratulations! You won the game!", 'blue', 'on_white', attrs=['bold', 'blink'])
    print(result.center(90))
    engine.say("Congratulations! You won the game!")
    engine.runAndWait()
elif u<c:
    result = colored("You lost. Better luck next time.", 'red', 'on_white', attrs=['bold', 'blink'])
    print(result.center(90))
    engine.say("You lost. Better luck next time!")
    engine.runAndWait()
else:
    result = colored("The game ends in a tie!", 'magenta', 'on_white', attrs=['bold', 'blink'])
    print(result.center(90))
    engine.say("The game ends in a tie!")
    engine.runAndWait()




