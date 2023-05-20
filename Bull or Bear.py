'''
  Chef is on his way to become the new big bull of the stock market but is a bit weak at calculating whether he made a profit or a loss on his deal.
  Given that Chef bought the stock at value X and sold it at value Y. 
  Help him calculate whether he made a profit, loss, or was it a neutral deal.
'''

for t in range(int(input())):
  
  X,Y = map(int, input().split())
  
  if X > Y:
      print("LOSS")
      
  elif X == Y:
      print("NEUTRAL")
      
  else:
      print("PROFIT")
