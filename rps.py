print("rock, paper, or, scissors")
p1=str(input())
p2=str(input())
if (p1==p2):
    print("It's a DRAW!")
else:
    if (p1=="rock"):
        if (p2=="scissors"):
            print ("P1 WINS!")
        else:
            print("P2 WINS!")
    elif (p1=="scissors"):
        if (p2=="paper"):
            print ("P1 WINS!")
        else:
            print ("P2 WINS!")
    else:
        if (p2=="rock"):
            print ("P1 WINS!")
        else:
            print ("P2 WINS!")
