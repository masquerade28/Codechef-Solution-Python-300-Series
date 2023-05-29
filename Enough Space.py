'''
  Chef's computer has N GB of free space. 
  He wants to save X files, each of size 1 GB and Y files, each of size 2 GB on his computer. 
  Will he be able to do so?
  Chef can save all the files on his computer only if the total size of the files is less than or equal to the space available on his computer.
'''

# Running Loop for Test Cases
for t in range(int(input())):
  
  # Taking Input For N = Free Space In Chef's Computer; X = Files Of 1 GB That Chef Want To Save; Y = Files Of 2 GB That Chef Want To Save
  N,X,Y = map(int, input().split())
    
  # If Total Space Occupied By Files < Total Free Space Availabe; Then Chef Can Save All The Files
  EnoughSpace = "YES" if (X+(Y*2)) <= N else "NO"
   
  # Printing Result
  print(EnoughSpace)
