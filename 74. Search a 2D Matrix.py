class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lower = 0
        upper = len(matrix) - 1
        while lower <= upper:
            mid = (lower + upper) // 2
            if target < matrix[mid][0]:
                upper = mid - 1
            elif target > matrix[mid][-1]:
                lower = mid + 1
            else:
                if target in matrix[mid]:
                    return True
                else:
                    return False
        return False


# Test Code
solution = Solution()
result = solution.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]])

# Print the result
print("Result:",result)
