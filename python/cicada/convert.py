from cicada import alphabets


class ConvertBase(object):
    '''Convert numbers of one base to another.

    Args:
        source (int): Source base.
        target (int): Target base.
        alphabet (str): An ordered list of characters used to represent the
            numbers. Defaults to 0-9A-Za-z
    '''

    def __init__(
            self, *,
            source, target,
            alphabet=alphabets.en_digits_upper_lower
    ):
        self.sourceAlphabet = alphabet[:source]
        self.targetAlphabet = alphabet[:target]
        self.sourceBase = source
        self.targetBase = target

    def convert(self, num):
        '''Perform convert.


        Args:
            num (str): A string or stringable value to be converted.

        Returns:
            string: num in target base.
        '''
        sourceDigits = [self.sourceAlphabet.index(i) for i in str(num)]

        number = 0
        for digit in sourceDigits:
            number = self.sourceBase * number + digit

        targetDigits = []
        while number > 0:
            targetDigits.insert(0, number % self.targetBase)
            number = number // self.targetBase

        return ''.join([self.targetAlphabet[d] for d in targetDigits]) or '0'
