
# ALGORITHM
# Note: assume that list and key are already set
# 1   set location = 1
# 2   repeat until location > (length of the list)
# 3       if list[location] == key
# 4           print "Found at " + location
# 5           end program
# 6       set location = location + 1     advance to next location
# 7
# 8   print "Value not found"

#Demo for Linear Search
import random

#main function
def main():
  find = 0
  SIZE = 9
  MIN = 1
  MAX = 9
  numbers = []
  indexes = []

  find = int(input("ENTER A NUMBER 1-9: "))

  for i in range(0, SIZE):
    indexes.append(i)
    numbers.append(random.randrange(MIN, MAX + 1))

  print(" INDEX: ", indexes)  
  print("NUMBER: ", numbers)

  print ("Searching for: ", find)

  i = 0
  while(i < SIZE):
    if(numbers[i] == find):
      print("Your number is in index: ", i)
      break
    i += 1
  else:
    print("Number not found!")

#call main
main()
