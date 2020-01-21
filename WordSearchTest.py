import unittest
from WordSearch import WordSearch


class WordSearchTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.word_search = WordSearch()

    def test_reading_search_grid_from_file_to_array(self):
        self.word_search.read_file("TestWordGrid.csv")
        self.assertEqual("Z", self.word_search.grid[5][1], "Test grid not correct!")
        self.assertIn("KIRK", self.word_search.target_words, "Did not successfully read target words!")
        self.assertEqual(7, len(self.word_search.target_words), "Did not successfully read all target words!")

    def test_word_search_finds_horizontal_words(self):
        self.word_search.read_file("TestHorizontalWordGrid.csv")
        self.word_search.solve_grid()
        self.assertIn("LINK", self.word_search.solved_words)
        self.assertIn((2,1), self.word_search.solved_words["LINK"])
        self.assertIn("FIRE", self.word_search.solved_words)
        self.assertIn((1, 4), self.word_search.solved_words["FIRE"])


if __name__ == '__main__':
    unittest.main()
