 # Problem: Given a sorted array of positive integers nums[] and a sum of value k,
 # find all unique combinations of integers from the nums[] array whose sum is equal to k.
 # Any integer in the array can be chosen an unlimited number of times.

def combination_sum(nums, target):
    combination_sum_helper(nums, target, pointer=0, combination=[], result=[])

def combination_sum_helper(nums, target, pointer, combination, result):
    # attempt to use each number in a combination, starting with smallest
    for i in range(pointer, len(nums)):
        # try each value in the combination
        combination.append(nums[i])
        target -= nums[i]
        # if we have not reached the target, add another number
        if target > 0:
            combination_sum_helper(nums, target, pointer, combination, result)
        # store valid solutions
        if target == 0:
            result.append(combination)
            return
        # if we went over target, backtrack
        if target < 0:
            combination.pop()
            target += nums[i]
            combination_sum_helper(nums, target, pointer+1, combination, result)

