'''
  A person is said to be sleep deprived if he slept strictly less than 7 hours in a day.
  Chef was only able to sleep X hours yesterday. 
  Determine if he is sleep deprived or not.
'''

# Running Loop For Test Cases
for t in range(int(input())):
  # Taking Input For X = The Number Of Hours Chef Slept
  X = int(input())
    
  # Checking If Chef Slept For Less Than 7 Hours Or Not If YES Chef Is Sleep Deprived
  SleepDeprivation = "YES" if X<7 else "NO"
    
  # Displaying Result
  print(SleepDeprivation)
