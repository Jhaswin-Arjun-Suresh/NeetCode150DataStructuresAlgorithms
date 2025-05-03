# https://neetcode.io/problems/duplicate-integer
from typing import List
class Solution:
    # Solution 1- Brute Force.
    # Time Complexity - O(n^2).
    # Space complexity - O(1)
    def hasDuplicate(self, nums : List[int]) -> bool:
        size = len(nums)
        for i in range(size):
            for j in range(i + 1, size):
                if nums[i] == nums[j]:
                    return True
        return False
    # Solution 2 - Sorting.
    # Time Complexity - O(nlogn)
    # O(n) or O(1) - Depends on sorting algorithm.
    def hasDuplicate(self, nums : List[int]) -> bool:
        sorted_array = sorted(nums)
        size = len(nums)
        for i in range(size - 1):
            if sorted_array[i] == sorted_array[i + 1]:
                return True
        return False
    # Same Solution 2 - to avoid index out of range error.
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        size = len(nums)
        for i in range(1, size):
            if nums[i] == nums[i - 1]:
                return True
        return False
    # Solution 3 - Optimal Solution - HashSet.
    # Time Complexity: O(n)
    # Space Complexity - O(n)
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        size = len(nums)
        for i in range(size):
            if nums[i] in seen:
                return True
            seen.add(nums[i])
        return False
    # Solution 4 - Hash Set length.
    # Space Complexity - O(n)
    # Time complexity - Converting nums to a set is O(n).
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) < len(nums)

if __name__ == '__main__':
    solution = Solution()
    nums = [9,2,3,9,8,7,3] 
    print(solution.hasDuplicate(nums))
    # [2,3,3,7,8,9,9]
    # Output: true - There are duplicates in the array.
    nums = [1, 2, 3, 3]
    print(solution.hasDuplicate(nums))
    # Output: true - There are duplicates in the array.
    nums = [1, 2, 3, 4]
    print(solution.hasDuplicate(nums))
    # Output: false - There are no duplicates in the array.
    








