'''
    This semester, Chef took X courses. 
    Each course has Y units and each unit has Z chapters in it.
    Find the total number of chapters Chef has to study this semester.
'''

# Running Loop For Test Cases
for t in range(int(input())):
    
  # Taking Input For X = No. Of Courses; Y = No. Of Units In Each Course; Z = No. Of Chapters In Each Units
  X,Y,Z = map(int, input().split())
    
  # No. Of Chapters Chef has To Study = No. Of Courses * No. Of Units In Each Course * No. Of Chapters In Each Units
  print(X*Y*Z)
