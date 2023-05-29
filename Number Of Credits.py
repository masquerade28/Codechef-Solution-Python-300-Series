'''
  In the current semester, you have taken X RTP courses, Y Audit courses and Z Non-RTP courses.
  The credit distribution for the courses are:
    -> 4 credits for clearing each RTP course.
    -> 2 credits for clearing each Audit course.
    -> No credits for clearing a Non-RTP course.
  Assuming that you cleared all your courses, report the number of credits you obtain this semester.
'''

# Running Loop For Test Cases
for t in range(int(input())):
  
  # Taking Input For X = No. Of RTP Courses; Y = No. Of Audit Courses; Z = No. Of Non-RTP Courses
  X,Y,Z = map(int, input().split())
  
  # No. Of Credits = RTP's Credit * No. Of RTP Courses + Audit's Credit * No. Of Audit Courses + Non-Audit's Credit * No. Of Non-Audit Courses
  print((X*4)+(Y*2))
