import random
# FUNCTION DEFINITION
def up_and_down(word):
# this function accepts a string, which it calls 'word'
# and prints it using random capital and lowercase letters
  for letter in word:
    ranNum = random.randint(0,1)
    if ranNum == 1:
      letter = ord(letter) - 32
      chrletter = chr(letter)
      print (chrletter,end="")
    else:
      print (letter,end="")
# MAIN PROGRAM
anotherWord = True
while anotherWord:
  # ask for a word
  print ("Please type a word. ")
  response = input("")
  print ()
  # call the function up_and_down, passing in the user's response
  up_and_down(response)
  print ()
  # ask the user if they want to continue
  print ()
  response = input("Try again? [y/n] ")
  if response != "y":
    anotherWord = False
  print ()
