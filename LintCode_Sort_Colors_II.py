class Solution:
    """ Count Sort. """
    def sortColors2(self, colors, k):
        """
        @param colors: A list of integer
        @param k: An integer
        @return: nothing
        """
        counts = [0]*(k+1)
        for color in colors:
            counts[color] += 1
        idx = 0
        for color, count in enumerate(counts):
            for _ in range(count):
                colors[idx] = color
                idx += 1
