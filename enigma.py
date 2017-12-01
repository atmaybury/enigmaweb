def enigma(inputString, rotorPos):

    # rotor strings
    # TODO: make loop to retrieve from db
    palpha = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    rotor1 = list("BDFHJLCPRTXVZNYEIWGAKMUSQO")
    rotor2 = list("AJDKSIRUXBLHWTMCQGZNPYFVOE")
    rotor3 = list("EKMFLGDQVZNTOWYHXUSPAIBRCJ")
    reflec = list("YRUHQSLDPXNGOKMIEBFZCWVJAT")

    rotors = []
    rotors.append(rotor1)
    rotors.append(rotor2)
    rotors.append(rotor3)

    for c, i in enumerate(rotorPos):
        if i != 0:
            rotors[c] = arrayRotate(rotors[c], i)

    plaintext = ""
    for c, i in enumerate(inputString):
        if i.isalpha():
            plaintext += i.upper()

    ciphertext = ""

    # encipher input
    for c, i in enumerate(plaintext):

        # turn rotors
        # TODO: make method to rotate and check next until :-1
        rotors[0] = arrayRotate(rotors[0], 1)
        rotorPos[0] = (rotorPos[0] + 1) % 26
        if rotorPos[0] == 26:
            rotors[1] = arrayRotate(rotors[1], 1)
            rotorPos[1] = (rotorPos + 1) % 26
            if rotorPos[1] == 26:
                rotors[2] = arrayRotate(rotors[2], 1)

        # passthrough
        c1 = rotorPass(rotors[0], i)
        c2 = rotorPass(rotors[1], c1)
        c3 = rotorPass(rotors[2], c2)
        ref = rotorPass(reflec, c3)
        c4 = palpha[rotors[2].index(ref)]
        c5 = palpha[rotors[1].index(c4)]
        c6 = palpha[rotors[0].index(c5)]

        ciphertext += c6

    return ciphertext


""" FUNCTIONS """

def arrayRotate(l, n):
    return l[n:] + l[:n]  

def rotorPass(rotor, n):
    i = ord(n) - 65
    return rotor[i]
