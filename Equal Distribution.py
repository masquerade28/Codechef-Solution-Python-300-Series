'''
  Alice and Bob are very good friends and they always distribute all the eatables equally among themselves.
  Alice has A chocolates and Bob has B chocolates. 
  Determine whether Alice and Bob can distribute all the chocolates equally among themselves.
  Note that:
    -> It is not allowed to break a chocolate into more than one piece.
    -> No chocolate shall be left in the distribution.
'''

# Running Loop Test Cases
for t in range(int(input())):
  
  # Taking Input For A & B ,i.e; Number Of Chocolates That Alice And Bob Have.
  A,B = map(int, input().split())
  
  # If Sum Of Their Chocolates Is Even Then They Can Divide Chocolates Equally Among Them
  EqualDistribution = "YES" if ((A+B) % 2 == 0) else "NO"
  
  # Printing Result
  print(EqualDistribution)
