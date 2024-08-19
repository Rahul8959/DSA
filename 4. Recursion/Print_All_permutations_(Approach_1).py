from typing import List

# Recursive function to generate permutations
# nums: List of numbers to permute
# freq: List to keep track of used elements
# ds: Temporary list to store the current permutation
# ans: List to store all permutations
def recurPermute(nums: List[int], freq: List[int], ds: List[int], ans: List[List[int]]):
    # Base case: If the current permutation is complete (same length as nums)
    if len(ds) == len(nums):
        ans.append(ds.copy())  # Add a copy of the current permutation to the answer list
        return  # Backtrack

    # Iterate through each element in the nums list
    for i in range(len(nums)):
        # If the current element has not been used in the current permutation
        if not freq[i]:
            ds.append(nums[i])  # Add the element to the current permutation
            freq[i] = 1  # Mark the element as used
            recurPermute(nums, freq, ds, ans)  # Recur to add more elements to the permutation
            freq[i] = 0  # Unmark the element (backtrack)
            ds.pop()  # Remove the last element added (backtrack)

# Function to initialize necessary lists and call the recursive function
def permute(nums: List[int]) -> List[List[int]]:
    ans = []  # List to store all permutations
    ds = []  # Temporary list to store the current permutation
    freq = [0] * len(nums)  # Frequency list initialized to 0 (indicating no elements are used)
    recurPermute(nums, freq, ds, ans)  # Call the recursive function to generate permutations
    return ans  # Return the list of all permutations

# Generate permutations for the list [1, 2, 3] and print them directly
x=input("Enter: ")
v = [int(x) for x in x.split()]  # The input list for which permutations are to be generated
permutations = permute(v)  # Generate all permutations of the list
print("All Permutations are:")  # Print a header
for perm in permutations:  # Iterate through each permutation
    print(" ".join(map(str, perm)))  # Print each permutation as a space-separated string
