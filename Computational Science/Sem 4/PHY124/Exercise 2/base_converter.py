def convert_to_base(num, base):
    if base < 2 or base > 36:
        raise ValueError("Base must be between 2 and 36")

    if num == 0:
        return "0"

    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    is_negative = num < 0
    num = abs(num)

    while num > 0:
        result = digits[num % base] + result
        num //= base

    if is_negative:
        result = "-" + result

    return result

print(convert_to_base(23080254, 15))