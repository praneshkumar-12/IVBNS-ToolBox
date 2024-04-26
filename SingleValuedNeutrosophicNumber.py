class SingleValuedNeutrosophicNumber:
    def __init__(self, parent, truth, indeterminacy, falsity):
        assert parent is not None  # makes sure that each element has a parent
        assert 0 <= truth <= 1  # truth value range
        assert 0 <= indeterminacy <= 1  # indeterminacy value range
        assert 0 <= falsity <= 1  # falsity value range
        assert 0 <= truth + indeterminacy + falsity <= 3  # sum value range
        self.__parent = parent
        self.__truth = truth
        self.__indeterminacy = indeterminacy
        self.__falsity = falsity

    def __str__(self):
        return f"Parent: {self.__parent} ; Truth: {self.__truth} ; Indeterminacy: {self.__indeterminacy} ; Falsity: {self.__falsity}"
