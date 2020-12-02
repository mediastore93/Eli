# SIMPLE BUBBLE SORT DEMO

# no optimizations

 

print ("Please enter eight numbers.")

numberList = []

 

for counter in range(8):

    number = int(input())

    numberList.append(number)

 

print (numberList)

 

# our worst case would require 7 passes

# that would allow a "1" to bubble from last to first

 

for passes in range(7):

    # in each pass, at worst we should look at every pair

    # there are 7 pairs in total: 0/1, 1/2, 2/3, 3/4, 4/5, 5/6, 6/7

    for pointer in range(7):

        if numberList[pointer]>numberList[pointer+1]:

            # swap

            hold = numberList[pointer]

            numberList[pointer] = numberList[pointer+1]

            numberList[pointer+1] = hold

 

    # show me

    print (numberList)

 

*******************************

*******************************

# BETTER BUBBLE SORT DEMO

# arbitrary number of numbers, optimized

 

print ("How many numbers would you like to sort?")

quantity = int(input())

      

print ("Please enter your numbers.")

numberList = []

 

for counter in range(quantity):

    number = int(input())

    numberList.append(number)

 

print (numberList)

 

# keep working until we have pass with no swaps

swaps = 1

passes = 0

      

while swaps > 0:

    swaps = 0

    passes = passes + 1

 

    for pointer in range(quantity-passes):

        if numberList[pointer]>numberList[pointer+1]:

            # swap

            hold = numberList[pointer]

            numberList[pointer] = numberList[pointer+1]

            numberList[pointer+1] = hold

            swaps = swaps + 1

            # show me

            print (numberList)

           

print (numberList)

 

*******************************

*******************************

# SIMPLE MERGE SORT

# sort with 8 numbers

# code each pass separately

 

print ("Please type eight numbers for me to sort.")

numberList = []

 

for counter in range(8):

    number = int(input())

    numberList.append(number)

 

print (numberList)

 

# pass 1:

# single values, in pairs

# 0/1, 2/3, 4/5, 6/7

 

for firstGroup in range(0,8,2):

    secondGroup = firstGroup + 1

    if numberList[firstGroup] > numberList[secondGroup]:

        temp = numberList[secondGroup]

        numberList[secondGroup] = numberList[firstGroup]

        numberList[firstGroup] = temp

 

print(numberList)

 

# pass 2:

# ordered pairs, in pairs

# 01/23, 45/67

 

newList = []

 

for firstGroup in range(0,8,4):

    secondGroup = firstGroup + 2

    firstPointer = firstGroup

    secondPointer = secondGroup

 

    while firstPointer<secondGroup or secondPointer < secondGroup+2:

        if firstPointer == secondGroup:

            newList.append(numberList[secondPointer])

            secondPointer = secondPointer + 1

        elif secondPointer == secondGroup + 2:

            newList.append(numberList[firstPointer])

            firstPointer = firstPointer+1

        elif numberList[firstPointer]<numberList[secondPointer]:

            newList.append(numberList[firstPointer])

            firstPointer = firstPointer+1

       else:

            newList.append(numberList[secondPointer])

            secondPointer = secondPointer + 1

 

numberList = newList

print(numberList)

 

 

# pass 3:

# ordered groups of 4, one pair

# 0123, 4567

 

newList = []

firstGroup = 0

secondGroup = 4

 

firstPointer = firstGroup

secondPointer = secondGroup

 

while firstPointer<secondGroup or secondPointer < secondGroup+4:

    if firstPointer == secondGroup:

        newList.append(numberList[secondPointer])

        secondPointer = secondPointer + 1

    elif secondPointer == secondGroup + 4:

        newList.append(numberList[firstPointer])

        firstPointer = firstPointer+1

    elif numberList[firstPointer]<numberList[secondPointer]:

        newList.append(numberList[firstPointer])

        firstPointer = firstPointer+1

    else:

        newList.append(numberList[secondPointer])

        secondPointer = secondPointer + 1

 

numberList = newList

print(numberList)

 

*************************************

*************************************

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
