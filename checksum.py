
# CHECKSUM GRID DECODER
#   This program accepts a 24-digit number,
#   reads the first 16 digits as if they were stored in four rows of 4 digits
#   and assumes the last 8 digits are, in order, the checksums for the
#   resulting rows followed by the checksums for the resulting columns.
#
# TEST DATA
#   If the user inputs this 24-digit number:
#       564359803214553382068260
#   The program should report back:
#       5643598032145533
#   If the user makes any single mistake, the program should still work.
#
#   Some sample mistakes are:
#   497821827391548923068120
#   417821827391548923068120
#   437821827391548923068140
#   437821827391548923068100
#
#
# MAIN PROGRAM
#
# ask for the encoded number
print ("Please type in a 24-digit encoded number.")
originalNumber = input("")

# now, separate the digits and store them as a list
# be sure to store them as integers
values = []
for digit in originalNumber:
    values.append(int(digit))

# calculate the checksums we expect
# and compare to the checksum values we received

# keep track of how many errors
errorCount = 0

# THIS BLOCK OF CODE CHECKS THE FIRST ROW

# this is the expected checksum
checksum = values[0]+values[1]+values[2]+values[3]

# now, focus on the 1's digit only
while checksum > 9:
    checksum = checksum - 10

# compare the calculated checksum to the received checksum
if checksum != values[16]:

    # if they are different, we have an error
    errorCount = errorCount + 1
    # remember which row this is
    badRow = 1


# THE NEXT BLOCKS OF CODE DO THE SAME WORK FOR EVERY ROW,
# AND THEN EVERY COLUMN
    
checksum = values[4]+values[5]+values[6]+values[7]
while checksum > 9:
    checksum = checksum - 10
if checksum != values[17]:
    errorCount = errorCount + 1
    badRow = 2

checksum = values[8]+values[9]+values[10]+values[11]
while checksum > 9:
    checksum = checksum - 10
if checksum != values[18]:
    errorCount = errorCount + 1
    badRow = 3

checksum = values[12]+values[13]+values[14]+values[15]
while checksum > 9:
    checksum = checksum - 10
if checksum != values[19]:
    errorCount = errorCount + 1
    badRow = 4

checksum = values[0]+values[4]+values[8]+values[12]
while checksum > 9:
    checksum = checksum - 10
if checksum != values[20]:
    errorCount = errorCount + 1
    badCol = 1

checksum = values[1]+values[5]+values[9]+values[13]
while checksum > 9:
    checksum = checksum - 10
if checksum != values[21]:
    errorCount = errorCount + 1
    badCol = 2

checksum = values[2]+values[6]+values[10]+values[14]
while checksum > 9:
    checksum = checksum - 10
if checksum != values[22]:
    errorCount = errorCount + 1
    badCol = 3

checksum = values[3]+values[7]+values[11]+values[15]
while checksum > 9:
    checksum = checksum - 10
if checksum != values[23]:
    errorCount = errorCount + 1
    badCol = 4


# now we just have to use the above information to print out
# the right answer

if errorCount == 0:
    # no errors!
    print ("The message came through perfectly.  The 16-digits are:")
    for counter in range(16):
        print (values[counter], end=" ")
    print()

if errorCount == 1:
    # if there really is only one mistake in the datastream,
    # then the error must be in the CHECKSUM, not the 16 digits
    # otherwise, we would have two errors (one row, one column)
    print ("There was an error in a checksum digit.")
    print ("Thus, the 16-digits are:")
    for counter in range(16):
        print (values[counter], end=" ")
    print()

if errorCount == 2:
    # if we have 2 errors, we can fix the problem
    # use badRow and badCol to find the location
    # and use the difference between the expected checksum and the real checksum to fix it
    badDigitNumber = (badRow-1)*4 + (badCol-1)
    receivedRowChecksum = values[16+(badRow-1)]
    calculatedRowChecksum = values[(badRow-1)*4]+values[(badRow-1)*4+1]+values[(badRow-1)*4+2]+values[(badRow-1)*4+3]
    while calculatedRowChecksum>9:
        calculatedRowChecksum = calculatedRowChecksum-10
        
    print ("The message had an error.")
    print ("But I fixed it.")
    print ("The 16-digits are:")
    for counter in range(16):
        if counter == badDigitNumber:
            correctValue = values[counter]-calculatedRowChecksum+receivedRowChecksum
            # make sure that the number did not end up negative by accident!
            if correctValue < 0:
                correctValue = correctValue + 10
            print (correctValue, end=" ")
        else:
            print (values[counter],end=" ")
    print()

if errorCount > 2:
    # this data has more than 1 error
    print ()
    print ("I am sorry.")
    print ("This data is corrupted.")
    print ("I found more than 2 errors.")
    print ()

## NOTES
##
## To focus on the 1's digit in the checksums, we keep subtracting 10 from the sum
## until the sum is only one digit.  Another way to solve the problem is to use the
## math operator "modulo" (%).  If you know about modulo, that is an easier way to
## write that portion of the code.
##
## To calculate the checksums, we repeat a lot of code.  A better approach would be
## to use FOR LOOPS to repeat the code, or to write FUNCTIONS that repeat the code.
## If you are comfortable with either of those approaches, those would simplify and
## shorten this code.
##
## When testing code, always be sure to test all relevant possible mistakes.  Here,
## for instance, it was important to test situations where a digit was wrongly high
## and also situations where a digit was wrongly low.  It was also important to test
## situations where the mistake was in the checksum, not in the 16 original digits.
##
