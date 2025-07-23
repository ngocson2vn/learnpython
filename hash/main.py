from hashlib import sha256

str = "Hello"
hash = sha256(str.encode('utf-8')).hexdigest()
out_str = f"{int(hash, base=16)}"
print(out_str[:6])