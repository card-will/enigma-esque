alpha = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
plugboard = alpha[:]
rotor1 = alpha[:]
rotor2 = alpha[:]
rotor3 = alpha[:]
wire1 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
wire2 = wire1[:]
wire3 = wire1[:]
wire1inverted = wire1[:]
wire2inverted = wire1[:]
wire3inverted = wire1[:]
rotor1count = 0
rotor2count = 0
reflector = alpha[:]
plugboardChecker = ["_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_"]
rotor1Checker = plugboardChecker[:]
rotor2Checker = plugboardChecker[:]
rotor3Checker = plugboardChecker[:]


def rotate(l):
    global rotor1count
    global rotor2count
    l.insert(0, l[-1])
    l.pop()
    if l == wire1:
        rotor1count += 1
        rotate(wire1inverted)
        print("rotating wire 1")
    if l == wire2:
        rotate(wire2inverted)
        rotor2count = rotor2count + 1
        print("rotating wire 2")
    if l == wire3:
        rotate(wire3inverted)
        print("rotating wire 3")

def checkApplyRotation(rotor):
    global rotor1count
    global rotor2count
    if rotor == 2:
        print("rotoating rotor", rotor," ", rotor1count % 26, " time(s)")
        for i in range(rotor1count % 26):
            rotate(wire2)
            rotate(wire2inverted)
    elif rotor == 3:
        print("rotating rotor", rotor, " ", rotor1count % 676, " time(s)")
        for i in range(rotor1count % 676):
            rotate(wire3)
            rotate(wire3inverted)
    else:
        print("Input of checkApplyRotation is wrong")
def plugboardSetup():
    if input("Changes to plugboard? y/n") == "n":
        print("No changes to plugboard")
    else:
        for i in range(26):
            try:
                plugboardChecker.index(plugboard[i])
                print("Already established ", plugboard[i], " is connected to", alpha[i])
            except:
                placeholder = input("What would you like to connect " + plugboard[i] + " to?").upper()
                try:
                    plugboardChecker.index(placeholder)
                    print("plug already used, default no connection")
                    plugboardChecker[i] = plugboard[i]
                    pass
                except:
                    if placeholder == "" or placeholder.isalpha() == False:
                        plugboardChecker[i] = plugboard[i]
                        print(*plugboard, "\n No connection")
                    else:
                        plugboard[alpha.index(placeholder)]=plugboard[i]
                        plugboard[i] = placeholder
                        plugboardChecker[i] = placeholder
                        plugboardChecker[alpha.index(placeholder)] = plugboard[alpha.index(placeholder)]
                        print(*plugboard, ": plugboard")
                        print(*plugboardChecker, ": plugboard checker")
            print(*alpha)
            print(*plugboard)
            
def rotor1Build():
    print("Rotor 1 building")
    for i in range(26):
        while True:
            setKey = input(rotor1[i] + ":")
            if setKey == "":
                rotor1Checker.append(setKey.upper())
                wire1[i] = 0
                break
            elif len(setKey) > 1 or setKey == " ":
                print("That is not a single letter.")
                #use later for input
            elif setKey.isalpha() == False:
                print("That is not a letter")
            elif setKey.upper() in rotor1Checker:
                e = rotor1Checker.index(setKey.upper())
                print("That plug has already been used by wire " + alpha[e]) # add which wire later
            else:
                rotor1Checker[i]= setKey.upper()
                rotor1[i] = setKey.upper()
                t = alpha.index(setKey.upper())-i
                wire1[i]=t % 26
                wire1inverted[alpha.index(setKey.upper())]= (i-alpha.index(setKey.upper())) % 26
                print(*alpha)
                print(*rotor1)
                print(rotor1Checker)
                print(*wire1)
                print(*wire1inverted)
                break

