
# Accept a phrase for compression
print ("Please enter a message for compression.")
phrase = input("")

# Or hard-code a song from Hamilton
# phrase = "I am not throwin' away my shot I am not throwin' away my shot Hey yo, I'm just like my country I'm young, scrappy and hungry And I'm not throwin' away my shot I'ma get a scholarship to King's College I probably shouldn't brag, but dang, I amaze and astonish The problem is I got a lot of brains but no polish I gotta holler just to be heard With every word, I drop knowledge I'm a diamond in the rough, a shiny piece of coal Tryna reach my goal my power of speech, unimpeachable Only nineteen but my mind is older These New York City streets get colder, I shoulder Every burden, every disadvantage I have learned to manage, I don't have a gun to brandish I walk these streets famished The plan is to fan this spark into a flame But damn, it's getting dark, so let me spell out my name I am the A-L-E-X-A-N-D-E-R we are meant to be A colony that runs independently Meanwhile, Britain keeps shittin' on us endlessly Essentially, they tax us relentlessly Then King George turns around, runs a spendin' spree He ain't ever gonna set his descendants free So there will be a revolution in this century Enter me, he says in parentheses Don't be shocked when your history book mentions me I will lay down my life if it sets us free Eventually, you'll see my ascendancy And I am not throwin' away my shot I am not throwin' away my shot Hey yo, I'm just like my country I'm young, scrappy and hungry And I'm not throwin' away my shot I am not throwin' away my shot I am not throwin' away my shot Hey yo, I'm just like my country I'm young, scrappy and hungry And I'm not throwin' away my shot It's time to take a shot I dream of life without a monarchy The unrest in France will lead to anarchy? Anarchy how you say, how you, oh, anarchy? When I fight, I make the other side panicky With my, shot Yo, I'm a tailor's apprentice And I got y'all knuckleheads in loco parentis (loco parentis) I'm joining the rebellion 'cause I know it's my chance To socially advance, instead of sewin' some pants (woo) I'm gonna take a shot And but we'll never be truly free Until those in bondage have the same rights as you and me You and I Do or die Wait 'til I sally in on a stallion With the first black battalion Have another shot Geniuses, lower your voices You keep out of trouble and you double your choices I'm with you, but the situation is fraught You've got to be carefully taught If you talk, you're gonna get shot Burr, check what we got Mister Lafayette, hard rock like Lancelot I think your pants look hot Laurens, I like you a lot Let's hatch a plot blacker than the kettle callin' the pot What are the odds the gods would put us all in one spot Poppin' a squat on conventional wisdom, like it or not A bunch of revolutionary manumission abolitionists? Give me a position, show me where the ammunition is Oh, am I talkin' too loud? Sometimes I get over excited, shoot off at the mouth I never had a group of friends before I promise that I'll make y'all proud Let's get this guy in front of a crowd I am not throwin' away my shot I am not throwin' away my shot Hey yo, I'm just like my country I'm young, scrappy and hungry And I'm not throwin' away my shot I am not throwin' away my shot I am not throwin' away my shot Hey yo, I'm just like my country I'm young, scrappy and hungry And I'm not throwin' away my shot Everybody sing Whoa, whoa, whoa Ayy, whoa (woo), whoa Should let 'em hear ya (yeah) Let's go Whoa, whoa, whoa I said shout it to the rooftops Whoa, whoa, whoa Said, to the rooftops Whoa, whoa, whoa A-come on (yeah) Come on, let's go Rise up When you're living on your knees, you rise up Tell your brother that he's gotta rise up Tell your sister that she's gotta rise up When are these colonies gonna rise up? (Whoa, whoa) When are these colonies gonna rise up? (Whoa) When are these colonies gonna rise up? (Whoa) When are these colonies gonna rise up? Rise upI imagine death so much it feels more like a memoryWhen's it gonna get me? In my sleep, seven feet ahead of me? If I see it comin', do I run or do I let it be? Is it like a beat without a melody? See, I never thought I'd live past twenty Where I come from some get half as manyAsk anybody why we livin' fast and we laugh, reach for a flask We have to make this moment last, that's plenty Scratch that this is not a moment, it's the movement Where all the hungriest brothers with something to prove went?Foes oppose us, we take an honest stand We roll like Moses, claimin' our promised land And? If we win our independence? Is that a guarantee of freedom for our descendants?Or will the blood we shed begin an endless cycle of vengeance and death with no defendants? I know the action in the street is excitin' But Jesus, between all the bleedin' 'n' fightin' I've been readin' 'n' writin'We need to handle our financial situation Are we a nation of states what's the state of our nation? I'm past patiently waitin' I'm passionately mashin' every expectation Every action's an act of creation I'm laughin' in the face of casualties and sorrowFor the first time, I'm thinkin' past tomorrow And I am not throwin' away my shot I am not throwin' away my shot Hey yo, I'm just like my country I'm young, scrappy and hungry And I'm not throwin' away my shot We're gonna rise up (time to take a shot) I am not throwin' away my shot We're gonna rise up (time to take a shot) I am not throwin' away my shot We're gonna, rise up, rise up It's time to take a shot Rise up, rise up It's time to take a shot Rise up, it's time to take a shot Rise up, take a shot, shot, shot It's time to take a shot, time to take a shotAnd I am not throwin' away my Not throwin' away my shot"

