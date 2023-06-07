'''
    There were initially X million people in a town, out of which Y million people left the town and Z million people immigrated to this town.
    Determine the final population of town in millions.
'''

# Running Loop For Test Cases
for t in range(int(input())):
    
  # Taking input For X = Initial Number Of People (In Million) ; Y = Number of People Who Left The Town (In Million) ; Z = Number Of People Who Immigrated To This Town (In Million)
  X,Y,Z = map(int, input().split())
    
  # Displaying Result
  print(X-Y+Z)
