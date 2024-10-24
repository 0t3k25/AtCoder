class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        p1 :int = 0
        for i in range(len(nums)):
            if nums[i] % 2 ==0:
                nums[i],nums[p1] =nums[p1], nums[i]
                p1 +=1
        return nums