'''
    Chef has his lunch only between 1 pm and 4 pm (both inclusive).
    Given that the current time is X pm, find out whether it is lunchtime for Chef.
'''

# Running Loop For Test Cases
for t in range(int(input())):
    
  # Taking Input For X = Current Time
  X = int(input())
    
  # If The Current Time Is Between 1pm And 4pm (Both inclusive) Then Chef Had His Lunch 
  lunchTime = "YES" if X>=1 and X<=4 else "NO"
    
  # Displaying Result
  print(lunchTime)
