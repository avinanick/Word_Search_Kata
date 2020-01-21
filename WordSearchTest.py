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

    def test_word_search_finds_vertical_words(self):
        self.word_search.read_file("TestVerticalWordGrid.csv")
        self.word_search.solve_grid()
        self.assertIn("HERO", self.word_search.solved_words)
        self.assertIn((2, 4), self.word_search.solved_words["HERO"])
        self.assertIn("CRAFT", self.word_search.solved_words)
        self.assertIn((6, 2), self.word_search.solved_words["CRAFT"])

    def test_word_search_finds_diagonal_words(self):
        self.word_search.read_file("TestDiagonalWordGrid.csv")
        self.word_search.solve_grid()
        self.assertIn("RING", self.word_search.solved_words)
        self.assertIn((4, 2), self.word_search.solved_words["RING"])
        self.assertIn("FOOTMAN", self.word_search.solved_words)
        self.assertIn((2, 5), self.word_search.solved_words["FOOTMAN"])


if __name__ == '__main__':
    unittest.main()
