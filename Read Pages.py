''' 
    Chef has started studying for the upcoming test. 
    The textbook has N pages in total. 
    Chef wants to read at most X pages a day for Y days.
    Find out whether it is possible for Chef to complete the whole book.
'''

# Running Loop For Test cases
for t in range(int(input())):
    
    # Taking Input For N = Total Number Of Pages; X = Number Of Pages Chef Want To Read Per Day; Y = Number Of Days Chef Will Read
    N,X,Y = map(int, input().split())
    
    # If Number Pages Read Per Day For Y Days Is Greater Than Total Number Of Pages, Chef Will Be Able To Complete The Book
    ReadPages = "YES" if ((X*Y)>=N) else "NO"
    
    # Displaying OUTPUT
    print(ReadPages)