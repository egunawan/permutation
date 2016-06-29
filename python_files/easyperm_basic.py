class EasyPerm(object):
    def __init__(self,line):
        self._line = line
        self._n = len(line)

    def __repr__(self):
        return 'My Permutation with one-line notation {}'.format(self._line)

    def compose(self,infront):
        """
        infront is applied, then self
        """
        new = [-1]*self._n
        for pos in range(0, self._n):
            new[pos]=self._line[infront._line[pos]-1]
        return EasyPerm(new)

    def descents(self):
        """
        Return a list with descents positions (where possible positions
        are 1,2, ..., n-1). A position k = 1,2, ..., n-1 is called
        a descent of a permutation p if p(k+1)<p(k).
        """
        D = []
        for pos in range(0,self._n-1):
            if self._line[pos]>self._line[pos+1]:
                D.append(pos+1)
        return D

############ BEGIN TESTS ##############

def test_EasyPerm(n=5):
    M = Permutations(n)
    m = M.random_element()
    if not len(EasyPerm(m).descents()) == len(m.descents()): # because Sage descents start at 0
        return False
    return True

