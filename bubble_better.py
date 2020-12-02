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
