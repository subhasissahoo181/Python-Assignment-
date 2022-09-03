# The game() function in a program lets a user play a game and returns the score as an integer. 
# You need to read a file 'High-score.txt' which is either blank or contains the previous High-score where game() breaks the Hi-score.

def game():
    return 64

score = game()
with open("ch-9/hiscore.txt") as f:
    hiscoreStr = f.read()

if hiscoreStr == '':
     with open("ch-9/hiscore.txt", "w") as f:
        f.write(str(score))
elif int(hiscoreStr)<score:
    with open("ch-9/hiscore.txt", "w") as f:
        f.write(str(score))