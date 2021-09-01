class ShortestPathFinder(object):

    @staticmethod
    def get_shortest_path(start: tuple[int, int], end: tuple[int, int]) -> list[tuple[int, int]]:

        start_row = start[0]
        start_column = start[1]

        path = [start]

        # Reach to the same row
        if start_row > end[0]:
            # If start position row is after the end position row, go to the end position row by decrementing
            while start_row != end[0]:
                start_row = start_row - 1
                path.append((start_row, start_column))
        elif start_row < end[0]:
            # If start position row is before the end position row, go to the end position row by incrementing
            while start_row != end[0]:
                start_row = start_row + 1
                path.append((start_row, start_column))

        if start_column > end[1]:
            # If start position column is after the end position row, go to the end position column by decrementing
            while start_column != end[1]:
                start_column = start_column - 1
                path.append((start_row, start_column))
        elif start_column < end[1]:
            # If start position column is before the end position row, go to the end position row by incrementing
            while start_column != end[1]:
                start_column = start_column + 1
                path.append((start_row, start_column))

        return path
