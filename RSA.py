import random
from sympy import isprime

 
def generate_prime(bitsize=2048):
    while True:
        number = random.getrandbits(bitsize)
        if isprime(number):
            return number

 
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
 
def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

 
def generate_keys(bitsize=2048):
    p = generate_prime(bitsize)
    q = generate_prime(bitsize)
    
    n = p * q
    phi = (p - 1) * (q - 1)
    
    e = random.randrange(2, phi)
    while gcd(e, phi) != 1:
        e = random.randrange(2, phi)
    
    d = mod_inverse(e, phi)
    
 
    return ((e, n), (d, n))

 
def encrypt(public_key, message):
    e, n = public_key
    
    message_int = int.from_bytes(message.encode(), 'big')
    cipher = pow(message_int, e, n)
    return cipher

 
def decrypt(private_key, cipher):
    d, n = private_key
    
    decrypted_int = pow(cipher, d, n)
    decrypted_message = decrypted_int.to_bytes((decrypted_int.bit_length() + 7) // 8, 'big').decode()
    return decrypted_message

 
if __name__ == "__main__":
 
    public_key, private_key = generate_keys(bitsize=2048)
    
  
    message = input("Enter a message to encrypt: ")
    print(f"Original Message: {message}")
    
   
    encrypted_message = encrypt(public_key, message)
    print(f"Encrypted Message: {encrypted_message}")
    
    
    decrypted_message = decrypt(private_key, encrypted_message)
    print(f"Decrypted Message: {decrypted_message}")
