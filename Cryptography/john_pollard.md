# john_pollard

## Problem

Sometimes RSA [certificates](https://2019shell1.picoctf.com/static/ccd7ba84ead965bd2033a54c4dbb8ae0/cert) are breakable

## Solution

Get copy of the cert (it is in x509 format):

```
curl https://2019shell1.picoctf.com/static/ccd7ba84ead965bd2033a54c4dbb8ae0/cert > test.cer
```

Extract the public key from certificate:

```
openssl x509 -inform pem -in test.cer -pubkey -noout > key.pub
```

Verify public key is feasibly attackable and extract the values:

```
./RsaCtfTool.py --publickey key.pub --private --verbose
./RsaCtfTool.py --dumpkey --key key.pub

[*] n: 4966306421059967
[*] e: 65537
```

Factorize:

[https://www.alpertron.com.ar/ECM.HTM] - prime factorization tool

```
4966306421059967 = 67867967 * 73176001 
```

**Flag: picoCTF{73176001,67867967}**