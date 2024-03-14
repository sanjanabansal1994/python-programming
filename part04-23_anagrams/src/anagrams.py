# Write your solution here
def anagrams(str1: str, str2:str):
    l1=[]
    for i in str1:
        l1.append(i)
    l2=[]
    for i in str2:
        l2.append(i)
    a= sorted(l1)==sorted(l2)
    return (a)

if __name__ == "__main__":
    anagrams("a","a")