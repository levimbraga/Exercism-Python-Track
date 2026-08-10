class Matrix:
    def __init__(self, matrix_string):
        string_split = matrix_string.split('\n')
        list_of_rows = []
        for row in string_split:
            list_of_rows.append(row.split())
        for row in list_of_rows:
            for number in range(len(row)):
                row[number] = int(row[number])

        self.list_of_rows = list_of_rows

    def row(self, index):
        return self.list_of_rows[index - 1]

    def column(self, index):
        self.column = []
        for row in self.list_of_rows:
            self.column.append(row[index - 1])

        return self.column
