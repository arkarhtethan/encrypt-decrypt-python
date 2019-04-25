#!/usr/bin/python3

"""

    This module can perform encrypt or decrypt the data

"""


def encrypt(data, shift):
    """ This function simply add 3 to each charcter's position  """

    n = len(data)

    result = ""

    for i in range(n):

        c = data[i]

        index = alphabet.find(c)

        encrypted_data = alphabet[index+shift]

        result += encrypted_data

    return result


alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

STR_IN = input("Enter your data  >> ")

shift_number = int(input("Enter number to shift data e.g. 4 >> "))

STR_OUT = encrypt(STR_IN.upper(), shift_number)

print(f"original {STR_IN}")

print(f"Encrypted format {STR_OUT}")

