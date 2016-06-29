"""
Bare minimum classes NoncrossingPartitions and NoncrossingPartition
"""

from sage.structure.list_clone import ClonableArray

class NoncrossingPartition(ClonableArray):
    def __init__(self, parent, blocks):
        ClonableArray.__init__(self, parent,blocks)

    def check(self): # check() is required for ClonableArray
        if self not in self.parent():
            raise ValueError("invalid noncrossing partition")

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



##### starts tests #####
def test_noncrossingpartition(n=4):
    sage_S=SetPartitions(n)
    my_NCPs = NoncrossingPartitions(n)
    if not len(list(my_NCPs)) == catalan_number(n):
        return False
    if not len(my_NCPs) == catalan_number(n):
        return False
    for ncp in my_NCPs:
        if not sage_S(ncp).is_noncrossing():
            return False
    return True

N = NoncrossingPartitions(4)
for ncp in N:
    print ncp