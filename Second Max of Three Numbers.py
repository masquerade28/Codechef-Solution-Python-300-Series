'''
  Write a program that accepts sets of three numbers, and prints the second-maximum number among the three.
'''

# Running Loop For Test Cases
for t in range(int(input())):
  
  # Taking Input For X = First Number; Y = Second Number; Z = Third Number
  X,Y,Z = map(int, input().split())
  
  # If First Number > Second Number Or First Number > Third Number
  if X > Y or X > Z:
    
    # If First Number < Second Number Or First Number < Third Number
    if X < Y or X < Z:
      
      # X Is The Second Maximum Number
      print(X)
   
  # If Second Number > First Number Or Second Number > Third Number 
  if Y > X or Y > Z:
      
      # If Second Number < First Number Or Second Number < Third Number
      if Y < X or Y < Z:
          
          # Y Is The Second Maximum Number
          print(Y)
  
  # If Third Number > First Number Or Third Number > Second Number
  if Z > X or Z > Y:
      
      # If Third Number < First Number Or Third Number < Second Number
      if Z < X or Z < Y:
          
          # Z Is The Second Maximum Number
          print(Z)
