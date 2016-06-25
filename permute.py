from sage.structure.unique_representation import UniqueRepresentation
from sage.structure.parent import Parent
from sage.categories.finite_enumerated_sets import FiniteEnumeratedSets
from sage.structure.element import Element
from sage.misc.inherit_comparison import InheritComparisonClasscallMetaclass
from sage.structure.list_clone import ClonableArray

class myobj(ClonableArray):
    """ A permutation is
    """
    __metaclass__ = InheritComparisonClasscallMetaclass

    @staticmethod
    def __classcall_private__(cls, line):
        """
        Create a permutation with input the one-line notation

        EXAMPLES::

            sage: myobj([1,2,3,4,5])
            [1, 2, 3, 4, 5]
        """
        for i in range(1,len(line)+1):
            if i not in line:
                raise ValueError("The input must a one-line notation of a permutation on {}. The number {} does not appear in {}".format(len(line),i,line))
        MOs = myobjs(len(line))
        return MOs(line)

    def __init__(self, parent, line):
        """
        Initialize ``self``.

        TESTS::
        """
        self._line = line
        self._n = parent._n
        ClonableArray.__init__(self, parent, line)


    def check(self):
        """
        """
        if self not in self.parent():
            raise ValueError("invalid permutation")

    def n(self):
        return self._n

    def compose(self,infront):
        """
        infront is applied, then self
        """
        new = [-1]*self._n
        infront_line = infront._line
        for pos in range(0, self._n):
            new[pos]=self._line[infront_line[pos]-1]
        return myobj(new)

    def to_matrix(self):
        r"""
        Return a matrix representing the permutation.
        This is copied and pasted from Sage implementation in permutation.py

        EXAMPLES::

            sage: myobj([1,2,3]).to_matrix()
            [1 0 0]
            [0 1 0]
            [0 0 1]

        ::

            sage: myobj([1,3,2]).to_matrix()
            [1 0 0]
            [0 0 1]
            [0 1 0]

        ::

            sage: p.to_matrix()*q.to_matrix()
            [0 0 1]
            [0 1 0]
            [1 0 0]

        """
        p = self[:]
        n = len(p)

        #Build the dictionary of entries since the matrix
        #is extremely sparse
        entries = {}
        for i in range(n):
            entries[(p[i]-1,i)] = 1
        return matrix(n, entries, sparse = True)


class myobjs(Parent,UniqueRepresentation):
    """
    Permutations on [n]
    """
    def __init__(self,n):
        self._n=n
        Parent.__init__(self, category=FiniteEnumeratedSets())

    def __repr__(self):
        return 'Permutations on [{}]'.format(self._n)

    Element = myobj

    def __iter__(self):
       perm = range(1,self._n+1) # identity permutation
       yield self.element_class(self,perm)
       while next_permutation(perm):
          yield self.element_class(self,perm)

    def bak__iter__(self):
        s=range(1,self._n+1)
        list=s
        used = [False] * len(list)
        L= do_permute(list, [], used, 0)
        for mm in L:
            #yield mm
            yield self.element_class(self,mm)

    def n(self):
        return self._n

class mytranspositions(myobjs):
    """
    Permutations on [n] which swaps exactly two numbers.
    Not ordered by lexicographic order
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
def test_myobjs(n=5):
    M = myobjs(n)
    if not len(M) == factorial(n):
        print 'len(M):',len(M)
        return False
    if not myobj([5,4,3,2,1]).compose(myobj([5,4,3,2,1]))._line == myobj([1,2,3,4,5])._line:
        print 'myobj([5,4,3,2,1]).compose(myobj([5,4,3,2,1]))._line:', myobj([5,4,3,2,1]).compose(myobj([5,4,3,2,1]))._line
        return False
    if not len(mytranspositions(n))==n*(n-1)/2:
        print 'len(mytranspositions(n))',len(mytranspositions(n))
        return False
    if not myobj([5,4,1,2,3,6]).to_matrix() == Permutation([5,4,1,2,3,6]).to_matrix():
        return False
    return True


#def do_permute(list, out, used, level):
#    """
#    Used to produce all permutations
#    """
#    if len(list) == level:#
#		yield out
#    else:
#        for i in range(0, len(list)):
#            if used[i]:
#                continue
#            used[i] = True
#            for perm in do_permute(list, out + [list[i]], used, level + 1):
#                #print 'perm:',perm
#                yield perm
#            used[i] = False