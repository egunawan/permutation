from sage.structure.list_clone import ClonableArray

class NoncrossingPartition(ClonableArray):
    def __init__(self, parent, blocks):
        #self._blocks = blocks
        self._number_of_blocks = len(blocks)
        self._n = parent._n
        if not SetPartitions(self._n)(blocks).is_noncrossing():
            raise ValueError("{} is not noncrossing".format(blocks))
        ClonableArray.__init__(self, parent,blocks)
    def _latex_(self):
        return self.to_permutation()

    def check(self):
        """
        """
        if self not in self.parent():
            raise ValueError("invalid noncrossing partition")

    def to_permutation(self):
        """
        Return the permutation corresponding to ``self`` in cycle notation
        """
        sp = SetPartitions(self._n)(self)
        perm = sp.to_permutation().to_cycles()
        return perm

class NoncrossingPartitions(UniqueRepresentation,Parent):
    def __init__(self,n):
        self._n = n
        Parent.__init__(self, category=FiniteEnumeratedSets())
    def __repr__(self):
        return 'Noncrossing set partitions of [{}]'.format(self._n)
    def __iter__(self):
        Ds = DyckWords(self._n)
        for d in Ds:
            NCP = d.to_noncrossing_partition()
            yield self.element_class(self,NCP)
    Element = NoncrossingPartition


####### starts tests #########
def test_noncrossingpartition(n=4):
    sage_S=SetPartitions(n)
    my_NCPs = NoncrossingPartitions(n)
    if not len(my_NCPs) == catalan_number(n):
        return False
    for ncp in my_NCPs:
        if not sage_S(ncp).is_noncrossing():
            return False
    return True


