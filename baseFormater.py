A_ASCII = 65

def base_format(num):
    if -1 < num and num < 10:
        return num
    elif 10 <= num and num <= 35:
        asci_char_code = num - 10 + A_ASCII
        return chr(asci_char_code)
    else:
        return "ERROR: number lower than 0 and higher than 35 is not supported!"