'''
  Alice, Bob and Charlie are bidding for an artifact at an auction.
  Alice bids A rupees, Bob bids B rupees, and Charlie bids C rupees (where A, B, and C are distinct).
  According to the rules of the auction, the person who bids the highest amount will win the auction.
  Determine who will win the auction.
'''

# Running Loop For Test Cases
for t in range(int(input())):
  
  # Taking Input For A,B And C ,i.e; The Amount Bid By Alice, Bob, And Charlie Respectively.
  A,B,C = map(int, input().split())
  
  # Alice's Bid Is Higher Print Alice
  if A>B and A>C:
    print("Alice")
  
  # Bod's Bid Is Higher Print Bob
  elif B>A and B>C:
    print("Bob")
  
  # Else Charlie Bids Highest Amount
  else:
    print("Charlie")
