class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()  # Sort the array
        
        def count_pairs(max_diff):
            count = left = 0
            for right in range(len(nums)):
                while nums[right] - nums[left] > max_diff:
                    left += 1
                count += right - left
            return count - (len(nums) - left) * (len(nums) - left - 1) // 2

        
        left, right = 0, nums[-1] - nums[0]
        
        while left < right:
            mid = (left + right) // 2
            if count_pairs(mid) >= p:
                right = mid
            else:
                left = mid + 1
        
        return left