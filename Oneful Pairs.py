'''
  Chef defines a pair of positive integers (a,b) to be a Oneful Pair, if
    a + b + ( a ⋅ b ) = 111
  For example, (1,55) is a Oneful Pair, since 
    1 + 55 + ( 1 ⋅ 55 ) = 56 + 55 = 111
  But (1,56) is not a Oneful Pair, since 
    1 + 56 + ( 1 ⋅ 56 ) = 57 + 56 = 113 ≠ 111
  Given two positive integers a and b, output Yes if they are a Oneful Pair. 
  And No otherwise.
'''

# Taking Input For Two Integers
A,B = map(int, input().split())

# Checking If a + b + ( a ⋅ b ) = 111
OnefulPairs = "YES" if (A+B+(A*B)) == 111 else "NO"

# Displaying Result
print(OnefulPairs)
