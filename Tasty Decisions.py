'''
  Chef is buying sweet things to prepare for Halloween!
  The shop sells both chocolate and candy.
    -> Each bar of chocolate has a tastiness of X.
    -> Each piece of candy has a tastiness of Y.
  One packet of chocolate contains 2 bars, while one packet of candy contains 5 pieces.
  Chef can only buy one packet of something sweet, and so has to make a decision: which one should he buy in order to maximize the total tastiness of his purchase?
  Print Chocolate if the packet of chocolate is tastier, Candy if the packet of candy is tastier, and Either if they have the same tastiness.
'''

# Running Loop For Test Cases
for t in range(int(input())):
  
  # Taking Input For X = Tastiness Of Chocolate; Y = Tastiness Of Candy
  X,Y = map(int, input().split())
  
  # Checking If Total Tastiness Of Chocolate Is Greater Than Total Tastiness Of Candy
  if (X*2) > (Y*5):
      print("Chocolate")
  
  # Checking If Total Tastiness Of Chocolate Is Equal To Total Tastiness Of Candy
  elif (X*2) == (Y*5):
      print("Either")
 
  # Else Candy Will Be More Tastier
  else:
      print("Candy")
