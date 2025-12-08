from cryptography.fernet import Fernet,InvalidToken
import random
import os
import sys

with open("key.key", 'rb') as kf:
    key = kf.read()

fn = Fernet(key)

os.chdir("encrypt_test")

def encrypt_random() -> bool:
    files = os.listdir()
    files = [file for file in files if os.path.isfile(file)]
    print(files)
    random_index = random.randint(0,len(files)-1)
    file = files[random_index]

    with open(file, 'rb') as f:
        content = f.read()

    try:
        fn.decrypt(content)
        print(f"File: {file} already encrypted!")
        return False
    except InvalidToken:
        pass
    except Exception as e:
        raise(e)

    encrypted_content = fn.encrypt(content)

    with open(file, 'wb') as f:
        f.write(encrypted_content)

    print(f"File: {file} encrypted!")
    return True

def decrypt_all():
    files = os.listdir()
    files = [file for file in files if os.path.isfile(file)]

    for file in files:
        with open(file, 'rb') as f:
            content = f.read()

        try:
            decrypted_content = fn.decrypt(content)
            print(f"Decrypted file: {file}")
        except InvalidToken:
            decrypted_content = None
        except Exception as e:
            raise(e)

        if decrypted_content:
            with open(file, 'wb') as f:
                f.write(decrypted_content)

register = {
    "1":encrypt_random,
    "2":decrypt_all,
}

def main():
    try:
        choice = input("1 = encrypt random\n2 = decrypt all\n$ ")
        func = register.get(choice)
        if func:
            func()
        else:
            print(f"Unknown option: {choice}")
    except KeyboardInterrupt:
        print("\nStopping...")
        sys.exit(2)


if __name__ == "__main__":
    main()