# ConvergenceModesProofs
Just a simple helper program for me to study the proofs of the relationships between probabilistic modes of convergences :)

Used for a course in measure theoretic probability theory.

**To run:**  
<code>git clone https://github.com/csamuelsson/ConvergenceModesProofs</code>   
<code>cd ConvergenceModesProofs</code>   
<code>python3 QuestionGenerator.py</code>

**Example output:**  
<code>Show that if a sequence of random variables converges almost surely, then the sequence converges in probability</code>

Also supports using hints with the <code>--hints</code> command line flag:    
<code>python3 QuestionGenerator.py --hints</code>  

that outputs  
<code>Show that if a sequence of random variables converges in probability, then the sequence converges in distribution</code>  

<code>almost surely => in probability</code>  
  
<code>HINT(S):</code>  
<code>1 :  Start with the delta-epsilon definition of convergence in probability</code>  
<code>2 :  Find upper limit with the union set for big n's (indexed by k)</code>  
<code>3 :  Let k go to infinity - what's this event?</code>  
<code>4 :  Use almost sure convergence</code>  
