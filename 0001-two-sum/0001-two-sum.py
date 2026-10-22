class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        numsdict = {}
        for idx, num in enumerate(nums) :
            if target-num in numsdict :
               return ([numsdict[target-num], idx])
            else :
                numsdict[num] = idx

            