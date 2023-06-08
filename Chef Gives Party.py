'''
  Chef wants to give a burger party to all his N friends i.e. he wants to buy one burger for each of his friends.
  The cost of each burger is X rupees while Chef has a total of K rupees.
  Determine whether he has enough money to buy a burger for each of his friends or not.
'''

# Running Loop For Test Cases
for t in range(int(input())):
  
  # Taking Input For N = Number Of Chef's Friends ; X = Cost Of Each Burger ; K = Total Money Chef Has 
  N,X,K = map(int, input().split())
  
  # If Total Cost Of Burgers Is Less Than Equal To Total Money Chef Has Then Chef Has Enough Money
  ChefGivesParty = "YES" if N*X <= K else "NO"
  
  # Displaying Result
  print(ChefGivesParty)
