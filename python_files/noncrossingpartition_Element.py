from sage.structure.element import Element

class NoncrossingPartition(Element):
    def __init__(self, parent, blocks):
        self._blocks = blocks
        self._number_of_blocks = len(blocks)
        self._n = parent._n
        if not SetPartitions(self._n)(self._blocks).is_noncrossing():
            raise ValueError("{} is not noncrossing".format(blocks))
        Element.__init__(self, parent)
    def __repr__(self):
        return 'Noncrossing Partition with blocks {}'.format(self._blocks)
    def _latex_(self):
        return self._blocks
    def arcs(self):
        """
        Return the linear representation of ``self``

        EXAMPLES::

            sage: N=NoncrossingPartitions(5)
            sage: ncp=N([[1,2,3,4],[5]])
            sage: ncp.arcs()
            [(1, 2), (2, 3), (3, 4)]
        """
        return SetPartitions(self._n)(self._blocks).arcs()
    def to_permutation(self):
        """
        Return the permutation corresponding to ``self`` in cycle notation
        """
        sp = SetPartitions(self._n)(self._blocks)
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
            ncp = d.to_noncrossing_partition()
            yield self.element_class(self,ncp)
    Element = NoncrossingPartition
    def chain(self):
        rels = []
        for pos in range(self._n):
            rels.append([str(self[pos]._blocks),str(self[pos+1]._blocks)])
        return Poset([[],rels])

####### starts tests #########
def test_noncrossingpartition(n=4):
    N = NoncrossingPartitions(n)
    if not len(N) == catalan_number(n):
        return False
    sage_S = SetPartitions(n)
    for ncp in N:
        if not sage_S(ncp._blocks).is_noncrossing():
            return False
        if not sage_S(ncp._blocks).arcs() == ncp.arcs():
            return False
    C = N.chain()
    if not C.is_chain():
        return False
    return True

