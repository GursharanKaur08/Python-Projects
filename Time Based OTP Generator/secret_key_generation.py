import pyotp

base_32_secret_key = pyotp.random_base32()
print(base_32_secret_key)

with open('secret_key.txt','w') as wf:
wf.write(base_32_secret_key)
