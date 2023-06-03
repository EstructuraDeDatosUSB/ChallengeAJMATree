import unittest
from challenge.scripts.CodeTreeADT import CodeTreeADT


class TestCodeTreeADT(unittest.TestCase):
    def setUp(self):
        self.morse_tree = CodeTreeADT(morse=True)
        self.binary_tree = CodeTreeADT(binary=True)
        self.morse_tree.load_morse()
        self.binary_tree.load_binary()

    def test_add(self):
        self.assertEqual(self.morse_tree.search('...'), 'S')
        self.assertEqual(self.morse_tree.search('---'), 'O')
        self.assertEqual(self.morse_tree.search('..-'), 'U')
        self.assertEqual(self.morse_tree.search('..'), 'I')
        self.assertEqual(self.binary_tree.search('01000001'), 'A')
        self.assertEqual(self.binary_tree.search('01000010'), 'B')
        self.assertEqual(self.binary_tree.search('01000011'), 'C')
        self.assertEqual(self.binary_tree.search('01000100'), 'D')

    def test_encode(self):
        self.assertEqual(self.morse_tree.encode('SOS'), '... --- ...')
        self.assertEqual(self.morse_tree.encode('SOS SOS'), '... --- ... / ... --- ...')
        self.assertEqual(self.morse_tree.encode('SOS SOS SOS'), '... --- ... / ... --- ... / ... --- ...')
        self.assertEqual(self.binary_tree.encode('ABCD'), '01000001 01000010 01000011 01000100')
        self.assertEqual(self.binary_tree.encode('ABCD ABCD'), '01000001 01000010 01000011 01000100 00100000 01000001 01000010 01000011 01000100')
        self.assertEqual(self.binary_tree.encode('ABCD ABCD ABCD'), '01000001 01000010 01000011 01000100 00100000 01000001 01000010 01000011 01000100 00100000 01000001 01000010 01000011 01000100')


    def test_decode(self):
        self.assertEqual(self.morse_tree.decode('... --- ...'), 'SOS')
        self.assertEqual(self.morse_tree.decode('... --- ... / ... --- ...'), 'SOS SOS')
        self.assertEqual(self.morse_tree.decode('... --- ... / ... --- ... / ... --- ...'), 'SOS SOS SOS')
        self.assertEqual(self.binary_tree.decode('01000001 01000010 01000011 01000100'), 'ABCD')
        self.assertEqual(self.binary_tree.decode('01000001 01000010 01000011 01000100 00100000 01000001 01000010 01000011 01000100'), 'ABCD ABCD')
        self.assertEqual(self.binary_tree.decode('01000001 01000010 01000011 01000100 00100000 01000001 01000010 01000011 01000100 00100000 01000001 01000010 01000011 01000100'), 'ABCD ABCD ABCD')


