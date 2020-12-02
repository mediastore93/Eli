# BETTER MERGE SORT

# still using only 8 numbers

# but now using a single loop!

 

print ("Please type eight numbers for me to sort.")

numberList = []

 

for counter in range(8):

    number = int(input())

    numberList.append(number)

 

print (numberList)

 

passCount = -1

 

while 2**passCount<4:

   

    passCount = passCount + 1

 

    newList = []

 

    for firstGroup in range(0,8,(2**(passCount+1))):

        secondGroup = firstGroup + (2**passCount)

        firstPointer = firstGroup

        secondPointer = secondGroup

 

        while firstPointer<secondGroup or secondPointer < secondGroup+(2**passCount):

            if firstPointer == secondGroup:

                newList.append(numberList[secondPointer])

                secondPointer = secondPointer + 1

                print(newList)

            elif secondPointer == secondGroup + (2**passCount):

                newList.append(numberList[firstPointer])

                firstPointer = firstPointer+1

                print(newList)

            elif numberList[firstPointer]<numberList[secondPointer]:

                newList.append(numberList[firstPointer])

                firstPointer = firstPointer+1

                print(newList)

            else:

                newList.append(numberList[secondPointer])

                secondPointer = secondPointer + 1

                print(newList)

 

    print("Finished a pass.")

    numberList = newList

    print(numberList)
