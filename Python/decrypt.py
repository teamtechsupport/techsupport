# this script is for decypting various ciphers when provided with a key
import string
import math


def decrypt(encoded, key, ciphertype):
    decrypted = ""
    if ciphertype == "substitution":
        # create a dictionary with each letter of the key corresponding to a letter in the text
        sol = dict(zip(string.ascii_uppercase, key))
        for l in encoded:
            decrypted += sol[l]
        return decrypted
    elif ciphertype == "transposition":
        key = list(key)
        columns = []
        colno = len(key)
        rowno = math.floor(len(encoded)/colno)
        extrachars = len(encoded) % colno
        offset = 0
        for i in range(0, len(encoded), rowno):
            if extrachars > 0:
                columns.append(encoded[i+offset:i+rowno+offset+1])
                extrachars -= 1
                offset += 1
            else:
                columns.append(encoded[i+offset:i+rowno+offset])
        if colno < len(columns):
            del columns[-1]

        neworder = []
        for x in key:
            neworder.append(columns[int(x)-1])

        # for x in range(rowno):
        #    neworder.append([])
        # print(neworder)
        for x in range(len(neworder[0])):
            for y in range(colno):
                # print(x,y)
                try:
                    decrypted += neworder[y][x]
                except:
                    continue

        # for x in range(colno):
        #    for y in range(len(rows)):
        #        try:
        #            decrypted += neworder[x][y]
        #        except:
        #            pass
        return decrypted
