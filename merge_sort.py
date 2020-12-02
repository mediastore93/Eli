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
