'''
  Om has X rupees. 
  He wants to gift a laptop worth N rupees to his girlfriend.
  We know that Om is the technical secretary of IIIT-A and has access to the Gymkhana funds of IIIT-A. 
  Currently there are M rupees in the fund and Om can use the fund as much as he wants.
  Find whether Om can gift his girlfriend a new laptop.
'''

# Taking Input For X = The Money Om Has ; N = Cost Of The Laptop ; M = Amount Present In The Gymkhana Fund
X,N,M = map(int, input().split())

# If Sum Of Money That Om Has And Money Present In The Gymkhana Fund Is >= The Cost Of Laptop, Then Om Can Buy The Laptop
TheGift = "YES" if X+M >= N else "NO"

# Displaying The Result
print(TheGift)
