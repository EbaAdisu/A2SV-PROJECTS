class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        #simple code using builtin 
        # y=int(num1)*int(num2)
        # return str(y)

        # Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

        #WITH OUT USING CONVERTERS.  
        #USING DICTIONARY
      
        nums={}
        for i in range(10):
           nums[f'{i}']=i
        n1=0
        for j in num1:
            n1=n1*10+nums[j]
        n2=0
        for j in num2:
            n2=n2*10+nums[j]
        n=n1*n2
        dic=[(v,k) for k,v in nums.items()]
        dic=dict(dic)
        s=''
        f=10**(len(num1)+len(num2)-1)
        while f>=1:
            q=n//f
            s+=dic[q]
            n%=f
            f//=10
        k=1
        y=len(s)
        while k<y:
            if s[0]=='0':
                s=s[1:]
            else:break
            k+=1
        return s
