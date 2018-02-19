import unittest
import random
from rsa.core import RSA

class TestRSA(unittest.TestCase):

  def test_enc_and_dec(self):
    for p, q in [(7, 11), (61, 53), (811, 101), (3, 997)]:
      rsa = RSA(p, q)
      samples = [random.randrange(1, p * q) for _ in range(5)]
      for m in samples:
        c = rsa.encryption(m)
        result = rsa.decryption(c)
        self.assertEqual(result, m)



