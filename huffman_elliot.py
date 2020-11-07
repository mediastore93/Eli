# ask for their input
phrase = input("What message would you like to compress? ")

# phrase = a man a plan a canal panama

frequencies = []
for letter in phrase:
   
    isCounted = False
    for item in frequencies:
        if item[0] == letter:
            isCounted = True
   
    #how do we get counter?
    if isCounted == False:
        counter = 0
        for character in phrase:
            if character == letter:
                counter += 1
           
        frequencies.append([letter, counter])
   
for item in frequencies:
    if item[0] == " ":
        print ("_", end = " ")
    else:
        print(item[0], end = " ")
    print (item[1])


# notSorted = [ ['a', # of times visited, "not connected"], [' ', # of times visited, "not connected"] ]

notSorted = []

# connected = [ ['n', 1, 1, "left"], [ ' ', 1, 1, "right" ] ]
connected = []
# notSorted = [ [1, 2, "not connected"]]

for item in frequencies:
    notSorted.append([item[0], item[1], "not connected"])

isSorted = False
newCircles = 0
while isSorted == False:
    smallest = 99999999
    secondSmallest = 99999999
    smallestIndex = 0
    secondSmallestIndex = 0
    for item in notSorted:
        if item[2] == "not connected":
            if item[1] < smallest:
                secondSmallest = smallest
                secondSmallestIndex = smallestIndex
                smallest = item[1]
                smallestIndex = item
               
            elif item[1] < secondSmallest:
                secondSmallest = item[1]
                secondSmallestIndex = item
    newCircles += 1
    connected.append([smallestIndex[0], smallest, newCircles, "left"])
    connected.append([secondSmallestIndex[0], secondSmallest, newCircles, "right"])
   
    entries = 0
    for item in notSorted:
        entries += 1

    for part in range(entries):
        if notSorted[part][0] == smallestIndex[0]:
            index1 = part
        if notSorted[part][0] == secondSmallestIndex[0]:
            index2 = part
   
    notSorted[index1][2] = "connected"
    notSorted[index2][2] = "connected"
   
    notSorted.append([newCircles, smallest + secondSmallest, "not connected"])
    numNotCounted = 0
    for item in notSorted:
        if item[2] == "not connected":
            numNotCounted += 1
    if numNotCounted == 1:
        connected.append([newCircles, smallest+secondSmallest, "finished"])
        print ("stopping")
        isSorted = True
       
print (connected)
