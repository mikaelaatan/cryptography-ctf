# Sussy Curve


### Description
**Elliptic Curve Cryptography** is an encryption algorithm that paved the way for stronger security with smaller key sizes. Compared to algorithms like RSA or Diffie Hellman, it is more efficient because of its ability to produce smaller key sizes without sacrificing security.

The Sussy Curve challenge makes use of *elliptic curve construction*, which is the set of solutions to y2 = x3 + Ax + B, where the constants A and B must satisfy 4A3 + 27B2 ≠ 0.1 to ensure x3 + Ax + B = 0 has no repeated roots. The given elements in this challenge are prime, p, elliptical curve, E, and points P and Q. 


### Insight
Due to time constraints, it was not possible for the team to capture the flag for this challenge. However, the attack we were planning to look into using was the invalid-curve attack. Assuming that the input points were not validated when applying the Elliptic curve Diffie-Hellman attack, it is possible to retrieve the shared secret, $bh_A$.

### Solution
N/A


### Final answer 
N/A
