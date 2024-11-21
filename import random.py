import random
prevAct = ()
currAct = ()
defectFlag = 0

def titForTatAlg():
    if prevAct == "cooperate":
        currAct == "cooperate"
        prevAct = "cooperate"
    if prevAct == "defect":
        currAct == "defect"
        prevAct = "defect"


def hardDefectAlg():
    if prevAct == "defect" or defectFlag == 1:
        currAct = "defect"
        prevAct = "defect"

def cooperateAlg():
    if prevAct == "cooperate":
        currAct= "cooperate"
        prevAct = "cooperate"
    if prevAct == "defect":
        currAct= "cooperate"
        prevAct = "cooperate"

def defectAlg():
    currAct = "defect"

        
#fun game (T_action, S_action)

#check stattement for score of action vs action (IF C AND C then)
   # T == C, S == C
    #Then T_score == 2, S_score == 2
    
  # return (T_Score, S_Score, T_prev_action, S_prev_action)

#fun teacher_choice (S_prev_action)

#if S_prev_action == B Then B else C

#return (T_action) """

