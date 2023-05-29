'''
  Chef's coding class is very famous in Chefland.
  This year X students joined his class and each student will require one chair to sit on. 
  Chef already has Y chairs in his class. 
  Determine the minimum number of new chairs Chef must buy so that every student is able to get one chair to sit on.
'''

# Running Loop For Test Cases
for t in range(int(input())):
  
  # Taking Input For X And Y, i.e; No. Of Students Joined And No. Of Chairs Chef Is Having
  X,Y = map(int, input().split())
  
  # If No. Of Students > No. Of Chairs, Required No. Of Chairs = X - Y 
  Chairs = (X-Y) if X>Y else 0
  
  # Printing Result
  print(Chairs)
