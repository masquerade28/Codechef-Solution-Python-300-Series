'''
  Chef rented a car for a day.
  Usually, the cost of the car is Rs 10 per km. 
  However, since Chef has booked the car for the whole day, he needs to pay for at least 300 kms even if the car runs less than 300 kms.
  If the car ran X kms, determine the cost Chef needs to pay.
'''

# Running Loop For Test Cases
for t in range(int(input())):
  
  # Taking input For X = Number Of Kms Chef Travelled
  X = int(input())
  
  # If Chef Travelled Less Than 300 Kms He Still Needs To Pay For Atleast 300 kms Else He Needs To Pay For Total Distance Travelled
  CarTrip = 300*10 if X<300 else X*10
    
  # Displaying Result
  print(CarTrip)
