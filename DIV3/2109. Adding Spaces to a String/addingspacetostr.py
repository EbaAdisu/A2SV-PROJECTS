class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:    
      #working
        k=0
        sn=''
        for i in spaces:
            sn+=s[k:i]
            sn+=' '
            k=i
        sn+=s[k:]
        return 
      
      #Time Limit Exceeded
        # k=0
        # for i in spaces:
        #     s=s[:i+k]+' '+s[i+k:]
        #     k+=1
        # return s
