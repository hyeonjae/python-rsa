from math import gcd
import random

def lcm(a, b):
  return int(a * b / gcd(a, b))

class RSA:
  def __init__(self, p, q):
    self.n = p * q
    phi = RSA._totient(p, q)
    self.e = RSA._find_e(phi)
    self.d = RSA._find_d(self.e, phi)

  def encryption(self, m):
    return RSA._encryption(m, self.e, self.n)

  def decryption(self, c):
    return RSA._decryption(c, self.d, self.n)

  @staticmethod
  def _encryption(m, e, n):
    return RSA._modular(m, e, n)

  @staticmethod
  def _decryption(c, d, n):
    return RSA._modular(c, d, n)

  @staticmethod
  def _modular(a, b, c):
    acc = 1
    for i in range(b):
      acc = (acc * a) % c
    return acc

  @staticmethod
  def _totient(a, b):
    return lcm(a - 1, b - 1)

  @staticmethod
  def _find_e(phi):
    candidates = []
    for e in range(2, phi - 1):
      if gcd(e, phi) == 1:
        candidates.append(e)
    return random.choice(candidates)
    
  @staticmethod
  def _find_d(e, phi):
    candidates = []
    for d in range(2, phi):
      if (e * d) % phi == 1:
        candidates.append(d)
    return random.choice(candidates)

