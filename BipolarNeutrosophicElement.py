class BipolarNeutrosophicElement:
    def __init__(
        self,
        parent,
        truth_positive,
        truth_negative,
        indeterminacy_positive,
        indeterminacy_negative,
        falsity_positive,
        falsity_negative,
    ):
        assert parent is not None  # Ensure that each element has a parent
        assert -1 <= truth_negative <= 0 <= truth_positive <= 1  # Truth value ranges
        assert (
            -1 <= indeterminacy_negative <= 0 <= indeterminacy_positive <= 1
        )  # Indeterminacy value ranges
        assert (
            -1 <= falsity_negative <= 0 <= falsity_positive <= 1
        )  # Falsity value ranges
        assert (
            -3 <= (truth_positive + indeterminacy_positive + falsity_positive) <= 3
        )  # Sum value range for positive memberships
        assert (
            -3 <= (truth_negative + indeterminacy_negative + falsity_negative) <= 3
        )  # Sum value range for negative memberships
        self.__parent = parent
        self.__truth_positive = truth_positive
        self.__truth_negative = truth_negative
        self.__indeterminacy_positive = indeterminacy_positive
        self.__indeterminacy_negative = indeterminacy_negative
        self.__falsity_positive = falsity_positive
        self.__falsity_negative = falsity_negative

    def __str__(self):
        return (
            f"Parent: {self.__parent} ; Truth (Positive): {self.__truth_positive} ; Truth"
            f"(Negative): {self.__truth_negative} ; Indeterminacy (Positive):"
            f"{self.__indeterminacy_positive} ; Indeterminacy (Negative):"
            f"{self.__indeterminacy_negative} ; Falsity (Positive): {self.__falsity_positive} ;"
            f"Falsity (Negative): {self.__falsity_negative}"
        )
