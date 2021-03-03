your_budget = int(input('What is your budget for it?'))

if your_budget <= 1000 :
    print("You'll have to go cheap!")
    if your_budget < 500 :
        print('Well, you might need to save up another paycheck')
        if your_budget < 250 :
            print("You don't have nearly enough")
if your_budget > 1000 :
    print('You should have just about enough!')
    if your_budget >= 2000 :
        print('You have some room to play around with it')
        if your_budget >= 3000 :
            print("Money isn't an object")
