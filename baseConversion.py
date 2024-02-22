from baseFormater import base_format

def dec_to_base_convert(dec_num, base):
    if not validate_dec_to_base_input(dec_num, base):
        return -1

    arr = dec_to_base_convert_array(dec_num, base)
    format_base_convert_array(arr)
    result = ''.join(str(num) for num in arr)
    return result

def validate_dec_to_base_input(dec_num, base):
    if dec_num < 0:
        print("ERROR: negative decimal numbers are not supported!")
        return False
    if 2 > base or base > 35:
        print("ERROR: only base between 2 and 35 are supported!")
        return False
    return True

def dec_to_base_convert_array(dec_num, base):
    result = []

    while dec_num >= base:
        result.insert(0, (dec_num % base))
        dec_num = dec_num // base

    result.insert(0, dec_num)
    return result

def base_to_dec_convert(num_str, base):
    if not validate_base_to_dec_input(num_str, base):
        return -1

    num_str = num_str[::-1]

    sum = 0
    for i, char in enumerate(num_str):
        num = num_of_digit_char(char)
        result = num * pow(base, i)
        sum += result

    return sum

    
def num_of_digit_char(digit_char):
    if digit_char.isdigit():
        return int(digit_char)
    else:
        char_ascii = ord(digit_char)
        if (65 <= char_ascii and char_ascii <= 90):
            return char_ascii - 65 + 10
    
    print("ERROR: invalid number only digit 0-9 and character A-Z allowed!")
    return -1

def validate_base_to_dec_input(num_str, base):
    for char in num_str:
        if not char.isdigit():
            char_ascii = ord(char)
            if (65 > char_ascii or char_ascii > 90):
                print("ERROR: invalid number only digit 0-9 and character A-Z allowed!")
                return False

    if 2 > base or base > 35:
        print("ERROR: only base between 2 and 35 are supported!")
        return False
    return True


def format_base_convert_array(array):
    for index, num in enumerate(array):
        array[index] = base_format(num)