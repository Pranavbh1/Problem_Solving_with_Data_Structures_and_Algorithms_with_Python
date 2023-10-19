class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_Index = {}
        for idx, number in enumerate(nums):
            if target - number in num_Index:
                return num_Index[target - number], idx
            num_Index[number] = idx

