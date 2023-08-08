# Is this cheating? lol, its just python built in methods
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        try:
            index = nums.index(target)
        except ValueError:
            return -1
        return index