from IntervalValuedBipolarNeutrosophicElement import (
    IntervalValuedBipolarNeutrosophicElement,
)

class IntervalValuedBipolarNeutrosophicSet:
    def __init__(self):
        # Initialize an empty list to store elements and set the length to 0
        self.items = []
        self.len = 0

    def add_element(self, elt):
        # Add an element to the set
        if not isinstance(elt, IntervalValuedBipolarNeutrosophicElement):
            raise TypeError(
                "Please provide the element as Interval Valued Bipolar Neutrosophic Element!"
            )
        else:
            self.items.append(elt)
            self.len += 1

    def complement(self):
        # Compute the complement of the set
        complement_set = IntervalValuedBipolarNeutrosophicSet()
        for elt in self.items:
            complement_set.add_element(elt.complement())
        return complement_set

    def __eq__(self, other):
        # Check if two sets are equal
        if self.len != other.len:
            return False

        flag = False
        for i in range(self.len):
            if self.items[i] == other.items[i]:
                flag = True

            if not flag:
                return False

        return True

    def is_subset(self, other):
        # Check if one set is a subset of another
        if self.len != other.len:
            return False

        flag = False
        for i in range(self.len):
            if self.items[i].is_subset(other.items[i]):
                flag = True

            if not flag:
                return False

        return True

    def union(self, other):
        # Compute the union of two sets
        if self.len != other.len:
            raise TypeError("Sets are not of the same size!")

        union_set = IntervalValuedBipolarNeutrosophicSet()

        for i in range(self.len):
            union_set.add_element(self.items[i].union(other.items[i]))

        return union_set

    def intersection(self, other):
        # Compute the intersection of two sets
        if self.len != other.len:
            raise TypeError("Sets are not of the same size!")

        intersection_set = IntervalValuedBipolarNeutrosophicSet()

        for i in range(self.len):
            intersection_set.add_element(self.items[i].intersection(other.items[i]))

        return intersection_set

    def __add__(self, other):
        # Compute the addition of two sets
        if self.len != other.len:
            raise TypeError("Sets are not of the same size!")

        sum_set = IntervalValuedBipolarNeutrosophicSet()

        for i in range(self.len):
            sum_set.add_element(self.items[i] + other.items[i])

        return sum_set

    def __mul__(self, other):
        # Compute the multiplication of a set with another element or set
        product_set = IntervalValuedBipolarNeutrosophicSet()
        if isinstance(other, int):
            for i in range(self.len):
                product_set.add_element(self.items[i] * other)
        elif isinstance(other, IntervalValuedBipolarNeutrosophicSet):
            for i in range(self.len):
                product_set.add_element(self.items[i] * other.items[i])

        return product_set

    def score(self):
        # Compute the scores of elements in the set
        score_result = []

        for elt in self.items:
            score_result.append(elt.score())

        return score_result

    def accuracy(self):
        # Compute the accuracies of elements in the set
        accuracy_result = []

        for elt in self.items:
            accuracy_result.append(elt.accuracy())

        return accuracy_result

    def certainity(self):
        # Compute the certainties of elements in the set
        certainity_result = []

        for elt in self.items:
            certainity_result.append(elt.certainity())

        return certainity_result

    def __str__(self):
        # Convert the set to a string representation
        string_to_be_returned = "{\n"
        for i in range(self.len):
            if i + 1 >= self.len:
                string_to_be_returned += (
                    "" + str(self.items[i]).replace("[", "").replace("]", "") + "\n"
                )
            else:
                string_to_be_returned += (
                    "" + str(self.items[i]).replace("[", "").replace("]", "") + ",\n"
                )

        string_to_be_returned += "}"

        return string_to_be_returned