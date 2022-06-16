# Shattered  

### Challenge
```
The Better Freedom Wall admins have made "significant progress," whatever that means! You just found out that they have a super secret admin portal: [](https://bfwadmin.lunchtimeattack.wtf)

Luckily, your friend also managed to yoink the server code that runs it.

[](/media/admin_server.py)

```

### Description

"This industry cryptographic hash function standard is used for digital signatures and file integrity verification ([shattered.io]( https://shattered.io/))." In 2017, cryptographic researchers announced the first real-world collision attack that allows the creation of two documents with different contents, but  have the same SHA-1 digital signature. 

In this challenge, the flag is revealed when SHA-1 digests of the username and password are the same, but the caveat is that its input values must be different. To solve the challenge, the user must find two unique input values that have the same SHA-1 digest, then send it to the login server through the POST method. 



### Insight

The webpage shows a simple sign-in form. Upon trying out different login combinations, `admin:admin`, `root:admin`, `admin:password`. The group identified two main responses:
* '**Error:** Your password cannot be the same as your username.'
* '**Error:** Incorrect password.'
This is also inline with the responses from `admin_server.py` code.

Upon further inspection of the Network tab in the browser's developer tools, the payload shows that the login page encodes the username and password using Base64. Afterwards, the group was able to identify the variables used in the form data (`user` & `pass`) that is submitted to the backend. For example for `admin:admin`, the parsed form data is `user=YWRtaW4%3D&pass=YWRtaW4%3D`.

After inspecting the webpage, the group viewed the `admin_server.py` back-end code. From here, we saw that:
1. The server uses the POST method to pass the data.
2. The server decodes the data using a Base64 decoder. 
3. **The flag is revealed if the username and password are different, but their SHA-1 digest are the same.** 

Going back to the form responses, the **username and password cannot be the same**; therefore, in order to get the flag, the user must input a  username and password combination that have *different* values but have the *same* SHA-1 digest. 

The website, https://shattered.io/, discusses that it is now possible for attackers to produce two different documents with same SHA-1 digital signature (collision attack). Therefore, we use the same SHA-1
  
### Solution

1. Find two inputs that have the same exact values but with different SHA-1 digest. 
	* The website, https://shattered.io/, provides two PDF files that have different content but same SHA-1 digest. 
	* PDF links: https://shattered.io/static/shattered-1.pdf & https://shattered.io/static/shattered-2.pdf

2. Using Python, open PDF links and read its content. Store the content of the 1st PDF as the username  `admin`, then store the content of the 2nd PDF as the password `adminpw`. In order to not exceed the max length data that the POST method can handle, we'll only use the first 1000 lines. 
```python
from urllib.request import urlopen

admin = urlopen("http://shattered.io/static/shattered-1.pdf").read()[:1000]
adminpw = urlopen("http://shattered.io/static/shattered-2.pdf").read()[:1000]
```

3. From what we saw on the payload from the Networks tab, the log-in form encodes the username and password using Base64 before it passes the data to the back-end server. 
```python
from base64 import b64encode

bfwuser = b64encode(admin)
bfwpass = b64encode(adminpw)
```

4. Send a POST request to the login page using the variables from the payload and the Base64 encoded credentials from the previous step. 
```python
import requests
 
url = 'http://bfwadmin.lunchtimeattack.wtf/login'
myjson = {'user': bfwuser, 'pass': bfwpass}

req = requests.post(url, data = myjson)
req.text
```
```python
'CSCI_184.03_CTF{7h3_SHA_1n_sha-1_57and5_4_SHAtt3r3d!!!}'
```

### Final answer 
`CSCI_184.03_CTF{7h3_SHA_1n_sha-1_57and5_4_SHAtt3r3d!!!}`
