class Solution:
    def isPalindrome(self, s: str) -> bool:
        alp="abcdefghijklmnopqrstuvwxyz0123456789"
        sn=""
        for c in s.lower():
            if c in alp:
                sn+=c
        return sn==sn[::-1]
