class Solution(object):
    def longestConsecutive(self, arr):
        arr.sort()
        count = 0
        last_smaller = float("-inf")
        longest = 0
        for num in arr:
            if num - 1 == last_smaller:
                count += 1
                last_smaller = num
            elif num != last_smaller:
                count = 1
                last_smaller = num
            longest = max(longest, count)
        return longest

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna