# python 3.5.0

class Solution(object):
    def isValid(self, s):
        l=len(s)
        #print(l)

        s_l = list(s)
        #print(s_l)
        
        for i in range(0, len(s), 2):
            print(a)
            one = s[i]
            two = s[i-1]
            if one != two:
                return False
        return True
            #print(b)
        """
        :type s: str
        :rtype: bool
        """
        
a = Solution()
a.isValid("[]()<>")

'''
每次循环多个元素
在3+版本可以用 zip
之前的就要用 itertools

'''
