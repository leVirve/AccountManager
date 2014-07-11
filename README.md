Colleac
==============

Colleac save accounts information in local computer.

  - Local storage database
  - Account information will be encrypted
  - AES-256 encryption and SHA hash

> [AES] [1] is a specification for the encryption of electronic data established by the U.S. National Institute of Standards and Technology (NIST) in 2001


Version
----

Demo Version

Tech
-----------

Colleac uses open source libraries ( Python packages ):

* [Python] - ( this poject base on python3 )
* [PyCrypto] - awesome collection of secure hash functions and encryption algorithms
* [SQLite3] - provides a lightweight disk-based database that doesn’t require a separate server process

Details
--------------

##### Encryption Used

```
    'Database': protected by an SHA-2(SHA512) hashed key
    'Account Entries': before saving, password will be encrypted by AES 256
```

##### Instructions


```
    '0 : add accounts list in file named "data.in"'
    '1 : add account manually'
    '2 : search account info in database'
    '3 : delete account in database by ID'
    'q : exit'
```


License
----

GPL v2


**Simple Demo with python, Yeah!**

[1]:http://en.wikipedia.org/wiki/Advanced_Encryption_Standard
[python]:https://www.python.org/
[PyCrypto]:https://pypi.python.org/pypi/pycrypto
[sqlite3]:https://docs.python.org/3.4/library/sqlite3.html
