'''
    Chef has a rectangular plate of length N cm and width M cm. 
    He wants to make a wireframe around the plate. 
    The wireframe costs X rupees per cm.
    Determine the cost Chef needs to incur to buy the wireframe.
'''

# Running Loop For Test Cases 
for t in range(int(input())):
    
  # Taking Input For N = Length Of The Plate ; M = Width Of The Plate ; X = Cost Of Frame Per cm
  N,M,X = map(int, input().split())
    
  # Total Cost = Perimeter Of The Rectangular Plate * Cost Of Frame Per cm
  print((2*(N+M))*X)
