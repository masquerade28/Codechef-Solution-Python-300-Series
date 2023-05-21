'''
  In a certain month, Chef earned X rupees while Chefina earned Y rupees such that Y>X.
  Since they want to end up with exactly the same amount, they decide to donate the difference between their income to a charity.
  Find the amount they donate in the month.
'''

# Running Loop For Test Cases
for t in range(int(input())):
  
  # Taking Input For X = The Income Of Chef ; Y = The Income Of Chefina
  X,Y = map(int, input().split())
  
  # The Amount They Donate In The Month = Y - X.
  print(Y-X)
