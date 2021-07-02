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
