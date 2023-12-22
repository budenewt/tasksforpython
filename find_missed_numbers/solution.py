def findMissedNumbers(nums):
     n = len(nums)
     # Create a set from the incoming list for quick search
     num_set = set(nums)
     # Create a list of missing numbers
     missed_numbers = [i for i in range(1, n + 1) if i not in num_set]
     return missed_numbers

# Examples of using
result1 = findMissedNumbers([4, 3, 2, 7, 8, 2, 3, 1])
print(result1) # Output: [5, 6]

result2 = findMissedNumbers([1, 1, 1])
print(result2) # Output: [2, 3]
