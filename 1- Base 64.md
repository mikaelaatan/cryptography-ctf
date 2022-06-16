# 🇧🇦🇸🇪6️⃣4️⃣

### Description
- The challenge used Base64 encoding to hide the flag, but the base64 characters are converted into emojis. The 64 emojis (key) is provided in the challenge, and this maps to the 64 characters in the Base64 encoding scheme. For instance, 😀 maps to index 0 which is A, 😁 maps to index 1 which is B, and so on... To get the base64 encoded flag, get the index of each emoji in the flag (😐 is index 16) and then match the index to the Base64 character list (index 16 = Q). Finally, to get the plaintext flag, decode the base64 flag using the b64decode package from Python. 

### Insight
* One of the algorithms in the private-key encryption scheme is the *decryption algorithm*. It involves taking a key *k* and a ciphertext *c*, in order to output the plaintext *m* (which in this case is the flag). Since the challenge revealed the 'first 64 emojis' used in encryption, the team realized that its number (64) matches the number of characters in the base64 encoding scheme.
  
### Solution

1.  Review the Base64 character chart. 
![[Pasted image 20220524172333.png]]
[Encoding and Decoding Base64 Strings in Python - GeeksforGeeks](https://www.geeksforgeeks.org/encoding-and-decoding-base64-strings-in-python/)

2.  Using Python, create a list of the given 64 emojis so that each emoji's index is easily retrievable. 
``` python
emojiDB = list("😀😁😂😃😄😅😆😇😈😉😊😋😌😍😎😏😐😑😒😓😔😕😖😗😘😙😚😛😜😝😞😟😠😡😢😣😤😥😦😧😨😩😪😫😬😭😮😯😰😱😲😳😴😵😶😷😸😹😺😻😼😽😾😿")
```

3. Find the index of each emoji in the encoded flag corresponding to the `emojiDB` list. For instance, the first emoji in the flag `😐` is index 16 in the `emojiDB` list. Repeat until all emojis have a corresponding index. 
```python
block = list('😐😵😍😃😒😕😼😱😎😃😐😮😌😃😍😟😐😵😑😆😞😶😉😡😜😶😔😶😍😂😭😥😛😓😁😪😌😕😽😩😜😵😽😮😌😇😑😟😙😖😹😣😜😧😥😰😍😳😄😰😛😢😄😡😈😒😅😽')

b64num = []
for emoji in block:
    emojinum = emojiDB.index(emoji)
    b64num.append(emojinum)
```

4.  Use the `b64num` index list in finding the corresponding Base64 character of each decimal number. For example, index 16 (`b64[16]`) is Q. Repeat until all decimal numbers are converted into characters. 
```python
b64 = list('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=') # from the Base64 character chart
b64letters = ''
for num in b64num:
    letters = b64[num]
    b64letters += letters
```
```python
#b64letters
'Q1NDSV8xODQuMDNfQ1RGe2Jhc2U2NCtlbTBqMV9pc19uMHRfZW5jcnlwNzEwbiEhISF9'
```

5.  Decode the string using the Base64 python package. 
```python
from base64 import b64encode, b64decode
b64decode(b64letters)
```
```python
b'CSCI_184.03_CTF{base64+em0j1_is_n0t_encryp710n!!!!}'
```

### Final answer
``CSCI_184.03_CTF{base64+em0j1_is_n0t_encryp710n!!!!}``
