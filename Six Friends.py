'''
  Six friends go on a trip and are looking for accommodation. 
  After looking for hours, they find a hotel which offers two types of rooms — double rooms and triple rooms. 
  A double room costs Rs. X, while a triple room costs Rs. Y.
  The friends can either get three double rooms or get two triple rooms. 
  Find the minimum amount they will have to pay to accommodate all six of them.
'''

# Running Loop For Test Cases
for t in range(int(input())):
  
  # Taking Input For X = Double Room Cost ; Y = Triple Room Cost
  X,Y = map(int, input().split())
  
  # The Minimum Amount They Will Pay To Accomodate All Six Of Them = min(3*Double Room Cost, 2*Triple Room Cost)
  print(min(3*X,2*Y))
