'''
    Bob has X rupees and goes to a market. 
    The cost of apples is Rs. A per kg and the cost of oranges is Rs. B per kg.
    Determine whether he can buy at least 1 kg each of apples and oranges.
'''

# Taking Input For X = Amount Of Money Bob Has
X = int(input())

# Taking Input For A = Cost Per Kg Of Apples ; B = Cost Per Kg Of Oranges 
A,B = map(int, input().split())

# If Cost Of Buying 1Kg Each Of Apple And Oranges i.e; (A+B) Is Less Than Or Equal To Money Bob Is Having Then He Can Buy Atleast !kg Each Of Apples And Oranges 
ApplesAndOranges = "YES" if (A+B)<=X else "NO"

# Displaying Result
print(ApplesAndOranges)
