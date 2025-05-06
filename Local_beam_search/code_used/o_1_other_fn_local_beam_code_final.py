# This is the first file

import numpy as np


"""The following function, will generate 
    random n-Queens state with one queen per column.
    Hopefully"""
def generate_random_state(n):
    # reference for using .permutation() [1]  *
    return np.random.permutation(n)


"""The following function, will compute 
    the number of attacking queen pairs for a given state."""
def compute_attacking_pairs(state):
    n = len(state) # this makes sure, that n is equal to the number of states that are present and avoid any eror
    attacking_pairs = 0 # since, this is counting the number of attacking pair, they start at 0 and go up
    for i in range(n): # this checks the columns
        for j in range(i + 1, n): # this checks the rows
            
            # reference used to know how to check rows and diagonals[2] *
            if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j): # the first condition checks the rows, the second condition checks the diagonals. 
            #if in each condition the different values are equal, that means that the queens are attacking one another, and you add +1 to attacking_pairs
                # reference used for incrementing attacking pairs[3] *
                attacking_pairs += 1
    return attacking_pairs



"""The following code will generate all possible 
    successor states by moving a queen in each column."""
def generate_successors(state):
    n = len(state) # this makes sure, that n is equal to the number of states that are present and avoid any eror
    successors = [] # this is an empty list where all successor will be stored
    for col in range(n): # this checks if there are any queen in columns
        for row in range(n): # this checks if there are any queens in rows, and place the queen in each row
            
            # reference for knowing to use the following code [4]  *
            if state[col] != row: # this condition is for when there are no queen, or just one queen in the row, and will be important to avoid placing a queen in the same position
                
                # reference for knowing to use the following code [4] *
                new_state = state.copy() # the state is copied and kept in memory(so we don’t modify the original)
                
                # reference for knowing to use the following code[4] *
                new_state[col] = row # this updates the board by placing a queen in a new row.
                successors.append(new_state) # the resulting new_state( new board configuration) is appended to the above empty successor
    return successors # and the successors is returned


""" 
# Example usage
n = 8  # Board size

# Generate random state
random_state = generate_random_state(n)
print("Random Initial State:", random_state)

# Compute attacking pairs state
attacks = compute_attacking_pairs(random_state)
print("Number of Attacking Pairs:", attacks)

# Generate successors 
successors = generate_successors(random_state)
print("Number of Successors Generated:", len(successors))
""" 
