class Solution(object):
    def rearrangeArray(self, nums):
        n = len(nums)
        result = [0] * n
        posIndex, negIndex = 0, 1

        for i in range(0, n):
            if nums[i] >= 0:
                result[posIndex] = nums[i]
                posIndex += 2

            else:
                result[negIndex] = nums[i]
                negIndex += 2

        return result

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna