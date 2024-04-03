# WRITE YOUR SOLUTION HERE:
class ListHelper:


    @classmethod
    def greatest_frequency(cls, mylist:list):
        cnt=0
        for i in mylist:
            if mylist.count(i)> cnt:
                cnt = mylist.count(i)
                res = i
        return res
    
    @classmethod
    def doubles(cls, mylist:list):
        res=0
        for i in set(mylist):
            if mylist.count(i)>= 2:
                res+=1
        return res

