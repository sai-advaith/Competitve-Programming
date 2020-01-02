class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        transpose = []
        k = len(A[0])
        e = len(A)
        for i in range (k):
            r = []
            for j in range (e):
                r.append(A[j][i])
            transpose.append(r)
        return (transpose)