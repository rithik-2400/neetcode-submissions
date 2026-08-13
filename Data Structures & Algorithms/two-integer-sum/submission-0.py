class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                t=nums[i]+nums[j]
                if t==target:
                    return [i,j]
  