'''
Sigil.py

ToDo:
[] be nice if check for duplicates was a function call
[] check for other characters besides alphabet and remove them
'''
# imports
import random

''' F U N C T I O N S '''
### title()
# SPLASH TITLE
def title():
    print("*****************************\n")
    print("Sigil.py\n")
    print("*****************************\n")
    print("\n")
    print("Please enter letters only for your phrases\n")
    print("Do not use any punctuation at all.\n")
    print("Phrases are not case sensitive.\n")

### left
# returns from the left the amount
def left(phrase, amount):
    return phrase[:amount]

### right
# returns from the right the amount
def right(phrase, amount):
    return phrase[-amount:]

### mid
# returns from left the amount of characters
def mid(phrase, offset, amount):
    return phrase[offset:offset+amount]

### rmSpc
# remove the spaces from the phrase
def rmSpc(phrase):
    return phrase.replace(" ", "")

### checkVowels
# check for vowels
def checkVowels(mlet):
# check the string contains vowels
   for char in mlet:
      if char in 'AEIOU':
         return True
   return False

### cypher phrase
# M A G I C K #
def cypher(phrase):
    # remove spaces from phrase
    phrase = rmSpc(phrase)
#    print("phrase: ", phrase)           # debug
    
    # count letters in phrase
    pLen = len(phrase)
    
#    print("*** phrase: ", phrase)       # debug
#    print("*** pLen: ", pLen)           # debug
    
    # leaveing out "vowels"
#    vowels = ['A', 'E', 'I', 'O', 'U']     # leaving for a better check sum coded later
    spell = ''
    for i in range(0, pLen):
        mlet = mid(phrase, i, 1)
#        print("*** mlet: ", mlet)       # debug

        if checkVowels(mlet) == False:
            spell += mlet
    print("*** spell: ", spell)         # debug
        
    # leaveing out "doubles"
    duplicates = []
    newSpell = ''
    for char in spell:
    ## checking whether the character have a duplicate or not
    ## str.count(char) returns the frequency of a char in the str
        if spell.count(char) > 1:
            ## appending to the list if it's already not present
            if char not in duplicates:
                duplicates.append(char)
    print("*** duplicates: ", *duplicates)  # debug

    for char in spell:
#        print("*** char ", char)            # debug
        if char not in duplicates:
            newSpell = newSpell + char
    print("*** newSpell: ", newSpell)       # debug

    # cypher the letters in array
    cSpell = []
    for char in newSpell:
        if char == 'A' or char == 'J' or char == 'S': 
            if char not in cSpell:
                cSpell.append('1')
        elif char == 'B' or char == 'K' or char == 'T': 
            if char not in cSpell:
                cSpell.append('2')
        elif char == 'C' or char == 'L' or char == 'U': 
            if char not in cSpell:
                cSpell.append('3')
        elif char == 'D' or char == 'M' or char == 'V':
            if char not in cSpell:
                cSpell.append('4')
        elif char == 'E' or char == 'N' or char == 'W':
            if char not in cSpell:
                cSpell.append('5')
        elif char == 'F' or char == 'O' or char == 'X':
            if char not in cSpell:
                cSpell.append('6')
        elif char == 'G' or char == 'P' or char == 'Y': 
            if char not in cSpell:
                cSpell.append('7')
        elif char == 'H' or char == 'Q' or char == 'Z':
            if char not in cSpell: 
                cSpell.append('8')
        elif char == 'I' or char == 'R':
            if char not in cSpell: 
                cSpell.append('9')
    print("*** cSpell: ", *cSpell)           # debug

    # leaving out "doubles" cypher2 = "7,9,3"
    duplicates = []
    fSpell = ''
    for char in cSpell:
    ## checking whether the character have a duplicate or not
    ## str.count(char) returns the frequency of a char in the str
        if cSpell.count(char) > 1:
            ## appending to the list if it's already not present
            if char not in duplicates:
                duplicates.append(char)
    print("*** duplicates: ", *duplicates)  # debug

    for char in cSpell:
#        print("*** char ", char)            # debug
        if char not in duplicates:
            fSpell = fSpell + char    
    print("*** fSpell: ", fSpell)       # debug
    
    # Re-order cypher2 smallest number to biggest number ie [7,9,3] = [3,7,9]
    spell = []
    pLen = len(fSpell)
    for i in range(0, pLen):
        mlet = mid(fSpell, i, 1)
        spell.append(mlet)
        
    spell.sort()
    print("*** spell: ", *spell)         # debug
    
    # use one of the 8 magick squares
        # [8,1,6]
        # [3,5,7]
        # [4,9,2]
        
        # [6,1,8]
        # [7,5,3]
        # [2,9,4]
        
        # [4,9,2]
        # [3,5,7]
        # [8,1,6]
        
        # [2,9,4]
        # [7,5,3]
        # [6,1,8]
        
        # [8,3,4]
        # [1,5,9]
        # [6,7,2]
        
        # [4,3,8]
        # [9,5,1]
        # [2,7,6]
        
        # [6,7,2]
        # [1,5,9]
        # [8,3,4]
        
        # [2,7,6]
        # [9,5,1]
        # [4,3,8]
    used = []
    num = random.randrange(1,9)
    
    if num not in used :
        used.append(num)
    
        # bold, highlight,or color the cypher-array numbers in grid # example would be 3 and 7
            # could use ascii to just print over the original text
            # o = begining of cast, x = end of cast # example from above
                # could look into doing basic screen graphics to
                # draw the casting lines.
        # example
        # [#,o,#]
        # [-,-,x]
        # [#,#,#]
        # example using 1234
        # [#,┌,x]
        # [#,|,#]
        # [#,#,o]

''' Main Execution '''
# Splash that title!
title()

# ask user for phrase
phrase = input("Phrase: ")
phrase = phrase.upper()
cypher(phrase)