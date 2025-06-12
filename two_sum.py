from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}  # Initialize an empty dictionary to store numbers and their indices

        # Iterate through the list of numbers with their indices
        for i, num in enumerate(nums):
            # Calculate the complement needed to reach the target
            complement = target - num

            # Check if the complement is already in our 'seen' dictionary
            if complement in seen:
                # If found, we have the two numbers. Return their indices.
                # seen[complement] gives the index of the complement
                # i is the index of the current number
                return [seen[complement], i]

            # If the complement is not found, add the current number and its index to 'seen'
            # This prepares for future iterations where 'num' might be the complement for another number
            seen[num] = i

        # If no two numbers are found that sum up to the target after checking all numbers,
        # return an empty list. (Though for this problem, it's typically guaranteed a solution exists).
        return []


# Assuming the Solution class is defined as you provided
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         # ... (rest of your code)

# Create an instance (object) of the Solution class
my_solution_object = Solution()

# Now you can use this object to call the twoSum method
nums_example = [2, 7, 11, 15]
target_example = 9
result = my_solution_object.twoSum(nums_example, target_example)

print(f"For nums={nums_example} and target={target_example}, the indices are: {result}")