#!/usr/bin/env python3

class Coffee:
    """Represents a coffee item in the bookstore."""
    
    def __init__(self, size, price):
        self.size = size
        self.price = price

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        # Enforce strict size constraints
        valid_sizes = ["Small", "Medium", "Large"]
        if value in valid_sizes:
            self._size = value
        else:
            print("size must be Small, Medium, or Large")
            self._size = None

    def tip(self):
        """Applies a tip and updates the coffee price."""
        print("This coffee is great, here’s a tip!")
        # Increase price by 1 as per business logic
        self.price += 1

if __name__ == "__main__":
    # Example usage of the bookstore objects
    my_book = Book("The Great Gatsby", 200)
    my_book.turn_page()

    my_coffee = Coffee("Medium", 5)
    my_coffee.tip()