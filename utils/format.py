

def print_error(message):
    # ANSI escape sequence for red color
    red_color_code = '\033[91m'
    # ANSI escape sequence for reset color
    reset_color_code = '\033[0m'

    # Print error message with red color
    print(red_color_code + "Error: " + message + reset_color_code)
    
def print_success(message):
    # ANSI escape sequence for green color
    green_color_code = '\033[92m'
    # ANSI escape sequence for reset color
    reset_color_code = '\033[0m'

    # Print success message with green color
    print(green_color_code + "Success: " + message + reset_color_code)
