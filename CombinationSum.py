 # Problem: Given a sorted array of positive integers nums[] and a sum of value k,
 # find all unique combinations of integers from the nums[] array whose sum is equal to k.
 # Any integer in the array can be chosen an unlimited number of times.

from copy import deepcopy
def combination_sum(nums, target):
    result = []
    combination_sum_helper(nums, target, result, pointer=0, combination=[])
    return result

def combination_sum_helper(nums, target, result, pointer, combination):
    # store valid solutions
    if target == 0:
        result.append(deepcopy(combination))
        return
    # if we went over target, backtrack
    if target < 0:
        return
    # attempt to use each number in a combination, starting with smallest
    for i in range(pointer, len(nums)):
        # try each value in the combination
        combination.append(nums[i])
        combination_sum_helper(nums, target - nums[i], result, i, combination)
        # backtrack
        combination.pop()

if __name__ == "__main__":
    print(combination_sum([1, 2, 3, 6, 7], 7))