import random
def get_code_length():
    code_length = int(input('Please enter how long you want your code to be, between 1 - 100: '))
    while not 1 <= code_length <= 100:
        code_length = int(input('Please enter how long you want your code to be, between 1 - 100: '))
    return code_length

def code_generator(code_length):
    numbers = ['1','2','3','4','5','6','7','8','9','0']
    code = []
    for i in range(code_length):
        index = random.randint(0,9)
        code.append(numbers[index])
    return code


def main():
    code_length = get_code_length()
    unjoined_code = code_generator(code_length)
    joined_code = ''.join(unjoined_code)
    print(f'Your generated code of length {code_length} is {joined_code}')
    
main()