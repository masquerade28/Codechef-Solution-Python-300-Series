'''
  Chef has to travel to another place. 
  For this, he can avail any one of two cab services.
  The first cab service charges X rupees.
  The second cab service charges Y rupees.
  Chef wants to spend the minimum amount of money. 
  Which cab service should Chef take?
'''

# Running Loop For Test Cases
for t in range(int(input())):
  
  # Taking Input For X = The Price Of First Cab Service ; Y = The Price Of Second Cab Service
  X,Y = map(int, input().split())
  
  # If Price Of First Cab Service Is Less Than Price Of Second Cab Service, Chef Should Use First Cab Service
  if X < Y:
    print("FIRST")
  
  # If Price Of First Cab Service Is Equal To The Price Of Second Cab Service, Chef Can Use Any Cab Service
  elif X == Y:
    print("ANY")
  
  # If Price Of First Cab Service Is Greater Than Price Of Second Cab Service, Chef Should Use Second Cab Service
  else:
    print("SECOND")
