# Function to encode password.
def encode(password):
    encoded_password = ''
    for i in password:
        encoded_character = int(i) + 3
        encoded_password += str(encoded_character)
    return encoded_password
# Nihitha added this portion
def decode(encoded_password):
    decoded_password = ''
    for i in encoded_password:
        decoded_character = int(i) - 3
        decoded_password += str(decoded_character)
    return decoded_password
def main():
    # Loop to keep printing menu.
    while True:
        print('\nMenu')
        print('-' * 13)
        print('1. Encode\n2. Decode\n3. Quit')

        user_option = int((input('\nPlease enter an option: ')))

        # If statements based on selection of user.
        if user_option == 1:
            user_password = input('Please enter your password to encode: ')
            encode(user_password)
            print('Your password has been encoded and stored!')

        if user_option == 2:
            encoded_password = encode(str(user_password))
            decoded_password = decode(encoded_password)
            print(f'\nThe encoded password is {encoded_password}, and the original password is {decoded_password}.')
        if user_option == 3:
            break

if __name__ == '__main__':
    main()

