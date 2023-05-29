'''
  Chef has recently started learning from the new CodeChef SQL course.
  He has a table which initially has R rows and C columns. 
  He then adds E extra rows to it. 
  How many total cells does he have finally?
'''

# Taking Input For R = No. Of Rows; C = No. Of Columns; E = No. Of Newly Added Rows
R,C,E = map(int, input().split())

# Total Number Of Cells = (Rows + New Rows) * Columns
print((R+E)*C)
