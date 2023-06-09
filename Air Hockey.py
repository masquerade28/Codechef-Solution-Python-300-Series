'''
  Alice is playing Air Hockey with Bob. 
  The first person to earn seven points wins the match. 
  Currently, Alice's score is A and Bob's score is B.
  Charlie is eagerly waiting for his turn. 
  Help Charlie by calculating the minimum number of points that will be further scored in the match before it ends.
'''

# Running Loop For Test Cases
for t in range(int(input())):
  
  # Taking Input For A = Points Of Alice ; B = Points Of Bob   
  A,B = map(int, input().split())
  
  # If Points Of Alice Is More Than Points Of Bob Then Minimum Number of Points That Will Be Scored Further Will Be 7-Points Of Alice, Else 7-Points Of Bob 
  AirHockey = 7-A if A>B else 7-B
    
  # Displaying Result
  print(AirHockey)
