#
# @lc app=leetcode id=509 lang=python
#
# [509] Fibonacci Number
#


# @lc code=start
class Solution(object):

    def func(self, num):
        if num == 0 or num == 1:
            return num
        return self.func(num - 1) + self.func(num - 2)

    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.func(n)


# @lc code=end