def is_valid_input(user_input):
    if not user_input:
        return False
    if not isinstance(user_input, str):
        return False
    if len(user_input) < 3:
        return False
    return True

def process_user_input():
    while True:
        user_input = input('Enter something (type exit to quit): ')
        if user_input.lower() == 'exit':
            print('Exiting the program.')
            break
        if not is_valid_input(user_input):
            print('Invalid input. Please enter at least 3 characters.')
            continue
        print(f'Processing input: {user_input}')

if __name__ == '__main__':
    process_user_input()