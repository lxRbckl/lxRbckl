from numpy import array, rot90


class Solution:


    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        for c, i in enumerate(rot90(m = array(matrix), axes = (1, 0))):

            matrix[c] = i