# Accept the challenge
print ()
print ("Okay.  I will now compress this message.")
print (phrase)

# Create a frequency table
frequency = []
entries = 0
letters = 0

for letter in phrase:
    letters = letters + 1
    found = False
    for counter in range(entries):
        if frequency[counter][0] == letter:
            frequency[counter][1] = frequency[counter][1]+1
            found = True
    if not found:
        frequency.append([letter,1])
        entries = entries+1
        
# Update the user
differentSymbols = entries
print ()
print ("I found %d different symbols." % differentSymbols)
print ()
print ("This is the frequency table.")
for counter in range(differentSymbols):
    print (frequency[counter][0], frequency[counter][1])

# Implement Huffman encoding

# create the two main lists: lonely circles, and connected circles
lonely = []
connected = []

# establish the list of lonely circles
for counter in range(entries):
    lonely.append([frequency[counter][0],frequency[counter][1], "not used"])

# round and round, find the two least frequent lonely circles

finished = False
newCircleCount = 0

while not finished:

    lowestFrequency = 999999
    secondLowestFrequency = 1000000
    lowestFrequencyPosition = 999999

    for counter in range(entries):
        if lonely[counter][2]=="not used":
            if lonely[counter][1]<lowestFrequency:
                secondLowestFrequency = lowestFrequency
                secondLowestFrequencyPosition = lowestFrequencyPosition
                lowestFrequency = lonely[counter][1]
                lowestFrequencyPosition = counter
            elif lonely[counter][1]<secondLowestFrequency:
                secondLowestFrequency = lonely[counter][1]
                secondLowestFrequencyPosition = counter

    if secondLowestFrequency != 999999:
        
        # we found two more lonely circles
        # make a new circle to join them
        newCircleCount = newCircleCount + 1
        newCircleFrequency = lonely[lowestFrequencyPosition][1] + lonely[secondLowestFrequencyPosition][1]
        
        # mark them as used
        lonely[lowestFrequencyPosition][2]="used"
        lonely[secondLowestFrequencyPosition][2]="used"
        
        # move them to the connected list, attached to the new circle
        connected.append([lonely[lowestFrequencyPosition][0],"left",newCircleCount])
        connected.append([lonely[secondLowestFrequencyPosition][0],"right",newCircleCount])

        # add the new circle to the lonely list
        lonely.append([newCircleCount, newCircleFrequency, "not used"])
        entries = entries + 1

    else:
        # we are done!
        # move the remaining circle to the connected list
        connected.append([lonely[lowestFrequencyPosition][0],"finished",lonely[lowestFrequencyPosition][1]])
        finished = True

print ()
print ("This is the Huffman Tree.")
print ("Letter or Circle - Left or Right - Parent")
print ()
for counter in range(entries):
    print (connected[counter][0],connected[counter][1],connected[counter][2])
    
# report the new codes

newCodes = []

# go symbol by symbol, using the original frequency chat as a guide
for symbolNumber in range(differentSymbols):

    # store the Huffman code for this symbol here
    thisCode = ""
    lengthCode = 0

    # now, go through the list of connected circles
    for counter in range(entries):
        if connected[counter][0] == frequency[symbolNumber][0]:
            # found this letter in connected list
            pointer = counter
            while connected[pointer][1]!="finished":
                lengthCode = lengthCode + 1
                if connected[pointer][1]=="left":
                    thisCode = thisCode + "0"
                else:
                    thisCode = thisCode + "1"
                nextCircle = connected[pointer][2]
                for counter2 in range(entries):
                    if connected[counter2][0] == nextCircle:
                        pointer = counter2
                
    # remember this symbol and its code
    newCodes.append([frequency[symbolNumber][0], thisCode, lengthCode, frequency[symbolNumber][1]])

print ()
print ("These are the compressed codes.")
print ("Letter - Code - Length - Frequency")
print ()
for counter in range(differentSymbols):
    print (newCodes[counter][0], newCodes[counter][1], newCodes[counter][2], newCodes[counter][3])

# calculate compression

print ()
print ("Using 6-digit codes, we'd need %d digits." % (letters*6))

totalDigits = 0
for counter in range(differentSymbols):
    totalDigits = totalDigits + newCodes[counter][3] * newCodes[counter][2]

print ("Using variable-length Huffman Encoding, we need %d digits." % totalDigits)
print ()