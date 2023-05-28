'''
  Chef was driving on a highway at a speed of X km/hour.
  To avoid accidents, there are fine imposed on overspeeding as follows:
    -> No fine if the speed of the car ≤ 70 km/hour.
    -> Rs 500 fine if the speed of the car is strictly greater than 70 and ≤ 100.
    -> Rs 2000 fine if the speed of the car is strictly greater than 100.
  Determine the fine Chef needs to pay.
'''

# Running Loop For Test Cases
for t in range(int(input())):
  
  # Taking Input For X, i.e; The Speed Of Chef's Car
  X = int(input())
  
  # If Speed Of Chef's Car Is Less Than Equal To 70 He Is Free From Fine
  if X<=70:
    print(0)
  
  # If Speed Of Chef's Car Is Greater Than 70 And Smaller Than Equal To 100, Chef Will Be Fined With Rs 500  
  elif X<=100:
    print(500)
  
  # If Speed Of Chef's Car Is Greater Than 100, Chef Will Be Fined With Rs 2000 
  else:
    print(2000)
