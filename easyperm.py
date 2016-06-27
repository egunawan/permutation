class EasyPerm(SageObject):
    def __init__(self,line):
        self._line = line
        self._n = len(line)
        for i in range(1,len(line)+1):
            if i not in line:
                raise ValueError("The input must a one-line notation of a permutation on [{}]. The number {} does not appear in {}".format(len(line),i,line))

    def __repr__(self):
        return 'My Easy Permutation with one-line notation {}'.format(self._line)
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

    def number_of_descents(self):
        """
        return the number of descents of ``self``.

        EXAMPLES::

            sage: EasyPerm([2,1,4,3]).number_of_descents()
            2
        """
        return 'exercise for audience'

    def to_cycles(self, singletons=True):
        """
        Return the permutation ``self`` as a list of disjoint cycles.

        The cycles are returned in the order of increasing smallest
        elements, and each cycle is returned as a tuple which starts
        with its smallest element.

        If ``singletons=False`` is given, the list does not contain the
        singleton cycles.

        EXAMPLES::

            sage: EasyPerm([2,1,3,4]).to_cycles()
            [(1, 2), (3,), (4,)]
            sage: EasyPerm([2,1,3,4]).to_cycles(singletons=False)
            [(1, 2)]

            sage: EasyPerm([4,1,5,2,6,3]).to_cycles()
            [(1, 4, 2), (3, 5, 6)]

        The algorithm is of complexity `O(n)` where `n` is the size of the
        given permutation.
        """
        cycles = []

        l = self._line[:]

        # Go through until we've considered every number between 1 and len(l)
        for i in range(len(l)):
            if not l[i]:
                continue
            cycleFirst = i + 1
            cycle = [cycleFirst]
            l[i], next = False, l[i]
            while next != cycleFirst:
                cycle.append( next )
                l[next - 1], next  = False, l[next - 1]
            # Add the cycle to the list of cycles
            if singletons or len(cycle) > 1:
                cycles.append(tuple(cycle))
        return cycles

    def is_derangement(self):
        """
        A fixed point of a permutation p is an element i such that p(i)=i.
        A derangement is a permutation that has no fixed points.
        Define a function called is_derangement that
        returns True if p is a derangement and returns False otherwise.

            EXAMPLES::

                sage: EasyPerm([2,1,4,3]).is_derangement()
                True
                sage: EasyPerm([2,1,3,4]).is_derangement()
                False
        """
        return 'exercise for audience'

############ BEGIN TESTS ##############

def test_EasyPerm(n=5):
    M = Permutations(n)
    m = M.random_element()
    if not EasyPerm(m).to_cycles(singletons=True) == m.to_cycles():
        return False
    if not EasyPerm(m).to_cycles(singletons=False) == m.to_cycles(singletons=False):
        return False
    if not EasyPerm(m).descents() == m.descents(from_zero=False):
        return False
    return True

