from cicada import alphabets


class Cipher(object):
    '''Base cipher class.

        Notes:
        * Every character in your text must be in self.alphabet.
        * `key` is an absolute value.
    '''
    def __init__(self, *, alphabet=alphabets.en_upper):
        self.alphabet = alphabet

    def encode(self, *, plaintext, key):
        '''Encode plaintext with key.

        Args:
            plaintext (str): The text to encode.
            key (int): Number of letters to shift.
        '''
        raise NotImplementedError()

    def decode(self, *, ciphertext, key):
        '''Decode ciphertext with key.

        Args:
            ciphertext (str): Some message to decode.
            key (int): Number of letters to shift.
        '''
        raise NotImplementedError()


class CaesarCipher(Cipher):
    '''Basic Caesar cipher ops.'''
    def _shift(self, text, key):
        '''Helper to shift through an alphabet.'''
        alpha_len = len(self.alphabet)
        new_text = ''

        for char in text:
            char_index = self.alphabet.index(char)  # 6
            shift_index = char_index + key  # 11 + -20 = -9

            if shift_index > alpha_len:
                shift_index -= alpha_len
            elif shift_index < 0:
                shift_index += alpha_len
            new_text += self.alphabet[shift_index]

        return new_text

    def encode(self, *, plaintext, key):
        return self._shift(plaintext, key)

    def decode(self, *, ciphertext, key):
        return self._shift(ciphertext, -1 * key)


class VigenereCipher(Cipher):
    def _shift_keys(self, key, start_at):
        '''Get position indexes of key letters in alphabet.'''
        shift_keys = []

        for char in key:
            start_index = (
                char + self.alphabet.index(start_at)
                if start_at
                else 0
            )
            key_index = self.alphabet.index(char)
            shift_key = key_index - start_index
            shift_keys.append(shift_key)

        return shift_keys

    def _shift(self, text, shift_keys):
        '''Just call Caesar on each letter.'''
        new_text = ''
        key_index = 0

        for char in text:
            key = shift_keys[key_index]
            new_text += CaesarCipher(alphabet=self.alphabet)._shift(char, key)
            key_index = (
                key_index + 1
                if key_index < len(shift_keys) - 1
                else 0
            )

        return new_text

    def encode(self, *, plaintext, key, start_at=''):
        shift_keys = self._shift_keys(key, start_at)

        return self._shift(plaintext, shift_keys)

    def decode(self, *, ciphertext, key, start_at=''):
        shift_keys = self._shift_keys(key, start_at)
        shift_keys = [-1 * sk for sk in shift_keys]

        return self._shift(ciphertext, shift_keys)
