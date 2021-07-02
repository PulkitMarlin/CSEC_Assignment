# Task 2

The task had given two links - one to the official Julia language page, and other to the challenge code. As it was clear that code is in Julia, and I was hearing about it for the first time, I started reading its documentation to get a basic feel.
After I got the hang if it, I started to go through the challenge.

The first thing that I noticed was that all even output come from “f(a::Int64)" and odd come from “f(a::Float64)”. 
I understood that FLAG is a string and on each character of the String, some operation was done followed by either calling the "Int64" version or "Float64" version.

I tried to understand the code more, and figured out that each character of the String was converted to an integer between 0 and 255 (both inclusive) and stored in vector s. 
Then 2 vectors, x and y were made which were 2 random subsequences of the indices of the vector s. 
Then a new vector o was made which had "Float64" type entries for all indices in x and "Int64" type entries for all indices in y.

Actually, Float was there just to distinguish the data types, as all values are integers between 0 and 255, it does not matter if we convert it to Float and apply some Round function.

After figuring this, it was simple, I wrote a script to compute the value of vector o (by checkinng odd-even), and from which I computed the given String.

```python
encryptedFlag = [204, 216, 389, 413, 493, 437, 234, 197, 465, 421, 224, 433, 205, 381, 401, 421, 213, 449, 209, 232, 198, 208, 381, 98, 461, 190, 209, 477, 202, 213, 193, 437, 405, 250]

o = []

for e in encryptedFlag:
    if e%2 == 0:
        o.append(chr(int(e/2)))    
    else:
        temp = e-1
        assert temp%4 == 0
        o.append(chr(int(temp/4)))
        
print(''.join([s for s in o]))

```

**The Final Flag:**

flag{mu1tipl3_di5p4tch_1s_4we50me}
