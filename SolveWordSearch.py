from WordSearch import WordSearch
import sys

if __name__ == '__main__':
    word_search = WordSearch()
    word_search.read_file(sys.argv[1])
    word_search.solve_grid()