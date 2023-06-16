'''
  There are only 2 type of denominations in Chefland:
    Coins worth 1 rupee each
    Notes worth 10 rupees each 
  Chef wants to pay his friend exactly X rupees. 
  What is the minimum number of coins Chef needs to pay exactly X rupees?
'''

# Running Loop For Test Cases
for t in range(int(input())):
  
  # Taking Input For X = Money Chef Needs To Pay
  X = int(input())
  
  # If The Amount Is Greater Than 10 Chef Can Use The 10 Rupees Notes 
  if X >= 10:
    
    # Coins Chef Needs To Pay Is The Remainder We Get After We Divide Amount By 10 
    print(X % 10)
  
  # If amount Is Less Than !0 Chef Will Not Be Able To Use 10 Rupees Note
  else:
      
     # Hence Chef Has To Pay All The Amount In Coins 
     print(X)
