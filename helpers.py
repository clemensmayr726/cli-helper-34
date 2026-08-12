def get_user_input(prompt: str) -> str:
    user_input = input(prompt).strip()
    if not user_input:
        raise ValueError('Input cannot be empty.')
    return user_input


def validate_input(user_input: str) -> bool:
    # Add basic validation logic here
    if len(user_input) < 3:
        print('Input is too short. It must be at least 3 characters.')
        return False
    return True


def process_input():
    while True:
        try:
            user_input = get_user_input('Please enter some input: ')
            if validate_input(user_input):
                print(f'Processing input: {user_input}')
                break
        except ValueError as e:
            print(e)


if __name__ == '__main__':
    process_input()