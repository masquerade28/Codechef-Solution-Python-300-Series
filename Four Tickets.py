'''
  Four friends want to attend a concert. Each ticket costs X rupees.
  They have decided to go to the concert if and only if the total cost of the tickets does not exceed 1000 rupees.
  Determine whether they will be going to the concert or not.
'''

# Running Loop For Test Cases 
for t in range(int(input())):
  
  # Taking Input For X = Cost Of Each Ticket
  X = int(input())
  
  # If Total Cost Of Tickets < 1000; They Will Go To The Concert
  FourTickets = "YES" if ((4*X) <= 1000) else "NO"
  
  # Printing Result
  print(FourTickets)
