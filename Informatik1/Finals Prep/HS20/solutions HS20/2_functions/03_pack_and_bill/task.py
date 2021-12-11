#-- THIS LINE SHOULD BE THE FIRST LINE OF YOUR SUBMISSION! --#

def pack_and_bill(order, prices):
	pass

#-- THIS LINE SHOULD BE THE LAST LINE OF YOUR SUBMISSION! ---#

### DO NOT SUBMIT THE FOLLOWING LINES!!! THESE ARE FOR LOCAL TESTING ONLY!
prices = {
	"ball":     0.20,
	"smallbox": 4.50,
	"largebox": 7.50
}
assert(pack_and_bill([1], prices)            == (0, 1, 4.70))   # 0 large boxes, 1 small box, total price 4.50 + 0.20 * 1
assert(pack_and_bill([500], prices)          == (1, 0, 107.50)) # 1 large box, 0 small boxes, total price 7.50 + 0.20 * 500
assert(pack_and_bill([600], prices)          == (1, 1, 132.00))
assert(pack_and_bill([601], prices)          == (2, 0, 135.20))
assert(pack_and_bill([50, 500, 500], prices) == (2, 1, 229.50))
