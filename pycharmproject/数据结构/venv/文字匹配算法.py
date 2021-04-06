class Solution:
    def isValid(self, s: str) -> bool:
        dict={}
        dict1={"{":"}","(":")","[":"]"}

        if str=="":
            return True
        if str[0] in list1:
            return False

        for i in str:
            if i in dict1.keys():
                dict[i] = dict.get(i, 0) + 1
            if i in dict1.values() and :
