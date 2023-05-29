'''
  Chef is eagerly waiting for a piece of information. 
  His secret agent told him that this information would be revealed to him after K weeks.
  X days have already passed and Chef is getting restless now. 
  Find the number of remaining days Chef has to wait for, to get the information.
  It is guaranteed that the information has not been revealed to the Chef yet.
'''

# Running Loop For Test Cases
for t in range(int(input())):
  
  # Taking Input For K = No. Of Weeks After Which The Information Will Be Revealed; X = No. Of Days Passed
  K,X = map(int, input().split())
  
  # No. Of Remaining Days = (7*K)-X
  print((7*K)-X)
