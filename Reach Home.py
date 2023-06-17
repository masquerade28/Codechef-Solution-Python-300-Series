'''
  Chef is hungry and wants to reach home.
  Chef can travel up to 5 kilometres on 1 litre of fuel on his motorcycle.
  Currently, his motorcycle is filled with X litres of fuel and his home is Y kilometres away.
  Determine whether Chef can reach his home on his motorcycle or not.
'''

# Running Loop For Test Cases
for t in range(int(input())):
  
  # Taking Input For X = Amount Of Fuel In Chef's Motorcycle ; Y = Distance To Chef's Home
  X,Y = map(int, input().split())
  
  # If Total Distance That Motorcycle Will Be Able To Cover i.e; 5 * X, Is Greater Than Or Equal To The Distance To The Chef's Home; Chef Will Be Able To Reach His Home 
  ReachHome = "YES" if 5*X >= Y else "NO"
  
  # Displaying Result
  print(ReachHome)
