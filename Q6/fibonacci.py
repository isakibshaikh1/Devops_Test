class FibonacciCalculator:
    def __init__(self, limit=100):
        """
        Initializes the FibonacciCalculator.

        Args:
        limit (int): The number of even Fibonacci numbers to sum. Default is 100.
        """
        self.limit = limit
        self.even_fib_sum = 0
        self.count = 0  # To keep track of how many even Fibonacci numbers we've found

    def generate_even_fibonacci(self):
        """
        Generates even Fibonacci numbers and calculates their sum
        until the specified limit is reached.
        """
        a, b = 1, 2  # Starting values for Fibonacci sequence

        while self.count < self.limit:
            if b % 2 == 0:
                self.even_fib_sum += b
                self.count += 1
            a, b = b, a + b  # Move to the next Fibonacci number

    def get_sum(self):
        """
        Returns the sum of the first 'limit' even Fibonacci numbers.
        """
        if self.count < self.limit:
            self.generate_even_fibonacci()
        return self.even_fib_sum

# Example usage
if __name__ == "__main__":
    calculator = FibonacciCalculator(limit=100)
    result = calculator.get_sum()
    print(f"The sum of the first 100 even-valued Fibonacci numbers is: {result}")
