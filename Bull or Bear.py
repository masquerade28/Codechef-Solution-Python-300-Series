'''
  Chef is on his way to become the new big bull of the stock market but is a bit weak at calculating whether he made a profit or a loss on his deal.
  Given that Chef bought the stock at value X and sold it at value Y. 
  Help him calculate whether he made a profit, loss, or was it a neutral deal.
'''

# Running Loop For Test Cases
for t in range(int(input())):
  
  # Taking Input For X And Y ,i.e; Price At Which Stock Was Bought And Price At Which It Was Sold
  X,Y = map(int, input().split())
  
  # If Bought Price > Selling Price, Chef Is In Loss
  if X > Y:
      print("LOSS")
  
  # If Bought Price = Selling Price, Chef Is Neither In Loss Nor In Profit
  elif X == Y:
      print("NEUTRAL")
  
  # If Bought Price < Selling Price, Chef Is In Profit
  else:
      print("PROFIT")
