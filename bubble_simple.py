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
