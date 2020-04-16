print("Hello World")
#A-Z 0-9 _
x = 3
print(x)
x = 5
print(x)
#integer
y= 3
#float
z = 3.14159
#String 
name = "Yvette"
#boolean 
roomcleaned = False 

print("My name is " + name)
name = "Katarina"
print("My name is " + name)

#input
urName = input("What is your name? ")

#if/elif/else statements
if urName=="Katarina":
  print("Hi Katarina, you're teaching this class!")
elif urName=="Yvette":
  print("Hi Yvette, you're teaching this class!")
else: 
  print("You aren't teaching this class :)")

#input
favNumber = input("What is your favorite number? ")

#nested if/elif/else statements
if urName=="Katarina":
  if favNumber=="5":
    print("You're definitely Katarina")
  elif favNumber=="6":
    print("You're probably Katarina")
  else:
    print("You're probably not Katarina")

elif urName=="Yvette":
  if favNumber=="9":
    print("You're definitely Yvette")
  elif favNumber=="8":
    print("You're probably Yvette")
  else:
    print("You're probably not Yvette")

else:
  print("You're not Yvette or Katarina, you're "+urName)