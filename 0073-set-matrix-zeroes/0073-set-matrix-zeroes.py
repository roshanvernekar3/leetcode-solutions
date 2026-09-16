class Solution(object):
    def setZeroes(self, matrix):
        r = len(matrix)
        c = len(matrix[0])
        rowtrack = [0 for _ in range(r)]
        coltrack = [0 for _ in range(c)]

        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 0:
                    rowtrack[i] = -1
                    coltrack[j] = -1

        for i in range(r):
            for j in range(c):
                   if rowtrack[i] == -1 or coltrack[j] == -1:
                    matrix[i][j] = 0             
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna