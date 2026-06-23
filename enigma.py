class Enigma:
    rotors: list[list[str]]
    reflector: list[str]
    rotor_offsets: list[int]

    def __init__(self, rotor_offsets: list[int]):
        self.rotors = [
            list("BDFHJLCPRTXVZNYEIWGAKMUSQO"),
            list("AJDKSIRUXBLHWTMCQGZNPYFVOE"),
            list("EKMFLGDQVZNTOWYHXUSPAIBRCJ"),
        ]
        self.reflector = list("YRUHQSLDPXNGOKMIEBFZCWVJAT")
        self.rotor_offsets = [offset % 26 for offset in rotor_offsets]

        # apply offsets
        for i, offset in enumerate(rotor_offsets):
            self.rotors[i] = self._rotate(self.rotors[i], offset)

    @staticmethod
    def _index_of(char: str) -> int:
        return ord(char) - 65

    @staticmethod
    def _char_at(index: int) -> str:
        return chr(index + 65)

    @staticmethod
    def _rotate(rotor: list[str], offset: int) -> list[str]:
        return rotor[offset:] + rotor[:offset]

    def _rotor_move(self, index: int = 0):
        rotate_next = self.rotor_offsets[index] >= 25

        self.rotors[index] = self._rotate(self.rotors[index], 1)
        self.rotor_offsets[index] = (self.rotor_offsets[index] + 1) % 26

        if rotate_next:
            self._rotor_move(index + 1)

    def encipher(self, input_string: str):
        ciphertext = []

        for char in input_string.upper():
            self._rotor_move()

            # forward pass through rotors
            # finds position in next row using index of char in current
            after_r1 = self.rotors[0][self._index_of(char)]
            after_r2 = self.rotors[1][self._index_of(after_r1)]
            after_r3 = self.rotors[2][self._index_of(after_r2)]

            # reverse direction
            after_reflector = self.reflector[self._index_of(after_r3)]

            # finds position in next row by finding char at position of index in current
            back_r3 = self._char_at(self.rotors[2].index(after_reflector))
            back_r2 = self._char_at(self.rotors[1].index(back_r3))
            back_r1 = self._char_at(self.rotors[0].index(back_r2))

            ciphertext.append(back_r1)

        return "".join(ciphertext)


if __name__ == "__main__":
    enigma = Enigma([1, 2, 7])
    result = enigma.encipher("A")
    print(result)
