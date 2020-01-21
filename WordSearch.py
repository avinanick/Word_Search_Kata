import csv


class WordSearch():

    grid = []
    target_words = []
    solved_words = {}

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

    def solve_grid(self):
        for current_word in self.target_words:
            word_coords = []
            # Search the grid until we find the first letter of the word
            for x, row in enumerate(self.grid):
                for y, letter in enumerate(row):
                    if letter == current_word[0]:
                        # Once we find the first letter, begin a depth-first search in all directions for the rest of the word
                        word_coords.append((x,y))
                        x_direction = 0
                        letter_index_in_word = 1
                        search_coords_stack = []
                        search_coords_stack.append((x-1, y))
                        search_coords_stack.append((x+1, y))
                        while len(word_coords) < len(current_word) and len(search_coords_stack) > 0:
                            next_coord = search_coords_stack.pop()
                            if len(self.grid) > next_coord[0] >= 0 and len(self.grid[x]) > next_coord[1] >= 0:
                                current_x_direction = next_coord[0] - x
                                if current_x_direction != 0:
                                    current_x_direction = current_x_direction / abs(current_x_direction)
                                if current_x_direction != x_direction:
                                    letter_index_in_word = 1
                                    word_coords = [(x,y)]
                                x_direction = int(current_x_direction)
                                if self.grid[next_coord[0]][next_coord[1]] == current_word[letter_index_in_word]:
                                    word_coords.append(next_coord)
                                    if len(word_coords) < len(current_word):
                                        search_coords_stack.append((next_coord[0] + x_direction, next_coord[1]))
                                        letter_index_in_word += 1
                                    else:
                                        # Found the whole word!
                                        self.solved_words[current_word] = word_coords
                                        print(current_word, " : ", word_coords)