# Sussy Curve

### Challenge
```
This curve is kinda sus...

p = 19795792123893480164707100824397222730984965037169701408771662919270303874559
E = EllipticCurve(GF(p), [0, 0])

P = (707002063975494596713847148175220691822212124553576248947618210771357641646, 18227228301613195162842834072053449250839439585958223304702634485212835672756)
Q = (2199645095445255323751849685677282723957624019648389953902214339928394082920, 2823110710129739364184391980414426860914344540615024907439483475467880621450)  # Q == d*P

key = SHA256(str(d))  # use this to decrypt the flag

[](/media/sussycurve.zip)

```

### Description
**Elliptic Curve Cryptography** is an encryption algorithm that paved the way for stronger security with smaller key sizes. Compared to algorithms like RSA or Diffie Hellman, it is more efficient because of its ability to produce smaller key sizes without sacrificing security.

The Sussy Curve challenge makes use of *elliptic curve construction*, which is the set of solutions to y2 = x3 + Ax + B, where the constants A and B must satisfy 4A3 + 27B2 ≠ 0.1 to ensure x3 + Ax + B = 0 has no repeated roots. The given elements in this challenge are prime, p, elliptical curve, E, and points P and Q. 


### Insight
Due to time constraints, it was not possible for the team to capture the flag for this challenge. However, the attack we were planning to look into using was the invalid-curve attack. Assuming that the input points were not validated when applying the Elliptic curve Diffie-Hellman attack, it is possible to retrieve the shared secret, $bh_A$.

### Solution
N/A


### Final answer 
N/A
