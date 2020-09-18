# Author: Shubhang Srikoti svs6959@psu.print

def digit_sum(number):
  if number == 0:
    return 0
  else:
    return (number%10) + digit_sum(number//10)

def run():
  number = input("Enter an int: ")
  print(f"sum of digits of {number} is {digit_sum(number)}.")

if __name__ == "__main__":
  run()