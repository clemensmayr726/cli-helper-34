class CustomError(Exception):
    """Base class for other exceptions."""
    pass

class ValueTooSmallError(CustomError):
    """Raised when the input value is too small."""
    def __init__(self, message="Value is too small!"):
        self.message = message
        super().__init__(self.message)

class ValueTooLargeError(CustomError):
    """Raised when the input value is too large."""
    def __init__(self, message="Value is too large!"):
        self.message = message
        super().__init__(self.message)

class InputValidationError(CustomError):
    """Raised when input validation fails."""
    def __init__(self, message="Invalid input provided!"):
        self.message = message
        super().__init__(self.message)

# Example usage

def validate_input(value):
    if value < 10:
        raise ValueTooSmallError()
    elif value > 100:
        raise ValueTooLargeError()
    return True

try:
    validate_input(5)
except CustomError as e:
    print(e.message)