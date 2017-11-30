def enigma(inputString, r1, r2, r3):

    # rotor strings
    palpha = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    rotor1 = list("BDFHJLCPRTXVZNYEIWGAKMUSQO")
    rotor2 = list("AJDKSIRUXBLHWTMCQGZNPYFVOE")
    rotor3 = list("EKMFLGDQVZNTOWYHXUSPAIBRCJ")
    reflec = list("YRUHQSLDPXNGOKMIEBFZCWVJAT")

    # initial rotor settings
    """
    r1 = int(input("Rotor 1: ")) % 26
    r2 = int(input("Rotor 2: ")) % 26
    r3 = int(input("Rotor 3: ")) % 26
    r1 = 0
    r2 = 0
    r3 = 0
    """

    # align rotors to settings
    if r1 != 0:
        rotor1 = arrayRotate(rotor1, r1)
    if r2 != 0:
        rotor2 = arrayRotate(rotor2, r2)
    if r3 != 0:
        rotor3 = arrayRotate(rotor3, r3)

    # TODO: take input from argument
    plaintext = ""
    for c, i in enumerate(inputString):
        if i.isalpha():
            plaintext += i.upper()

    ciphertext = ""

    # encipher input
    for c, i in enumerate(plaintext):

        # turn rotors
        rotor1 = arrayRotate(rotor1, 1)
        r1 = (r1 + 1) % 26
        if rotor1 == 26:
            rotor2 = arrayRotate(rotor2, 1)
            r2 = (r2 + 1) % 26
            if rotor2 == 26:
                rotor3 = arrayRotate(rotor3, 1)

        # passthrough
        c1 = rotorPass(rotor1, i)
        c2 = rotorPass(rotor2, c1)
        c3 = rotorPass(rotor3, c2)
        ref = rotorPass(reflec, c3)
        c4 = palpha[rotor3.index(ref)]
        c5 = palpha[rotor2.index(c4)]
        c6 = palpha[rotor1.index(c5)]

        ciphertext += c6

    return ciphertext


""" FUNCTIONS """

def arrayRotate(l, n):
    return l[n:] + l[:n]  

def rotorPass(rotor, n):
    i = ord(n) - 65
    return rotor[i]
