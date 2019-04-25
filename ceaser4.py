#!/usr/bin/python3

"""

    This module can perform encrypt or decrypt the data

"""

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def encrypt(data, shift):
    """ This function simply add 3 to each charcter's position  """

    n = len(data)

    result = ""

    for i in range(n):

        character = data[i]

        if character != ' ':

            loc = alphabet.find(character)

            new_loc = (loc + shift) % 26

            encrypted_data = alphabet[new_loc]

            # print(f'encrypted_data {encrypted_data} new_loc {new_loc} loc {loc} character {character}')
        
            result += encrypted_data

    return result


if __name__ == "__main__":

    STR_IN = input("Enter your data  >> ")

    shift_number = int(input("Enter number to shift data e.g. 4 >> "))

    STR_OUT = encrypt(STR_IN.upper(), shift_number)

    print(f"original {STR_IN}")

    print(f"Encrypted format {STR_OUT}")

