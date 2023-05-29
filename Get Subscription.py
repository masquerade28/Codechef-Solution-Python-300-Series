'''
  Chef wants to conduct a lecture for which he needs to set up an online meeting of exactly X minutes.
  The meeting platform supports a meeting of maximum 30 minutes without subscription and a meeting of unlimited duration with subscription.
  Determine whether Chef needs to take a subscription or not for setting up the meet.
'''

# Running Loop For Test Cases
for t in range(int(input())):
  
  # Taking Input For X = Duration Of Meeting (In Minutes)
  X = int(input())
  
  # If Meeting's Duration Exceeds 30 Minutes Chef Needs To Buy Subscription
  GetSubscription = "YES" if X > 30 else "NO"
  
  # Displaying Result
  print(GetSubscription)
