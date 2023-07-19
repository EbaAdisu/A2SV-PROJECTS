class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        dic={}
        for p in paths:
            l=p.split()
            root=l[0]
            for i in range(1,len(l)):
                fil=l[i].split('(')
                f=fil[0]
                con=fil[1]
                con=con[:len(con)-1]
                dic[con]=dic.get(con,[])+[root+'/'+f]
        dub=[]
        for v in dic.values():
            if len(v)>1:
                dub.append(v)
        return dub
