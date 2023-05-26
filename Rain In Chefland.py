'''
  In Chefland, precipitation is measured using a rain gauge in millimetre per hour.
  Chef categorises rainfall as:
    -> LIGHT, if rainfall is less than 3 millimetre per hour.
    -> MODERATE, if rainfall is greater than equal to 3 millimetre per hour and less than 7 millimetre per hour.
    -> HEAVY if rainfall is greater than equal to 7 millimetre per hour.
  Given that it rains at X millimetre per hour on a day, find whether the rain is LIGHT, MODERATE, or HEAVY.
'''

# Running Loop Test Cases
for t in range(int(input())):
  
  # Taking Input For X =  The Rate Of Rainfall In Millimetre Per Hour.
  X = int(input())
  
  # Checking If Rainfall Is Less Than 3 Millimetre Per Hour
  if X < 3:
    
    # If Yes, Print "Light"
    print("LIGHT")
      
  # Checking If Rainfall Is Less Than 7 Millimetre Per Hour    
  elif X < 7:
    
    # If Yes, Print "MODERATE"
    print("MODERATE")
  
  # Else Print "HEAVY"
  else:
    print("HEAVY")
