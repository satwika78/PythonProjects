import random
def guessgame():
    rand=random.randint(1,100)
    guess=int(input("Guess the number:"))
    attempt=1
    while(True):
        if(guess>rand):
            guess=int(input("Guess is too high,select other number:"))
            attempt+=1;
        elif(guess<rand):
            guess=int(input("Guess is too low,select other number:"))
            attempt+=1;
        else:
            print("you are right")
            return attempt
            break;


player1=input("enter player one name:")
player2=input("enter player two name:")
score1=guessgame()
score2=guessgame()
if(score1==score2):
    print("its s Draw")
elif(score1<score2):
    print(f"{player1} won the game by {score2-score1} attempts")
else:
    print(f"{player2} won the game by {score1-score2} attempts")