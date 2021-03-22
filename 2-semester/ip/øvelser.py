class SolutionFound(Exception):
  pass

def subset_sum(x, L):
  
  # rekursiv funktion
  def solution(x, L_):
    if sum(L_) == x:
      raise SolutionFound(L_)
    else:
      for n in range(len(L_)):
        solution(x, L_[0:n] + L_[n+1:])
  #
  try:
    solution(x, L)
  except SolutionFound as sol:
    return sol.args[0] # retuner løsningen. 
  else:
    return None