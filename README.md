# ConvergenceModesProofs
Just a simple helper program for me to study the proofs of the relationships between probabilistic modes of convergences :)

Used for a course in measure theoretic probability theory.

**To run:**  
<code>git clone https://github.com/csamuelsson/ConvergenceModesProofs</code>  
<code>python3 QuestionGenerator.py</code>

**Example output:**  
<code>Show that if a sequence of random variables converges almost surely, then the sequence converges in probability</code>

Also supports using hints with the <code>--hints</code> command line flag:    
<code>python3 QuestionGenerator.py --hints</code>  

that outputs  
<code>Show that if a sequence of random variables converges in probability, then the sequence converges in distribution

CLUES:
1 : Use the definition for the CDF for x + epsilon and x - epsilon
2 : Split the probability space to |X_n - X| > and <= epsilon</code>  

**TODO:**  
Fix hints for a.s. => Prob.