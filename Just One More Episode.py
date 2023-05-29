'''
  Chef has to attend an exam that starts in X minutes, but of course, watching shows takes priority.
  Every episode of the show that Chef is watching, is 24 minutes long.
  If he starts watching a new episode now, will he finish watching it strictly before the exam starts?
'''

# Running Loop For Test Cases
for t in range(int(input())):
  
  # Taking Input For X = Time Chef Is Having
  X = int(input())
  
  # If Time Chef Is Having > 24 Minutes; He Will Be Able To Finish It
  JustOneMoreEpisode = "YES" if X>24 else "NO"
  
  # Displaying Result
  print(JustOneMoreEpisode)
