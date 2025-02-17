


#Demo for Linear Search
import random

#main function
def main():
  value = 6;
  numbers = []
  for num in range(1, 10):
    numbers.append(random.randrange(1, 10, 1))
  print(numbers)
  for num in range(1, len(numbers)):
    if(numbers[num] == value):
      print("Your number is in index: ", num)
  if(num == len(numbers)-1):
    print("Number not found!")

#call main
main()
