'''
  Each item in Chef’s menu is assigned a spice level from 1 to 10.
  Based on the spice level, the item is categorised as:
    MILD: If the spice level is less than 4.
    MEDIUM: If the spice level is greater than equal to 4 but less than 7.
    HOT: If the spice level is greater than equal to 7.
  Given that the spice level of an item is X, find the category it lies in.
'''

# Running Loop For Test Cases
for t in range(int(input())):
  
  # Taking Input For X = Spice Level Of An Item
  X = int(input())
  
  # If Spice Level Is Less Than 4 It Is Mild
  if X < 4:
      print("MILD")
      
  # If Spice Level Is Greater Than Equal To 4 And Less Than 7 It Is Medium
  elif X >= 4 and X < 7:
      print("MEDIUM")
  
  # If Spice Level Is Greater Than Equal To 7 It Is Hot
  else:
      print("HOT")
