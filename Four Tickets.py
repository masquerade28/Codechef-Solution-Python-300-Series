'''
  Four friends want to attend a concert. Each ticket costs X rupees.
  They have decided to go to the concert if and only if the total cost of the tickets does not exceed 1000 rupees.
  Determine whether they will be going to the concert or not.
'''

for t in range(int(input())):
  
  X = int(input())
  
  FourTickets = "YES" if ((4*X) <= 1000) else "NO"
  
  print(FourTickets)
