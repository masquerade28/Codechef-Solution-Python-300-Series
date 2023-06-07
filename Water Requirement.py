'''
    Finally, after purchasing a water cooler during the April long challenge, Chef noticed that his water cooler requires 2 liters of water to cool for one hour.
    How much water (in liters) would be required by the cooler to cool for N hours?
'''

# Running Loop For Test Cases
for t in range(int(input())):
    
  # Taking Input For N = Number Of Hours
  N = int(input())
    
  # Water Required By The Coller To Cool For N Hours = 2 * N
  print(2*N)
