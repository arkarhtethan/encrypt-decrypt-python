
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def brute_force_cipher_text(data):

	result_list = []

	for j in range(26):

	    n = len(data)

	    data=data.upper()

	    result = ""

	    shift = j

	    for i in range(n):

	        character = data[i]

	        if character != ' ':

	            loc = alphabet.find(character)

	            new_loc = (loc + shift) % 26

	            encrypted_data = alphabet[new_loc]

	            result += encrypted_data

	    result_list.append(result)

	return result_list

if __name__ == "__main__":

	brute_force_cipher_text()