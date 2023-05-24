'''
  Bob received an assignment from his school: he has two numbers A and B, and he has to find the sum of these two numbers.
  Alice, being a good friend of Bob, told him that the answer to this question is C.
  Bob doesn't completely trust Alice and asked you to tell him if the answer given by Alice is correct or not.
  If the answer is correct print "YES", otherwise print "NO" (without quotes).
'''

for t in range(int(input())):
  
  A,B,C = map(int, input().split())
  
  SumIt = "YES" if (A+B == C) else "NO"
  
  print(SumIt)
