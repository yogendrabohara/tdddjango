from django.test import TestCase

from .factories import ClueFactory, EntryFactory, PuzzleFactory


class TestXWordModels(TestCase):

    def test_clue(self):
        clue = ClueFactory()
        string_repr = str(vars(clue)) + str(vars(clue.entry))
        self.assertTrue(True)
        self.assertTrue(clue.entry.entry_text in string_repr)
        self.assertTrue(clue.clue_text in string_repr)

    def test_entry(self):
        entry = EntryFactory()
        string_repr = str(vars(entry))
        self.assertTrue(entry.entry_text in string_repr)

    def test_puzzle(self):
        puzzle = PuzzleFactory()
        string_repr = str(vars(puzzle))
        self.assertTrue(puzzle.publisher in string_repr)
        self.assertTrue(puzzle.date.strftime('%Y, %#m, %#d') in string_repr)
