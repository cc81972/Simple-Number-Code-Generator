import random
def get_code_length():
    while True:
        try:
            code_length = int(input('Please enter how long you want your code to be, between 1 - 100: '))
            if 1 <= code_length <= 100:
                return code_length
            else:
                raise ValueError
        except ValueError:
            print('Invalid input, please try again...')

def get_code_type():
    while True:
        try:
            code_type = int(input('Enter 1 for letter-only code, 2 for number-only code, or 3 for alphanumeric code'))
            if code_type is 1 or 2 or 3:
                return code_type
            else:
                raise ValueError
        except ValueError:
            print('Invalid code_type, please try again...')

def code_generator(code_length, code_type):
    if code_type == 1:
        return letter_code(code_length)
    elif code_type == 2:
        return number_code(code_length)
    else:
        return alphanumeric_code(code_length)
    
def letter_code(code_length):
    code = []
    for i in range(code_length):
        code.append(chr(random.randint(97,122)))
    return code

def number_code(code_length):
    numbers = ['1','2','3','4','5','6','7','8','9','0']
    code = []
    for i in range(code_length):
        code.append(numbers[random.randint(0,9)])
    return code

def alphanumeric_code(code_length):
    code = []
    for i in range(code_length):
        if random.randint(0,1) == 0:
            code.append(chr(random.randint(97,122)))
        else:
            numbers = ['1','2','3','4','5','6','7','8','9','0']
            code.append(numbers[random.randint(0,9)])
    return code

def main():
    code_length = get_code_length()
    code_type = get_code_type()
    unjoined_code = code_generator(code_length,code_type)
    joined_code = ''.join(unjoined_code)
    print(f'Your generated code of length {code_length} is {joined_code}')
    
main()