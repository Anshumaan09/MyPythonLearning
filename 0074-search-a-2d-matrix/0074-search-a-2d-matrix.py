class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        column = len(matrix[0])
        left = 0
        right = (row*column) - 1
        while left <= right:
            mid = left + (right - left) // 2
            r = mid // column
            c = mid % column
            value = matrix[r][c]
            if value == target:
                return True
            elif value > target:
                right = mid - 1
            else:
                left = mid + 1
        return False