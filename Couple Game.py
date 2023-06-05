'''
    There are G girl and B boy students at IIT (BHU) such that B>G.
    If ICM were a team game where teams could only be of size 2, having exactly 1 girl student and 1 boy student, what would be the minimum number of boy students from IIT (BHU) who would not be able to participate?
'''

# Running Loop For Test Cases
for t in range(int(input())):
    
    # Taking Input For G = Number Of Girls; B = Number Of Boys
    G,B = map(int, input().split())
    
    # Number Of boys Who Would Not Be Able To Participate = Number Of Boys - Number Of Girls
    print(B-G)