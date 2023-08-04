class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        dic={}
        for i,k in reversed(operations):
            dic[i]=dic.get(k,k)
        for k,v in enumerate(nums):
            if v in dic:
                nums[k]=dic[v]
        return nums
