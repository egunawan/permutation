from sage.misc.inherit_comparison import InheritComparisonClasscallMetaclass
from sage.structure.list_clone import ClonableIntArray

class MyPerm(ClonableIntArray):
    """ A permutation is
    """
    __metaclass__ = InheritComparisonClasscallMetaclass

    @staticmethod
    def __classcall_private__(cls, line):
        """
        Create a permutation with input the one-line notation

        EXAMPLES::

            sage: MyPerm([1,2,3,4,5])
            [1, 2, 3, 4, 5]
        """
        for i in range(1,len(line)+1):
            if i not in line:
                raise ValueError("The input must a one-line notation of a permutation on [{}]. The number {} does not appear in {}".format(len(line),i,line))
        MOs = MyPerms(len(line))
        return MOs(line)

    def __init__(self, parent, line):
        """
        Initialize ``self``.

        EXAMPLES::

            sage: MyPerm([1,4,3,2])
            [1, 4, 3, 2]
        """
        ClonableIntArray.__init__(self, parent, line)

    def check(self):
        """
        """
        if self not in self.parent():
            raise ValueError("invalid permutation")

    def compose(self,infront):
        """
        infront is applied, then self
        """
        new = [-1]*len(self)
        for pos in range(0, len(self)):
            new[pos]=self[infront[pos]-1]
        return MyPerm(new)

    def to_matrix(self):
        r"""
        Return a matrix representing the permutation.
        This is copied and pasted from Sage implementation in permutation.py

        EXAMPLES::

            sage: MyPerm([1,2,3]).to_matrix()
            [1 0 0]
            [0 1 0]
            [0 0 1]

        ::

            sage: MyPerm([1,3,2]).to_matrix()
            [1 0 0]
            [0 0 1]
            [0 1 0]


        """
        p = self[:]
        n = len(p)
        entries = {}
        for i in range(n):
            entries[(p[i]-1,i)] = 1
        return matrix(n, entries, sparse = True)


class MyPerms(Parent,UniqueRepresentation):
    """
    Permutations on [n]
    """
    def __init__(self,n):
        self._n=n
        Parent.__init__(self, category=FiniteEnumeratedSets())

    def __repr__(self):
        return 'Permutations on [{}]'.format(self._n)

    Element = MyPerm

    def __iter__(self):
        """
        Ordered in Lexicographic order
        """
        perm = range(1,self._n+1) # identity permutation
        yield self.element_class(self,perm)
        while next_permutation(perm):
           yield self.element_class(self,perm)

    def n(self):
        return self._n

class MyTranspositions(MyPerms):
    """
    Permutations on [n] which swaps exactly two numbers.
    NOT ordered in lexicographic order
    """
    def __iter__(self):
        line = range(1,self._n+1)
        for i in range(0,self._n+1):
            for j in range(i+1,self._n):
                line[i],line[j]=j+1,i+1
                yield self.element_class(self,line)
                line[i],line[j]=i+1,j+1

    def __repr__(self):
        return 'Transposition permutations on [{}]'.format(self._n)

def next_permutation(arr):
    """
    https://www.nayuki.io/res/next-lexicographical-permutation-algorithm/nextperm.py
    """
    # Find non-increasing suffix
    i = len(arr) - 1
    while i > 0 and arr[i - 1] >= arr[i]:
        i -= 1
    if i <= 0:
        return False

    # Find successor to pivot
    j = len(arr) - 1
    while arr[j] <= arr[i - 1]:
        j -= 1
    arr[i - 1], arr[j] = arr[j], arr[i - 1]

    # Reverse suffix
    arr[i : ] = arr[len(arr) - 1 : i - 1 : -1]
    return True



###################### start test ########################
def test_MyPerms(n=5):
    M = MyPerms(n)
    SageM = Permutations(n)
    if not len(M) == factorial(n):
        print 'len(M):',len(M)
        return False
    if not M(range(1,n+1))==MyPerm(range(1,n+1)):
        return False
    if not MyPerm([5,4,3,2,1]).compose(MyPerm([5,4,3,2,1])) == MyPerm([1,2,3,4,5]):
        print 'MyPerm([5,4,3,2,1]).compose(MyPerm([5,4,3,2,1]))._line:', MyPerm([5,4,3,2,1]).compose(MyPerm([5,4,3,2,1]))
        return False
    if not len(MyPerm(range(1,n+1)))==n:
        return False
    if not len(MyTranspositions(n))==n*(n-1)/2:
        print 'len(MyTranspositions(n))',len(MyTranspositions(n))
        return False
    if not MyPerm([5,4,1,2,3,6]).to_matrix() == Permutation([5,4,1,2,3,6]).to_matrix():
        return False
    for P,SageP in zip(M,SageM): # compare with Sage Permutations class
        if not tuple(P)==tuple(SageP):
            return False
    return True
