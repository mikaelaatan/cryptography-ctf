# RSA Encraption


### Challenge
```
The flag has been encrypted using 256-bit RSA encraption (no that's not a typo). This RSA variant is so secure you can't even decrypt it with "normal" RSA!

N = 0x69692c95b90574445a697e1a5e6e10169cb172365f5273b492005b883265b26a15b8e76dc1c0a821e41fba789319851c2d5dd5f3c4fe3344f434c94852ba2d0d
e = 0x11
c = 0x3e79575d4ed2ba453618ba60cbd55421ea7e63723126991b6f4114e5f85937be4e3833d79741330a42938b68dc38eb0eada56bba2803566a0589c2d630d886db

[](/media/rsa_encraption.sage)
```


### Description
The RSA encryption scheme is insecure, but a huge stepping stone for more secure schemes that are used in practice (Guadalupe, 2022). It makes use of public and private keys, wherein the concept is somewhat similar to giving someone you trust the key to your house to give them access to your place.

The challenge used 256-bit RSA encryption to hide the flag. The details given are the modulus $N$, public exponent $e$ and ciphertext $c$.

### Insight
In this situation, there was no vulnerability in the situation, the situation was more of incorrectly generated RSA keys, wherein the problem was that it is impossible to decrypt due to the incorrectly generated keys. When generating the public exponent, e, this must be relatively prime to Euler’s totient function. The problem is that this step was not assured in this situation. Lucky for us, there was an algorithm created to decrypt incorrectly generated p and q primes in an RSA scheme. The algorithm recovers potential plaintexts in seconds for 4096-bit keys.


### Solution


**1. Understanding the problem**

Initially, the problems that the group was looking for were weakly generated RSA keys, or small generated RSA keys. This was done by trying to factor out modulus $N$, and double checking the size of modulus $N$. In this case, none of the aforementioned were the problems, instead, the problem was trying to recover the plaintext because of the incorrectly generated keys. In the case of incorrectly generated keys, it is impossible to decrypt the message.

The keys were incorrectly generated because they oversaw the step that the public exponent $e$ must be relatively prime to totient’s function. In this case, totient’s function is divisible by $e$.

![](https://lh5.googleusercontent.com/u9aDDtcBOJk_QvSz1uYCRX5G5wBWhzy2js8-CZ3gX9y5gVPTqSg9jBqD4Um98xcxC3XVeApXUs4ZD5JiICPvZLxAPqMWvHc7_iSGAZ9HkMJ1_cFZ3BVsoDx6LyBNkvSTIM4OK6iZ__EJXiwx-w)



**2. Creating Algorithm 1**

After understanding the problem, we identified that the decryption algorithm was taken from [Daniel Shumow’s paper on “Incorrectly Generated RSA Keys”](https://eprint.iacr.org/2020/1059.pdf). Algorithm 1 makes use of a subgroup $E$, which is a set of e-order elements in $(Z/NZ)^X$ that will give all the potentially lost factors of the plaintext. 
![](https://lh6.googleusercontent.com/Tt31ekUFJWJ7E76R6KYTCCybkUM2hrp7nxFnnue7XdN4ls6RtGkSi-aGnHe2PLVaZk4UQ_oO6CBtqkGp1P3hjnl3C6-P4JeIlAkqjvYug5RtWvlq9dLnrynlgcmdeq2dJss-_e69iD33pvHqww)

The end result of the algorithm is returning a generator $gE$ of $E$. This generator is responsible for generating all elements of the subgroup $E$, which is important to use in Algorithm 2.

```python
# Algorithm 1
def rsa_decrapt(c,N,e,p,q):
	totient = (p-1) * (q-1)
	totient_over_e = totient / e
	g = 1
	ge = 1

	while ge == 1:
		g += 1
		ge = pow(g, totient_over_e, N)

	print(f'GE: {ge}')
```

**3. Creating Algorithm 2**

Algorithm 2 makes use of this generator to create all elements from subgroup $E$, and using each element, creates a plaintext with correct padding. The algorithm then returns all potential plaintexts from the code.

![](https://lh3.googleusercontent.com/GDrJ2fiLDmwq_nVXiDUrgb35n3Hs7sDOVTr9S22N9MA1Nos5uv9j8ceqLz0XwouTwcdInTCT7qxWCOoEaVVu36efgCYbMj-wySu5SM843eevhSHbHXYtCdKrYwlo0IW1ulkzq75H32T2_Aujvw)

Due to time constraints, we were unable to implement Algorithm 2 fully. Instead of looking for the correct padding, we decided to go through all the plain texts and figure out which of the plain texts looks most likely to be the flag. We faced a problem here, however, because some of the plain texts returned a non-hexadecimal number, giving an error. In order to bypass this, the group used a try and except clause so that the algorithm would continue running despite running through an error. From there, we got the flag: `CSCI_184.03_CTF{n0_m3s5age_15_und3cr4p7abl3}`

```python 
# Algorithm 2
p = [] 
plain_texts = [] 
d = mod(1/e, totient_over_e) 
a = pow(Integer(c), d, N) 
ell = mod(1, N) 

print(f'd: {d}') 
print(f'a: {a}') 

for i in range(0, e): 
	x = mod(a * ell, N) 
	p.append(x) 
	ell = mod(ge * ell, N) 
	
for j in p: 
	try: 
		plain_texts.append(bytes.fromhex(hex(j).replace('0x', '')).decode('unicode-escape'))
	except Exception as e: 
		print(e)

return plain_texts
```

*Outputs:*
![](https://lh4.googleusercontent.com/Cw2XPDiAmyrm9qu_ACQn8GQOzJdJjj0GJUCWNXXoSYmIG5sNY9thu52kHUj5KU0Z2UizmT1c093X0YWaeigl1j-uprruiyx9xgz65tt4dQFxglbSbiDiMRWgBpb4f8XMUhjbVmQp-uWDm5k0Ew)
![](https://lh3.googleusercontent.com/_N4eDkbBDQzTp-yKol2BGgyguzxQCd_xEjjeQ1vJuXLlMIeUAJjSCnBughuIBaABHFBL8zVbYQ2eRU6aXjoDVEgOybJG5Wu_-H4Ox9eThONUM2CwuJFI3tNY9DlKuxUFfFLjrkAfC4glVxG9_w)


### Final answer 
`CSCI_184.03_CTF{n0_m3s5age_15_und3cr4p7abl3}`
