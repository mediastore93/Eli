print("Do you want to play a game of NIM?")
i=str(input())
while(i=="yes"):
    chips=21
    print ("this is the game of NIM!")
    while(chips>0):
        print("there are "+str (chips)+" chips left")
        print("how many chips do you want to take?")
        n=int(input())
        while (n<1 or n>3):
            print("how many chips do you want to take?")
            n=int(input())    
        chips-=n
        if (chips<=0):
            print("GAME_OVER robot WINS!")
        else:
            robot=(4-n)
            chips-=robot
            if (chips<=0):
                print("GAME_OVER you WIN!")

    print("Do you want to play another game of NIM?")
    i=str(input())
print("OK oh well, you missed out on a lot of fun! BYE!") 
