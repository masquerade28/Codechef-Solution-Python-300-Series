'''
  On the occasion of World Blood Donor Day, Chef has organized an event to reward regular blood donars in Chefland.
    -> If the donor has made less than or equal to 3 donations, they receive a BRONZE donor badge.
    -> If the donor has made more than 3 but less than equal to 6 donations, they receive a SILVER donor badge.
    -> If the donor has made more than 6 donations, they receive a GOLD donor badge.
  Given that a person has made X donations, find the badge they receive.
'''

# Running Loop For Test Cases
for t in range(int(input())):
  
  # Taking Input For X = Number Of Blood Donation The Person Has Made
  X = int(input())
  
  # Checking The Given Conditons
  
  if X <= 3:
    print("BRONZE")
    
  elif X > 3 and X <= 6:
    print("SILVER")
  
  else:
    print("GOLD")
