'''
    There is a fair going on in Chefland. 
    Chef wants to visit the fair along with his N friends. 
    Chef manages to collect K passes for the fair. 
    Will Chef be able to enter the fair with all his N friends?
    A person can enter the fair using one pass, and each pass can be used by only one person.
'''

# Running Loop For Test Cases
for t in range(int(input())):
    
    # Taking Input For N = Number Of Friends; K = Number Of Passes
    N,K = map(int, input().split())
    
    # If Number Of Passes Is More Than Number Of Friends Chef Will Be Able To Enter The Fair Will All His Friends
    PassesForFair = "YES" if N<K else "NO"
    
    # Displaying Result
    print(PassesForFair)