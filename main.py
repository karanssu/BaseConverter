from baseConversion import dec_to_base_convert
from baseConversion import base_to_dec_convert

dec_num = int(input("Decimal Num: "))
base = int(input("Base (2-35): "))
result = dec_to_base_convert(dec_num, base)

if (result != -1):
    result_string = f"The equivalent base-{base} value of decimal {dec_num} is: {result}"
    print(result_string)

print('\n')

num_str = input("Num: ")
base = int(input("Base (2-35): "))
result = base_to_dec_convert(num_str, base)

if (result != -1):
    result_string = f"The equivalent decimal value of base-{base} value of {num_str} is: {result}"
    print(result_string)