
import random
prevAct = ()
currAct = ()
defectFlag = 0

def titForTatAlg():
    global prevAct, currAct
    if prevAct == "cooperate":
        currAct = "cooperate"
    elif prevAct == "defect":
        currAct = "defect"
    prevAct = currAct

def hardDefectAlg():
    global prevAct, currAct, defectFlag
    if prevAct == "defect" or defectFlag == 1:
        currAct = "defect"
        defectFlag = 1
    else:
        currAct = "cooperate"
    prevAct = currAct

def cooperateAlg():
    global prevAct, currAct
    currAct = "cooperate"
    prevAct = currAct

def defectAlg():
    global currAct, prevAct
    currAct = "defect"
    prevAct = currAct

def fun_game(T_action, S_action):
    # Initialize scores
    T_score = 0
    S_score = 0

    # Check statement for score of action vs action
    if T_action == 'cooperate' and S_action == 'cooperate':
        T_score = 3
        S_score = 3
    elif T_action == 'cooperate' and S_action == 'defect':
        T_score = 0
        S_score = 5
    elif T_action == 'defect' and S_action == 'cooperate':
        T_score = 5
        S_score = 0
    elif T_action == 'defect' and S_action == 'defect':
        T_score = 1
        S_score = 1

    # Return scores and previous actions
    return (T_score, S_score, T_action, S_action)

# Function to run the algorithms multiple times
def run_algorithms(num_runs):
    results = {"titForTatAlg": [], "hardDefectAlg": [], "cooperateAlg": [], "defectAlg": []}
    global prevAct, currAct, defectFlag

    T_total_score = 0
    S_total_score = 0

    for _ in range(num_runs):
        # Reset actions and flag for each run
        prevAct = "cooperate"
        defectFlag = 0

        # Run tit-for-tat algorithm
        prevAct = "cooperate"
        S_action = prevAct
        titForTatAlg()
        T_action = currAct
        T_score, S_score, T_prev_action, S_prev_action = fun_game(T_action, S_action)
        T_total_score += T_score
        S_total_score += S_score
        results["titForTatAlg"].append((T_prev_action, S_prev_action, T_score, S_score))

        # Run hard defect algorithm
        prevAct = "defect"
        S_action = prevAct
        hardDefectAlg()
        T_action = currAct
        T_score, S_score, T_prev_action, S_prev_action = fun_game(T_action, S_action)
        T_total_score += T_score
        S_total_score += S_score
        results["hardDefectAlg"].append((T_prev_action, S_prev_action, T_score, S_score))

        # Run cooperate algorithm
        prevAct = "defect"
        S_action = prevAct
        cooperateAlg()
        T_action = currAct
        T_score, S_score, T_prev_action, S_prev_action = fun_game(T_action, S_action)
        T_total_score += T_score
        S_total_score += S_score
        results["cooperateAlg"].append((T_prev_action, S_prev_action, T_score, S_score))

        # Run defect algorithm
        prevAct = "cooperate"
        S_action = prevAct
        defectAlg()
        T_action = currAct
        T_score, S_score, T_prev_action, S_prev_action = fun_game(T_action, S_action)
        T_total_score += T_score
        S_total_score += S_score
        results["defectAlg"].append((T_prev_action, S_prev_action, T_score, S_score))

    return results, T_total_score, S_total_score

# Run the algorithms 100 times
num_runs = 100
results, T_total_score, S_total_score = run_algorithms(num_runs)

# Print the results
for alg, actions in results.items():
    print(f"Results for {alg}:")
    for i, (T_prev, S_prev, T_score, S_score) in enumerate(actions):
        print(f"Run {i + 1}: Teacher - {T_prev} (Score: {T_score}), Student - {S_prev} (Score: {S_score})")
    print()

# Print total scores
print(f"Total Score for Teacher: {T_total_score}")
print(f"Total Score for Student: {S_total_score}")
