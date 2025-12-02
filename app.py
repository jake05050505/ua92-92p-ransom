from cryptography.fernet import Fernet
import random
import os

with open("key.key", 'rb') as kf:
    key = kf.read()

    # print(key)

fn = Fernet(key)

os.chdir("encrypt_test")

def encrypt_random():
    dir = os.listdir()
    ran = random.randint(0,len(dir)-1)
    random_file = dir[ran]

    with open(random_file, 'r') as f:
        content = f.readlines()[0].encode()
    encrypted_content = str(fn.encrypt(content))

    with open(random_file, 'w') as f:
        f.write(encrypted_content)

    print(f"File {random_file} encrypted!")

def decrypt_all():
    for file in os.listdir():
        with open(file, 'r') as f:
            content = f.readlines()[0]
            if content[0:2] == 'b\'' and content[-1] == '\'':
                decrypted_content = fn.decrypt(content.lstrip('b').strip('\'').encode())
                pass
            else:
                decrypted_content = None

        if decrypted_content:
            with open(file, 'w') as f:
                f.write(str(decrypted_content).lstrip('b').strip('\''))

if __name__ == "__main__":
    choice = int(input("1 = encrypt random\n2 = decrypt all\n$ "))
    if choice == 1:
        encrypt_random()
    elif choice == 2:
        decrypt_all()