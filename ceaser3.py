#!/usr/bin/python3

"""

    This module can perform encrypt or decrypt the data

"""


def encrypt(data, shift):
    """ This function simply add 3 to each charcter's position  """

    n = len(data)

    result = ""

    for i in range(n):

        character = data[i]

        loc = alphabet.find(character)

        new_loc = loc + shift

        if new_loc > 26:

            new_loc -= 26

        encrypted_data = alphabet[new_loc]

        result += encrypted_data

    return result


alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

STR_IN = input("Enter your data  >> ")

shift_number = int(input("Enter number to shift data e.g. 4 >> "))

STR_OUT = encrypt(STR_IN.upper(), shift_number)

print(f"original {STR_IN}")

print(f"Encrypted format {STR_OUT}")

