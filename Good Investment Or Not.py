'''
    Chef has invested his money at an interest rate of X percent per annum while the current inflation rate is Y percent per annum.
    An investment is called good if and only if the interest rate of the investment is at least twice of the inflation rate.
    Determine whether the investment made by Chef is good or not.
'''

# Running Loop For Test Cases
for t in range(int(input())):
    
  # Taking Input For X = Interest Rate ; Y = Current Inflation Rate
  X,Y = map(int, input().split())
    
  # If The Interest Rate Of The Investment >= 2 * The Inflation Rate, Investment Is Called Good
  GoodInvestmentOrNot = "YES" if X >= (2*Y) else "NO"
    
  # Displaying Result
  print(GoodInvestmentOrNot)
