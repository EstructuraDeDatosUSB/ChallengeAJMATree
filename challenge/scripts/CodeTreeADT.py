class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class CodeTreeADT:
    def __init__(self, morse=False, binary=False):
        self.root = Node("")
        self.morse = morse
        self.binary = binary

        if self.morse:
            self.load_morse()
        elif self.binary:
            self.load_binary()

    def _recursive_add(self, node, code, char):
        left_code = ""
        if self.morse:
            left_code = "."
        elif self.binary:
            left_code = "0"

        if len(code) == 0:
            node.data = char
            return
        if code[0] == left_code:
            if node.left is None:
                node.left = Node("")
            self._recursive_add(node.left, code[1:], char)
        else:
            if node.right is None:
                node.right = Node("")
            self._recursive_add(node.right, code[1:], char)

    def add(self, code, char):
        self._recursive_add(self.root, code, char)

    def _recursive_search(self, node, code):
        left_code = ""
        if self.morse:
            left_code = "."
        elif self.binary:
            left_code = "0"

        if node is None:
            return "?"

        if len(code) == 0:
            return node.data
        if code[0] == left_code:
            return self._recursive_search(node.left, code[1:])
        else:
            return self._recursive_search(node.right, code[1:])

    def search(self, code):
        return self._recursive_search(self.root, code)

    def _recursive_reverse_search(self, node, char):
        left_code = ""
        right_code = ""

        if self.morse:
            left_code = "."
            right_code = "-"
        elif self.binary:
            left_code = "0"
            right_code = "1"

        if node is None:
            return None
        if node.data == char:
            return ""
        left = self._recursive_reverse_search(node.left, char)
        if left is not None:
            return left_code + left
        right = self._recursive_reverse_search(node.right, char)
        if right is not None:
            return right_code + right
        return None

    def reverse_search(self, char):
        return self._recursive_reverse_search(self.root, char)

    def _recursive_height(self, node):
        if node is None:
            return 0

        left = self._recursive_height(node.left)
        right = self._recursive_height(node.right)
        return 1 + max(left, right)

    def height(self):
        return self._recursive_height(self.root)

    def encode(self, message):
        encoded = ""
        for char in message:
            if self.morse and char == " ":
                encoded += "/" + " "
            else:
                if self.morse:
                    char = char.upper()
                code = self.reverse_search(char)
                if code is not None:
                    encoded += code + " "
        return encoded

    def decode(self, message):
        decoded = ""
        codes = message.split()
        for code in codes:
            if self.morse and code == "/":
                decoded += " "
            else:
                char = self.search(code)
                if char is not None:
                    decoded += char
                else:
                    continue
        return decoded

    def load_morse(self):
        self.add(".-", "A")
        self.add("-...", "B")
        self.add("-.-.", "C")
        self.add("-..", "D")
        self.add(".", "E")
        self.add("..-.", "F")
        self.add("--.", "G")
        self.add("....", "H")
        self.add("..", "I")
        self.add(".---", "J")
        self.add("-.-", "K")
        self.add(".-..", "L")
        self.add("--", "M")
        self.add("-.", "N")
        self.add("---", "O")
        self.add(".--.", "P")
        self.add("--.-", "Q")
        self.add(".-.", "R")
        self.add("...", "S")
        self.add("-", "T")
        self.add("..-", "U")
        self.add("...-", "V")
        self.add(".--", "W")
        self.add("-..-", "X")
        self.add("-.--", "Y")
        self.add("--..", "Z")
        self.add(".----", "1")
        self.add("..---", "2")
        self.add("...--", "3")
        self.add("....-", "4")
        self.add(".....", "5")
        self.add("-....", "6")
        self.add("--...", "7")
        self.add("---..", "8")
        self.add("----.", "9")
        self.add("-----", "0")
        self.add(".-.-.-", ".")
        self.add("--..--", ",")
        self.add("..--..", "?")
        self.add(".----.", "'")
        self.add("-.-.--", "!")
        self.add("-..-.", "/")
        self.add("-.--.", "(")
        self.add("-.--.-", ")")
        self.add(".-...", "&")
        self.add("---...", ":")
        self.add("-.-.-.", ";")
        self.add("-...-", "=")
        self.add(".-.-.", "+")
        self.add("-....-", "-")
        self.add("..--.-", "_")
        self.add(".-..-.", '"')
        self.add(".--.-.", "@")

    def load_binary(self):
        self.add("01000001", "A")
        self.add("01000010", "B")
        self.add("01000011", "C")
        self.add("01000100", "D")
        self.add("01000101", "E")
        self.add("01000110", "F")
        self.add("01000111", "G")
        self.add("01001000", "H")
        self.add("01001001", "I")
        self.add("01001010", "J")
        self.add("01001011", "K")
        self.add("01001100", "L")
        self.add("01001101", "M")
        self.add("01001110", "N")
        self.add("01001111", "O")
        self.add("01010000", "P")
        self.add("01010001", "Q")
        self.add("01010010", "R")
        self.add("01010011", "S")
        self.add("01010100", "T")
        self.add("01010101", "U")
        self.add("01010110", "V")
        self.add("01010111", "W")
        self.add("01011000", "X")
        self.add("01011001", "Y")
        self.add("01011010", "Z")

        self.add("01100001", "a")
        self.add("01100010", "b")
        self.add("01100011", "c")
        self.add("01100100", "d")
        self.add("01100101", "e")
        self.add("01100110", "f")
        self.add("01100111", "g")
        self.add("01101000", "h")
        self.add("01101001", "i")
        self.add("01101010", "j")
        self.add("01101011", "k")
        self.add("01101100", "l")
        self.add("01101101", "m")
        self.add("01101110", "n")
        self.add("01101111", "o")
        self.add("01110000", "p")
        self.add("01110001", "q")
        self.add("01110010", "r")
        self.add("01110011", "s")
        self.add("01110100", "t")
        self.add("01110101", "u")
        self.add("01110110", "v")
        self.add("01110111", "w")
        self.add("01111000", "x")
        self.add("01111001", "y")
        self.add("01111010", "z")

        self.add("00110001", "1")
        self.add("00110010", "2")
        self.add("00110011", "3")
        self.add("00110100", "4")
        self.add("00110101", "5")
        self.add("00110110", "6")
        self.add("00110111", "7")
        self.add("00111000", "8")
        self.add("00111001", "9")
        self.add("00110000", "0")
        self.add("00101110", ".")
        self.add("00101100", ",")
        self.add("00111111", "?")
        self.add("00100111", "'")
        self.add("00100001", "!")
        self.add("00101111", "/")
        self.add("00101000", "(")
        self.add("00101001", ")")
        self.add("00100110", "&")
        self.add("00111010", ":")
        self.add("00111011", ";")
        self.add("00111101", "=")
        self.add("00101011", "+")
        self.add("00101101", "-")
        self.add("00101111", "_")
        self.add("00100010", '"')
        self.add("01000000", "@")
        self.add("00100000", " ")
