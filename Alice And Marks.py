'''
  Alice has scored X marks in her test and Bob has scored Y marks in the same test. 
  Alice is happy if she scored at least twice the marks of Bob’s score. 
  Determine whether she is happy or not.
'''

# Taking Input For X = Marks Of Alice ; Y = Marks Of Bob
X,Y = map(int, input().split())

# Alice Will Be Happy If Marks Of Alice >= 2 * Marks Of Bob
AliceAndMarks = "YES" if (X >= 2*Y) else "NO"

# Displaying Result
print(AliceAndMarks)
