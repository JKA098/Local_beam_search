# This is the second file

import time

import pandas as pd

import numpy as np

from o_1_other_fn_local_beam_code_final import generate_random_state, compute_attacking_pairs, generate_successors

class LocalBeamSearch:
    # reference for how and where I learned why to use classes are used [5],[6],[7]. *
    """The following is a class for the
    Local Beam Search Algorithm for solving the n-Queens problem.
    Written this way it is easier to read and debug"""
    

    # reference for knowing to start with __init__: [5],[6],[7]. *
    """This function initialize the class 
        LocalBeamSearch and the search parameters."""
    def __init__(self, n, k, max_iterations=1000):
        self.n = n # n will represent the number of queens 
        self.k = k # k will represent the number of states
        self.max_iterations = max_iterations # represents the maximum amount of iterations possible, just to make sure it does not run for ever
        self.states = []  # Stores the k current states
        self.start_time = None  # Tracks execution time to know how much it took

    # for debugging purpose, most function will have some sort of try/except method/function, used to make it easy when debugging.


    """The following function generates k random initial states."""
    def initialize_states(self):
        self.states = [] # this initialise an empty state that will store all the random states. Furthermore, because,we are inside a class, we must use 'self'whenever we call states for consistency.
        
        # reference of where I learned to use an underscore [3]. *
        for _ in range(self.k): # this for a loop
            try:
                state = generate_random_state(self.n)  # this will generate a random state
                self.states.append(state)  # this will append state to empty variable self.states
            except ValueError:  # this is wrapped in a try except, so that if there is an error, it can be debugged easilly
                print("⚠️ There is an issue with initialize_states()")




    """this function computes heuristic values (aka, the number of attacking pairs) for a given states."""
    def compute_scores(self, states):
        scores = []  # this initialize an empty list used later for storing
        try:
            for state in states:  # this iterate through each state in the list
                score = compute_attacking_pairs(state)  # this compute the heuristic value (number of attacking pairs)
                
                # reference for why use tuple[8]. * 
                state_tuple = tuple(state)  # this code convert state to a tuple, that way it can be stored safely without being modified everytime it is called.
                
                scores.append((score, state_tuple))  # this append heuristic and state to scores, created above
            
            scores.sort(key=lambda x: x[0])  # this is done to make it easy to see which score is the best. In short, it sort scores based on the number of attacking pairs (lower is better)
        except ValueError:  # exception syntax
                print("⚠️ There is an issue with compute_scores()")

        return scores  # Return the sorted list of (score, state) pairs


    
    """This function selects the top k states from the sorted scores list."""
    def select_best_states(self, scores):
        selected_states = [] # this is an empty list, that will be used later.
        try:
            """
            this code is slightly complex but at its core is relatively easy to understand.
            first, the loop, go through the states k, and the scores.
            however, to avoid making mistakes, we need to make sure that the loop, stays within a given range. 
            and in this case, the range is the amount of k(self.k, because we are inside a class) states available and scores.
            and we have to select the lowest score.

            second, since previously, scores was turned into a tuple for safe storing, we need to convert it to a list.
            scores[i][1]: could be the most confusing part, but all it does, is select the second element of the tuple scores; which is none 
            other than the state.
            and lastly the state is appended to selected_states, and returns it.
            """
            for i in range(min(self.k, len(scores))): 
                # reference used to figure out to use scores[i][1]: [9]. * 
                selected_states.append(list(scores[i][1]))

        except ValueError:  #  exception syntax
                print("⚠️ There is an issue with selected_states()")
        return selected_states

    

    """This function generates successors states for each state and computes their scores."""
    def generate_successor_states(self, scores):
        all_successors = [] #this is an empty list, that will be used later
        try:

            for score, state in scores:  # Loop through each state, from scores inside of which there is a score and state
                state_array = np.array(state)  # this convert to NumPy array, mostly just in case, other function might not accept tuples
                successors = generate_successors(state_array)  # this generate successors using the generate_successors function created above.
                
                # reference for knowing to use extend [10]. * 
                all_successors.extend(successors)  # this add the successors generated to the empty list above. Notice that it is different from others that used append. and this is because we want each state to be added individually, not replace the previous state. At least that is what the code claims to do.
                # fun fact, 'score, state' can be replaced by a single underscore: _

        
        except ValueError:  #  exception syntax
                print("⚠️ There is an issue with generate_successor_states()")

        return self.compute_scores(all_successors)  # this return the computed heuristic values for successors, by using the above function compute_scores.
        # the actual reason why the above return code works, is very uknown to even myself, all I know is that, the result is different if you don't use it, 
        # and I have had to debate with gemini for several hours, and I still did not understand. But it works.

    

    
    """
        This function checks for solutions or local minima.
        Another way to put it is that; check_termination() is responsible for 
        deciding when the Local Beam Search algorithm should stop.
        """
    def check_termination(self, scores):
        # like with all the others, it firsts get wrapped in a try/except method.
        try:
            for score, state in scores:  # first the Loop. with the first condition
                if score == 0:  # this code Checks if a solution was found. In this case, the solution would be a score of 0. that is 0 attacking pairs
                    # reference for how to find runtime for answering question 3 and 4 [11]. * 
                    runtime = time.time() - self.start_time # if it gets reached, check how long it took to reach that solution. 
                    
                    print(f"✅ Solution Found! Board: {list(state)}, Attacks: {score}, Time: {runtime:.4f}s") # print the solution. the state is printed as an array, the score is printed as well, the runtime is also printed with 4 decimal values after.
                    return list(state), score, runtime  # this code return the solution
            
            # the following will check if the code is stuck
            # reference used to find out that I should use is_true[12]. * 
            is_stuck = True  # the following is a flag. that can be used and reused. Also I learned it from: Python Crash course. 
            
            best_score = scores[0][0]  # this defines what the best score is supposed to be like. in this case it Extracts the heuristic score of the first state. which is supposed to be the best state since they are orded in that way, and is also the first value of the tuple.

            for i in range(min(self.k, len(scores))):  
                
                # reference for knowing how to verify best score[3]. * 
                if scores[i][0] != best_score:  # this code checks if any state has a different score
                    # if successive k states have the same heuristic score, that means that there are no improvement happening and
                    # the code is likely stuck in a local optimum(or minimum)
                    # ⚠️ however, there is a chance, it could be otherwise.
                    
                    is_stuck = False  
                    break  # as such it should stop
                    # this part of the code can seem confusing at first. But the following part, complements it


            if is_stuck:  # If all k states have the same score. the following is what happens
                
                runtime = time.time() - self.start_time # if it gets stuck, check the time it took.
                print(f"⚠️ The code is stuck in Local Minima(optima). Best Board: {list(scores[0][1])}, Attacks: {scores[0][0]}, Time: {runtime:.4f}s")
                return list(scores[0][1]), scores[0][0], runtime  

        except ValueError:  # exception syntax
                
                print("⚠️ There is an issue with check_termination()")
        
        return None  # in the case, the code is not stuck, the search continues

    
    
    
    
    """
        This is the function where everything come together.
        In short, it executes the Local Beam Search algorithm.
        However, I do not claim credit for all of it. Gemini and Copilot, did help organise it, debugg
        and remove errors that I was unable to see, after long hours of asking questions and 
        getting answers that made no sense, eventually, it started making sense.
        Only to not make sense. But it works!.
        """
    def run(self):
        self.start_time = time.time()  # Start timing
        self.initialize_states()  # Step 1: Generate initial k states

        for _ in range(self.max_iterations):
            scores = self.compute_scores(self.states)  # Step 2: Compute heuristic scores

            # Step 3: Check for termination conditions
            result = self.check_termination(scores)
            if result:
                return result  # If solution found or stuck in local minima, return or break

            self.states = self.select_best_states(scores)  # Step 4: Select top k states

            successor_scores = self.generate_successor_states(scores)  # Step 5-6: Generate successors & compute scores
            self.states = self.select_best_states(successor_scores)  # Step 7: Select top k successor states

        # Step 8: If max iterations reached, return the best found solution
        best_state = min(self.states, key=compute_attacking_pairs)
        best_attacks = compute_attacking_pairs(best_state)
        runtime = time.time() - self.start_time
        print(f"🔍 Max Iterations Reached. Best Board: {best_state}, Attacks: {best_attacks}, Time: {runtime:.4f}s")
        return best_state, best_attacks, runtime



""" The following runs the algorithm for different values of n and k 
basically, For each of these combinations of k and n, execute the program several times starting with
a different initial random state. """
n_values = [8, 12, 16, 20]
k_values = [1, 3, 5, 7]

for n in n_values:
    for k in k_values:
        print(f"\n🚀 Running Local Beam Search for n={n}, k={k}...")
        lbs = LocalBeamSearch(n, k)  # Create an instance of LocalBeamSearch
        lbs.run()  # Run the search algorithm
