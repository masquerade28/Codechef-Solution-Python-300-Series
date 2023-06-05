'''
    Chef is not feeling well today. 
    He measured his body temperature using a thermometer and it came out to be X °F.
    A person is said to have fever if his body temperature is strictly greater than 98 °F.
    Determine if Chef has fever or not.
'''

# Running Loop For Test Cases
for t in range(int(input())):
    
    # Taking Input For X = The Body Temperature Of Chef In °F
    X = int(input())
    
    # If Chef's Body Temperature > 98 °F, Chef Is Having Fever
    Fever = "YES" if X>98 else "NO"
    
    # Displaying Output
    print(Fever)