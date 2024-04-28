# Given a list of numbers, return a subsequence of non-consecutive numbers in the form of a
# list that would have the maximum sum. When the numbers are all negatives your code
# should return []

def max_independent_set(nums):
    """
    Finds a subsequence of non-consecutive numbers that has the maximum sum.
    If all numbers are negative, then an empty set [] will be considered maximum.
    :param nums: a list of numbers
    :return: a list of the non-consecutive numbers used to find the maximum sum
    """
    # build an array to store our solutions for a bottom-up approach
    solutions = [0] * (len(nums)+2)
    numbers_used = []
    # start from the base case and build up
    for i in range(2, len(nums)+2):
        # choose the optimal subsequence for each sub-problem
        if nums[i-2] + solutions[i-2] > solutions[i-1]:
            # Use a new number and the max substring that is not consecutive to it
            solutions[i] = nums[i-2] + solutions[i-2]
        else:
            # do not use the new number
            solutions[i] = solutions[i-1]

    j = len(nums) + 1 # last position in our solutions array

    # the sum of an optimal subsequence is at the last index of solutions
    total = solutions[j]
    # use solutions to determine which numbers were used
    while total > 0:
        # if the total changed then we used a new number
        if solutions[j] != solutions[j-1]:
            numbers_used.append(nums[j-2])
            # adjust the total and ignore the consecutive number
            total -= nums[j-2]
            j -= 2
        else:
            j-=1

    # perform a linear search on nums to ensure we include 0 if applicable
    if numbers_used == [] and 0 in nums:
        return [0]

    return numbers_used



if __name__ == "__main__":
    print(max_independent_set([-1, -1, 0, -34]))