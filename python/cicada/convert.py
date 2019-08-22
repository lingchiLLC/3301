from cicada import alphabets


class ConvertBase(object):
    def __init__(
            self, *,
            source, target,
            alphabet=alphabets.en_digits_upper_lower
    ):
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
