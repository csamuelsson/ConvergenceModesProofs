from random import randint

class ConvergenceMode:
    # One mode of convergence can have exactly one implication, i.e. another mode of convergence being true
    # if the current mode of convergence (object) is true.

    def __init__(self, cleanText, childConvergence = None):
        self.childConvergence = childConvergence
        self.cleanText = cleanText

    def getCleanText(self):
        return self.cleanText

    def getChildConvergence(self):
        return self.childConvergence


# Define the different types of convergences:
distribution = ConvergenceMode("in distribution")
prob = ConvergenceMode("in probability", distribution)
almostSure = ConvergenceMode("almost surely", prob)
rmean = ConvergenceMode("in R mean", prob)

convergenceArray = [distribution, prob, almostSure, rmean]

def QuestionParser():
    randomNumber = randint(0, 3) # only 4 modes of convergences to consider, NOT subject to change
    randomConvergenceMode = convergenceArray[randomNumber]
    implicationConvergence = randomConvergenceMode.getChildConvergence().getCleanText()

    print("Show that if a sequence of random variables converges %s, then the sequence converges %s" 
        % (randomConvergenceMode.getCleanText(), implicationConvergence))

if __name__ == '__main__':
    QuestionParser()