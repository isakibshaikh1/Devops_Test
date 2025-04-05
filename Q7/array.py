class ArrayIntersection:
    def __init__(self, array1, array2):
        """
        Initializes the ArrayIntersection with two sorted arrays.

        Args:
        array1 (list): First sorted array of integers.
        array2 (list): Second sorted array of integers.
        """
        self.array1 = array1
        self.array2 = array2

    def find_intersection(self):
        """
        Finds the intersection of the two sorted arrays without duplicates
        using the two-pointer technique for efficiency.

        Returns:
        list: A list containing numbers common to both arrays.
        """
        i, j = 0, 0  # Pointers for array1 and array2
        result = []  # To store the common elements

        while i < len(self.array1) and j < len(self.array2):
            # Skip duplicates in both arrays
            while i > 0 and i < len(self.array1) and self.array1[i] == self.array1[i - 1]:
                i += 1
            while j > 0 and j < len(self.array2) and self.array2[j] == self.array2[j - 1]:
                j += 1

            # Compare elements from both arrays
            if self.array1[i] == self.array2[j]:
                result.append(self.array1[i])
                i += 1
                j += 1
            elif self.array1[i] < self.array2[j]:
                i += 1
            else:
                j += 1

        return result

# Example usage
if __name__ == "__main__":
    array1 = [1, 2, 4, 5, 6]
    array2 = [2, 3, 5, 7]

    intersection = ArrayIntersection(array1, array2)
    common_elements = intersection.find_intersection()

    print(f"Common elements: {common_elements}")
