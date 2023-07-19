class Solution:
    def reverse(self, x: int) -> int:
        # p='+'
        # if x<0:
        #     p='-'
        # s=str(abs(x))
        # x=int(p+s[::-1])
        # if x<-2**31 or x>2**31-1: return 0
        # return x
        p=1
        if x<0:
            x=-x
            p=-1
        ans=0
        while x>0:
            r=x%10
            ans=ans*10+r
            x=x//10
        ans*=p
        if ans>=-2**31 and ans<=2**31-1:
            return ans
        return 0
