'''
  Chef wants to conduct a lecture for which he needs to set up an online meeting of exactly X minutes.
  The meeting platform supports a meeting of maximum 30 minutes without subscription and a meeting of unlimited duration with subscription.
  Determine whether Chef needs to take a subscription or not for setting up the meet.
'''

for t in range(int(input())):
  
  X = int(input())
  
  GetSubscription = "YES" if X > 30 else "NO"
  
  print(GetSubscription)
