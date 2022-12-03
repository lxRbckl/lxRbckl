class Solution:

    def removeDuplicates(self, s: str) -> str:
        '''  '''

        l = []
        [l.pop() if ((l) and (l[-1] == i)) else l.append(i) for i in s]

        return ''.join(l)
