'''
  Chef is playing a mobile game. 
  In the game, Chef's character Chefario can perform special attacks. 
  However, one special attack costs X mana points to Chefario.
  If Chefario currently has Y mana points, determine the maximum number of special attacks he can perform.
'''

# Running Loop For Test Cases
for t in range(int(input())):
  
  # Taking Input For X = No. Of Points Special Attack Costs; Y = Chef's Current Mana Points
  X,Y = map(int, input().split())
  
  # Maximum Number Of Special Attacks He Can Perform = Y // X
  print(int(Y//X))
