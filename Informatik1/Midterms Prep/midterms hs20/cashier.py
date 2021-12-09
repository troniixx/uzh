menu = {
"Hot Dog": 3.50,
"Spicy Dog": 4.00,
"Vegan Dog": 3.50,
"Water": 1.50,
"Fizzy Drink": 2.50,
"Beer": 4.00
}

# bill({"Spicy Dog": 2, "Water": 3, "Beer": 8}) should return 37.5
# --> 37.5 = (2*4.00 + 3*1.50 - 2*1.50 + 8*4.00 - 1*4.00)
# --> 2 waters and one beer are free in this order
def bill(order):
    parse_qsl(qs, keep_blank_values=False, strict_parsing=False)