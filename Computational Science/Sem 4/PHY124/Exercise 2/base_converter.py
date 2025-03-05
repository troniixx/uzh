def convert_to_base(num, base):
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

print(convert_to_base(23080251, 13))