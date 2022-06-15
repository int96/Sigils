newSpell = "MPRCD"
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
    print("cSpell: ", *cSpell)           # debug