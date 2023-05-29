'''
  Chef has recently started playing chess, and wants to play as many games as possible.
  He calculated that playing one game of chess takes at least 20 minutes of his time.
  Chef has N hours of free time. 
  What is the maximum number of complete chess games he can play in that time?
'''

# Running Loop For Test Cases
for t in range(int(input())):
  
  # Taking Input For N, i.e; Chef's Free Time (In Hour)
  N = int(input())
  
  # No. Of Complete Chess Game That Chef Can Play = Chef's Free Time In Minutes / 20 Minutes
  print(int((60*N)/20))
