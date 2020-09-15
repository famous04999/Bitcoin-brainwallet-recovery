Bitcoin wallet recovery tool
![bwrt](MainImage.png)

How it works:
```
From seed phrase create bitcoin
privatekey and then convert it to Wallet Interchange Format key (WiF) format, 
which is a Base-58 form for the random key. 
This is the format that is stored in the Bitcoin Wallet. 


For example a sample private key is generated from:

seed phrase:   alfanumerico

Privatekey:  

05d95cf373f63b44267a193a1ef875c6758996e6c8ab5e049c48eb444206fce8

We then convert this into WiF format (Base-58):

5HrrzGnmMMr6fwkftrtL6AEfkkwWfgFQ8a2Lh8tAtF3MkXF9bPD

This can be stored in a Bitcoin wallet. Next we can take then private key and a 
hash value, and covert it into a useable Bitcoin address, such as:

19JsLFDRxuTsAjapE79FgoVNdNdB2hNU5M

The format of the keys is defined below, where we create a 256-bit private key 
and convert this to a WiF private key. Next we generate a 512-bit public key, 
and then take a 160-bit RIPEM-160 hash and convert to a Bitcoin address:

```
![Bitcoin wallet recovery](hash.png)




Usage:

```
Python3:


cd bitcoin wallet recovery

pip3 install -r requirements.txt

python3 bwr.py



Windows:

dist folder
start bwr.exe

```
Sample:

```
-------------------------------------------------------------------------------------------------------------------------------

Wallet: 


seed phrase:  alfanumerico

Address:    19JsLFDRxuTsAjapE79FgoVNdNdB2hNU5M

Privatekey: 05d95cf373f63b44267a193a1ef875c6758996e6c8ab5e049c48eb444206fce8

Publickey:  046eb8003a20926240dd969929650ac85dc28dcd1a7651c2c39d020c2977704ba4f74ff0ad50361aa7c557d962ccccde34cf7ed7a85e10440c40647c6d17f5b08d

WIF:        b'5HrrzGnmMMr6fwkftrtL6AEfkkwWfgFQ8a2Lh8tAtF3MkXF9bPD'
-------------------------------------------------------------------------------------------------------------------------------

Wallet: 


seed phrase: 
  
Address:    1HZwkjkeaoZfTSaJxDw6aKkxp45agDiEzN

Privatekey: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855

Publickey:  04a34b99f22c790c4e36b2b3c2c35a36db06226e41c692fc82b8b56ac1c540c5bd5b8dec5235a0fa8722476c7709c02559e3aa73aa03918ba2d492eea75abea235

WIF:        b'5KYZdUEo39z3FPrtuX2QbbwGnNP5zTd7yyr2SC1j299sBCnWjss'
-------------------------------------------------------------------------------------------------------------------------------

```
![Bitcoin wallet recovery](screenshot.png)
![Bitcoin wallet recovery](screenshot1.png)



