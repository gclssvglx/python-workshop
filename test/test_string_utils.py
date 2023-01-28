"""
Unit tests for string_utils
"""
import unittest

from src.string_utils import count, contains


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
