"""
Unit tests for string_utils
"""
import unittest

from src.string_utils import count, contains, sanitize


class TestStringUtils(unittest.TestCase):
    """ Tests for the string_utils file. """
    def test_count(self):
        """ Check it returns the correct count """
        self.assertEqual(count("Monty Python"), 12)

    def test_contains(self):
        """ Check it only returns true if the text is in the given string """
        self.assertEqual(
            contains(
                "Monty",
                "Monty Python and the Holy Grail"),
            True)
        self.assertEqual(contains("Monty", "Star Wars"), False)

    def test_sanitize(self):
        """ Check the Spam Song reduces to three words """
        # pylint: disable=line-too-long
        spam_song = "Lovely Spam Wonderful Spam Lovely Spam Wonderful Spam Spam Spam Spam Spam Lovely Spam Lovely Spam Lovely Spam Spam Spam Spam Spam"
        expected_answer = ['Lovely', 'Spam', 'Wonderful']
        self.assertEqual(sanitize(spam_song), expected_answer)
