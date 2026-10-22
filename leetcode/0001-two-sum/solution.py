class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        '''
        nums를 2회 순회하는 코드는 시간복잡도 O(n^2)임.
        시간복잡도 줄이기 위해, Hash map인 dict를 사용하여 nums를 한번만 순회하게 함으로서 시간복잡도 O(n)으로 감소
        숫자1 + 숫자2 = target 이므로, 숫자1이 정해지면 숫자2는 target-num인 것을 이용, 숫자를 key & 해당 숫자의 리스트 내 인덱스를 value로 함
        이 때, 리스트(nums) 내 중복되는 숫자가 존재할 수 있으므로, numsdict에 숫자를 한번에 저장하지 말고 nums에서 하나씩 검토 후 return을 못하였을 시에만 저장
        '''
        numsdict = {}
        for idx, num in enumerate(nums) :
            if target-num in numsdict :
               return ([numsdict[target-num], idx])
            else :
                numsdict[num] = idx

            
