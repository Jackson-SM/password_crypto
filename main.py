from cryptography.fernet import Fernet

def encrypt_password(password):
  key = Fernet.generate_key()
  f = Fernet(key)
  password_encrypt = f.encrypt(password).decode('utf-8')
  print("Chave: " + key.decode())
  
  return password_encrypt

def main():
  input_password = input("Password: ")
  password_bytes = input_password.encode()
  password = encrypt_password(password_bytes)

  print("Password Encrypted: " + password)

main()