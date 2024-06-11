import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

def main():
    
    while(True):
        try:
            length = int(input("Enter the length of the password: "))
            password = generate_password(length)
            print("Your generated password is:", password)
        except:
            print("Invalid length. Please enter a valid length.")
            continue



if __name__ == "__main__":
    main()
