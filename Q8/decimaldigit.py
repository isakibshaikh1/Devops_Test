class DecimalDigitTransformer:
    def __init__(self, digit):
        """
        Initializes the DecimalDigitTransformer with a given digit.

        Args:
        digit (int): A single decimal digit (0-9).
        """
        self.digit = digit

    def validate_input(self):
        """
        Validates if the input is a single decimal digit (0-9).

        Returns:
        bool: True if valid, False otherwise.
        """
        return isinstance(self.digit, int) and 0 <= self.digit <= 9

    def transform(self):
        """
        Calculates the sum: X + XX + XXX + XXXX.

        Returns:
        int: The calculated sum if the input is valid.

        Raises:
        ValueError: If the input is invalid.
        """
        if not self.validate_input():
            raise ValueError(f"Invalid input: {self.digit}. Please provide a single digit between 0 and 9.")

        # Creating the numbers dynamically
        x = str(self.digit)
        result = int(x) + int(x*2) + int(x*3) + int(x*4)
        return result

# Example usage
if __name__ == "__main__":
    try:
        # Get input from the user
        user_input = int(input("Enter a single decimal digit (0-9): "))
        transformer = DecimalDigitTransformer(user_input)
        result = transformer.transform()
        print(f"The transformed value is: {result}")
    except ValueError as e:
        print(f"Error: {e}")
