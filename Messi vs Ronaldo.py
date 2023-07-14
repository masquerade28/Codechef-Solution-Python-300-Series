'''
  In Chefland, a football player gets 2 points for each goal and 1 point for each assist.
  Messi has A goals and B assists this season, whereas Ronaldo has  goals and Y assists.
  Find out the player with more points this season.
'''

A,B,X,Y = map(int, input().split())

if 2*A+B > 2*X+Y:
  print("Messi")

elif 2*A+B == 2*X+Y:
  print("Equal")

else:
  print("Ronaldo")
