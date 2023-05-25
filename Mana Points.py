'''
  Chef is playing a mobile game. 
  In the game, Chef's character Chefario can perform special attacks. 
  However, one special attack costs X mana points to Chefario.
  If Chefario currently has Y mana points, determine the maximum number of special attacks he can perform.
'''

for t in range(int(input())):
  
  X,Y = map(int, input().split())
  
  print(int(Y//X))
