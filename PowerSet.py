# Dominic Fantauzzo
# fantauzd
# CS 325 - 400
# Dynamic Programming and Backtracking

# Given a set of n distinct numbers return its power set.
import copy

def powerset(inputSet):
    """
    Given a set of n distinct numbers return its power set.
    :param inputSet: an array of distinct numbers
    :return: an array that is the power set of inputSet
    """
    # store results in an array
    result = []
    # initialize pointer to last index of the inputSet
    powerset_helper(len(inputSet)-1, [], inputSet, result)
    return result

def powerset_helper(pointer, choices_made, inputSet, result):
    """
    Helper function for powerset.
    :param pointer: A pointer for the number we are examining
    :param choices_made: an array of the numbers that we are considering
    :param inputSet: an array of numbers
    :param result: an array representing the power set of inputSet
    :return: None, modifying result in powerset()
    """
    # once we have decided to consider or not consider each element, the remaining combination is a result
    if pointer < 0:
        result.append(copy.deepcopy(choices_made))
        return

    # at each number we can either consider the number or not consider the number
    choices_made.append(inputSet[pointer]) # consider the number
    powerset_helper(pointer-1, choices_made, inputSet, result)
    choices_made.pop() # do not consider the number
    powerset_helper(pointer-1, choices_made, inputSet, result)



if __name__ == "__main__":
    print(powerset([1, 2, 3]))