'''
  Bob received an assignment from his school: he has two numbers A and B, and he has to find the sum of these two numbers.
  Alice, being a good friend of Bob, told him that the answer to this question is C.
  Bob doesn't completely trust Alice and asked you to tell him if the answer given by Alice is correct or not.
  If the answer is correct print "YES", otherwise print "NO" (without quotes).
'''

# Running Loop For Test Cases
for t in range(int(input())):
  
  # Taking Input For A = First Number; B = Secomd Number; C = Answer Told By Alice
  A,B,C = map(int, input().split())
  
  # If Answer Told Told By Alice Is Same As The Sum Print "YES"
  SumIt = "YES" if (A+B == C) else "NO"
  
  # Displaying Result
  print(SumIt)
