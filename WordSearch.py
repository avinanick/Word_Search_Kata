import csv


class WordSearch():

    grid = []
    target_words = []

    def read_file(self, file_name):
        self.grid = []
        self.target_words = []
        with open(file_name) as word_search_csv:
            grid_reader = csv.reader(word_search_csv)
            for i, row in enumerate(grid_reader):
                # The first row is the list of words in the grid, those following are the grid
                if i == 0:
                    for word in row:
                        self.target_words.append(word)
                else:
                    # Since we are treating the grid coordinates as traditional x and y cartesian coords,
                    # this will input the letters flipped across the diagonal for easy work later
                    for j, letter in enumerate(row):
                        if j >= len(self.grid):
                            self.grid.append([])
                        self.grid[j].append(letter)