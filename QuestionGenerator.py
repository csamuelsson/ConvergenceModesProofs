from random import randint
import argparse

# Declare parser for the command line flags
def parseFlags():
    parser = argparse.ArgumentParser(description='Training on convergence modes proofs with hints.')
    parser.add_argument("-hints", "--hints", action="store_true", help="Show available hints")

    return parser.parse_args()


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

    def setClues(self, clueArray):
        self.clueArray = clueArray

    def getClues(self):
        return self.clueArray


# Define the different types of convergences:
distribution = ConvergenceMode("in distribution")
prob = ConvergenceMode("in probability", distribution)
almostSure = ConvergenceMode("almost surely", prob)
rmean = ConvergenceMode("in R mean", prob)

# Set the clues:
rmean.setClues(["Use Markov's inequality to rewrite the definition of the probability convergence"])
prob.setClues(["Use the definition for the CDF for x + epsilon and x - epsilon",
    "Split the probability space to |X_n - X| > and <= epsilon"])
# TODO: Write proper hints for every proof:
almostSure.setClues(["TBD", "TBD", "TBD", "TBD"])

convergenceArray = [distribution, prob, almostSure, rmean]

def QuestionParser(parentConvergence):
    implicationConvergence = parentConvergence.getChildConvergence().getCleanText()

    print("Show that if a sequence of random variables converges %s, then the sequence converges %s" 
        % (parentConvergence.getCleanText(), implicationConvergence))

    if args.hints:
        clues = parentConvergence.getClues()
        print("\n\nCLUES:")
        i = 1
        for clue in clues:
            print(i, ': ', clue)
            i += 1

if __name__ == '__main__':
    args = parseFlags()
    parentConvergence = convergenceArray[randint(1,3)] # only 3 modes of convergences to consider (not the grandchild)
    QuestionParser(parentConvergence)