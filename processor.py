import sys

def validate_input(user_input):
    if not user_input.isdigit():
        print("Error: Input must be a number.")
        return False
    if int(user_input) < 1:
        print("Error: Input must be a positive integer.")
        return False
    return True

def process_data(data):
    result = int(data) * 2  # Example processing: doubling the input
    print(f"Processed result: {result}")

if __name__ == '__main__':
    while True:
        user_input = input("Enter a positive integer (or 'exit' to quit): ").strip()
        if user_input.lower() == 'exit':
            print("Exiting program.")
            sys.exit(0)
        if validate_input(user_input):
            process_data(user_input)