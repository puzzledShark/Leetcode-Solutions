from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        try: 
            index = nums.index(target)
            return True
        except ValueError:
            return False



# Test Code
solution = Solution()
#result = solution.search([6, 7, 8, 9, 0, 0, 1, 1, 2, 3, 4, 5, 6], 8)
result = solution.search([1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1], 8)


# Print the result
print("Result:",result)
