def reverseBits(n):
  """Reverses the bits of a given number.

  Args:
    n: The number whose bits need to be reversed.

  Returns:
    The number with reversed bits.
  """
  result = 0
  for i in range(32):
    result |= (n >> i) & 1 << (31 - i)
  return result

# Get the number from the user
number = int(input("Enter a number: "))

# Reverse the bits
reversed_number = reverseBits(number)

# Print the reversed number
print("The reversed number is:", reversed_number)