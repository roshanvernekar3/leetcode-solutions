class Solution(object):
    def maxSubArray(self, nums):
        maxi = float("-inf")   # best seen so far
        curSum = 0             # sum of current window

        for num in nums:
            curSum += num          # extend window
            maxi = max(maxi, curSum)

            if curSum < 0:         # negative drag – cut here
                curSum = 0

        return maxi

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna