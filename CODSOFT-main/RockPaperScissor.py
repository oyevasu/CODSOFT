import random
userchoice=int(input('Enter your Choice: \nType 0 for Rock\nType 1 for Paper\nType 2 for Scissor\n'))
if userchoice >=3 or userchoice<0:
    print('You entered Invalid Number,Think Again')
else:
  computerchance=random.randint(0,2)
print('this is Computer Choice:')
print(computerchance)
if computerchance==userchoice:
    print('Tie/Draw')

#here 0=Rock and 2=Scissor    
elif computerchance== 0 and userchoice == 2:   
    print('you Loose')
elif userchoice == 0 and computerchance ==2:
    print('you are Winner')

if computerchance>userchoice:
    print('LOSER')
if userchoice>computerchance:
    print('Congrats!!You are Winner')