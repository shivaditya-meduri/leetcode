# Problem link : https://leetcode.com/problems/design-a-number-container-system/description/?envType=daily-question&envId=2025-02-08
### Clean implementation
import heapq
class minSet:
    def __init__(self):
        # O(1) indexing, adding and removing
        # O(1) return minimum of the set
        self.data = set()
        self.minheap = []
    def add(self, elem):
        self.data.add(elem)
        heapq.heappush(self.minheap, elem)
    def remove(self, elem):
        # Remove the element only from the set
        # Lazy removal of elements from heap
        self.data.remove(elem)
    def min(self):
        while self.minheap:
            if self.minheap[0] not in self.data:
                heapq.heappop(self.minheap)
            else:
                return self.minheap[0]
        return -1
        
    
class NumberContainers:
    def __init__(self):
        self.data = {} # Store index : Number
        self.rev_data = {} # Store number : Indexes
    def change(self, index: int, number: int) -> None:
        if index in self.data:
            prev_num = self.data[index]
            self.rev_data[prev_num].remove(index)
            self.data[index] = number
            if number in self.rev_data:
                self.rev_data[number].add(index)
            else:
                self.rev_data[number] = minSet()
                self.rev_data[number].add(index)
        else:
            self.data[index] = number
            if number in self.rev_data:
                self.rev_data[number].add(index)
            else:
                self.rev_data[number] = minSet()
                self.rev_data[number].add(index)
    def find(self, number: int) -> int:
        if number in self.rev_data:
            return self.rev_data[number].min()
        else:
            return -1
    
