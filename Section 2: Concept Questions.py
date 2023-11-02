#2.1
def is_isogram(word):
    word = word.lower()  # Convert to lowercase for consistent checking
    letter_count = {}    # Dictionary 

    for letter in word:
        if letter in letter_count:
            return False
        else:
            letter_count[letter] = 1

    return True

#2.2
import unittest

class TestIsIsogramFunction(unittest.TestCase):

    def test_basic_isograms(self):
        # basic test isograms
        self.assertTrue(is_isogram("isogram"))
        self.assertTrue(is_isogram("uncopyrightable"))
        self.assertTrue(is_isogram("ambidextrously"))

    def test_word_with_repeated_letters(self):
        # test not isograms
        self.assertFalse(is_isogram("repeated"))
        self.assertFalse(is_isogram("hello"))

    def test_empty_string(self):
        # I consider empty string can be seen as isograms
        self.assertTrue(is_isogram(""))


    def test_words_with_spaces_and_hyphens(self):
        # Words with spaces or hyphens, common in compound words or phrases
        self.assertTrue(is_isogram("first-name"))  # Hyphenated word
        self.assertFalse(is_isogram("hello world"))  # Phrase with space, repeated 'l'

    def test_words_with_numbers(self):
        # The request doesn't say numbers aren't included, so I'm assuming numbers don't affect judgment
        self.assertTrue(is_isogram("12345"))
        self.assertFalse(is_isogram("112345"))

if __name__ == "__main__":
    unittest.main()
