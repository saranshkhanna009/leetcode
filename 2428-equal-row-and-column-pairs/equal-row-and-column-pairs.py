class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        row_count = {}

        # Count every row
        for row in grid:
            row = tuple(row)
            row_count[row] = row_count.get(row, 0) + 1

        count = 0
        n = len(grid)

        # Compare every column
        for c in range(n):
            column = []

            for r in range(n):
                column.append(grid[r][c])

            column = tuple(column)

            if column in row_count:
                count += row_count[column]

        return count