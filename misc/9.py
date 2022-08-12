#9: Palindrome Number

#change to string and compare with reverse
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        return str(x) == str(x)[::-1]
        

# standard way of iteration
class Solution(object):
    def isPalindrome(self, x):
        x = list(x)
        for i in range(0, len(x)//2):
            if x[i] != x[len(x)-i-1]:
                return False
        return True
