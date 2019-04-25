
from ceaser4 import encrypt

def main():
    
    with open('hello.txt') as f:

        data = f.read()

        encrypted_data = encrypt(data.strip().upper(),414)

        with open('encrypted_data.txt','w') as ed:

        	ed.write(encrypted_data)

        	ed.write("\n")

        print(f'encrypted data {encrypted_data}')

if __name__ == "__main__":

    main()
