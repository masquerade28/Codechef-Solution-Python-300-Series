'''
  On a certain train, Chef-the ticket collector, collects a fine of Rs. X if a passenger is travelling without a ticket. 
  It is known that a passenger carries either a single ticket or no ticket.
  P passengers are travelling and they have a total of Q tickets. 
  Help Chef calculate the total fine collected.
'''

# Running Loop For Test Cases
for t in range(int(input())):
  
  # Taking Input For X = The Fee ; P = Number Passengers On Train ; Q = Number Of Tickets Chef Collected
  X,P,Q = map(int, input().split())
  
  # Total Fine Collected = ( Total Passengers - Passengers Having Tickets ) * The Fee
  print((P-Q)*X)
