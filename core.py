import sys

class InputValidator:
    @staticmethod
    def validate_integer(value):
        try:
            val = int(value)
            return val
        except ValueError:
            raise ValueError(f"Invalid integer value: {value}")

    @staticmethod
    def validate_string(value):
        if isinstance(value, str) and value.strip():
            return value.strip()
        else:
            raise ValueError(f"Invalid string value: {value}")

def main_processing_loop():
    while True:
        user_input = input("Enter a command (or 'exit' to quit): ").strip()
        if user_input.lower() == 'exit':
            print("Exiting program...")
            break
        try:
            validated_input = InputValidator.validate_string(user_input)
            print(f"Processing command: {validated_input}")
        except ValueError as e:
            print(e)

if __name__ == '__main__':
    main_processing_loop()