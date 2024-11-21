



#tit fo tat
def titForTatAlg(self):
    class Teacher:
        def __init__(self):
            self.cooperation = True  # Initially cooperating

        def decide(self, student_action):
            if student_action == "cooperate":
                return "cooperate"  # Continue supporting
            elif student_action == "defect":
                self.cooperation = False
                return "defect"  # Stop supporting if student defects
            
    class Student:
        def __init__(self):
            self.cooperation = True  # Initially cooperating

        def decide(self, teacher_action):
            if teacher_action == "cooperate":
                return "cooperate"  # Continue engaging
            elif teacher_action == "defect":
                self.cooperation = False
                return "defect"  # Stop engaging if teacher defects
#tit for tat

#cooperate

def cooperateAlg(self):
    class Teacher:
        def __init__(self):
            # Always cooperating, provides support
            self.cooperation = True
        
        def cooperate(self):
            # Teacher cooperates by always providing feedback and encouragement
            return "cooperate"

    class Student:
        def __init__(self):
            # Always cooperating, engages with the course
            self.cooperation = True
        
        def cooperate(self):
            # Student cooperates by always engaging, attending, and completing tasks
            return "cooperate"
#cooperate

#defect
def defectAlg(self):
    class Teacher:
        def __init__(self):
            # Always defecting, providing no support or feedback
            self.cooperation = False
        
        def defect(self):
            # Teacher defects by withholding support, ignoring the student, or grading harshly
            return "defect"

    class Student:
        def __init__(self):
            # Always defecting, not engaging with the material
            self.cooperation = False
        
        def defect(self):
            # Student defects by not attending class, skipping assignments, or cheating
            return "defect"
        
#defect

#hard defect
def hardDefectAlg():
    class Teacher:
        def __init__(self):
            # Starts defecting: providing no support, being harsh
            self.cooperation = False
        
        def defect(self):
            # Teacher continues to defect: harsh grading, no feedback
            return "hard_defect"

    class Student:
        def __init__(self):
            # Initially cooperates: attends class, does assignments
            self.cooperation = True
        
        def cooperate(self):
            # Initially, student is cooperating by attending, doing work
            return "cooperate"
        
        def hard_defect(self):
            # After being provoked, the student defects: misbehaving, ignoring assignments
            return "hard_defect"
        
#hard defect