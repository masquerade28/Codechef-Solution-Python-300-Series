'''
  Chef decided to redecorate his house, and now needs to decide between two different styles of interior design.
  For the first style, tiling the floor will cost X1 rupees and painting the walls will cost Y1 rupees.
  For the second style, tiling the floor will cost X2 rupees and painting the walls will cost Y2 rupees.
  Chef will choose whichever style has the lower total cost. 
  How much will Chef pay for his interior design?
'''

# Running Loop For Test Cases
for t in range(int(input())):
  
  # Taking Input For X1 = Cost Of Tiling The Floor In First Style ; Y1 = Cost Of Painting The Walls In first Style ; X2 = Cost Of Tiling The Floor In Second style ; Y2 = Cost Of Painting The Walls In Second Style
  X1,Y1,X2,Y2 = map(int, input().split())
  
  # If Cost Of Tiling And Painting The Walls Is Lower In The First Style Than Cost Of Tiling And Painting The Walls In The Second Style 
    # Than Chef Will Have To Pay Cost Of Tiling In First Style + Painting The Walls In First Style And Vice-Versa
  InteriorDesign = X1+Y1 if X1+Y1 < X2+Y2 else X2+Y2
  
  # Displaying Result
  print(InteriorDesign)
