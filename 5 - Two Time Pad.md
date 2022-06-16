# Two-Time Pad

### Challenge
```
Here are five hex-encoded ciphertexts that are encrypted using a one-time pad, but they are all encrypted with the same key.

64111f55cc2852fb7bc84a87614939c55b5ed07d7b60205a14592ad3ae2270603409b20c8db4f7f57bd284ec385e56d444d2ddf9ef1d5dddbcb4a4 781c0443cc2852fb7b865792674824880952db6a676c6752514f37d1bb3e20713f0ee00294b4fab12fcd88b83f104791559bc3fda2081cd2f7e3a4 791f565f833401b87b8618956a4876dc135ac62e7c69225114482cd9af7b6d71221ef31c81e0f7b47c9a83a9325e139d55d8c2e5bf1959ddb2deb0 7159075385224afb789a5791610d30c70313df7b6571225b145332d5ae7b747c344dfe1a9eb9bfb160ddc1ad39541391559bdbf5a30159ddb2f3fe 532a356fb37019ef34d80bb94c7910d3246cda606d5e335659591bddb93a6e670e19fa1ebbabfaac50d392932243569d6fd4def0b63253d7f1fff7

Decrypt the last ciphertext to get the flag.
```

### Description
The Two-Time Pad challenge makes use of the one time pad encryption technique to produce multiple cipher texts using the same key. The one time pad is an uncrackable encryption technique, if multiple conditions are met. In order to encrypt a message, a random secret key is used, and each bit or character of the plain text is encrypted by combining it with the corresponding bit or character of the secret key. 


### Insight
The main vulnerability that the group was able to exploit was the use of the same key to encrypt multiple cipher texts. Hence, it's possible to XOR two ciphertext to get the plaintexts as the key is cancelled out in the equation.
$$C_{1} \oplus C_2 = P_1 \oplus K \oplus P_2 \oplus K$$

In this situation, it is possible to get the message through the crib drag method. By applying XOR to multiple cipher texts, we were able to uncover small clues of the message. We can get the message by using common words and intelligently guessing the rest of the message based on what is given. This was implemented more easily through the use of a [crib drag calculator](https://toolbox.lotusfa.com/crib_drag/). (This is explained more in the solutions part.)

Then, after getting the ciphertext-plaintext pair, we can XOR these with the ciphertext flag to get the plaintext flag. 
$$P_2 = C_{1} \oplus C_2 \oplus P_1$$


### Solution
Our first impression when facing this problem was to try and find the key through the use of repeating key XOR. Due to time constraints, however, we were unable to implement this algorithm, and decided to use the crib drag method since we knew a decent amount of characters already, `CSCI_184.03_CTF{`. 

The **strategy** was to look for the remaining characters of “CSCI_184.03_CTF{“. In order to do this, we focused on using 3 ciphertexts: C1, C2, and C5 (flag). 

We knew that the characters were in C5, so we applied XOR to C2 and C5 to retrieve the first 16 characters of M2. Image below is from the crib drag website (using C2 as ciphertext 1 input, and flag as ciphertext 2 input). The result from the crib drag is the message from C2 which is `here is another `.

[](/media/Pasted image 20220531175423.png)

From there, we were able to find the rest of the characters of M2 by using the crib text that we had and the XOR of C1 and C2. By using the previous message, we were able to get some of the plaintext message from C1 which is `this is a random`. 

[](/media/Pasted image 20220531175559.png)


After that, we tried guessing the plaintext message of C1 and C2 alternately. For instance, we guessed that the next word after `this is random` is  `message`. Then by using the plaintext of C1 as `this is a random message`, we were able to get a longer plaintext of C2 which is `here is another random m`. 

Repeatedly, we used `here is a another random m` as the crib words, then we get `this is a random message encry`. We did the alternating guess strategy repeatedly until we got plaintext M2 from C2: `here is another random message encrypted with the same key.`

After retrieving M2, we were able to retrieve M5 by simply applying XOR: $M2 \oplus C2 \oplus C5$. 

```python
from binascii import hexlify, unhexlify

# from homework 1
def xor_bytes(a, b):
    xorblist = []
    for (a_ch,b_ch) in zip(a,b):
        xor = a_ch^b_ch
        xorb = bytes([xor])
        xorblist.append(xorb)
    xorbytes = b''.join(xorblist)
    return xorbytes

C1 = unhexlify(b'64111f55cc2852fb7bc84a87614939c55b5ed07d7b60205a14592ad3ae2270603409b20c8db4f7f57bd284ec385e56d444d2ddf9ef1d5dddbcb4a4')

C2 = unhexlify(b'781c0443cc2852fb7b865792674824880952db6a676c6752514f37d1bb3e20713f0ee00294b4fab12fcd88b83f104791559bc3fda2081cd2f7e3a4')

C5flag = unhexlify(b'532a356fb37019ef34d80bb94c7910d3246cda606d5e335659591bddb93a6e670e19fa1ebbabfaac50d392932243569d6fd4def0b63253d7f1fff7')

xor_c = xor_bytes(C2,C5flag)

# we already know the first few characters of the flag is  CSCI_184.03_CTF{ (len=16)
# use the crib drag calculator online to try and guess the message https://toolbox.lotusfa.com/crib_drag/

M2 = b'here is another random message encrypted with the same key.'

flag = xor_bytes(M2,xor_c)
flag
```

This gave us a flag of `CSCI_184.03_CTF{__one_time_means_the_key_is_used_only_once}`.


### Final answer 
`CSCI_184.03_CTF{__one_time_means_the_key_is_used_only_once}`
