class IntervalValuedBipolarNeutrosophicElement:
    def __init__(
        self,
        parent,
        truth_pos_left,
        truth_pos_right,
        indeterminacy_pos_left,
        indeterminacy_pos_right,
        falsity_pos_left,
        falsity_pos_right,
        truth_neg_left,
        truth_neg_right,
        indeterminacy_neg_left,
        indeterminacy_neg_right,
        falsity_neg_left,
        falsity_neg_right,
    ):
        # Ensure input values are within valid ranges
        assert 0 <= truth_pos_left <= 1
        assert 0 <= truth_pos_right <= 1
        assert 0 <= indeterminacy_pos_left <= 1
        assert 0 <= indeterminacy_pos_right <= 1
        assert 0 <= falsity_pos_left <= 1
        assert 0 <= falsity_pos_right <= 1
        assert -1 <= truth_neg_left <= 0
        assert -1 <= truth_neg_right <= 0
        assert -1 <= indeterminacy_neg_left <= 0
        assert -1 <= indeterminacy_neg_right <= 0
        assert -1 <= falsity_neg_left <= 0
        assert -1 <= falsity_neg_right <= 0

        # Assign input values to instance variables
        self.parent = parent
        self.truth_pos_left = truth_pos_left
        self.truth_pos_right = truth_pos_right
        self.indeterminacy_pos_left = indeterminacy_pos_left
        self.indeterminacy_pos_right = indeterminacy_pos_right
        self.falsity_pos_left = falsity_pos_left
        self.falsity_pos_right = falsity_pos_right
        self.truth_neg_left = truth_neg_left
        self.truth_neg_right = truth_neg_right
        self.indeterminacy_neg_left = indeterminacy_neg_left
        self.indeterminacy_neg_right = indeterminacy_neg_right
        self.falsity_neg_left = falsity_neg_left
        self.falsity_neg_right = falsity_neg_right

    def __str__(self):
        # Format string representation of the object
        return (
            f"<{self.parent},"
            f"[{round(self.truth_pos_left, 3)},{round(self.truth_pos_right, 3)}],"
            f"[{round(self.indeterminacy_pos_left, 3)},{round(self.indeterminacy_pos_right, 3)}],"
            f"[{round(self.falsity_pos_left, 3)},{round(self.falsity_pos_right, 3)}],"
            f"[{round(self.truth_neg_left, 3)},{round(self.truth_neg_right, 3)}],"
            f"[{round(self.indeterminacy_neg_left, 3)},{round(self.indeterminacy_neg_right, 3)}],"
            f"[{round(self.falsity_neg_left, 3)},{round(self.falsity_neg_right, 3)}]>"
        )

    def complement(self):
        # Compute the complement of the interval-valued bipolar neutrosophic element
        return IntervalValuedBipolarNeutrosophicElement(
            self.parent,
            1 - self.truth_pos_right,
            1 - self.truth_pos_left,
            1 - self.indeterminacy_pos_right,
            1 - self.indeterminacy_pos_left,
            1 - self.falsity_pos_right,
            1 - self.falsity_pos_left,
            -1 - self.truth_neg_right,
            -1 - self.truth_neg_left,
            -1 - self.indeterminacy_neg_right,
            -1 - self.indeterminacy_neg_left,
            -1 - self.falsity_neg_right,
            -1 - self.falsity_neg_left,
        )

    def __eq__(self, other):
        # Check if two interval-valued bipolar neutrosophic elements are equal
        if (
            self.parent == other.parent
            and self.truth_pos_left == other.truth_pos_left
            and self.truth_pos_right == other.truth_pos_right
            and self.indeterminacy_pos_left == other.indeterminacy_pos_left
            and self.indeterminacy_pos_right == other.indeterminacy_pos_right
            and self.falsity_pos_left == other.falsity_pos_left
            and self.falsity_pos_right == other.falsity_pos_right
            and self.truth_neg_left == other.truth_neg_left
            and self.truth_neg_right == other.truth_neg_right
            and self.indeterminacy_neg_left == other.indeterminacy_neg_left
            and self.indeterminacy_neg_right == other.indeterminacy_neg_right
            and self.falsity_neg_left == other.falsity_neg_left
            and self.falsity_neg_right == other.falsity_neg_right
        ):
            return True

        return False

    def is_subset(self, other):
        # Check if one interval-valued bipolar neutrosophic element is a subset of another
        if (
            self.parent == other.parent
            and self.truth_pos_left <= other.truth_pos_left
            and self.truth_pos_right <= other.truth_pos_right
            and self.indeterminacy_pos_left >= other.indeterminacy_pos_left
            and self.indeterminacy_pos_right >= other.indeterminacy_pos_right
            and self.falsity_pos_left >= other.falsity_pos_left
            and self.falsity_pos_right >= other.falsity_pos_right
            and self.truth_neg_left <= other.truth_neg_left
            and self.truth_neg_right <= other.truth_neg_right
            and self.indeterminacy_neg_left >= other.indeterminacy_neg_left
            and self.indeterminacy_neg_right >= other.indeterminacy_neg_right
            and self.falsity_neg_left >= other.falsity_neg_left
            and self.falsity_neg_right >= other.falsity_neg_right
        ):
            return True

        return False

    def union(self, other):
        # Compute the union of two interval-valued bipolar neutrosophic elements
        return IntervalValuedBipolarNeutrosophicElement(
            self.parent,
            max(self.truth_pos_left, other.truth_pos_left),
            max(self.truth_pos_right, other.truth_pos_right),
            min(self.indeterminacy_pos_left, other.indeterminacy_pos_left),
            min(self.indeterminacy_pos_right, other.indeterminacy_pos_right),
            min(self.falsity_pos_left, other.falsity_pos_left),
            min(self.falsity_pos_right, other.falsity_pos_right),
            min(self.truth_neg_left, other.truth_neg_left),
            min(self.truth_neg_right, other.truth_neg_right),
            max(self.indeterminacy_neg_left, other.indeterminacy_neg_left),
            max(self.indeterminacy_neg_right, other.indeterminacy_neg_right),
            max(self.falsity_neg_left, other.falsity_neg_left),
            max(self.falsity_neg_right, other.falsity_neg_right),
        )

    def intersection(self, other):
        # Compute the intersection of two interval-valued bipolar neutrosophic elements
        return IntervalValuedBipolarNeutrosophicElement(
            self.parent,
            min(self.truth_pos_left, other.truth_pos_left),
            min(self.truth_pos_right, other.truth_pos_right),
            max(self.indeterminacy_pos_left, other.indeterminacy_pos_left),
            max(self.indeterminacy_pos_right, other.indeterminacy_pos_right),
            max(self.falsity_pos_left, other.falsity_pos_left),
            max(self.falsity_pos_right, other.falsity_pos_right),
            max(self.truth_neg_left, other.truth_neg_left),
            max(self.truth_neg_right, other.truth_neg_right),
            min(self.indeterminacy_neg_left, other.indeterminacy_neg_left),
            min(self.indeterminacy_neg_right, other.indeterminacy_neg_right),
            min(self.falsity_neg_left, other.falsity_neg_left),
            min(self.falsity_neg_right, other.falsity_neg_right),
        )

    def __add__(self, other):
        # Compute the addition of two interval-valued bipolar neutrosophic elements
        return IntervalValuedBipolarNeutrosophicElement(
            self.parent,
            self.truth_pos_left
            + other.truth_pos_left
            - (self.truth_pos_left * other.truth_pos_left),
            self.truth_pos_right
            + other.truth_pos_right
            - (self.truth_pos_right * other.truth_pos_right),
            self.indeterminacy_pos_left * other.indeterminacy_pos_left,
            self.indeterminacy_pos_right * other.indeterminacy_pos_right,
            self.falsity_pos_left * other.falsity_pos_left,
            self.falsity_pos_right * other.falsity_pos_right,
            -1 * self.truth_neg_left * other.truth_neg_left,
            -1 * self.truth_neg_right * other.truth_neg_right,
            -1
            * (
                (-1 * self.indeterminacy_neg_left)
                - other.indeterminacy_neg_left
                - (self.indeterminacy_neg_left * other.indeterminacy_neg_left)
            ),
            -1
            * (
                (-1 * self.indeterminacy_neg_right)
                - other.indeterminacy_neg_right
                - (self.indeterminacy_neg_right * other.indeterminacy_neg_right)
            ),
            -1
            * (
                (-1 * self.falsity_neg_left)
                - other.falsity_neg_left
                - (self.falsity_neg_left * other.falsity_neg_left)
            ),
            -1
            * (
                (-1 * self.falsity_neg_right)
                - other.falsity_neg_right
                - (self.falsity_neg_right * other.falsity_neg_right)
            ),
        )

    def __mul__(self, other):
        # Compute the multiplication of an interval-valued bipolar neutrosophic element with another element
        if isinstance(other, int):
            return IntervalValuedBipolarNeutrosophicElement(
                self.parent,
                1 - pow(1 - self.truth_pos_left, other),
                1 - pow(1 - self.truth_pos_right, other),
                pow(self.indeterminacy_pos_left, other),
                pow(self.indeterminacy_pos_right, other),
                pow(self.falsity_pos_left, other),
                pow(self.falsity_pos_right, other),
                -1 * pow(-1 * self.truth_neg_left, other),
                -1 * pow(-1 * self.truth_neg_right, other),
                -1 * pow(-1 * self.indeterminacy_neg_left, other),
                -1 * pow(-1 * self.indeterminacy_neg_right, other),
                -1 * (1 - pow(1 - (-1 * self.falsity_neg_left), other)),
                -1 * (1 - pow(1 - (-1 * self.falsity_neg_right), other)),
            )
        else:
            return IntervalValuedBipolarNeutrosophicElement(
                self.parent,
                self.truth_pos_left * other.truth_pos_left,
                self.truth_pos_right * other.truth_pos_right,
                self.indeterminacy_pos_left
                + other.indeterminacy_pos_left
                - (self.indeterminacy_pos_left * other.indeterminacy_pos_left),
                self.indeterminacy_pos_right
                + other.indeterminacy_pos_right
                - (self.indeterminacy_pos_right * other.indeterminacy_pos_right),
                self.falsity_pos_left
                + other.falsity_pos_left
                - (self.falsity_pos_left * other.falsity_pos_left),
                self.falsity_pos_right
                + other.falsity_pos_right
                - (self.falsity_pos_right * other.falsity_pos_right),
                -1
                * (
                    (-1 * self.truth_neg_left)
                    - other.truth_neg_left
                    - (self.truth_neg_left * other.truth_neg_left)
                ),
                -1
                * (
                    (-1 * self.truth_neg_right)
                    - other.truth_neg_right
                    - (self.truth_neg_right * other.truth_neg_right)
                ),
                -1 * self.indeterminacy_neg_left * other.indeterminacy_neg_left,
                -1 * self.indeterminacy_neg_right * other.indeterminacy_neg_right,
                -1 * self.falsity_neg_left * other.falsity_neg_left,
                -1 * self.falsity_neg_right * other.falsity_neg_right,
            )

    def score(self):
        # Compute the score of the interval-valued bipolar neutrosophic element
        return (1 / 12) * (
            self.truth_pos_left
            + self.truth_pos_right
            + 1
            - self.indeterminacy_pos_left
            + 1
            - self.indeterminacy_pos_right
            + 1
            - self.falsity_pos_left
            + 1
            - self.falsity_pos_right
            + 1
            + self.truth_neg_left
            + 1
            + self.truth_neg_right
            - self.indeterminacy_neg_left
            - self.indeterminacy_neg_right
            - self.falsity_neg_left
            - self.falsity_neg_right
        )

    def accuracy(self):
        # Compute the accuracy of the interval-valued bipolar neutrosophic element
        return (
            self.truth_pos_left
            + self.truth_pos_right
            - self.falsity_pos_left
            - self.falsity_pos_right
            + self.truth_neg_left
            + self.truth_neg_right
            - self.falsity_neg_left
            - self.falsity_neg_right
        )

    def certainity(self):
        # Compute the certainty of the interval-valued bipolar neutrosophic element
        return (
            self.truth_pos_left
            + self.truth_pos_right
            - self.falsity_neg_left
            - self.falsity_neg_right
        )