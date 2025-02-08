class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for i, num in enumerate(nums):
            complete = target-num
            if complete in num_map:
                return [num_map[complete], i]
            num_map[num] = i
        return []
    solution = Solution()
