# Problem link : https://leetcode.com/problems/product-of-the-last-k-numbers/description/?envType=daily-question&envId=2025-02-14
'''
Problem description:
Product of the last k numbers of the stream
Design an algorithm that accepts a stream of integers and retrieves the product of the last k integers of the stream.

Implement the ProductOfNumbers class:

ProductOfNumbers() Initializes the object with an empty stream.
void add(int num) Appends the integer num to the stream.
int getProduct(int k) Returns the product of the last k numbers in the current list. You can assume that always the current list has at least k numbers.
The test cases are generated so that, at any time, the product of any contiguous sequence of numbers will fit into a single 32-bit integer without overflowing.
'''
class ProductOfNumbers:
    def __init__(self):
        self.prefix_products = [1]  # Start with multiplicative identity

    def add(self, num: int) -> None:
        if num == 0:
            # A zero resets the running product
            self.prefix_products = [1]
        else:
            self.prefix_products.append(self.prefix_products[-1] * num)

    def getProduct(self, k: int) -> int:
        # If k is at least as large as the current product streak, there was a zero.
        if k >= len(self.prefix_products):
            return 0
        # Otherwise, compute the product of the last k numbers.
        return self.prefix_products[-1] // self.prefix_products[-k-1]
