#coding: utf-8


class BinaryRelationUtils(object):
    """Class providing utilities to verify properties of a binary relation."""

    @staticmethod
    def verify_reflexivity(binary_relation, input_set):
        """
        This method verifies if a given binary relation is reflexive or not.

        Arguments:
        binary_relation - A subclass of the BinaryRelation class.

        input_set - A set closed under the binary relation.

        Return True if the binary relation in the given input set is reflexive
        or False if it is not.
        """
        # TODO: Replace line below with actual code.
        conjunto = binary_relation.relation(input_set)
        tamanhoConjunto = len(input_set)
        contReflexividade = 0
        for x, y in conjunto:
            if x == y:
                contReflexividade += 1
        if contReflexividade == tamanhoConjunto:
            return True
        else:
            return False

    @staticmethod
    def verify_symmetry(binary_relation, input_set):
        """
        This method verifies if a given binary relation is symmetric or not.

        Arguments:
        binary_relation - A subclass of the BinaryRelation class.

        input_set - A set closed under the binary relation.

        Return True if the binary relation in the given input set is symmetric
        or False if it is not.
        """
        # TODO: Replace line below with actual code.
        conjunto = binary_relation.relation(input_set)
        for x in input_set:
            for y in input_set:
                if (x, y) in conjunto and (y, x) not in conjunto:
                    return False

        return True
    @staticmethod
    def verify_transitivity(binary_relation, input_set):
        """
        This method verifies if a given binary relation is transitive or not.

        Arguments:
        binary_relation - A subclass of the BinaryRelation class.

        input_set - A set closed under the binary relation.

        Return True if the binary relation in the given input set is transitive
        or False if it is not.
        """
        # TODO: Replace line below with actual code.
        conjunto = sorted(binary_relation.relation(input_set))
        contador = 0
        contador2 = 0
        for x in range(len(conjunto)-1):
            if (conjunto[x][1] == conjunto[x+1][0]):
                contador2 +=1
                if (conjunto[x][0],conjunto[x+1][1])in conjunto:
                    contador+=1
        if contador == contador2:
            return True
        else:
            return False

    @staticmethod
    def verify_antisymmetry(binary_relation, input_set):
        """
        This method verifies if a given binary relation is antisymmetric or not.

        Arguments:
        binary_relation - A subclass of the BinaryRelation class.

        input_set - A set closed under the binary relation.

        Return True if the binary relation in the given input set is
        antisymmetric or False if it is not.
        """
        # TODO: Replace line below with actual code.
        conjunto = binary_relation.relation(input_set)
        for x, y in conjunto:
            if(y,x)in conjunto and x != y:
                return False
        return True

    @staticmethod
    def verify_equivalency(binary_relation, input_set):
        """
        This method verifies if a given binary relation is an equivalence relation.

        Arguments:
        binary_relation - A subclass of the BinaryRelation class.

        input_set - A set closed under the binary relation.

        Return True if the binary relation in the given input set is
        an equivalence relation or False if it is not.
        """
        # TODO: Replace line below with actual code.
        relacao = BinaryRelationUtils
        if relacao.verify_reflexivity(binary_relation, input_set):
            if relacao.verify_symmetry(binary_relation, input_set):
                if relacao.verify_transitivity(binary_relation, input_set):
                    return True
        else:
            return False

    @staticmethod
    def get_partitioning(binary_relation, input_set):
        """
        This method first verifies if binary relation is an equivalence relation and, if it is, generates a partitioning of the input set using the binary relation. If the binary relation is not an equivalence relation, it returns None.

        Note: The partitioning of the set should be a list of subsets.

        Arguments:
        binary_relation - A subclass of the BinaryRelation class.

        input_set - A set closed under the binary relation.

        Return None if the binary relation is not an equivalence relation or a partitioning of the input set (e.g.: [{1, 3, 5, ...}, {2, 4, 6, ...}]) if it is an equivalence relation.
        """
        # TODO: Replace line below with actual code.
        conjunto = binary_relation.relation(input_set)
        particionamento = []
        relacao = BinaryRelationUtils

        if relacao.verify_equivalency(binary_relation, input_set):
            for x in input_set:
                particao = set()
                for y in input_set:
                    if (x, y) in conjunto:
                        particao.add(y)
                if particao not in particionamento:
                    particionamento.append(particao)
            return particionamento
        else:
            return []
