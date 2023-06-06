'''
    For the upcoming semester, the admins of your university decided to keep a total of X seats for the MATH-1 course. 
    A student interest survey was conducted by the admins and it was found that Y students were interested in taking up the MATH-1 course.
    Find the minimum number of extra seats that the admins need to add into the MATH-1 course to make sure that every student who is interested in taking the course would be able to do so.
'''

# Running Loop For Test Cases
for t in range(int(input())):
    
  # Taking Input For X = The Current Number Of Seats for Enrollment ; Y = Number Of Students Who Are Interested In Taking Up The Course 
  X,Y = map(int, input().split())
    
  # Minimum Nuber Of Extra Seats That The Admins Need To Add = Y - X ; If No. Of Students > No. Of Seats
  Math1Enrolment = (Y-X) if Y>X else 0
    
  # Displaying Result
  print(Math1Enrolment)
