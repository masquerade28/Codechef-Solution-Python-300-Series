'''
  A sorting algorithm A is said to have more time complexity than a sorting algorithm B if it uses more number of comparisons for sorting the same array than algorithm B.
  Given that algorithm A uses X comparisons to sort an array and algorithm B uses Y comparisons to sort the same array, find whether algorithm A has more time complexity.
'''

# Running Loop For Test Cases
for t in range(int(input())):
  
  # Taking Input X = Number Of Comparisons Made By Algorithm A ; Y = Number Of Comparisons Made By Algorithm B 
  X,Y = map(int, input().split())
  
  # If Number Of Comparisons Of Algorithm A Is More Than That Of B, Algorithm A Has More Time complexity
  TimeComplexity = "YES" if X>Y else "NO"
  
  # Displaying Result
  print(TimeComplexity)
