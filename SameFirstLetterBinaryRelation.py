#coding: utf-8

from BinaryRelation import BinaryRelation


class SameFirstLetterBinaryRelation(BinaryRelation):
    """A Binary Relation which elements in an ordered pair share the same first letter."""

    def contains_ordered_pair(self, x, y):
        """
        This method returns a boolean value indicating if both elements of a given ordered pair have the same first letter.

        Arguments:
        x - The first element of the ordered pair.
        y - The second element of the ordered pair.

        Return True if the ordered pair belongs to the binary relation, otherwise, return False.
        """
        if x[0] == y[0]:
            return True
        else:
            return False

    def relation(self, S):
        """
        This method returns a set of pairs in SxS (a.k.a. S²) that belong to the binary relation.

        Arguments:
        S - The input set.

        Return a set of pairs in SxS (a.k.a. S²) that belong to the binary relation.
        """
        S_S = set()
        for x in S:
            for y in S:
                if self.contains_ordered_pair(x, y):
                    S_S.add((x, y))
        return S_S

