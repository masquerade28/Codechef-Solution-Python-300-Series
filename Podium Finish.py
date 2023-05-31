'''
    Chef got his dream seat in F1 and secured a 3rd place in his debut race. 
    He now wants to know the time gap between him and the winner of the race.
    You are his chief engineer and you only know the time gap between Chef and the runner up of the race, given as A seconds, and the time gap between the runner up and the winner of the race, given as B seconds.
    Please calculate and inform Chef about the time gap between him and the winner of the race.
'''

# Running Loop For Test Cases
for t in range(int(input())):
    
    # Taking Input For A = Time Gap Between Chef And Runner Up, B = Time Gap Between The Runner Up And The Winner
    A,B = map(int, input().split())
    
    # Time gap Between Chef And The Winner = Time Gap Between Chef And Runner Up + Time Gap Between The Runner Up And The Winner
    print(A+B)