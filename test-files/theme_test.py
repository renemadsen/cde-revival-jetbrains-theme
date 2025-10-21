#!/usr/bin/env python3
"""
Test file to demonstrate the CDE Revival Theme syntax highlighting for Python.
This file includes various Python language constructs to showcase
the theme's color scheme for different code elements.

Author: René Schultz Madsen
Version: 1.0.0
"""

import sys
import os
from typing import List, Optional, Dict
from dataclasses import dataclass

# Constants - should appear in purple/violet
THEME_NAME = "CDE Revival Theme"
MAX_ITEMS = 100


@dataclass
class ThemeTestData:
    """Data class to demonstrate class and type highlighting."""
    
    name: str
    value: int
    items: List[str]
    
    def __post_init__(self):
        """Initialize after dataclass creation."""
        if self.value < 0:
            raise ValueError("Value must be non-negative")


class ThemeTest:
    """
    Test class demonstrating Python syntax highlighting.
    
    This class includes various Python constructs to showcase
    how the theme handles different code elements.
    """
    
    def __init__(self, name: str):
        """
        Constructor demonstrating keywords, types, and strings.
        
        Args:
            name: The name parameter
        """
        self.name = name  # Instance variable
        self.items: List[str] = []
        self._private_value = 0
    
    def add_item(self, value: int) -> bool:
        """
        Method to show function highlighting and type hints.
        Keywords like 'def', 'if', 'else', 'return' should be bold.
        
        Args:
            value: An integer value
            
        Returns:
            True if the value is valid, False otherwise
        """
        # Comments should appear in grey and italic
        if value > MAX_ITEMS:
            print(f"Error: Value {value} exceeds maximum", file=sys.stderr)
            return False
        elif value < 0:
            print(f"Warning: Negative value {value}")
            return False
        
        # String literals should be green
        # f-strings with interpolation
        item = f"Item #{value}"
        self.items.append(item)
        
        return True
    
    def demonstrate_operators(self):
        """Demonstrates various operators and numeric literals."""
        # Numeric literals - should appear in purple
        decimal = 42
        floating = 3.14159
        binary = 0b101010
        hexadecimal = 0x2A
        
        # Mathematical operators
        result = decimal + 10 - 5 * 2 / 3
        comparison = (result > 0) and (result < 100) or (result == 42)
        
        # Bitwise operators
        bitwise = decimal & 0xFF | 0x10 ^ 0x05
        
        # String operations
        text = "Hello" + " " + "World"
        repeated = "CDE " * 3
    
    def modern_python_features(self):
        """Shows modern Python features like comprehensions and generators."""
        # List comprehension
        squares = [x ** 2 for x in range(10) if x % 2 == 0]
        
        # Dictionary comprehension
        square_dict = {x: x ** 2 for x in range(5)}
        
        # Set comprehension
        unique_squares = {x ** 2 for x in range(-5, 5)}
        
        # Generator expression
        even_numbers = (x for x in range(100) if x % 2 == 0)
        
        # Lambda functions
        items_filtered = list(filter(lambda x: len(x) > 5, self.items))
        items_mapped = list(map(lambda x: x.upper(), self.items))
    
    def context_managers(self):
        """Demonstrates context managers and file operations."""
        # With statement
        with open('test.txt', 'r') as file:
            content = file.read()
        
        # Multiple context managers
        with open('input.txt', 'r') as infile, \
             open('output.txt', 'w') as outfile:
            outfile.write(infile.read())
    
    def exception_handling(self):
        """Shows exception handling constructs."""
        try:
            # Try block with potential error
            result = 10 / 0
        except ZeroDivisionError as e:
            # Specific exception handling
            print(f"Error: {e}")
        except Exception as e:
            # General exception handling
            print(f"Unexpected error: {e}")
        else:
            # Executed if no exception occurs
            print("Success!")
        finally:
            # Always executed
            print("Cleanup complete")
    
    @staticmethod
    def static_method() -> str:
        """Static method demonstration."""
        return "This is a static method"
    
    @classmethod
    def class_method(cls) -> str:
        """Class method demonstration."""
        return f"This is a class method of {cls.__name__}"
    
    @property
    def private_value(self) -> int:
        """Property getter demonstration."""
        return self._private_value
    
    @private_value.setter
    def private_value(self, value: int):
        """Property setter demonstration."""
        if value >= 0:
            self._private_value = value


def main():
    """
    Main function for testing.
    
    TODO: Add more test cases
    FIXME: Handle edge cases better
    """
    # Create test instance
    test = ThemeTest("CDE Theme Test")
    
    # Loop structures
    for i in range(10):
        test.add_item(i)
    
    # Enumerate
    for index, item in enumerate(test.items):
        print(f"{index}: {item}")
    
    # While loop
    counter = 0
    while counter < 5:
        print(f"Counter: {counter}")
        counter += 1
    
    # Match statement (Python 3.10+)
    # Uncomment if using Python 3.10+
    # status = 200
    # match status:
    #     case 200:
    #         print("OK")
    #     case 404:
    #         print("Not Found")
    #     case _:
    #         print("Unknown status")
    
    # Exception handling
    test.exception_handling()
    
    # Print test results
    print(f"Test complete: {test.name}")
    print(f"Items added: {len(test.items)}")


if __name__ == "__main__":
    main()
