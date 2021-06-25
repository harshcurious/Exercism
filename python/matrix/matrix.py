class Matrix:
    def __init__(self, matrix_string):
        self.matrix_string = matrix_string
        
    def row(self, index):
        split1 = self.matrix_string.split('\n')
        matrix_split = [sent.split() for sent in split1]
        row = list(map(int, matrix_split[index-1]))
        return row

    def column(self, index):
        split1 = self.matrix_string.split('\n')
        matrix_split = [sent.split() for sent in split1]
        col_string = [row[index-1] for row in matrix_split]
        col = list(map(int, col_string))
        return col
