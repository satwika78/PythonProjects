import random;
def rps(comp,mine):
    if(comp==mine):
        return None
    elif(comp=='r' and mine=='p'):
        return True
    elif(comp=='p' and mine=='s'):
        return True
    elif(comp=='s' and mine=='r'):
        return True
    else:
        return False

choice = ('r','p','s')
comp = random.randint(0,2)
comp=choice[comp]
mine=input("choose rock:'r' or paper:'p' or scissor: 's' ")
win=rps(comp,mine)
print(f"you choose {mine} and computer choose {comp}")
if(win==None):
    print("its a Draw")
elif(win):
    print("You Win")
else:
    print("You Lose")
