class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        # using sort()
        
        nums.sort()
        n=[]
        for i in range(len(nums)):
            if nums[i] == target:
                n.append(i)
        return n

        # without sorting 
        
        l=[0]
        bu=False
        for j in nums:
            if j<target:
                for i in range(len(l)):
                    l[i]+=1
            elif j==target:
                if bu:
                    l.append(l[-1]+1)
                bu=True
        if bu :return l
        return []
