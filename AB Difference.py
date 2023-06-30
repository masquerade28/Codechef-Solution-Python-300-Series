'''
  Chef is taking his baby steps into the world of programming.
  The very first program he's tasked to write is as follows:
    -> "Given two integers A and B, print A+B."
  Unfortunately, Chef makes a typo: his program outputs A×B instead of A+B.
  Given the values of A and B, can you help Chef find the absolute difference between the correct answer and the value his program prints?
'''

# Taking Input For Two Integers A And B
A,B = map(int, input().split())

# To Finds Absolute We Will Use abs() function. So Absolute Difference = abs((A*B)-(A+B))
print(abs((A*B)-(A+B)))
