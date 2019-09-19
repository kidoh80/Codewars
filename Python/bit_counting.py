/*
https://www.codewars.com/kata/526571aae218b8ee490006f4

Write a function that takes an integer as input, and returns the number of bits that are equal to one in the binary representation of that number. You can guarantee that input is non-negative.

Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case
*/

import math

def countBits(n):
  if n < 1:
      return (0)
  num_of_digits = int(math.log2(n))
  current_value_num = n
  bits = ""
  for i in range(num_of_digits,-1,-1):
    if 2**i <= current_value_num:
      bits += "1"
      current_value_num -= 2**i
    else:
      bits += "0"
  return (bits.count("1"))
