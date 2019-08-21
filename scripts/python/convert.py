from string import (
    ascii_lowercase,
    ascii_uppercase,
    digits
)

ALPHABET = digits + ascii_uppercase + ascii_lowercase

class ConvertBase(object):
    def __init__(self, *, source, target, alphabet=ALPHABET):
        self.sourceAlphabet = alphabet[:source]
        self.targetAlphabet = alphabet[:target]
        self.sourceBase = source
        self.targetBase = target

    def convert(self, x):
        sourceDigits = [self.sourceAlphabet.index(i) for i in str(x)]

        number = 0
        for digit in sourceDigits:
            number = self.sourceBase * number + digit

        targetDigits = []
        while number > 0:
            targetDigits.insert(0, number % self.targetBase)
            number = number // self.targetBase

        return ''.join([self.targetAlphabet[d] for d in targetDigits]) or '0'
