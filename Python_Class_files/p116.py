s="hello,how are you?"
s2=""
for c in s:
    s2=s2+chr(ord(c)+10)
print(s2)

s3=""
for c in s2:
    s3=s3+chr(ord(c)-10)
print(s3)
