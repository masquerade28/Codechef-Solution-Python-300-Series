'''
  Chef's computer has N GB of free space. 
  He wants to save X files, each of size 1 GB and Y files, each of size 2 GB on his computer. 
  Will he be able to do so?
  Chef can save all the files on his computer only if the total size of the files is less than or equal to the space available on his computer.
'''

for t in range(int(input())):
    
  N,X,Y = map(int, input().split())
    
  EnoughSpace = "YES" if (X+(Y*2)) <= N else "NO"
    
  print(EnoughSpace)
