class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for first_idx in range(0,len(nums)-1) :
            for second_idx in range(first_idx+1, len(nums)) :
                if nums[first_idx] + nums[second_idx] == target :
                    return([first_idx,second_idx])
            