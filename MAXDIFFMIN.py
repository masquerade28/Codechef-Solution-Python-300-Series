'''
    Chef is given 3 integers A,B, and C such that A<B<C.
    Chef needs to find the value of max(A,B,C)−min(A,B,C).
    Here max(A,B,C) denotes the maximum value among A,B,C while min(A,B,C) denotes the minimum value among A,B,C.
'''

# Running Loop For Test Cases
for t in range(int(input())):
    
    # Taking Input For A = First Integer, B = Second Integer, C = Third Integer
    A,B,C = map(int, input().split())
    
    # Displaying Out 
    print(max(A,B,C)-min(A,B,C))
    
    # Another Way Of Doing Is Subtracting A From C Bcz, A<B<C
    print(C-A)