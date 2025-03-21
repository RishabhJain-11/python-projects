"""
Password Manager

An application to store and generate secure passwords.

Key Features:
- Encryption for security
- Password generator
- Data storage
"""
import string
import random
import getpass
import base64
import hashlib
import os

class PasswordManager:
    def __init__(self, master_password):
        self.master_password = master_password
        self.storage = {}

    def generate_password(self, length=12):
        """
        Generate a random password of a given length.

        :param length: The length of the password.
        :return: The generated password.
        """
        chars = string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.choice(chars) for _ in range(length))

    def set_password(self, key, password):
        """
        Set a password for a given key.

        :param key: The key for the password.
        :param password: The password.
        """
        encrypted_password = self.encrypt(password)
        self.storage[key] = encrypted_password

    def get_password(self, key):
        """
        Get a password for a given key.

        :param key: The key for the password.
        :return: The password.
        """
        encrypted_password = self.storage.get(key)
        if encrypted_password is None:
            return None
        return self.decrypt(encrypted_password)

    def encrypt(self, password):
        """
        Encrypt a password.

        :param password: The password.
        :return: The encrypted password.
        """
        salt = os.urandom(16)
        cipher = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
        return base64.b64encode(salt + cipher).decode()

    def decrypt(self, encrypted_password):
        """
        Decrypt a password.

        :param encrypted_password: The encrypted password.
        :return: The decrypted password.
        """
        encrypted_password = base64.b64decode(encrypted_password)
        salt = encrypted_password[:16]
        cipher = encrypted_password[16:]
        decrypted_password = hashlib.pbkdf2_hmac('sha256', self.master_password.encode(), salt, 100000)
        if decrypted_password != cipher:
            raise ValueError('Invalid master password')
        return decrypted_password.hex()

def main():
    master_password = getpass.getpass('Enter master password: ')
    manager = PasswordManager(master_password)
    while True:
        print('1. Set password')
        print('2. Get password')
        print('3. Generate password')
        print('4. Exit')
        choice = input('Choose an option: ')
        if choice == '1':
            key = input('Enter key: ')
            password = getpass.getpass('Enter password: ')
            manager.set_password(key, password)
        elif choice == '2':
            key = input('Enter key: ')
            password = manager.get_password(key)
            if password is None:
                print('Key not found')
            else:
                print(password)
        elif choice == '3':
            length = int(input('Enter length: '))
            password = manager.generate_password(length)
            print(password)
        elif choice == '4':
            break
        else:
            print('Invalid option')

if __name__ == '__main__':
    main()