def rotor2Build():
    print("Rotor 2 building")
    for i in range(26):
        while True:
            setKey = input(rotor2[i] + ":")
            if setKey == "":
                rotor2Checker.append(setKey.upper())
                wire2.append(0)
                break
            elif len(setKey) > 1 or setKey == " ":
                print("That is not a single letter.")
                #use later for input
            elif setKey.isalpha() == False:
                print("That is not a letter")
            elif setKey.upper() in rotor2Checker:
                e = rotor2Checker.index(setKey.upper())
                print("That plug has already been used by wire " + alpha[e]) # add which wire later
            else:
                rotor2Checker[i]= setKey.upper()
                rotor2[i] = setKey.upper()
                t = alpha.index(setKey.upper())-i
                wire2[i]=t % 26
                wire2inverted[alpha.index(setKey.upper())]= (i-alpha.index(setKey.upper())) % 26
                print(*rotor2)
                print(rotor2Checker)
                print(*wire2)
                break
def rotor3Build():
    print("Rotor 2 building")
    for i in range(26):
        while True:
            setKey = input(rotor3[i] + ":")
            if setKey == "":
                rotor3Checker.append(setKey.upper())
                wire3.append(0)
                break
            elif len(setKey) > 1 or setKey == " ":
                print("That is not a single letter.")
                #use later for input
            elif setKey.isalpha() == False:
                print("That is not a letter")
            elif setKey.upper() in rotor3Checker:
                e = rotor3Checker.index(setKey.upper())
                print("That plug has already been used by wire " + alpha[e]) # add which wire later
            else:
                rotor3Checker[i]= setKey.upper()
                rotor3[i] = setKey.upper()
                t = alpha.index(setKey.upper())-i
                wire3[i]=t % 26
                wire3inverted[alpha.index(setKey.upper())]= (i-alpha.index(setKey.upper())) % 26
                print(*rotor3)
                print(rotor3Checker)
                print(*wire3)
                break

def reflectorSetup():
    for i in range(26):
        reflector[25-i] = alpha[i]
        print(*reflector)
        



def encoding(message):
    global rotor1count
    global rotor2count
    print("Encoding " + message)
    message = list(message.upper())
    encoded = ""
    for i in range(len(message)):
        if message[i].isalpha():
            PBout = plugboard[alpha.index(message[i])]
            print("plugboard output: " + PBout)
            rotate(wire1)

            R1 = alpha[(alpha.index(PBout) + wire1[alpha.index(PBout)]) % 26]
            print("output of rotor 1 is" + R1)
            if rotor1count == 26:
                rotate(wire2)
                print("rotated wire2")
                rotor1count = 1
                rotor2count = rotor2count + 1
                # check
            R2 = (alpha.index(R1) + wire2[alpha.index(R1)]) % 26
            print("output rotor 2: " + alpha[R2])
            if rotor2count == 26:
                rotate(wire3)
                print("rotated wire3")
                rotor3count = rotor3count + 1
                rotor2count = 1
                # check
            R3 = (R2 + wire3[R2]) % 26
            # rotor 2 ? x = rotor2[rotor1[alpha.index(plugboard[alpha.index(message[i])])]]
            #x = (alpha.index(x) + wire3[alpha.index(message[i])]) % 26
            print("output rotor3: " + alpha[R3])
            ref = reflector[R3]
            print("output reflector: " + ref)
            R3I = (alpha.index(ref) + wire3inverted[alpha.index(ref)]) % 26
            print("output 2 rotor 3: " + alpha[R3I])
            R2I = (R3I + wire2inverted[R3I]) % 26
            print("output 2 rotor 2: " + alpha[R2I])
            R1I = (R2I + wire1inverted[R2I]) % 26
            print("output 2 rotor 1: " + alpha[R1I])
            PBout2 = plugboard[R1I]
            print("PB output 2: " + PBout2)
            encoded += PBout2
        else:
            encoded += message[i]
    return encoded
            


print(plugboard)
print(*plugboard)
plugboardSetup()
rotor1Build()
rotor2Build()
rotor3Build()
reflectorSetup()
print(plugboard)
print(rotor1)
print(rotor2)
print(rotor3)
inp = input("encode")
end = encoding(inp)
print(end)




