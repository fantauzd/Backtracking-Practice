# Problem description: You are given a string of characters.
# You have to print all possible combinations of those characters (all permutations).
# You should not repeat any character. Assume that you will be given distinct characters in the string.
import copy


def permuations_backtracking(str):
    permutations([],str)

def permutations(result, str):
    #base Case, print the result when we obtain the result using all characters
    if(len(result) == len(str)):
        print(''.join(result))

    for i in range(len(str)):
        current_choice = str[i]
        # If the choice was not already made we chose it to include in our result
        if(current_choice not in result):
            result.append(current_choice)
            #recursively calling permutations function until we obtain our result
            permutations(result, str)
            #Once we have exhausted all possible paths we backtrack
            result.pop()

# Given a set of n distinct numbers return its power set.

def powerset_backtracking(input):
    result = []
    powerset(len(input)-1, [], input, result)
    return result
def powerset(pointer, choices_made, input, result):
    if pointer < 0:
        result.append(copy.deepcopy(choices_made))
        return

    choices_made.append(input[pointer])
    powerset(pointer-1, choices_made, input, result)

    choices_made.pop()
    powerset(pointer-1, choices_made, input, result)



if __name__ == "__main__":
    print(powerset_backtracking("ABC"))