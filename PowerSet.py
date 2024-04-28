# Given a set of n distinct numbers return its power set.
import copy

def powerset_backtracking(inputSet):
    result = []
    powerset(len(inputSet)-1, [], inputSet, result)
    return result
def powerset(pointer, choices_made, inputSet, result):
    if pointer < 0:
        result.append(copy.deepcopy(choices_made))
        return

    choices_made.append(inputSet[pointer])
    powerset(pointer-1, choices_made, inputSet, result)

    choices_made.pop()
    powerset(pointer-1, choices_made, inputSet, result)



if __name__ == "__main__":
    print(powerset_backtracking("ABC"))