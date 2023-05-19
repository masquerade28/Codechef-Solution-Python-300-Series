'''
  Write a program that accepts sets of three numbers, and prints the second-maximum number among the three.
'''

for t in range(int(input())):
  
  x,y,z = map(int, input().split())
  
  if x > y or x > z:
    
    if x < y or x < z:
      
      print(x)
    
  if y > x or y > z:
        
      if y < x or y < z:
            
          print(y)
   
  if z > x or z > y:
        
      if z < x or z < y:
           
          print(z)
