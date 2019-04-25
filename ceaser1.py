#!/usr/bin/python3

"""

    This module can perform encrypt or decrypt the data

"""


def encrypt(data):
    """ This function simply add 3 to each charcter's position  """

    n = len(data)

    result = ""

    for i in range(n):

        c = data[i]

        index = alphabet.find(c)

        encrypted_data = alphabet[index+3]
        print(f'c = {c} index={index} encrypted-data={encrypted_data}')
        result += encrypted_data

    return result


alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

STR_IN = input("Enter your data  >> ")

STR_OUT = encrypt(STR_IN.upper())

print(f"original {STR_IN}")

print(f"Encrypted format {STR_OUT}")

