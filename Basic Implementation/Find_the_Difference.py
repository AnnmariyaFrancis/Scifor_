"""You are given two strings s and t.

String t is generated by random shuffling string s and then add one more letter at a random position.

Return the letter that was added to t."""


class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        e = ""
        sum1 = 0
        sum2 = 0
        for i in s:
            sum1 = sum1 + ord(i)
        for j in t:
            sum2 = sum2 + ord(j)
        if sum1 > sum2:
            sum = sum1 - sum2
        else:
            sum = sum2 - sum1
        return chr(sum)


s1 = Solution()
s1.findTheDifference