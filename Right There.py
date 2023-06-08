'''
    If you wanna party, if you, if you wanna party
    Then put your hands up
    Chef wants to host a party with a total of N people.
    However, the party hall has a capacity of X people. 
    Find whether Chef can host the party.
'''

# Running Loop For Test Cases
for t in range(int(input())):
    
  # Taking Input For N = Total number Of People ; X Capacity Of The Party Hall
  N,X = map(int, input().split())
    
  # If Number Of People Is Less Than Or Equal To Capacity Of The Hall, Chef Will Be Able To Host The Party
  RightThere = "YES" if N<=X else "NO"
    
  # Displaying Result
  print(RightThere)
