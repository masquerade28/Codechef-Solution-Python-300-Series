'''
  Chef has to attend an exam that starts in X minutes, but of course, watching shows takes priority.
  Every episode of the show that Chef is watching, is 24 minutes long.
  If he starts watching a new episode now, will he finish watching it strictly before the exam starts?
'''

for t in range(int(input())):
  
  X = int(input())
    
  JustOneMoreEpisode = "YES" if X>24 else "NO"
    
  print(JustOneMoreEpisode)
