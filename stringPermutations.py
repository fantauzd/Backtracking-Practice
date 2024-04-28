# Problem description: You are given a string of characters.
# You have to print all possible combinations of those characters (all permutations).
# You should not repeat any character. Assume that you will be given distinct characters in the string.

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


if __name__ == "__main__":
    permuations_backtracking("ABC")