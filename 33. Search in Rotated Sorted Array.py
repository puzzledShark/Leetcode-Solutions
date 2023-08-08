# Basically does a binary search to find pivot
# Then it does a binary search again to actually find the target
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left, right = 0, n - 1
        
        # Find the index of the pivot element (the smallest element)
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > nums[-1]:
                # If nums[mid] > nums[-1], the pivot is to the right
                left = mid + 1
            else:
                # If nums[mid] <= nums[-1], the pivot is to the left or at mid
                right = mid - 1
        
        # Binary search over an inclusive range [left_boundary ~ right_boundary]
        def binarySearch(left_boundary, right_boundary, target):
            left, right = left_boundary, right_boundary
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid  # Found the target
                elif nums[mid] > target:
                    right = mid - 1  # Target is in the left half
                else:
                    left = mid + 1   # Target is in the right half
            return -1  # Target not found
        
        # The pivot index indicates where the array is split into two sorted subarrays
        pivot_index = left
        
        # Check if the target is in the left sorted subarray
        left_result = binarySearch(0, pivot_index - 1, target)
        if left_result != -1:
            return left_result
        
        # Check if the target is in the right sorted subarray
        right_result = binarySearch(pivot_index, n - 1, target)
        return right_result
