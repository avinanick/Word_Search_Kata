import unittest
from WordSearch import WordSearch


class WordSearchTestCase(unittest.TestCase):
    def test_reading_search_grid_from_file_to_array(self):
        word_search = WordSearch()
        word_search.read_file("TestWordGrid.csv")
        self.assertEqual("Z", word_search.grid[5][1], "Test grid not correct!")
        self.assertIn("KIRK", word_search.target_words, "Did not successfully read target words!")
        self.assertEqual(7, len(word_search.target_words), "Did not successfully read all target words!")


if __name__ == '__main__':
    unittest.main()
