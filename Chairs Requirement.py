'''
  Chef's coding class is very famous in Chefland.
  This year X students joined his class and each student will require one chair to sit on. 
  Chef already has Y chairs in his class. 
  Determine the minimum number of new chairs Chef must buy so that every student is able to get one chair to sit on.
'''

for t in range(int(input())):
  
  X,Y = map(int, input().split())
  
  Chairs = (X-Y) if X>Y else 0
  
  print(Chairs)
