#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?
import math


class Problem_3:
  def __init__(self):
    self.result = 0

  def is_prime(self, number):
    if number < 2: return False
    for i in range(2, int(math.sqrt(number)) + 1):
      if number % i == 0:
        return False
    return True

  def solve(self, limit):
    i = 2
    while i * i <= limit:
      if limit % i:
        i += 1
      else:
        limit //= i
      self.result = limit

    return self.result


p = Problem_3()
print(p.solve(600851475143))
print(p.is_prime(p.solve(600851475143)))

