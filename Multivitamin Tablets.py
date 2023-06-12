'''
  The doctor prescribed Chef to take a multivitamin tablet 3 times a day for the next X days.
  Chef already has Y multivitamin tablets.
  Determine if Chef has enough tablets for these X days or not.
'''

# Running Loop For Test Cases
for t in range(int(input())):
  
  # Taking Input For X = No. Of Days Chef Need To Take Tablets ; Y = Number Of Tablet Chef Already Has
  X,Y = map(int, input().split())
  
  # Chef Has Y Tablets And Need 3 Tablets Per Day, So If No. Of Tablets That Chef Already Has // 3 is Greater Than No. Of Days Chef Need To Take Tablets Then Chef Has Enough Tablets Else No
  MultivitaminTablets = "YES" if (Y//3>=X) else "NO"
    
  # Displaying Result
  print(MultivitaminTablets)
