from sage.structure.list_clone import ClonableArray

class NoncrossingPartition(ClonableArray):
    def __init__(self, parent, blocks):
        if not SetPartitions(parent._n)(blocks).is_noncrossing():
            raise ValueError("{} is not noncrossing".format(blocks))
        ClonableArray.__init__(self, parent,blocks)
    def _latex_(self):
        return latex(self.to_permutation())
    def __repr__(self):
        return str(self.to_permutation())

    def check(self):
        """
        """
        if self not in self.parent():
            raise ValueError("invalid noncrossing partition")

    def to_permutation(self):
        """
        Return the permutation corresponding to ``self`` in cycle notation
        """
        sp = SetPartitions(self.parent()._n)(self)
        perm = sp.to_permutation().to_cycles()
        return perm

    def arcs(self):
        """
        Return the linear representation of ``self``

        EXAMPLES::

            sage: N=NoncrossingPartitions(5)
            sage: ncp=N([[1,2,3,4],[5]])
            sage: ncp.arcs()
            [(1, 2), (2, 3), (3, 4)]
        """
        return SetPartitions(self.parent()._n)(self).arcs()

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

    def create_chain(self):
        rels = []
        for pos in range(len(self)-1):
            rels.append([str(self[pos].to_permutation()),\
            str(self[pos+1].to_permutation())])
        return Poset([[],rels])


####### starts tests #########
def test_noncrossingpartition(n=4):
    sage_S=SetPartitions(n)
    my_NCPs = NoncrossingPartitions(n)
    if not len(my_NCPs) == catalan_number(n):
        return False
    for ncp in my_NCPs:
        if not sage_S(ncp).is_noncrossing():
            return False
        if not sage_S(ncp).arcs() == ncp.arcs():
            return False
    C = my_NCPs.create_chain()
    if not C.is_chain():
        return False
    return True