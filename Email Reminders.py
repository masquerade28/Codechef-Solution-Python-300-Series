'''
  MoEngage helps the Chef send email reminders about rated contests to the participants.
  There are a total of N participants on Chef’s platform, and U of them have told Chef not to send emails to them.
  If so, how many participants should MoEngage send the contest emails to?
'''

# Taking Input For U = Total Number Of Users ; N = Number Of Users Who Doesn't Want Reminders
U,N = map(int, input().split())

# No. Of Participants Whom MoEngage Will Sebd Emails = Total Number Of Users - Number Of Users Who Doesn't Want Reminders
print(U-N)
