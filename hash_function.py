import hashlib
str = "Hellow world"
hast_object = hashlib.sha256(str.encode())
hast_dihest = hast_object.hexdigest()
print(hast_dihest)